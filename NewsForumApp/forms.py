from django.forms import ModelForm
from .models import Post, Author, Category
from django import forms
from django.contrib.auth.models import User
from django.db import models


# Создаём модельную форму
class PostForm(ModelForm):
    postAuthor = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор')
    postTitle = forms.CharField(label='Заголовок', max_length=128)
    postCategory = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категория')
    postText = forms.CharField(label='Текст', max_length=10240)

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['postAuthor', 'postTitle', 'postCategory', 'postText']


class UserForm(ModelForm):

    username = forms.CharField(label='Логин', max_length=30)
    first_name = forms.CharField(label='Имя', max_length=30)
    last_name = forms.CharField(label='Фамилия', max_length=30)
    email = forms.EmailField(label='Электронная почта')

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email']