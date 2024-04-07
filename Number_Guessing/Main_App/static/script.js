const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
  const p1 = document.getElementById('p1');

  if (p1.style.display === 'none') {
    // 👇️ this SHOWS the form
    p1.style.display = 'block';
  } else {
    // 👇️ this HIDES the form
    p1.style.display = 'none';
  }
});