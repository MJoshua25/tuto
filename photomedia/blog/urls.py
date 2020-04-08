from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('single-blog/',views.single,name='singleb'),
    path('contact/',views.contact,name='contact'),
    path('about/', views.about, name='apropos'),
    path('category/', views.category, name='categories'),

]
