from django.shortcuts import render
from shop.models import Goods
from django.views.generic.list import ListView


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def iphone_view(request):
    return render(request, 'iphone.html')


class IpadListView(ListView):
    model = Goods
    template_name = 'ipad.html'


class MacListView(ListView):
    model = Goods
    template_name = 'mac.html'


class IwatchListView(ListView):
    model = Goods
    template_name = 'iwatch.html'


def about_view(request):
    return render(request, 'about.html')


def contacts_view(request):
    return render(request, 'contacts.html')
