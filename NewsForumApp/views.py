# from django.shortcuts import render
# from .models import *
#
# from NewsForumApp.models import *
#
# u1 = User.objects.create_user(username='Чикибряк')
# u2 = User.objects.create_user(username='Бубылда')
#
# a1 = Author.objects.create(authorAccount=u1)
# a2 = Author.objects.create(authorAccount=u2)
#
# c1 = Category.objects.create(categoryName='Пельменеведение')
# c2 = Category.objects.create(categoryName='Румынские народные сказки')
# c3 = Category.objects.create(categoryName='Дабстеп народов мира')
# c4 = Category.objects.create(categoryName='Всемирный заговор кукол из улицы Сезам')
#
# p1 = Post.objects.create(
#     postAuthor=a1,
#     postType='AR',
#     postTitle='Зелибоба на румынском',
#     postText='Зелибоба на румынском будет звучать как Zeliboba.'
# )
# p2 = Post.objects.create(
#     postAuthor=a1,
#     postType='NW',
#     postTitle='Печальная кончина великого певца',
#     postText='Вася, певец из электрички Москав-Черусти скончался от передозировки пельменным бульоном.'
# )
# p3 = Post.objects.create(
#     postAuthor=a2,
#     postType='AR',
#     postTitle='Дабстеп как культурное наследие Инков',
#     postText='Skrillex оказался последним представителем рода Инков.'
# )
#
# Post.objects.get(postTitle='Зелибоба на румынском').postCategory.add(c2)
# Post.objects.get(postTitle='Зелибоба на румынском').postCategory.add(c4)
# Post.objects.get(postTitle='Печальная кончина великого певца').postCategory.add(c1)
# Post.objects.get(postTitle='Дабстеп как культурное наследие Инков').postCategory.add(c3)
#
# com1 = Comment.objects.create(commentPost=p1, commentUser=u1, commentText='А как будует на румынском Влас и Еник?')
# com2 = Comment.objects.create(commentPost=p1, commentUser=u2, commentText='Vlas si Enik')
# com3 = Comment.objects.create(commentPost=p3, commentUser=u1, commentText='Раз-раз-раз, это хардбас')
# com4 = Comment.objects.create(commentPost=p2, commentUser=u2, commentText='Был пацан, и нет пацана')
# com5 = Comment.objects.create(commentPost=p3, commentUser=u2, commentText='Все в кроссовках abibas')
#
# Comment.objects.get(id=1).like()
# Comment.objects.get(id=1).like()
# Comment.objects.get(id=1).like()
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=4).dislike()
# Comment.objects.get(id=4).dislike()
#
# Post.objects.get(id=1).like()
# Post.objects.get(id=2).dislike()
# Post.objects.get(id=3).like()
# Post.objects.get(id=3).dislike()
#
# for i in Author.objects.all().values('id'):
#     Author.objects.get(id=i['id']).update_rating()
#
# sort = Author.objects.order_by('-authorRating')
# f"{sort[0].authorAccount.username} - {sort[0].authorRating}"
#
# postsort = Post.objects.order_by('-postRating')
# best = [f"{postsort[0].postTime.strftime('%d-%m-%y')}",
#         f"{postsort[0].postAuthor.authorAccount.username}",
#         f"{postsort[0].postAuthor.authorRating} ",
#         f"{postsort[0].postTitle} ",
#         f"{postsort[0].preview()}"
#         ]
# print(best)
#
# for i in Comment.objects.filter(commentPost=postsort[0]):
#     bestcom = [f"Дата и время: {i.commentTime.strftime('%d-%m-%y %H:%M:%S')}",
#                f"Пользователь: {i.commentUser.username}",
#                f"Рейтинг комментария: {i.commentRating} ",
#                f"{i.commentText}"
#                ]
#     print(bestcom)
