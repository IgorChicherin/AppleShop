from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from registration.forms import Registration
from django.template.context_processors import csrf
from django.template import loader
from django.http import Http404, JsonResponse
from shop.models import Goods, Category
from shop.forms import MacContent
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.
@user_passes_test(lambda user: user.is_superuser)
def admin_view(request):
    users = User.objects.all()
    user_form = Registration()
    context = {'users': users, 'form': user_form}
    return render(request, 'admin.html', context)


def get_user(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        form = Registration(instance=user)
        context = {'form': form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration-form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def del_user(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user.delete()
        users = User.objects.all()
        html = loader.render_to_string('inc-user-list.html', {'users': users})
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


class ManageConntentListView(ListView):
    model = Goods
    template_name = 'manage_content.html'


def edit_content(request, item_id):
    item = get_object_or_404(Goods, id=item_id)
    if request.method == 'POST':
        form = MacContent(request.POST, files=request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/content/')
        context = {'form': form}
        return render(request, 'edit_content.html', context)
    context = {'form': MacContent(instance=item)}
    return render(request, 'edit_content.html', context)


def delete_content(request, item_id):
    if request.is_ajax():
        item = get_object_or_404(Goods, id=item_id)
        item.delete()
        macs = Goods.objects.all()
        html = loader.render_to_string('inc-registration-form.html', {'macs': macs})
        data = {'errors': False, 'html': html}
        JsonResponse(data)
    raise Http404


def add_content(request):
    if request.method == 'POST':
        form = MacContent(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/content')
        context = {'form': form}
        return render(request, 'edit_content.html', context)
    context = {'form': MacContent()}
    return render(request, 'edit_content.html', context)


class PreviewContentDetailView(DetailView):
    model = Goods
    template_name = 'preview_content.html'


class CategoriesListView(ListView):
    model = Category
    template_name = 'manage_content.html'


class CategoriesCreateView(CreateView):
    model = Category
    template_name = 'edit_content.html'
    success_url = '/admin/categories/'
    fields = '__all__'


def delete_category(request, item_id):
    if request.is_ajax():
        item = get_object_or_404(Category, id=item_id)
        item.delete()
        cat = Category.objects.all()
        html = loader.render_to_string('inc-registration-form.html', {'cat': cat})
        data = {'errors': False, 'html': html}
        JsonResponse(data)
    raise Http404


class CategoriesUpdateView(UpdateView):
    model = Category
    template_name = 'edit_content.html'
    success_url = '/admin/categories/'
    fields = '__all__'
