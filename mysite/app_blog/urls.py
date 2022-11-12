# app_blog/urls.py
from django.urls import path
from app_blog import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]

# from django.conf.urls import url
# from app_blog import views
# urlpatterns = [
# url(r’^$’, views.home, name=‘home’),
# url(r’^(?P&lt;username&gt;[\w.@+-]+)/$’, views.user_profile,
#
# name=‘user_profile’),
# ]

from django.urls import path
from .views import (HomePageView, ArticleDetail,
                    ArticleList, ArticleCategoryList)

urlpatterns = [
    path(r'', HomePageView.as_view()),
    path(r'articles', ArticleList.as_view(), name='articles-list'),
    path(r'articles/category/&lt;slug&gt;', ArticleCategoryList.as_view(), name='articles-category-list'),
    path(r'articles/&lt;year&gt;/&lt;month&gt;/&lt;day&gt;/&lt;slug&gt;', ArticleDetail.as_view(), name='news-detail'),
]

