from user.views import *
from django.urls import path

urlpatterns =[
    path('users/',getAllUsers,name="allUsers"),
    path('register/',register,name="userRegistration"),
    path('register/addUser',registerAddUser,name="userRegistrationAddUser"),
    path('home/',home,name="home"),
    path('edit/<int:user_id>',editUser,name="editUser"),
    path('update/<int:user_id>',updateUser,name="updateUser"),
    path('delete/<int:user_id>',deleteUser,name="deleteUser"),
]
