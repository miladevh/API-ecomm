from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('change_password/', views.UserChangePassword.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjE5OTkzNSwiaWF0IjoxNzE2MTEzNTM1LCJqdGkiOiJlM2E0MmYyMWU2YWU0YTFiOThmOWQxMmQ1YWIzZjM2MSIsInVzZXJfaWQiOjJ9.q0yYKagLZu_cwlrTMEK7N8NjHIAp0T6M7tOrRcOT4VA",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTEzODM1LCJpYXQiOjE3MTYxMTM1MzUsImp0aSI6IjgwNmVhYmNjZmVkZDQzYjJiZWVkODFjZGU2NTgwZWMzIiwidXNlcl9pZCI6Mn0._3PVN7IC35AuXvNkDrArpzW6rYLc1Ox-gAfhTF_m0Lk"
# }