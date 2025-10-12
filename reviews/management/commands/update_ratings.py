from django.core.management.base import BaseCommand
from products.models import Product
from reviews.models import Review
from django.db.models import Avg


class Command(BaseCommand):
    help = 'Update product ratings based on existing reviews'

    def handle(self, *args, **options):
        """
        Update all product ratings based on their existing reviews.
        This command calculates the average rating for each product
        and updates the product's rating field.
        """
        self.stdout.write('Starting to update product ratings...')
        
        updated_count = 0
        products = Product.objects.all()
        
        for product in products:
            reviews = Review.objects.filter(product=product)
            
            if reviews.exists():
                avg_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
                product.rating = round(avg_rating, 2)
                product.save(update_fields=['rating'])
                updated_count += 1
                self.stdout.write(
                    f'Updated {product.name}: {product.rating}/5 '
                    f'({reviews.count()} reviews)'
                )
            else:
                product.rating = None
                product.save(update_fields=['rating'])
                self.stdout.write(f'No reviews for {product.name}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully updated ratings for {updated_count} products'
            )
        )

