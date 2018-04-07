from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from article.models import Article
from artical.models import Tag


# Create your views here.


def home(request) :
    # for demo
    # return HttpResponse("Hello, This is Django!")
    posts = Article.objects.all() # get all article objects
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)

    return render(request, 'home.html', {'post_list' : post_list})


def detail(request, my_args) :
    # return HttpResponse("You're looking at my_args %s."%(my_args))
    try :
        post = Article.objects.get(id = str(id))
        tags = post.tag.all()
    except Article.DoesNotExist :
        raise Http404

    return render(request, 'post.html', {'post' : post, 'tag': tags})


def archives(request) :
    try :
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404

    return render(request, 'tag.html', {'post_list' : post_list,
                                        'error' : False})

def searchTag(request, tag) :
    try :
        post_list = Article.objects.filter(category__iexact = tag) # contains
    except Article.DoesNotExist :
        raise Http404

    return render(request, 'tag.html', {'post_list' : post_list})


def aboutMe(request) :
    return render(request, 'aboutme.html')


def searchBlog(request) :
    if 's' in request.GET :
        s = request.GET['s'] :
        if not s :
            return render(request, 'home.html')
        else :
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list == 0) :
                return render(request, 'archives.html', {'post_list' : post_list,
                                                         'error' : True})
            else :
                return render(request, 'archives.html', {'post_list' : post_list,
                                                         'error' : False})

def getArticle(request, article_id) :
    article_max_id = len(Article.objects.all())
    if int(article_id) <= int(article_max_id) :
        post = Article.objects.all()[int(article_id)]
        str = ("title = %s, category = %s, date_time = %s, content = %s"
               %(post.title, post.category, post.date_time, post.content))
    else :
        try :
            str = ("Your request [%s] is out of range [%s]" %(article_id, article_max_id))
        except Exception :
            raise Http404(str)
    return HttpResponse(str)


class RSSFeed(Feed) :
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self) :
        return Article.objects.order_by('-date_time')


    def itemTitle(self, item) :
        return item.title


    def itemPubDate(self, item) :
        return item.date_time


    def itemDecription(self, item) :
        return item.content


def testTemplate(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})