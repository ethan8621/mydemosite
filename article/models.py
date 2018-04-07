from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

import marco

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length = 100) # article title
    category = models.CharField(max_length = 50, blank = True) # article tag
    date_time = models.DateTimeField(auto_now_add = True) # article date
    content = models.TextField(blank = True, null = True) # article content
    tag = models.ManyToManyField(Tag, blank=True) # blog tag

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title.encode('utf-8')

    # return article url
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "%s:%s%s" %(marco.SITE_LOCAL_URL, marco.SITE_LOCAL_PORT, path)

    # order by date decrease
    class Meta:
        ordering = ['-date_time']
