import React, { useEffect, useState } from 'react';
import './App.css';
import { Data } from './components/Data';

function App() {
  // const [stuff, myData] = useState([]);

  useEffect(() => {
    fetch('/test_data').then(response =>
       response.json().then(data => {
         console.log(data);
        //  myData(data.stuff);
        })
      );
    // Empty array forces component to only run on first load
  }, [])

  // console.log(stuff);
  return (
    <div className="App">
      {/* <Data  stuff={stuff}/> */}

    </div>
  );
}

export default App;
