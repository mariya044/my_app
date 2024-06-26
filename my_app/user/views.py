from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import request
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from user.forms import CustomUserCreationForm
from user.models import MyUser


# def users(request):
#     users_list = MyUser.objects.all()
#     paginator=Paginator(users_list,5)
#     page_number=request.GET.get('page',1)
#     users=paginator.page(page_number)
#     return render(request, "UsersList.html", {"users": users})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # user_group = Group.objects.get()
            # user.groups.add(user_group)
            return redirect("/")
        else:
            return render(request, self.template_name, {'form': form})


class LoginView(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return self.render_to_response(self.get_context_data())