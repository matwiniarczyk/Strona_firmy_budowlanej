from django.shortcuts import render, redirect

from website_app.forms import ContactForm
from website_app.models import ServiceOffers, MessagesFromForm, ProjectsDone, FrequentlyAsked


def home_view(request):
    services = ServiceOffers.objects.all()
    return render(request, 'home.html', {'services': services})


def cost_estimate_view(request):
    services = ServiceOffers.objects.all()
    return render(request, 'cost_estimate.html', {'services': services})


def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            MessagesFromForm.objects.create(**form.cleaned_data)

            return redirect('form_sent')

    return render(request, 'contact.html', {'form': form})


def form_sent_view(request):
    return render(request, 'form_sent.html')


def projects_galery_view(request):
    projects = ProjectsDone.objects.all()
    return render(request, 'projects_galery.html', {'projects': projects})


def faq_view(request):
    frequently_asked = FrequentlyAsked.objects.all()
    return render(request, 'FAQ.html', {'frequently_asked': frequently_asked})
