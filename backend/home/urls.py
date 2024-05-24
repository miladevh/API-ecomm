from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('product/search/', views.ProductSearchView.as_view()),
    path('comment/<int:pk>/create/', views.CommentCreateView.as_view()),
    
]