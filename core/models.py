from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Categories"

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    features = models.TextField(help_text="Enter features separated by newlines", blank=True)
    whatsapp_number = models.CharField(max_length=20, default='+919833010277', help_text="Number for inquiry (without spaces)")

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Image for {self.product.name}"

class ProductVideo(models.Model):
    product = models.ForeignKey(Product, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='products/videos/', help_text="Upload video file")
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title or f"Video for {self.product.name}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="FontAwesome icon class (e.g., 'fa-cogs') or similar", default='fa-cogs')
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    completion_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')

    def __str__(self):
        return f"Image for {self.project.title}"

class ProjectVideo(models.Model):
    project = models.ForeignKey(Project, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='projects/videos/', help_text="Upload video file")
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title or f"Video for {self.project.title}"
