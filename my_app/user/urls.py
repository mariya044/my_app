from django.contrib.auth.views import LogoutView
from django.urls import path, include
from user.views import SignUpView, LoginView
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path("accounts/logout/", LogoutView.as_view(), name="logout")

]
