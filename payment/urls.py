#payment/urls

from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='payment_success'),
    path('cancel/', views.cancel, name='payment_cancel'),
]
