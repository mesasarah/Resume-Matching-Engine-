import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import ResumeAnalysis from './components/ResumeAnalysis';
import SkillsRecommendations from './components/SkillsRecommendations';
import CoursesRecommendations from './components/CoursesRecommendations';
import ResumeTips from './components/ResumeTips';
import LinkedInJobs from './components/LinkedInJobs';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/resume-analysis" element={<ResumeAnalysis />} />
        <Route path="/skills-recommendations" element={<SkillsRecommendations />} />
        <Route path="/courses-recommendations" element={<CoursesRecommendations />} />
        <Route path="/resume-tips" element={<ResumeTips />} />
        <Route path="/linkedin-jobs" element={<LinkedInJobs />} />
      </Routes>
    </Router>
  );
};

export default App;
