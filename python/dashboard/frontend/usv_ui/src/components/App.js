import React, { Component } from 'react';
import './App.css';
import ButtonAppBar from './templates/Header';
import PaperSheet from './templates/bodyLayout';


class App extends Component {
  
  componentDidMount() {
    this.renderMap()
  }
  
  initMap = () => {
    // eslint-disable-next-line
    var map = new window.google.maps.Map(document.getElementById('map'), {
      center: {lat: 43.266951, lng: -79.921734},
      zoom: 15
    });
    
    // eslint-disable-next-line
    var marker = new window.google.maps.Marker({
      position: {lat: 43.266951, lng: -79.921734},
      map: map,
      draggable: true,
      title: 'Hello World!'
    });
  }

    
  
  renderMap = () => {
    loadScript("https://maps.googleapis.com/maps/api/js?key=AIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs&callback=initMap")
    window.initMap = this.initMap
  }
   
  render() {
    return (
      <main>
        <ButtonAppBar/>
        <PaperSheet></PaperSheet>
      </main>
    );
  } 
}

function loadScript(url) {
  // First element of all elements with tag name script
  var index = window.document.getElementsByTagName("script")[0] 
  var script = window.document.createElement("script")
  
  script.src = url
  script.async = true
  script.defer = true

  // Ensures child is appended to parent
  // newNode -> script | referenceNode -> index
  index.parentNode.insertBefore(script, index)
}

export default App;
