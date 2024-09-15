from django.db import models
from django.conf import settings

class HomePage(models.Model):
    title = models.CharField(max_length=100, default='Home')
    content = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'

    def __str__(self):
        return self.title

class AboutPage(models.Model):
    title = models.CharField(max_length=100, default='About Us')
    content = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Pages'

    def __str__(self):
        return self.title

class ContactPage(models.Model):
    title = models.CharField(max_length=100, default='Contact Us')
    content = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # New phone number field
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Pages'

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Testimonial from {self.user.first_name}'
