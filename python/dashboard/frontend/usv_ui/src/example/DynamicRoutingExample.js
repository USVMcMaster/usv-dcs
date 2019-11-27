import React, { useState, useEffect } from 'react';
import '../App.css';
import {Link} from 'react-router-dom';

function Item() {

  // Only runs on component mount
  useEffect(() => {
    fetchItem()
  }, []);


  const [item, setItem] = useState({});

  const fetchItem = async () => {
    const fetchItem = await fetch(`url`);

    const item = await fetchItem.json();
  };

  return (
    <div>
      <h1></h1>
    </div>
  );
}

export default Item;