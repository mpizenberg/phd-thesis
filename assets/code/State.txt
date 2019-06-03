type State
    = NothingProvided
    | ConfigProvided Config Classes (Zipper Tool)
    | ImagesProvided (Zipper RawImage)
    | AllProvided Config Classes (Zipper Tool) (Zipper AnnotatedImage)