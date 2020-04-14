from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('single-blog/',views.single,name='singleb'),
    path('contact/',views.contact,name='contact'),
    path('about/', views.about, name='apropos'),
    path('category/', views.category, name='categories'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    

]
