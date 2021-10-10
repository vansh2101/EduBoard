from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('classes/', views.meets, name='classes'),
    path('assignments/', views.assignments, name='assignments'),
    path('circulars/', views.circulars, name='circulars'),
    path('ebooks/', views.ebooks, name='ebooks'),
    path('add/<str:task>/', views.forms, name='forms'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
]