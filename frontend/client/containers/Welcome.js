import React from 'react';
import { Link } from 'react-router';

const Welcome = React.createClass({
	render() {
		return (
			<div className="welcome-page">
				<h1>Welcome</h1>


				<Link className="button" to="/researcher">I'm a researcher</Link>
				<Link className="button" to="/participant">I'm a participant</Link>
			</div>

		)
	}
});

export default Welcome;
