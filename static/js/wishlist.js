document.addEventListener('DOMContentLoaded', function() {
    // Initialize wishlist functionality
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
    const originalText = button.innerHTML;
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
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update button state
            updateWishlistButton(productId, data.in_wishlist);
            
            // Show success message
            showMessage(data.message, 'success');
        } else {
            showMessage(data.message || 'An error occurred', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showMessage('An error occurred while updating wishlist', 'error');
    })
    .finally(() => {
        // Restore button state
        button.innerHTML = originalText;
        button.disabled = false;
    });
}

function updateWishlistButton(productId, inWishlist) {
    const container = document.querySelector(`[data-product-id="${productId}"]`);
    if (!container) return;
    
    const addForm = container.querySelector('form[action*="add"]');
    const removeForm = container.querySelector('form[action*="remove"]');
    
    if (inWishlist) {
        // Show remove button
        addForm.style.display = 'none';
        removeForm.style.display = 'inline';
    } else {
        // Show add button
        addForm.style.display = 'inline';
        removeForm.style.display = 'none';
    }
}

function checkWishlistStatuses() {
    // Get all product IDs on the page
    const productIds = Array.from(document.querySelectorAll('[data-product-id]'))
        .map(el => el.dataset.productId)
        .filter((id, index, arr) => arr.indexOf(id) === index); // Remove duplicates
    
    // Check status for each product
    productIds.forEach(productId => {
        fetch(`/wishlist/check/${productId}/`)
            .then(response => response.json())
            .then(data => {
                updateWishlistButton(productId, data.in_wishlist);
            })
            .catch(error => {
                console.error('Error checking wishlist status:', error);
            });
    });
}

function showMessage(message, type) {
    // Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show position-fixed`;
    messageDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    messageDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Add to page
    document.body.appendChild(messageDiv);
    
    // Auto-remove after 3 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.remove();
        }
    }, 3000);
}

// Export functions for use in other scripts
window.WishlistManager = {
    initializeWishlist,
    handleWishlistClick,
    updateWishlistButton,
    checkWishlistStatuses,
    showMessage
}; 