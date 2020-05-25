from django.shortcuts import render
from cltgm import constants

def home(request):
    name = "Riley"
    context = {
        'constants': constants,
    }
    return render(request, 'cltgm/index.html', context)
