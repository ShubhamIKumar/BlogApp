from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup , name = 'signup'),
    path('login/', views.Login , name = 'login'),
    path('logout/', views.logout , name = 'logout'),
    # # path('user/', views.user , name = 'user'),
    
    
]
