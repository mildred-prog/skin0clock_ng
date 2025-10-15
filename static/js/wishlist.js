document.addEventListener('DOMContentLoaded', function () {
  initializeWishlist();
});

function initializeWishlist() {
  // Add event listeners to wishlist buttons
  document.querySelectorAll('.wishlist-btn').forEach(button => {
    button.addEventListener('click', handleWishlistClick);
  });

  // Check wishlist status for all products on page load
  checkWishlistStatuses();
}

function handleWishlistClick(event) {
  event.preventDefault();

  const button = event.target.closest('.wishlist-btn');
  const form = button.closest('.wishlist-form');
  const productId = button.dataset.productId;

  // Show loading state
  const originalHTML = button.innerHTML;
  button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
  button.disabled = true;

  // Submit form via AJAX
  fetch(form.action, {
    method: 'POST',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
    }
  })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        updateWishlistButton(productId, data.in_wishlist);
        showMessage(data.message, 'success');
      } else {
         showMessage(data.message || 'An error occurred', 'error');
      }
    })
    .catch(err => {
      showMessage('An error occurred while updating wishlist', 'error');
    })
    .finally(() => {
      // Restore button state
      button.disabled = false;
    });
}

function updateWishlistButton(productId, inWishlist) {
  // Be specific: only pick the container div, not the button
  const container = document.querySelector(
    `.wishlist-button-container[data-product-id="${productId}"]`
  );
  if (!container) return;

  const form = container.querySelector('form.wishlist-form');
  if (!form) return;

  const btn = form.querySelector('.wishlist-btn');
  if (!btn) return;

  // Prefer explicit URLs if provided via data-*; otherwise fall back to pattern
  const addUrl = container.dataset.addUrl || `/wishlist/add/${productId}/`;
  const removeUrl = container.dataset.removeUrl || `/wishlist/remove/${productId}/`;

  if (inWishlist) {
    // Make this a "remove" form/button
    form.action = removeUrl;
    btn.classList.remove('btn-primary');
    btn.classList.add('btn-danger');
    btn.setAttribute('aria-label', `Remove from Wishlist for ${btn.getAttribute('aria-label')?.replace(/^Add to Wishlist for /, '') || ''}`);
    btn.innerHTML = `<i class="fas fa-heart-broken" aria-hidden="true"></i> Remove from Wishlist`;
  } else {
    // Make this an "add" form/button
    form.action = addUrl;
    btn.classList.remove('btn-danger');
    btn.classList.add('btn-primary');
    btn.setAttribute('aria-label', `Add to Wishlist for ${btn.getAttribute('aria-label')?.replace(/^Remove from Wishlist for /, '') || ''}`);
    btn.innerHTML = `<i class="fas fa-heart" aria-hidden="true"></i> Add to Wishlist`;
  }
}

function checkWishlistStatuses() {
  // Only collect IDs from the dedicated containers (avoid grabbing buttons)
  const productIds = Array.from(
    document.querySelectorAll('.wishlist-button-container[data-product-id]')
  )
    .map(el => el.dataset.productId)
    .filter((id, i, arr) => arr.indexOf(id) === i);

  productIds.forEach(productId => {
    fetch(`/wishlist/check/${productId}/`)
      .then(r => r.json())
      .then(data => {
        updateWishlistButton(productId, data.in_wishlist);
      })
      .catch(error => {
        console.error('Error checking wishlist status:', error);
      });
  });
}

function showMessage(message, type) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show position-fixed`;
  messageDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
  messageDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
  document.body.appendChild(messageDiv);
  setTimeout(() => messageDiv.remove(), 3000);
}

window.WishlistManager = {
  initializeWishlist,
  handleWishlistClick,
  updateWishlistButton,
  checkWishlistStatuses,
  showMessage
};
