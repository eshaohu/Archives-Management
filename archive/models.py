from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
# Create your models here.
class Archive(models.Model):
    title = models.CharField(max_length=512, default='blank')
    author = models.CharField(max_length=128, default='admin')
    content = models.TextField(null=True)

    classify = models.CharField(max_length=256, default='common')
    sub_classify = models.CharField(max_length=256, default='common')


    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    star_count = models.IntegerField(default=0)
    read_count = models.IntegerField(default=0)
    download_count = models.IntegerField(default=0)


    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}'
    __str__ = __repr__

    class Meta:
        db_table = 'archives'


