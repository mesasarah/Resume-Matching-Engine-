// Smooth Scrolling for Navigation Links
document.querySelectorAll('nav a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
      });
  });
});

// File upload button
const uploadButton = document.querySelector('.upload-btn');
uploadButton.addEventListener('change', function() {
  if (this.files.length > 0) {
      alert('File uploaded: ' + this.files[0].name);
  }
});
