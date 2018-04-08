// let's go!
import React from 'react';

import { render } from 'react-dom';

// Import css
import css from './styles/style.styl';

//Import Components
import App from './components/App';
import Single from './components/Single';
import Welcome from './components/Welcome';
import ParticipantView from './components/ParticipantView';
import ResearcherView from './components/ResearcherView';


//Import react router deps
import { Router, Route, IndexRoute, browserHistory } from 'react-router';

import { Provider } from 'react-redux';
import store, { history } from './store';


const router = (
	<Provider store={store}>
		<Router history={history}>
			<Route path="/" component={App}>
				<IndexRoute component={Welcome}></IndexRoute>
				<Route path="/researcher" component={ResearcherView}></Route>
				<Route path="/participant" component={ParticipantView}></Route>

			</Route>
		</Router>
	</Provider>	
)


render(router, document.getElementById('root'));
