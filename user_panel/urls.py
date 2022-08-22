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
from user_panel import views
from .check_me import check_user, login_user

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('demo', views.demo, name='demo'),
    path('logout', views.logout, name="logout"),

    path('forgot_password', views.forgot_password, name="forgot_password"),
    path('send_otp', views.send_otp, name="send-otp"),
    path('reset_password', views.reset_password, name="reset_password"),

    path('staffTask', views.staffTask, name="staffTask"),
    path('taskSheet', views.taskSheet, name="taskSheet"),
    path('editTaskSheet/<int:id>', views.editTaskSheet, name="editTaskSheet"),
    path('deleteStaffTask/<int:id>', views.deleteStaffTask, name="deleteStaffTask"),

    path('dailyBsnlWork', views.dailyBsnlWork, name="dailyBsnlWork"),
    path('addnewDailyBsnlWork', views.addnewDailyBsnlWork, name="addnewDailyBsnlWork"),
    path('editDailyBsnlWork/<int:id>', views.editDailyBsnlWork, name="editDailyBsnlWork"),
    path('deleteDailyBsnlWork/<int:id>', views.deleteDailyBsnlWork, name="deleteDailyBsnlWork"),

    path('dailyCashReport', views.dailyCashReport, name="dailyCashReport"),
    path('addDailyCashReport', views.addDailyCashReport, name="addDailyCashReport"),

    path('balance', views.balance, name="balance"),
    path('addBalance', views.addBalance, name="addBalance"),

    path('deposite', views.deposite, name="deposite"),
    path('addDeposite', views.addDeposite, name="addDeposite"),

    path('chequeDetails', views.chequeDetails, name="chequeDetails"),
    path('addChequeDetails', views.addChequeDetails, name="addChequeDetails"),
    path('editChequeDeatils/<int:id>', views.editChequeDeatils, name="editChequeDeatils"),
    path('deleteChequeDetails/<int:id>', views.deleteChequeDetails, name="deleteChequeDetails"),

    path('stockDetails', views.stockDetails, name="stockDetails"),

    path('otfValue', views.otfValue, name="otfValue"),
    path('addOtf', views.addOtf, name="addOtf"),

    path('weeklyReport', views.weeklyReport, name="weeklyReport"),

    path('sendDailyMail',views.sendDailyMail,name="sendDailyMail"),

]
