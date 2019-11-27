import React from 'react';
import axios from 'axios';

// export default function Hello() {

//   return (
//     axios.get('http://localhost:5000/mask?map=https%3A%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fstaticmap%3Fcenter%3D43.266951%2C-79.921734%26zoom%3D15%26size%3D800x800%26markers%3D%26style%3Dfeature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff%26style%3Dfeature%3Aroad%7Cvisibility%3Aoff%26key%3DAIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs')
//       .then(response => console.log(response))
//   );
// }

export function gen_map_snapshot(event) {
  var static_map_url = "https://maps.googleapis.com/maps/api/staticmap?";
  
  // Map Center
  static_map_url += "center=" + event[0] + "," + event[1];

  // Map Zoom Level
  static_map_url += "&zoom=" + event[2];

  // Map Size
  static_map_url += "&size=" + "480x480";

  // Map Marker
  static_map_url += "&markers=" + event[0] + "," + event[1];

  // Remove all text
  static_map_url += "&style=" + "feature:all|element:labels|visibility:off";

  // Remove Roads
  static_map_url += "&style=" + "feature:road|visibility:off";

  // Appending Key
  static_map_url += "&key=" + 'AIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs';
  return static_map_url;
}

export default class Test extends React.Component {
  state = {
    data: [],
  };

  componentDidMount() {
    // axios.get('http://localhost:5000/mask?map=https%3A%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fstaticmap%3Fcenter%3D43.266951%2C-79.921734%26zoom%3D15%26size%3D800x800%26markers%3D%26style%3Dfeature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff%26style%3Dfeature%3Aroad%7Cvisibility%3Aoff%26key%3DAIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs')
    axios.get(`https://jsonplaceholder.typicode.com/users`)
    .then(res => {
      const persons = res.data;
      this.setState({ persons });
    })
}

render() {
  return (
    <ul>

      {/* { this.state.persons.map(person => <li>{person.name}</li>)} */}
    </ul>
  )
}
}


// class Test extends React.Component {
//   constructor(props) {
//     super(props);

//     this.state = {
//       items: []
//     };
//   }

//   render() {
//     const {items} = this.state;
//     return (
//       <div>
//         <p>{items.points}</p>
//       </div>
//     );
//   } 
// }
// export default Test;