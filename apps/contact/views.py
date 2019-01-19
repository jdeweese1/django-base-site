from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import ContactCreateForm
from .models import Contact


# Create your views here.
class ContactFormView(generic.FormView, generic.CreateView):
    form_class = ContactCreateForm
    template_name = 'contact/contact.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def post(self, request):
        sender_name = request.POST.get('sender_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(sender_name=sender_name, email=email, subject=subject, message=message, created=timezone.now())
        return redirect(reverse('contact:contact_submitted'))  # add a list view


def contact_submitted(request):
    return HttpResponse(render_to_string('contact/contact_submitted.html', request=request))


class ContactListView(generic.ListView):
    model = Contact

    def get_queryset(self):
        qs = Contact.objects.all().order_by('-created')
        return qs



class ContactDetailView(generic.DetailView):
    model = Contact
    template_name = 'contact/contact_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        self.object.is_read = True  # Because we are loading the Detail View, the Contact object is now read
        self.object.save()
        return context
