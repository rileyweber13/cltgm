from django.shortcuts import render
from cltgm import constants

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
