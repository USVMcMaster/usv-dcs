import React, { useState, useEffect } from 'react';
import '../App.css';
import {Link} from 'react-router-dom';

function Autonomous() {

  // Only runs on component mount
  useEffect(() => {
    fetchItems()
  }, []);

  const [items, setItems] = useState([]);

  const fetchItems = async () => {
    const data = await fetch(
      'https://jsonplaceholder.typicode.com/users'
    );

    const items = await data.json();
    console.log(items);
    setItems(items);
  }

  return (
    <div>
      {/* Dynamic routing example */}
      {items.map(item => (
        <h1 key={item.id}>
          <Link to={`/autonomous/${item.id}`}>{item.name}</Link>
        </h1>
      ))}
    </div>
  );
}

export default Autonomous;