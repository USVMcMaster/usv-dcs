import React, { Component } from 'react';
import './App.css';
import ButtonAppBar from './templates/Header';
import PaperSheet from './templates/bodyLayout';


class App extends Component {
  
  componentDidMount() {
    this.renderMap()
  }
  
  initMap = () => {
    var marker_count = 0;
    var markers = [];

    // eslint-disable-next-line
    var map = new window.google.maps.Map(document.getElementById('map'), {
      center: {lat: 43.266951, lng: -79.921734},
      zoom: 15
    });

    function addMarker (latLng, map) {
      // eslint-disable-next-line
      markers[marker_count] = new window.google.maps.Marker({
      position: {lat: latLng.lat(), lng:latLng.lng()},
      map: map
      });

      marker_count++
    }
    
    window.google.maps.event.addListener(map, 'click', function(event) {
      // console.log(event.latLng.lat())
      // console.log(event.latLng.lng())
      addMarker(event.latLng, map) //<-- adds new marker per function call
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
        {/* <div id="map"></div> */}
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
