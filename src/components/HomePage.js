import React from 'react';
import Navbar from './Navbar';
import '../css/HomePage.css'; // Updated import path

const HomePage = () => {
  return (
    <div className="home-container">
      <Navbar />
      <h1>Welcome to the ATS</h1>
      <p>Your one-stop solution for resume analysis and job matching.</p>
    </div>
  );
};

export default HomePage;
