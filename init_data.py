import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import ProductCategory, Product

def init_data():
    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created with password 'admin123'")

    # Create Categories
    cat_rolling, _ = ProductCategory.objects.get_or_create(name='Rolling Shutter', slug='rolling-shutter')
    cat_sliding, _ = ProductCategory.objects.get_or_create(name='Sliding Gates', slug='sliding-gates')
    # Removed High Speed Doors and Dock Levelers as per requirement

    # Create Sample Product
    if not Product.objects.filter(slug='motorised-rolling-shutter').exists():
        Product.objects.create(
            category=cat_rolling,
            name='Motorised Rolling Shutter',
            slug='motorised-rolling-shutter',
            description='Perfect for industrial warehouses and commercial storefronts. Our motorised shutters provide ease of operation with robust security.',
            features='Remote Control Operation\nManual Override Chain\nWind Lock System\nNoise Reduction Technology',
            whatsapp_number='+918767825705'
        )
        print("Sample Product Created: Motorised Rolling Shutter")

    print("Initialization Complete.")

if __name__ == '__main__':
    init_data()
