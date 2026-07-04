from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),

    # Employee urls details
    path('add-employee/', views.addEmployee, name='add-employee'),
    path('edit-employee/<str:pk>/', views.editEmployee, name='edit-employee'),
    path('delete-employee/<str:pk>/', views.deleteEmployee, name='delete-employee'),

    # Client urls
    path('mark-attendance/',views.markAttendance, name='mark-attendance'),
    path('add-client/', views.addClient, name='add-client'),
    path('add-site/',views.addSite, name='add-site'),
    path('add-designation/',views.addDesignation, name='add-designation'),

    # for sheets
    path('all-employees/', views.allEmployees, name='all-employees'),
]