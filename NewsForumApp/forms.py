from django.forms import ModelForm
from .models import Post, Author, Category
from django import forms
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
