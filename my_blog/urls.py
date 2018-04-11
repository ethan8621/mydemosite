"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article import views
from article.views import RSSFeed


"""
old version
urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('article/', views.home),
    path('test/', views.testTemplate, name='testTemplate'),
    path('article/<article_id>', views.getArticle, name='getArticle'),
    path('<my_args>', views.detail, name='detail'),
]
"""

"""
how to use path to parser url
https://blog.csdn.net/qq_40272386/article/details/78800507
https://docs.djangoproject.com/en/2.0/topics/http/urls/#example

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('test/', views.test_template, name='test_template'),
    path('^$/', views.home),
    path('article/<int:article_id>', views.get_article, name='get_article'),
    path('<int:id>', views.detail, name='detail'),
    path('aboutme/', views.about_me, name='about_me'),
    path('tag/', views.search_tag, name='search_tag'),
    path('search/', views.search_blog, name='search_blog'),
    path('archives/', views.archives, name='archives'),
    path('feeds/', RSSFeed(), name='RSS'),
]
