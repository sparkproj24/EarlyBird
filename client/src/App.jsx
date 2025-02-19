import { useState, useEffect } from "react";
import axios from "axios";
import birdLogo from "./assets/bird.png";
import "./App.css";

function App() {
  const [array, setArray] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/users");
    const data = response.data.users;
   setArray(data);
  };
  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <div>
        <a
          href="https://www.ticketmaster.com"
          target="_blank"
        >
          <img src={birdLogo} className="logo" alt="Bird logo" />
        </a>
      </div>
      <h1>EarlyBird</h1>
      <div className="card">
        <p>Welcome to project EarlyBird!</p>
        <p className="read-the-docs">More coming soon...</p>
      </div>
      <p>test connection:</p>
      {
        array.map((user) => {
          return (
            <div key={user.id}>
              <span>{user.name}</span>
            </div>
          );
        })
      }
    
    </>
  );
}

export default App;
