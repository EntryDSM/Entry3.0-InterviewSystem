import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Login } from './container';

class App extends Component {
  render() {
    return (
      <Provider>
        <Router>
          <Switch>
            <Route path="/" component={Login} exact/>
          </Switch>
        </Router>
      </Provider>
      
    );
  }
}

export default App;
