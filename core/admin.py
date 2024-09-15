#core/admin

from django.contrib import admin
from .models import HomePage, AboutPage, ContactPage, Testimonial

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'email', 'message')
 

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')

