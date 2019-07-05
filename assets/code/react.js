// Leaving out details in ...
class Timer extends React.Component {
	constructor() {
		this.state = { seconds: 0 }
	}
	...
	render() {
		return (<div>Seconds: {this.state.seconds}</div>);
	}
	...
}
