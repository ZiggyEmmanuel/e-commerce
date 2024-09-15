#dashboard/views.py
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Order
from core.models import Testimonial
from core.forms import TestimonialForm
from payment.models import BillingAddress

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)
        context['billing_address'] = BillingAddress.objects.filter(user=self.request.user).first()
        
        # Add the testimonial form and existing testimonials to the context
        context['form'] = TestimonialForm()
        context['testimonials'] = Testimonial.objects.filter(user=self.request.user)
        
        return context

    def post(self, request, *args, **kwargs):
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            return self.get(request, *args, **kwargs)
        return self.render_to_response(self.get_context_data(form=form))
