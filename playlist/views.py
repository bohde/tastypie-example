# Create your views here.
from django.shortcuts import render

def index(request):
    #logger.debug(request.user.profile)
    ctx = locals()
    return render(request, 'index.html', ctx)