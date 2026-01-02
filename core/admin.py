from django.contrib import admin
from .models import ProductCategory, Product, ProductImage, ProductVideo, Client, Service, Project, ProjectImage, ProjectVideo

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [ProductImageInline, ProductVideoInline]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'completion_date')
    search_fields = ('title', 'client_name')
    inlines = [ProjectImageInline, ProjectVideoInline]
