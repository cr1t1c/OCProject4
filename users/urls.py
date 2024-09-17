""" Defines URL patterns for accounts. """

from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    # Login page
    path('', views.login_page, name='login'),
    # Logout page
    path('users/logout/', views.logout_user, name='logout'),
    # Registration page
    path("users/signup/", views.signup, name="signup"),
]