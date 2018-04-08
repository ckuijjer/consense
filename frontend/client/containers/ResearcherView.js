import React from 'react';

export default class Reservation extends React.Component {
	constructor(props) {
		super(props);
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
			fetch(`http://localhost:3000/getAvailableResearchData/sex/${sex}/age/${age}`)
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
					<p>Change the parameters to check how many consents have been provided:</p>

					<label>Sex:</label>
					<select value={this.state.sex} onChange={this.handleInputChange}>
						<option value="male">Male</option>
						<option value="female">Female</option>
					</select>

					<br />

					<label>Age:</label>
					<input
						name="age"
						type="number"
						value={this.state.age}
						onChange={this.handleInputChange} />
					<br />

					<button onClick={this.handleClick}>Request the research data</button>

					<p>The consent has been provided by {this.state.numberOfConsents} participants.</p>
				</div>
			</div>
		);
	}
}
