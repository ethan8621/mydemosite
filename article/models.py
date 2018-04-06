from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100) # article title
    category = models.CharField(max_length = 50, blank = True) # article tag
    date_time = models.DateTimeField(auto_now_add = True) # article date
    content = models.TextField(blank = True, null = True) # article content

    def __unicode__(self):
        return self.title

    # order by date decrease
    class Meta:
        ordering = ['-date_time']
