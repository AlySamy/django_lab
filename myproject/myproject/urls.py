
from django.contrib import admin
from django.urls import path, include
from user.views import login
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
     path('user/login/', login, name='login'),
     path('', login, name='login'),
    path('user/', include(user_urls)),
]
