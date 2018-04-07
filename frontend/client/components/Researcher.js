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
			<form>
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

				<p>server response: {this.state.serverReply}</p>
			</form>
		);
	}
}

/*
ReactDOM.render(
	<Reservation />,
	document.getElementById('root')
);
*/