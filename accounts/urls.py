from django.urls import path
from .views import RegisterUserView, HomeView, UserLoginView, UserLogoutView, UserView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('', HomeView.as_view(), name='home'),
]


