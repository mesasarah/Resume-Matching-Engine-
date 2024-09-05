// Smooth Scrolling for Navigation Links
document.querySelectorAll('nav a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
      });
  });
});
document.getElementById('resumeForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const formData = new FormData();
  const file = document.getElementById('resumeFile').files[0];

  if (!file) {
      alert('Please upload a PDF file.');
      return;
  }

  formData.append('file', file);

  const response = await fetch('/upload', {
      method: 'POST',
      body: formData
  });

  const result = await response.json();
  if (result.error) {
      alert(result.error);
  } else {
      displayResult(result);
  }
});

function displayResult(result) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = `
      <h3>Recommended Job: ${result.recommended_job}</h3>
      <p>Certification Links: <ul>
          ${Object.entries(result.certification_links).map(([skill, link]) => `<li>${skill}: <a href="${link}" target="_blank">${link}</a></li>`).join('')}
      </ul></p>
      <h3>Job Openings:</h3>
      ${result.job_openings.map(job => `
          <div>
              <h4>${job.job_title} - ${job.company}</h4>
              <p>${job.location}</p>
              <p>${job.summary}</p>
              <a href="${job.url}" target="_blank">View Job</a>
          </div>
      `).join('')}
  `;
}


// File upload button
const uploadButton = document.querySelector('.upload-btn');
uploadButton.addEventListener('change', function() {
  if (this.files.length > 0) {
      alert('File uploaded: ' + this.files[0].name);
  }
});
