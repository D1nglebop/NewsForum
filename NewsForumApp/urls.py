from django.urls import path
from .views import PostList, PostDetails, PostListSearch  # импортируем наше представление

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetails.as_view()),
    path('search/', PostListSearch.as_view()),

]