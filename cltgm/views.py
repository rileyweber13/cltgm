import configparser

from django.core.mail import send_mail
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
    return render(request, 'cltgm/info/contact-me.html', context)

def not_found(request):
    context = {
        'constants': constants,
    }
    return render(request, 'cltgm/404.html', context)

def send_email(request):
    if request.method == 'GET':
        form = forms.ContactForm()
        return redirect('404')
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            config = configparser.ConfigParser()
            config.read('cltgm/config.ini')

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, 
                    message, 
                    from_email, 
                    [config['secrets']['business_contact_email']])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "contact-me", {'form': form})
