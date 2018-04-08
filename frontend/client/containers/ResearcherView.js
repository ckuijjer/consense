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
		this.handleClick = this.handleClick.bind(this);
	}

	fetchDataFromTheServer(sex, age) {
		return new Promise((resolve, reject) => {
			fetch('http://localhost:3000/getAvailableResearchData/sex/' + sex + '/age/' + age)
				.then((resp) => resp.text())
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
	}

	handleClick(event) {

		this.fetchDataFromTheServer(this.state.sex, this.state.age).then((availableResearchData) => {
			this.setState({
				numberOfConsents: availableResearchData
			});
		});
		event.preventDefault();
	}

	render() {
		return (
			<div>
				<h2>This is this researcher view</h2>
				<div>
					<FormGroup>
						<p>Change the parameters to check how many consents have been provided:</p>

						<div className="form-item">
							<FormGroup>
								<ControlLabel className="form-label">Sex:</ControlLabel>
								<FormControl componentClass="select" value={this.state.sex} onChange={this.handleInputChange}>
									<option value="male">Male</option>
									<option value="female">Female</option>
								</FormControl>
							</FormGroup>

						</div>

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
							<br />

							<button onClick={this.handleClick}>Request the research data</button>

							<p>The consent has been provided by {this.state.numberOfConsents} participants.</p>
						</div>
					</FormGroup>
				</div>
			</div>
		);
	}
}
