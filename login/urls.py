from django.urls import path
from .views import *

#app_name = 'login'

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LoginRedirectView.as_view(), name='logout'),
]