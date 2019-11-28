import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Navigation from './components/Navigation';

import Home from './components/Home';

import RemoteControl from './components/RemoteControl';
import Autonomous from './components/Autonomous';

import Tuning from './components/Tuning';
import Settings from './components/Settings';
import About from './components/About';

function App() {
  return (
    <Router>
      <div className="App">
        {/* <Nav /> */}
        <Navigation />
        {/* Switch forces router to stop on first match of path */}
        <Switch>
          <Route path="/" exact component={Home} />

          <Route path="/remote-control" exact component={RemoteControl} />
          <Route path="/autonomous" exact component={Autonomous} />
          
          <Route path="/tuning" exact component={Tuning} />
          <Route path="/settings" exact component={Settings} />
          <Route path="/about" exact component={About} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;