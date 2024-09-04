import React, { useState } from 'react';
import '../css/ResumeAnalysis.css'; // Updated import path

const ResumeAnalysis = () => {
  const [resume, setResume] = useState('');
  const [jobDescription, setJobDescription] = useState('');

  const handleAnalyze = () => {
    // Analyze resume and job description here
  };

  return (
    <div className="resume-analysis-container">
      <h2>Resume Analysis</h2>
      <textarea
        placeholder="Paste your resume here..."
        value={resume}
        onChange={(e) => setResume(e.target.value)}
      />
      <textarea
        placeholder="Paste job description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />
      <button onClick={handleAnalyze}>Analyze</button>
      {/* Display results here */}
    </div>
  );
};

export default ResumeAnalysis;
