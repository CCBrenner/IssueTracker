from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib.auth import logout
# from django.views.decorators.cache import cache_control
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm


def about_view(request):
    template = 'users/about.html'
    return render(request, template)


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    template = 'users/register.html'
    context = {'form': form}
    return render(request, template, context)


# For some reason could not get cache control to disable user
# from going back to a page that requires a login
# @cache_control(no_cache=True, must_revalidate=True)
# def logout_view(request):
#     logout(request)
#     return render(request, 'users/logout.html')


class UserUpdateView(UpdateView):

    model = User
    template_name = 'users/user_update.html'
    fields = ['first_name', 'last_name', 'email']
    context = 'user'
    success_url = reverse_lazy('track:track-home')
