import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import ProductCategory, Product

def populate_products():
    # 1. Rolling Shutters
    rolling_cat, _ = ProductCategory.objects.get_or_create(name='Rolling Shutter', defaults={'slug': 'rolling-shutter'})
    
    rolling_products = [
        "Motorised Rolling Shutters",
        "GI Rolling Shutter",
        "Double Wall Rolling Shutter",
        "Aluminium Rolling Shutter",
        "Puff Insulated Rolling Shutter",
        "MS Rolling Shutters",
        "Fire Rated Rolling Shutters",
        "Fire Rated Doors"
    ]

    print(f"Populating {rolling_cat.name}...")
    for prod_name in rolling_products:
        slug = slugify(prod_name)
        if not Product.objects.filter(slug=slug).exists():
            Product.objects.create(
                category=rolling_cat,
                name=prod_name,
                slug=slug,
                description=f"Premium quality {prod_name} designed for maximum security and durability. Ideal for industrial and commercial applications.",
                features="High durability\nCustom sizes available\nLow maintenance\nWeather resistant",
                whatsapp_number="+919876543210"
            )
            print(f"  Created: {prod_name}")
        else:
            print(f"  Skipped (exists): {prod_name}")

    # 2. Sliding Gates
    sliding_cat, _ = ProductCategory.objects.get_or_create(name='Sliding Gates', defaults={'slug': 'sliding-gates'})
    
    sliding_products = [
        "Motorised Sliding Gates",
        "Cantilever Sliding Gates",
        "Swing Gates",
        "Telescopic Sliding Gates",
        "Sliding Folding Gate" # Requested extra
    ]

    print(f"Populating {sliding_cat.name}...")
    for prod_name in sliding_products:
        slug = slugify(prod_name)
        if not Product.objects.filter(slug=slug).exists():
            Product.objects.create(
                category=sliding_cat,
                name=prod_name,
                slug=slug,
                description=f"Advanced {prod_name} offering seamless operation and robust protection. Engineered for smooth performance.",
                features="Smooth operation\nRemote control compatible\nHeavy duty construction\nModern design",
                whatsapp_number="+919876543210"
            )
            print(f"  Created: {prod_name}")
        else:
            print(f"  Skipped (exists): {prod_name}")

if __name__ == '__main__':
    populate_products()
