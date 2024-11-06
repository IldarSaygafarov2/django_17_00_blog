from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'short_description',
            'full_description',
            'preview',
            'category',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
            'full_description': forms.Textarea(attrs={'class': 'form-control'}),
            'preview': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# 1.  Разработать простое веб-приложение на фреймворке
# Django, которое позволит пользователям регистрироваться, авторизовываться
# и вести список личных задач (to-do list). Приложение должно предоставлять
# возможности для создания, просмотра, редактирования и удаления задач.
# Также необходима функциональность поиска среди своих задач.
# Технические требования
# 1.  Бэкенд
# •  Язык программирования: Python 3.8+
# •  Веб-фреймворк: Django 3.2+
# •  База данных: SQLite в разработке
# •  Аутентификация и авторизация: использовать стандартные механизмы Django
# 2.  Фронтенд
# •  HTML, CSS (Bootstrap или любой другой CSS фреймворк)
# 3.  Функциональные требования
# •  Регистрация/авторизация пользователей
# •  Создание, просмотр, редактирование и удаление задач
# •  Возможность отмечать задачи выполненными
# •  Поиск по задачам