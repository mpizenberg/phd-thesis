#!/usr/bin/env python

import numpy as np

class BoxPlot:
    def __init__(self, d):
        data = sorted(d)
        self.minimum = data[0]
        self.first = np.percentile(data, 25)
        self.median = np.percentile(data, 50)
        self.third = np.percentile(data, 75)
        self.maximum = data[-1]

    def to_tikz(self):
        return """
        \\addplot+[
        color=black,
        style=solid,
        boxplot prepared={{
            median={:f},
            upper quartile={:f},
            lower quartile={:f},
            upper whisker={:f},
            lower whisker={:f}
        }},
        ] coordinates {{}};""".format(self.median, self.third, self.first, self.maximum, self.minimum)

class Line:
    def __init__(self, line):
        split = line.split(',')
        self.sequence = split[0]
        self.camera = split[1]
        self.algo = split[2]
        self.t_err_rmse_f   = float(split[3])
        self.t_err_median_f = float(split[4])
        self.r_err_rmse_f   = float(split[5])
        self.r_err_median_f = float(split[6])
        self.t_err_rmse_s   = float(split[7])
        self.t_err_median_s = float(split[8])
        self.r_err_rmse_s   = float(split[9])
        self.r_err_median_s = float(split[10])

def parse_rpe(path):
    algos = dict()

    with open(path, 'r') as f:
        for line in f.readlines()[1:]:
            parsed_line = Line(line)
            if algos.get(parsed_line.algo, None) == None:
                algos[parsed_line.algo] = []
            algos[parsed_line.algo].append(parsed_line)

    return algos

def empty_dict():
    output = dict()

    output["vors"] = []
    output["fovis"] = []
    output["dvo"] = []
    output["ocv-rgbd"] = []
    output["ocv-rgbd-icp"] = []
    output["ocv-icp"] = []
    output["still"] = []

    return output

def t_err_median_all(data):
    output = empty_dict()

    for key, val in data.items():
        if key.startswith('vors-'):
            continue

        output[key] = BoxPlot(map(lambda x: x.t_err_median_s, val))

    return output

def t_err_rmse_all(data):
    output = empty_dict()

    for key, val in data.items():
        if key.startswith('vors-'):
            continue

        output[key] = BoxPlot(map(lambda x: x.t_err_rmse_s, val))

    return output

def t_err_median_tum(data):
    output = empty_dict()

    for key, val in data.items():
        if key.startswith('vors-'):
            continue

        filtered = filter(lambda x: x.camera != 'icl', val)
        mapped = map(lambda x: x.t_err_median_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def t_err_rmse_tum(data):
    output = empty_dict()

    for key, val in data.items():
        if key.startswith('vors-'):
            continue

        filtered = filter(lambda x: x.camera != 'icl', val)
        mapped = map(lambda x: x.t_err_rmse_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def t_err_median_icl(data):
    output = empty_dict()

    for key, val in data.items():
        if key.startswith('vors-'):
            continue

        filtered = filter(lambda x: x.camera == 'icl', val)
        mapped = map(lambda x: x.t_err_median_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def t_err_rmse_icl(data):
    output = empty_dict()

    for key, val in data.items():
        if key.startswith('vors-'):
            continue

        filtered = filter(lambda x: x.camera == 'icl', val)
        mapped = map(lambda x: x.t_err_rmse_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def t_err_median_icl_no_fovis(data):
    output = empty_dict()
    del output["fovis"]

    for key, val in data.items():
        if key.startswith('vors-') or key == 'fovis':
            continue

        filtered = filter(lambda x: x.camera == 'icl', val)
        mapped = map(lambda x: x.t_err_median_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def t_err_rmse_icl_no_fovis(data):
    output = empty_dict()
    del output["fovis"]

    for key, val in data.items():
        if key.startswith('vors-') or key == 'fovis':
            continue

        filtered = filter(lambda x: x.camera == 'icl', val)
        mapped = map(lambda x: x.t_err_rmse_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def t_err_median_icl_no_fovis_no_still(data):
    output = empty_dict()
    del output['still']
    del output["fovis"]

    for key, val in data.items():
        if key.startswith('vors-') or key == 'fovis' or key == 'still':
            continue

        filtered = filter(lambda x: x.camera == 'icl', val)
        mapped = map(lambda x: x.t_err_median_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def t_err_rmse_icl_no_fovis_no_still(data):
    output = empty_dict()
    del output['still']
    del output["fovis"]

    for key, val in data.items():
        if key.startswith('vors-') or key == 'fovis' or key == 'still':
            continue

        filtered = filter(lambda x: x.camera == 'icl', val)
        mapped = map(lambda x: x.t_err_rmse_s, filtered)
        output[key] = BoxPlot(mapped)

    return output

def generate_figure(dictionnary, output):
    with open(output + '.tex', 'w') as f:
        f.write('\\begin{tikzpicture}\n')
        f.write('    \\begin{axis}\n')
        f.write('    [\n')
        f.write('    ytick={{{}}}\n,'.format(",".join(map(lambda x: str(x), range(1, 1 + len(dictionnary.keys()))))))
        f.write('    yticklabels={{{}}},\n'.format(",".join(map(lambda x: str(x), dictionnary.keys()))))
        f.write('    ]\n')

        for key, val in dictionnary.items():
            f.write(val.to_tikz())

        f.write('    \\end{axis}\n')
        f.write('\\end{tikzpicture}\n')

def main():
    rpe_all = parse_rpe("rpe.csv")
    generate_figure(t_err_median_all(rpe_all), "t_err_median_all")
    generate_figure(t_err_rmse_all(rpe_all), "t_err_rmse_all")
    generate_figure(t_err_median_icl(rpe_all), "t_err_median_icl")
    generate_figure(t_err_rmse_icl(rpe_all), "t_err_rmse_icl")
    generate_figure(t_err_median_tum(rpe_all), "t_err_median_tum")
    generate_figure(t_err_rmse_tum(rpe_all), "t_err_rmse_tum")
    generate_figure(t_err_median_icl_no_fovis(rpe_all), "t_err_median_icl_no_fovis")
    generate_figure(t_err_rmse_icl_no_fovis(rpe_all), "t_err_rmse_icl_no_fovis")
    generate_figure(t_err_median_icl_no_fovis_no_still(rpe_all), "t_err_median_icl_no_fovis_no_still")
    generate_figure(t_err_rmse_icl_no_fovis_no_still(rpe_all), "t_err_rmse_icl_no_fovis_no_still")

if __name__ == '__main__':
    main()


