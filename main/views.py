from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View, DetailView
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


class HomeDebat(ListView):
    paginate_by = 4
    model = Debat
    template_name = 'index.html'
    form = ThemeForm()
    context_object_name = 'Debats'
    extra_context = {
        'title': 'title',
        'form': form,
        'themes': Theme.objects.all().order_by('-rating'),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


def offer_theme(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            Theme.objects.create(**form.cleaned_data)
            print(form.cleaned_data)
            return redirect('main')


class DebatByTheme(ListView):
    paginate_by = 4
    model = Debat
    template_name = 'index.html'
    context_object_name = 'Debats'
    extra_context = {
        'themes': Theme.objects.all().order_by('-rating'),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Theme.objects.get(pk=self.kwargs['theme_id'])
        return context

    def get_queryset(self):
        return Debat.objects.filter(theme_id=self.kwargs['theme_id']).select_related('theme')


class StartDebat(CreateView):
    form_class = StartDebatForm
    template_name = 'startdebat.html'
    extra_context = {
        'themes': Theme.objects.all(),
    }

    def post(self, request, *args, **kwargs):
        form = StartDebatForm(request.POST)
        if form.is_valid():
            form.cleaned_data['theme_id'] = request.POST.get('theme-id')
            Debat.objects.create(**form.cleaned_data).members.add(request.user.id)
            print(form.cleaned_data)
            return redirect('main')


class DebatPage(ListView):
    model = Debat
    template_name = 'debat_page.html'
    context_object_name = 'debats'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Debat - ' + str(self.kwargs['debat_id'])
        return context

    def get_queryset(self):
        return Debat.objects.get(id=self.kwargs['debat_id'])


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        context = {
            'form': UserLoginForm(),
        }
        return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('main')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        context = {
            'form': UserRegisterForm()
        }
        return render(request, 'register.html', context)

def all_themes(request):
    themes = Theme.objects.all()
    context = {
        'themes':themes
    }
    return render(request, 'themes.html', context)