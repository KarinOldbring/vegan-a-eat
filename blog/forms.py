from django import forms
from .models import Recipe, Comments
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteInplaceWidget

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')


class RecipeForm(forms.ModelForm):
    """
    Form to add recipe
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'excerpt',
            'cooking_time',
            'ingredients',
            'instructions',
            'featured_image',
        ]

        widgets = {
            'ingredients': SummernoteInplaceWidget(),
            'instructions': SummernoteInplaceWidget()
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)