// Star Rating Functionality
document.addEventListener('DOMContentLoaded', function() {
    const starContainers = document.querySelectorAll('.star-rating');
    
    starContainers.forEach(container => {
        const stars = container.querySelectorAll('.star');
        const hiddenInput = container.querySelector('input[type="hidden"]');
        const ratingText = container.querySelector('.rating-text');
        const currentRating = parseInt(container.dataset.currentRating) || 0;
        
        // Set initial state
        updateStars(currentRating);
        updateRatingText(currentRating);
        
        stars.forEach(star => {
            const rating = parseInt(star.dataset.rating);
            
            // Click event
            star.addEventListener('click', function() {
                updateStars(rating);
                updateRatingText(rating);
                hiddenInput.value = rating;
            });
            
            // Hover events
            star.addEventListener('mouseenter', function() {
                highlightStars(rating);
            });
            
            star.addEventListener('mouseleave', function() {
                updateStars(parseInt(hiddenInput.value) || 0);
            });
        });
        
        function updateStars(rating) {
            stars.forEach((star, index) => {
                if (index < rating) {
                    star.classList.add('active');
                } else {
                    star.classList.remove('active');
                }
            });
        }
        
        function highlightStars(rating) {
            stars.forEach((star, index) => {
                if (index < rating) {
                    star.style.color = '#ffd700';
                } else {
                    star.style.color = '#ddd';
                }
            });
        }
        
        function updateRatingText(rating) {
            if (rating > 0) {
                ratingText.textContent = `${rating} out of 5 stars`;
            } else {
                ratingText.textContent = 'Click to rate';
            }
        }
    });
}); 