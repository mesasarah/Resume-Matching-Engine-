<<<<<<< HEAD
window.onload = function() {
    const data = JSON.parse(localStorage.getItem('resumeData'));

    if (data) {
        document.getElementById('userName').textContent = data.name;
        document.getElementById('resumeScore').textContent = data.score;
        document.getElementById('resumeLevel').textContent = data.level;
        document.getElementById('recommendedJob').textContent = data.recommendedJob;
        document.getElementById('recommendedSkills').textContent = data.recommendedSkills;
        document.getElementById('certifications').textContent = data.certifications;
        document.getElementById('jobRecommendations').textContent = data.jobRecommendations;
    }
};

function goBack() {
    window.history.back();
}
=======
window.onload = function() {
    const data = JSON.parse(localStorage.getItem('resumeData'));

    if (data) {
        document.getElementById('userName').textContent = data.name;
        document.getElementById('resumeScore').textContent = data.score;
        document.getElementById('resumeLevel').textContent = data.level;
        document.getElementById('recommendedJob').textContent = data.recommendedJob;
        document.getElementById('recommendedSkills').textContent = data.recommendedSkills;
        document.getElementById('certifications').textContent = data.certifications;
        document.getElementById('jobRecommendations').textContent = data.jobRecommendations;
    }
};

function goBack() {
    window.history.back();
}
>>>>>>> 1a2a1b9509515ccfd2a93b6628dc505a516b7753
