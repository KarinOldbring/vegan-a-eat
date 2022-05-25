from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic, View
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Recipe
from . import forms
from .forms import RecipeForm


@login_required
def add_recipe(request):
    """
    Add recipe page
    """
    recipe_form = RecipeForm()

    if request.method == "POST":
        recipe_form = RecipeForm()
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.author = request.user
            recipe_form.status = 1
            recipe_form.save()
            return redirect('home')
    
    return render(request, 'add_recipe.html', context={'recipe_form': recipe_form})

class RecipeList(generic.ListView):
    """
    Creates recipe list
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6

class RecipeDetail(View):
    """
    Shows recipe in detail
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked
            },
        )

def login_page(request):
    """
    Login page
    """
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Login failed, please try again'
    return render(request, 'login.html', context={'form': form,
     'message': message})

def logout_user(request):
    """
    Logout function
    """
    logout(request)
    return redirect('login')

def signup_page(request):
    """
    Sign Up page
    """
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'sign_up.html', context={'form': form})