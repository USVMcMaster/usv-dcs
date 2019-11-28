import React, { Component } from 'react';
import '../App.css';
import AutonomousBody from './AutonomousBody';

var start;
var end;

class Autonomous extends Component {


  componentDidMount() {
    this.renderMap()
  }

  initMap = () => {
    var marker_count = 0;
    var markers = [];

    var click_timeout = null;

    // eslint-disable-next-line
    var map = new window.google.maps.Map(document.getElementById('map'), {
      center: { lat: 43.266951, lng: -79.921734 },
      zoom: 15
    });

    function addMarker(latLng, map) {
      // eslint-disable-next-line
      if (marker_count < 2) {
        markers[marker_count] = new window.google.maps.Marker({
          position: { lat: latLng.lat(), lng: latLng.lng() },
          map: map
        });

        if (marker_count === 0) {
          start = markers[marker_count]
          console.log(start)
        }

        if (marker_count === 1) {
          end = markers[marker_count]
          console.log(end)
        }
        marker_count++
      }
      else {
        console.log("Reached max markers")
      }      
    }

    // Handler for single click event
    window.google.maps.event.addListener(map, 'click', function (event) {
      // console.log(event.latLng.lat())
      // console.log(event.latLng.lng())
      click_timeout = setTimeout(function () {
        addMarker(event.latLng, map) //<-- adds new marker per function call
      }, 200);
    });

    // Handler for double click event (ensures double click doesn't place marker)
    window.google.maps.event.addListener(map, 'dblclick', function (event) {
      clearTimeout(click_timeout);
    });
  }

  renderMap = () => {
    loadScript("https://maps.googleapis.com/maps/api/js?key=AIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs&callback=initMap")
    window.initMap = this.initMap
  }


  render() {
    return (
      <AutonomousBody />
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

export default Autonomous;



// function Autonomous() {

//   // Only runs on component mount
//   useEffect(() => {
//     fetchItems()
//   }, []);

//   const [items, setItems] = useState([]);

//   const fetchItems = async () => {
//     const data = await fetch(
//       'https://jsonplaceholder.typicode.com/users'
//     );

//     const items = await data.json();
//     console.log(items);
//     setItems(items);
//   }

//   return (
//     <div>
//       {/* Dynamic routing example */}
//       {items.map(item => (
//         <h1 key={item.id}>
//           <Link to={`/autonomous/${item.id}`}>{item.name}</Link>
//         </h1>
//       ))}
//     </div>
//   );
// }