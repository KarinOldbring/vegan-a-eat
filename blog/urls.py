from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('addrecipe/', views.add_recipe, name='addrecipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]