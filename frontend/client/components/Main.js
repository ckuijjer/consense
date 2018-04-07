import React from 'react';
import { Link } from 'react-router';
import Researcher from './Researcher';

const Main = React.createClass({
	render() {
		return (
			<div>
				<h1>
				<Link to="/">Consense Data Exchange</Link>
				</h1>
				{React.cloneElement(this.props.children, this.props)}
			</div>	
		)
	}
});

export default Main;