const toggle = document.querySelector('.toggle');
const body = document.body;

// Retrieve the saved mode from local storage or default to an empty string
const savedMode = localStorage.getItem('mode') || '';

// Apply the saved mode (if any) to the body
body.className = savedMode;

toggle.addEventListener('click', () => {
  // Check if the current mode is light
  const isLightMode = body.classList.contains('light');

  if (isLightMode) {
    // If it's light mode, remove the light class and update local storage
    body.classList.remove('light');
    localStorage.setItem('mode', '');
  } else {
    // If it's not light mode, add the light class and update local storage
    body.classList.add('light');
    localStorage.setItem('mode', 'light');
  }
});

