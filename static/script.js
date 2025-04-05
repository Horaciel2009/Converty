document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('video-file');
  const fileLabel = document.querySelector('.file-input-label');
  const fileName = document.querySelector('.file-name');
  const form = document.getElementById('convert-form');
  const progressWrapper = document.querySelector('.progress-wrapper');
  const progressBar = document.querySelector('.progress-bar');
  const alertContainer = document.getElementById('alert-container');
  let progressInterval = null;
  
  // Gestion de l'affichage du nom de fichier
  fileInput.addEventListener('change', () => {
    if (fileInput.files.length) {
      fileName.textContent = fileInput.files[0].name;
      fileName.style.display = 'block';
    } else {
      fileName.style.display = 'none';
    }
  });
  
  // Animation de drag and drop
  const dropArea = document.querySelector('.file-input-wrapper');
  
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
  });
  
  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }
  
  ['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
  });
  
  ['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
  });
  
  function highlight() {
    dropArea.classList.add('border-primary');
    dropArea.style.backgroundColor = 'rgba(139, 92, 246, 0.2)';
  }
  
  function unhighlight() {
    dropArea.classList.remove('border-primary');
    dropArea.style.backgroundColor = 'rgba(139, 92, 246, 0.1)';
  }
  
  dropArea.addEventListener('drop', handleDrop, false);
  
  function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    fileInput.files = files;
    
    if (fileInput.files.length) {
      fileName.textContent = fileInput.files[0].name;
      fileName.style.display = 'block';
    }
  }
  
  // Gestion du formulaire de soumission
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    if (!fileInput.files.length) {
      showAlert('Veuillez sélectionner un fichier vidéo', 'error');
      return;
    }
    
    // Afficher la barre de progression
    progressWrapper.style.display = 'block';
    startProgressSimulation();
    
    // Soumettre le formulaire
    const formData = new FormData(form);
    try {
      const response = await fetch('/', {
        method: 'POST',
        body: formData
      });
      
      // Arrêter la simulation et compléter la barre
      stopProgressSimulation();
      completeProgress();
      
      if (response.redirected) {
        window.location.href = response.url;
      } else {
        const text = await response.text();
        if (text.includes('Erreur')) {
          showAlert(text, 'error');
          resetProgress();
        }
      }
    } catch (error) {
      showAlert('Une erreur est survenue lors de la conversion', 'error');
      console.error('Erreur:', error);
      resetProgress();
    }
  });
  
  function startProgressSimulation() {
    let width = 0;
    // Stockons l'intervalle pour pouvoir l'arrêter plus tard
    progressInterval = setInterval(() => {
      if (width >= 90) {
        clearInterval(progressInterval);
      } else {
        width += 5;
        progressBar.style.width = width + '%';
      }
    }, 500);
  }
  
  function stopProgressSimulation() {
    if (progressInterval) {
      clearInterval(progressInterval);
      progressInterval = null;
    }
  }
  
  function completeProgress() {
    progressBar.style.width = '100%';
    // La transition CSS prend 300ms, donc attendons un peu avant de cacher
    setTimeout(() => {
      resetProgress();
    }, 500);
  }
  
  function resetProgress() {
    stopProgressSimulation();
    progressWrapper.style.display = 'none';
    progressBar.style.width = '0%';
  }
  
  function showAlert(message, type) {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
        ${type === 'success' 
          ? '<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>'
          : '<path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>'}
      </svg>
      <span>${message}</span>
    `;
    
    alertContainer.innerHTML = '';
    alertContainer.appendChild(alert);
    
    setTimeout(() => {
      alert.classList.add('fade-out');
      setTimeout(() => {
        alertContainer.removeChild(alert);
      }, 300);
    }, 5000);
  }
});