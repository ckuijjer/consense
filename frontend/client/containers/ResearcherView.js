import React, { Component } from 'react';
import { FormGroup, ControlLabel, FormControl, Radio } from 'react-bootstrap';

export default class Reservation extends React.Component {
	constructor(props, context) {
		super(props, context);
		this.state = {
			sex: 'male',
			age: 17,
			serverReply: 'no server reply',
			numberOfConsents: 0
		};

		this.handleInputChange = this.handleInputChange.bind(this);
	}

	fetchDataFromTheServer(sex, age) {
		return new Promise((resolve, reject) => {
			fetch(`http://localhost:3000/getAvailableResearchData/sex/${sex}/age/${age}`)
				.then((resp) => resp.text() )
				.then(function (data) {
					console.log(data);
					resolve(data);
				});
		});
	}


	handleInputChange(event) {
		const target = event.target;
		const value = target.value;
		const name = target.name;
		this.setState({
			[name]: value
		});

		this.fetchDataFromTheServer(this.state.sex, this.state.age).then((availableResearchData) => {
			this.setState({
				serverReply: availableResearchData
			});
		});
	}

	render() {
		return (
			<div>
			<h2>This is this researcher view</h2>
			<form>
				<FormGroup>
				<p>Change the parameters to check how many consents have been provided:</p>
				
				<div className="form-item">
				<ControlLabel className="form-label">Sex:</ControlLabel>
				<select value={this.state.sex} onChange={this.handleInputChange}>
            		<option value="male">Male</option>
            		<option value="female">Female</option>
				</select>
				</div>

				<br />
				<div className="form-item">
				<ControlLabel className="form-label">Age:</ControlLabel>
				<FormControl
						name="age"
						type="number"
						value={this.state.age}
						onChange={this.handleInputChange} />
				</div>
				<br />

				<p>server response: {this.state.serverReply}</p>
				</FormGroup>
			</form>
			</div>
		);
	}
}
