import React, { useState, useEffect } from 'react';
import '../App.css';

function GetMapData() {

  // Only runs on component mount
  useEffect(() => {
    fetchItems()
  }, []);

  const [items, setItems] = useState([]);

  const fetchItems = async () => {
    const data = await fetch(
      'http://localhost:5000/mask?map=https%3A%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fstaticmap%3Fcenter%3D43.266951%2C-79.921734%26zoom%3D15%26size%3D800x800%26markers%3D%26style%3Dfeature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff%26style%3Dfeature%3Aroad%7Cvisibility%3Aoff%26key%3DAIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs'
    );

    console.log(data)
    const items = await data.json();
    // console.log(items);
    // setItems(items);
  }

  return (
    <div>
      {/* {items.map(item => (
        <p key={item.id}>
          <img src={`$item.image`} />
        </p>
      ))} */}
      {/* <img src={items} /> */}
    </div>

    // <Link to={`/autonomous/${item.id}`}>{item.name}</Link>
  );
}

export default GetMapData;