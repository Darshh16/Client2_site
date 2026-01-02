import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import ProductCategory

def remove_extras():
    # Delete High Speed Doors and Dock Levelers
    categories_to_delete = ['High Speed Doors', 'Dock Levelers']
    
    for cat_name in categories_to_delete:
        try:
            category = ProductCategory.objects.get(name=cat_name)
            category.delete()
            print(f"Deleted category: {cat_name}")
        except ProductCategory.DoesNotExist:
            print(f"Category not found (already deleted): {cat_name}")

if __name__ == '__main__':
    remove_extras()
