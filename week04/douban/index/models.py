from django.db import models

# Create your models here.

# 电影名称、短评、星级
class Movies(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie_title = models.CharField(max_length=1000)
    short_evaluate = models.CharField(max_length=1000)
    star = models.CharField(max_length=10)
    
    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'movies'