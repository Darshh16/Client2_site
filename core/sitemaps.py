from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, ProductCategory, Project

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'services', 'projects', 'contact', 'about']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.created_at if hasattr(obj, 'created_at') else None


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return ProductCategory.objects.all()

    def location(self, obj):
        return reverse('category_detail', args=[obj.slug])


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.date if hasattr(obj, 'date') else None
