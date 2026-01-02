"""
Image Compression Script for Riddhi Siddhi Rolling Shutter Website
This script compresses all images in static/images and media/products folders
while maintaining visual quality.
"""

import os
from PIL import Image
from pathlib import Path

def compress_image(image_path, quality=85, max_width=1920):
    """
    Compress a single image file.
    
    Args:
        image_path: Path to the image file
        quality: JPEG quality (1-100, default 85)
        max_width: Maximum width in pixels (default 1920)
    """
    try:
        # Open image
        img = Image.open(image_path)
        
        # Get original size
        original_size = os.path.getsize(image_path)
        
        # Convert RGBA to RGB if needed (for JPEG)
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        # Resize if image is too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            print(f"  ↳ Resized to {max_width}x{new_height}")
        
        # Save with compression
        if image_path.suffix.lower() in ['.jpg', '.jpeg']:
            img.save(image_path, 'JPEG', quality=quality, optimize=True)
        elif image_path.suffix.lower() == '.png':
            img.save(image_path, 'PNG', optimize=True)
        else:
            print(f"  ↳ Skipped (unsupported format)")
            return
        
        # Get new size
        new_size = os.path.getsize(image_path)
        reduction = ((original_size - new_size) / original_size) * 100
        
        print(f"  ✓ {original_size // 1024}KB → {new_size // 1024}KB (Saved {reduction:.1f}%)")
        
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")


def compress_directory(directory, quality=85, max_width=1920):
    """
    Compress all images in a directory.
    
    Args:
        directory: Path to directory
        quality: JPEG quality (1-100)
        max_width: Maximum width in pixels
    """
    directory = Path(directory)
    
    if not directory.exists():
        print(f"⚠ Directory not found: {directory}")
        return
    
    print(f"\n📁 Processing: {directory}")
    print("=" * 60)
    
    # Supported image formats
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    
    # Find all images
    image_files = []
    for ext in image_extensions:
        image_files.extend(directory.rglob(f'*{ext}'))
        image_files.extend(directory.rglob(f'*{ext.upper()}'))
    
    if not image_files:
        print("  No images found.")
        return
    
    print(f"Found {len(image_files)} images\n")
    
    # Compress each image
    for img_path in image_files:
        print(f"📷 {img_path.name}")
        compress_image(img_path, quality=quality, max_width=max_width)


def main():
    """Main function to compress all website images."""
    
    print("\n" + "=" * 60)
    print("🖼️  IMAGE COMPRESSION TOOL")
    print("=" * 60)
    print("\nThis will compress images in:")
    print("  • static/images/")
    print("  • media/products/")
    print("\nSettings:")
    print("  • Quality: 85% (high quality)")
    print("  • Max Width: 1920px")
    print("  • Maintains aspect ratio")
    print("\n" + "=" * 60)
    
    # Get base directory
    base_dir = Path(__file__).parent
    
    # Compress static images
    static_images = base_dir / 'static' / 'images'
    compress_directory(static_images, quality=85, max_width=1920)
    
    # Compress media/product images
    media_products = base_dir / 'media' / 'products'
    compress_directory(media_products, quality=85, max_width=1920)
    
    print("\n" + "=" * 60)
    print("✅ COMPRESSION COMPLETE!")
    print("=" * 60)
    print("\nRecommendations:")
    print("  • Clear browser cache (Ctrl + F5)")
    print("  • Test website loading speed")
    print("  • Check image quality on key pages")
    print("\n")


if __name__ == "__main__":
    main()
