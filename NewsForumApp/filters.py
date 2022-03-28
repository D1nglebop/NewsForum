from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'postTitle': ['icontains'],
            'postAuthor__authorAccount': ['exact'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'postCategory': ['exact'],  # цена должна быть меньше или равна тому, что указал пользователь
            'postTime': ['gt'],
        }
