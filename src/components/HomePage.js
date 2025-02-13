import React from "react";
import { useNavigate } from "react-router-dom";
import "/Users/yughjuneja/Sahayak/src/App.css";

function HomePage() {
  const navigate = useNavigate();

  return (
    <div className="home-page">
      <h1 className="logo">SAHAYAK</h1>
      <div className="options">
        <button onClick={() => navigate("/sign-language")}>Sign Language Translation</button>
        <button onClick={() => navigate("/environment-detection")}>Environment Detection</button>
        <button onClick={() => navigate("/language-translation")}>Language Translation</button>
      </div>
    </div>
  );
}

export default HomePage;