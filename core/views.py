# core/views.py

from django.shortcuts import render, redirect
from .models import HomePage, AboutPage, ContactPage, Testimonial
from product.models import Product
from .forms import ContactForm

def home(request):
    page = HomePage.objects.first()
    featured_products = Product.objects.filter(featured=True)[:4]
    testimonials = Testimonial.objects.all()
    context = {
        'page': page,
        'featured_products': featured_products,
        'testimonials': testimonials
    }
    return render(request, 'core/home.html', context)

def about(request):
    page = AboutPage.objects.first()  # Assuming there is only one AboutPage entry
    return render(request, 'core/about.html', {'page': page})



def contact(request):
    page = ContactPage.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle success (e.g., redirect or display a success message)
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'page': page, 'form': form})
