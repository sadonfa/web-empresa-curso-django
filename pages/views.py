from django.shortcuts import render
from .models import Page
# Create your views here.

def sample(request, page_id ):

    page = Page.objects.get(id=page_id)

    return render(request, 'pages/sample.html', {
        'page': page
    })