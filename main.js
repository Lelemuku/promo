// ===== DYNAMIC THEME LOADER =====
// Auto-detect brand color from CSS variables or data attribute
(function() {
  const root = document.documentElement;
  const brandColor = getComputedStyle(root).getPropertyValue('--brand-color').trim();

  // Apply brand color to all dynamic elements
  if (brandColor) {
    document.querySelectorAll('.brand-dynamic').forEach(el => {
      el.style.color = brandColor;
    });
  }
})();

// ===== RIPPLE EFFECT =====
document.querySelectorAll('.link-card').forEach(card => {
  card.addEventListener('click', function (e) {
    const ripple = document.createElement('span');
    const rect = this.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;

    ripple.style.cssText = `
      position:absolute;
      width:${size}px;height:${size}px;
      left:${x}px;top:${y}px;
      border-radius:50%;
      background:rgba(201,168,76,0.12);
      transform:scale(0);
      animation:ripple 0.5s ease-out forwards;
      pointer-events:none;
    `;
    this.appendChild(ripple);
    setTimeout(() => ripple.remove(), 600);
  });
});

// Inject ripple keyframe
const style = document.createElement('style');
style.textContent = `@keyframes ripple { to { transform:scale(2.5); opacity:0; } }`;
document.head.appendChild(style);

// ===== CLICK ANALYTICS (Optional) =====
// Track link clicks - can be connected to Google Analytics or custom backend
document.querySelectorAll('.link-card').forEach(card => {
  card.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    const title = this.querySelector('.link-title')?.textContent || 'Unknown';

    // Log to console (replace with actual analytics)
    console.log(`[CLICK] ${title} → ${href}`);

    // Example: Send to analytics endpoint
    // fetch('/api/analytics/click', { method: 'POST', body: JSON.stringify({ url: href, title }) });
  });
});

// ===== SMOOTH SCROLL FOR ANCHORS =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth' });
  });
});
