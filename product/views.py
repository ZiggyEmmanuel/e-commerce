# product/views.py


from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Review
from .forms import ProductFilterForm, ReviewForm
from urllib.parse import urlencode

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Initialize the form with the request's GET data
    form = ProductFilterForm(request.GET)
    
    if request.method == 'GET':
        if form.is_valid():
            # Apply filters
            min_price = form.cleaned_data.get('min_price')
            if min_price:
                products = products.filter(price__gte=min_price)
            
            max_price = form.cleaned_data.get('max_price')
            if max_price:
                products = products.filter(price__lte=max_price)
            
            if form.cleaned_data.get('discount'):
                products = products.filter(discount_price__isnull=False)
            
            sort_by = form.cleaned_data.get('sort_by')
            if sort_by:
                products = products.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(products, 4)  # Show 4 products per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if not specified
    page_obj = paginator.get_page(page_number)
    
    # Preserve filter parameters in pagination links
    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']  # Remove existing page parameter
    
    return render(request, 'product/product_list.html', {
        'category': category,
        'categories': categories,
        'page_obj': page_obj,
        'form': form,
        'query_params': query_params
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = product.reviews.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product:product_detail', id=product.id, slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, 'product/product_detail.html', {
        'product': product,
        'form': form,
        'reviews': reviews
    })


def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = Product.objects.none()
    return render(request, 'product/search_results.html', {'results': results, 'query': query})
