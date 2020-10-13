from django.shortcuts import render

# Create your views here.
from forms.forms import AuthorForm


def index(request):
    return render(request, 'forms/index.html', { 'form': AuthorForm()})
