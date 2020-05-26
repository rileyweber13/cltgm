import configparser

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cltgm import constants, forms

def home(request):
    context = {
        'constants': constants,
        'navbar_home_classes': "active",
    }
    return render(request, 'cltgm/index.html', context)

def what_is_dnd(request):
    context = {
        'constants': constants,
        'navbar_what_is_dnd_classes': "active",
    }
    return render(request, 'cltgm/info/what-is-dnd.html', context)

def pricing(request):
    context = {
        'constants': constants,
        'navbar_pricing_classes': "active",
    }
    return render(request, 'cltgm/info/pricing.html', context)

def for_parents(request):
    context = {
        'constants': constants,
        'navbar_for_parents_classes': "active",
    } 
    return render(request, 'cltgm/info/for-parents.html', context)

def contact_me(request):
    context = {
        'constants': constants,
        'navbar_contact_me_classes': "active",
    }

    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            config = configparser.ConfigParser()
            config.read('cltgm/config.ini')

            subject = form.cleaned_data['subject']
            author_email = form.cleaned_data['author_email']
            author_name = form.cleaned_data['author_name']
            message = "This is an email sent using the 'contact me' page on " \
                + "the " + constants.BUSINESS_NAME + " website.\n" \
                + "Author's name: " + author_name + "\n" \
                + "Author's email: " + author_email + "\n" \
                + "Subject: " + subject + "\n" \
                + "Message: \n" \
                + form.cleaned_data['message']

            try:
                send_mail(subject, 
                    message, 
                    author_email, 
                    [config['server_settings']['business_contact_email']])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            context['form_status'] = "success"
        
        else:
            # form is not valid
            context['form'] = form
            context['form_status'] = "invalid"

    return render(request, 'cltgm/info/contact-me.html', context)

def not_found(request):
    context = {
        'constants': constants,
    }
    return render(request, 'cltgm/404.html', context)
