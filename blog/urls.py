from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('login/', views.login_page, name='login'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]