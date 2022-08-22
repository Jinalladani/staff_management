"""staff_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admin_panel import views
from .check_me import check_user, login_user

urlpatterns = [
    path('admindashbord', check_user(views.admindashbord), name="admindashbord"),
    path('', views.adminlogin, name="adminlogin"),
    path('adminlogout', views.adminlogout, name="adminlogout"),

    path('staff_list', check_user(views.staff_list), name="staff_list"),
    path('addnewStaff', check_user(views.addnewStaff), name="addnewStaff"),
    path('editStaff/<int:id>', check_user(views.editStaff), name="editStaff"),
    path('deleteStaff/<int:id>', check_user(views.deleteStaff), name="deleteStaff"),
    path('statusChange<int:id>', views.statusChange),

    path('adminstaffTaskSheet', check_user(views.adminstaffTaskSheet), name="adminstaffTaskSheet"),
    path('taskStatusChange/<int:id>', views.taskStatusChange, name="taskStatusChange"),
    path('deleteTask', views.deleteTask, name="deleteTask"),
    path('taskStatus', views.taskStatus, name="taskStatus"),
    path('admineditTaskSheet/<int:id>', check_user(views.admineditTaskSheet), name="admineditTaskSheet"),
    path('admindeleteTaskSheet/<int:id>', check_user(views.admindeleteTaskSheet), name="admindeleteTaskSheet"),
    path('export_users_xlsTaskSheet', views.export_users_xlsTaskSheet, name="export_users_xlsTaskSheet"),

    path('appData_list', check_user(views.appData_list), name="appData_list"),
    path('editappData/<int:id>', check_user(views.editappData), name="editappData"),
    path('addNewaddData', check_user(views.addNewaddData), name="addNewaddData"),


    path('adminDailyBsnlWork',check_user(views.adminDailyBsnlWork),name="adminDailyBsnlWork"),
    path('admineditDailyBsnlWork/<int:id>',check_user(views.admineditDailyBsnlWork),name="admineditDailyBsnlWork"),
    path('admindeleteDailyBsnlWork/<int:id>',check_user(views.admindeleteDailyBsnlWork),name="admindeleteDailyBsnlWork"),

    path('admindailyCashReport',check_user(views.admindailyCashReport),name="admindailyCashReport"),

    path('adminbalance',check_user(views.adminbalance),name="adminbalance"),

    path('admindeposite',check_user(views.admindeposite),name="admindeposite"),

    path('adminchequeDetails',check_user(views.adminchequeDetails),name="adminchequeDetails"),
    path('admineditChequeDeatils/<int:id>',check_user(views.admineditChequeDeatils),name="admineditChequeDeatils"),
    path('admindeleteChequeDetails/<int:id>',check_user(views.admindeleteChequeDetails),name="admindeleteChequeDetails"),

    path('aadharPortalCashReport',check_user(views.aadharPortalCashReport),name="aadharPortalCashReport"),

    path('stock',check_user(views.stock),name="stock"),
    path('addStock',check_user(views.addStock),name="addStock"),
    path('adminStockUpdate',check_user(views.adminStockUpdate),name="adminStockUpdate"),

    path('get-csc/<int:pk>', views.GetCSCApiView.as_view(), name="get-csc"),
    path('get-station-id/<int:pk>', views.GetStationIdView.as_view(), name="get-station-id"),
]

