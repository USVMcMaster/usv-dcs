import React from 'react';
import './App.css';

import Autonomous from './components/Autonomous';
import About from './components/About';
import Layout from './components/Layout';
// import DynamicRoutingExample from './components/DynamicRoutingExample';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import RemoteControl from './components/RemoteControl';
import Settings from './components/Settings';
import Tuning from './components/Tuning';


function App() {
  return (
    <Router>
      <div className="App">
        {/* <Nav /> */}
        <Layout />
        {/* Switch forces router to stop on first match of path */}
        <Switch>
          <Route path="/" exact component={Home} />

          <Route path="/remote-control" exact component={RemoteControl} />
          <Route path="/autonomous" exact component={Autonomous} />
          
          <Route path="/tuning" exact component={Tuning} />
          <Route path="/settings" exact component={Settings} />
          <Route path="/about" exact component={About} />

          {/* Dynamic routing example */}
          {/* <Route path="/automonous/:id" component={DynamicRoutingExample}/> */}
        </Switch>
      </div>
    </Router>
  );
}

const Home = () => (
  <div>
    <h1>Home Page</h1>
  </div>

);

export default App;