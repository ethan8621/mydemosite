from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404


# Create your views here.


def home(request):
    # for demo
    # return HttpResponse("Hello, This is Django!")
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s."%(my_args))


def getArticle(request, article_id):
    article_max_id = len(Article.objects.all())
    if int(article_id) <= int(article_max_id):
        post = Article.objects.all()[int(article_id)]
        str = ("title = %s, category = %s, date_time = %s, content = %s"
               %(post.title, post.category, post.date_time, post.content))
    else:
        try:
            str = ("Your request [%s] is out of range [%s]" %(article_id, article_max_id))
        except Exception:
            raise Http404(str)
    return HttpResponse(str)


def testTemplate(request):
    return render(request, 'test.html', {'current_time': datetime.now()})