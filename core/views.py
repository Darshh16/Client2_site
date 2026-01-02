from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product, Client, Service, Project

def home(request):
    categories = ProductCategory.objects.all()
    clients = Client.objects.all()
    # Maybe get some featured products?
    featured_products = Product.objects.all()[:4]
    return render(request, 'index.html', {
        'categories': categories,
        'clients': clients,
        'featured_products': featured_products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = ProductCategory.objects.all() # Needed for navbar everywhere
    return render(request, 'product_detail.html', {
        'product': product,
        'categories': categories
    })

def services_page(request):
    services = Service.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'services.html', {
        'services': services,
        'categories': categories
    })

def projects_page(request):
    projects = Project.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'projects.html', {
        'projects': projects,
        'categories': categories
    })

def contact_page(request):
    categories = ProductCategory.objects.all()
    return render(request, 'contact.html', {'categories': categories})

def category_detail(request, slug):
    current_category = get_object_or_404(ProductCategory, slug=slug)
    products = current_category.products.all()
    categories = ProductCategory.objects.all()
    return render(request, 'category_detail.html', {
        'category': current_category,
        'products': products,
        'categories': categories
    })

def about_page(request):
    categories = ProductCategory.objects.all()
    return render(request, 'about.html', {'categories': categories})
