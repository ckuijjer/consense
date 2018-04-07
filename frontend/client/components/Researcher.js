import React from 'react';

export default class Reservation extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			isGoing: true,
			numberOfGuests: 2,
			serverReply: 'no server reply',
			numberOfConsents: 0
		};

		this.handleInputChange = this.handleInputChange.bind(this);
	}

	fetchDataFromTheServer(sex, age) {
		return new Promise((resolve, reject) => {
			fetch(`http://localhost:3000/getAvailableResearchData/sex/${sex}/age/${age}`)
				.then((resp) => resp.text() )// Transform the data into json
				.then(function (data) {
					console.log(data);
					resolve(data);
				});
		});
	}


	handleInputChange(event) {
		const target = event.target;
		const value = target.type === 'checkbox' ? target.checked : target.value;
		const name = target.name;

		this.fetchDataFromTheServer('male', 42).then((availableResearchData) => {
			this.setState({
				serverReply: availableResearchData
			});
		});
	}

	render() {
		return (
			<form>
				<label>
					Is going:
				<input
						name="isGoing"
						type="checkbox"
						checked={this.state.isGoing}
						onChange={this.handleInputChange} />
				</label>
				<br />
				<label>
					Number of guests:
				<input
						name="numberOfGuests"
						type="number"
						value={this.state.numberOfGuests}
						onChange={this.handleInputChange} />
				</label>

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