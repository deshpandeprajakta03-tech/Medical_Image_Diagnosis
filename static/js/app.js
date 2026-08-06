/* =============================================
   MEDICAL AI DIAGNOSIS — APP.JS
   ============================================= */

document.addEventListener('DOMContentLoaded', function () {

  /* ---- Drag & Drop + File Preview ---- */
  const dropZone      = document.getElementById('dropZone');
  const fileInput     = document.getElementById('fileInput');
  const previewWrapper = document.getElementById('previewWrapper');
  const imgPreview    = document.getElementById('imgPreview');
  const removeBtn     = document.getElementById('removeBtn');
  const predictForm   = document.getElementById('predictForm');
  const predictBtn    = document.getElementById('predictBtn');
  const loadingOverlay = document.getElementById('loadingOverlay');

  if (!dropZone) return; // not a prediction page

  /* Drag events */
  ['dragenter', 'dragover'].forEach(evt => {
    dropZone.addEventListener(evt, e => {
      e.preventDefault();
      dropZone.classList.add('dragover');
    });
  });

  ['dragleave', 'drop'].forEach(evt => {
    dropZone.addEventListener(evt, e => {
      e.preventDefault();
      dropZone.classList.remove('dragover');
    });
  });

  dropZone.addEventListener('drop', e => {
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
      setFile(file);
    }
  });

  /* File input change */
  fileInput.addEventListener('change', function () {
    if (this.files && this.files[0]) {
      setFile(this.files[0]);
    }
  });

  /* Set file and show preview */
  function setFile(file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      imgPreview.src = e.target.result;
      previewWrapper.style.display = 'block';
      dropZone.style.display = 'none';
    };
    reader.readAsDataURL(file);

    /* Sync file to input if dropped */
    const dt = new DataTransfer();
    dt.items.add(file);
    fileInput.files = dt.files;
  }

  /* Remove image */
  if (removeBtn) {
    removeBtn.addEventListener('click', function () {
      imgPreview.src = '#';
      previewWrapper.style.display = 'none';
      dropZone.style.display = 'block';
      fileInput.value = '';
    });
  }

  /* Form submit — show loading overlay */
  if (predictForm) {
    predictForm.addEventListener('submit', function (e) {
      if (!fileInput.files || fileInput.files.length === 0) {
        e.preventDefault();
        alert('Please select an image before predicting.');
        return;
      }
      if (loadingOverlay) loadingOverlay.classList.add('show');
      if (predictBtn) {
        predictBtn.disabled = true;
        predictBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';
      }
    });
  }

  /* ---- Animate confidence bar on load ---- */
  const fill = document.querySelector('.confidence-fill');
  if (fill) {
    const target = fill.style.width;
    fill.style.width = '0%';
    setTimeout(() => { fill.style.width = target; }, 300);
  }

  /* ---- Smooth scroll for anchor links ---- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ---- Navbar active link highlight ---- */
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  /* ---- Feature cards entrance animation ---- */
  const cards = document.querySelectorAll('.feature-card');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
          }, i * 100);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    cards.forEach(card => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(30px)';
      card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      observer.observe(card);
    });
  }

});
