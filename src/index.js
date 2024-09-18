// Form submission event for resume upload
document.getElementById('resumeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);
    
    // Simulate backend NLP processing (replace with actual backend call)
    const file = formData.get('file');
    
    if (!file) {
        alert("Please upload a resume before submitting!");
        return;
    }
    
    // Simulated NLP result (replace this with your actual backend API call)
    const data = {
        name: "John Doe",  // Example name extracted from resume (replace with dynamic data)
        score: 85,         // Example score (replace with dynamic data)
        level: "Intermediate",
        recommendedJob: "Software Developer",
        recommendedSkills: "JavaScript, Python, React",
        certifications: "AWS Certified Developer, Google Cloud Associate",
        jobRecommendations: "Full Stack Developer at XYZ Corp, Backend Developer at ABC Ltd."
    };

    // Save the result data to localStorage for use on the results page
    localStorage.setItem('resumeData', JSON.stringify(data));

    // Redirect to the results page after processing
    window.location.href = "results.html";  // Adjust this if your results page has a different name or path
});

// On window load, display resume data on the results page
window.onload = function() {
    const data = JSON.parse(localStorage.getItem('resumeData'));

    if (data) {
        // Dynamically populate the results page with NLP output
        document.getElementById('userName').textContent = data.name;
        document.getElementById('resumeScore').textContent = data.score;
        document.getElementById('resumeLevel').textContent = data.level;
        document.getElementById('recommendedJob').textContent = data.recommendedJob;
        document.getElementById('recommendedSkills').textContent = data.recommendedSkills;
        document.getElementById('certifications').textContent = data.certifications;
        document.getElementById('jobRecommendations').textContent = data.jobRecommendations;
    } else {
        // Handle the case where there is no resume data (e.g., user directly accessed the results page)
        alert("No resume data found. Please upload your resume.");
        window.location.href = "/";  // Redirect back to the form page or home
    }
};

// Function to navigate back to the previous page
const goBack = () => {
    window.history.back();
};

// Assuming you have a button to trigger the `goBack` function, such as:
document.getElementById('backButton').addEventListener('click', goBack);
