from django.urls import path
from .views import PostList, PostDetails  # импортируем наше представление

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetails.as_view()),
]