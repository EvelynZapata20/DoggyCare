from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view.as_view(), name='login'),
    path('vet_signup/', views.vet_signup.as_view(), name='vet_signup'),
    path('owner_signup/', views.owner_signup.as_view(), name='owner_signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('manage_vet/', views.manage_vet, name='manage_vet'),
    path('manage_owner/', views.manage_owner, name='manage_owner'),
]