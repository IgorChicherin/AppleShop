from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import Registration

# Create your views here.

def registration_view(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/auth/login/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': Registration()}
    return render(request, 'registration.html', context)
