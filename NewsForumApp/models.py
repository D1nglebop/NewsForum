from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorAccount = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.IntegerField(default=0)

    def update_rating(self):
        post_sum_rating = self.post_set.all().aggregate(postSumRating=Sum('postRating'))
        post_rating = 0
        post_rating += post_sum_rating.get('postSumRating')

        comment_author_sum_rating = self.authorAccount.comment_set.all().aggregate(commentSumRating=Sum('commentRating'))
        comment_rating = 0
        comment_rating += comment_author_sum_rating.get('commentSumRating')

        self.authorRating = post_rating * 3 + comment_rating
        self.save()

    def __str__(self):
        return f'{self.authorAccount.username}'


class Category(models.Model):
    categoryName = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.categoryName.title()}'


class Post(models.Model):

    NEWS = 'NW'
    ARTICLE = 'AR'
    TYPE_NEWS = ((NEWS, 'Новость'), (ARTICLE, 'Статья'))

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    postType = models.CharField(max_length=2, choices=TYPE_NEWS, default=ARTICLE)
    postTime = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    postTitle = models.CharField(max_length=128)
    postText = models.TextField()
    postRating = models.IntegerField(default=0)

    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

    def preview(self):
        if len(str(self.postText)) > 124:
            return "{:123}...".format(self.postText)
        else:
            return self.postText

    def __str__(self):
        return f'{self.postAuthor.authorAccount.username}: {self.postTitle}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    commentTime = models.DateTimeField(auto_now_add=True)
    commentRating = models.IntegerField(default=0)

    def like(self):
        self.commentRating += 1
        self.save()

    def dislike(self):
        self.commentRating -= 1
        self.save()
