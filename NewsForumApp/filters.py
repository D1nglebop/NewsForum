from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):
    postTime = DateFromToRangeFilter()
    class Meta:
        model = Post
        fields = {
            'postTitle': ['icontains'],
            'postAuthor': ['exact'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'postCategory': ['exact'],  # цена должна быть меньше или равна тому, что указал пользователь
            'postTime': ['exact'],
        }
