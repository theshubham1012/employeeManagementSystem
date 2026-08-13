from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),

    # Employee urls details
    path('add-employee/', views.addEmployee, name='add-employee'),
    path('edit-employee/<str:pk>/', views.editEmployee, name='edit-employee'),
    path('delete-employee/<str:pk>/', views.deleteEmployee, name='delete-employee'),

    # Client urls
    path('mark-attendance/',views.updateAttendance, name='mark-attendance'),
    path('add-client/', views.addClient, name='add-client'),
    path('edit-client/<int:pk>/', views.editClient, name='edit-client'),
    path('delete-client/<int:pk>/', views.deleteClient, name='delete-client'),

    #Site urls
    path('add-site/',views.addSite, name='add-site'),
    path('edit-site/<int:pk>/', views.editSite, name='edit-site'),
    path('delete-site/<int:pk>/', views.deleteSite, name='delete-site'),

    #designation urls
    path('add-designation/',views.addDesignation, name='add-designation'),
    path('edit-designation/<int:pk>/', views.editDesignation, name='edit-designation'),
    path('delete-designation/<int:pk>/', views.deleteDesignation, name='delete-designation'),

    # for sheets
    path('all-employees/', views.allEmployees, name='all-employees'),
    path('all-employees-salary/',views.allEmployeesSalary, name='all-employees-salary'),
    path('all-employee-salaryslips/', views.salarySlips, name='salary-slips'),
    path('all-sites/', views.allSites, name='all-sites'),
    path('all-clients/', views.allClients, name='all-clients'),

    #for editing data from sheets
    path('edit-all-employees/', views.editAllEmployees, name='edit-all-employees'),
    path('edit-all-clients/', views.editAllClients, name='edit-all-clients'),
    path('edit-all-sites/', views.editAllSites, name='edit-all-site'),
    path('edit-all-designations/', views.editAllDesignations, name='edit-all-designations')
]