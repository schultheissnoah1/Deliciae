for (const comparison of document.querySelectorAll('[data-comparison]')) {
  const slider = comparison.querySelector('input');
  const update = () => comparison.style.setProperty('--position', slider.value + '%');

  slider.addEventListener('input', update);
  update();
}
