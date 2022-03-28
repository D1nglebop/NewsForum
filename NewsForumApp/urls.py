from django.urls import path
from .views import PostList, PostListSearch, PostCreateView, PostUpdateView, PostDeleteView
from .views import PostDetails

urlpatterns = [
    path('', PostList.as_view()),
    path('add/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('<int:pk>', PostDetails.as_view(), name='post_details'),
    path('search/', PostListSearch.as_view()),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]