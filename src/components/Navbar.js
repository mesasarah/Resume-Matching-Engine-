import React from 'react';
import { Link } from 'react-router-dom';
import '../css/Navbar.css'; // Updated import path

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/resume-analysis">Resume Analysis</Link></li>
        <li><Link to="/skills-recommendations">Skills Recommendations</Link></li>
        <li><Link to="/courses-recommendations">Courses Recommendations</Link></li>
        <li><Link to="/resume-tips">Resume Tips</Link></li>
        <li><Link to="/linkedin-jobs">LinkedIn Jobs</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
