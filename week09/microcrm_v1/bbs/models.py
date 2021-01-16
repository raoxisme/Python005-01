from django.db import models

# Create your models here.
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Orders(models.Model):
    """
    订单
    """
    __tablename__ = 'orders'
    title = models.CharField(max_length=30, verbose_name='订单标题', default='')
    body = models.CharField(max_length=30, verbose_name='订单内容', default='')
    
    ORDERSTATUS = (
        (1, "New"),
        (2, "Cancelled")
    )
    status = models.SmallIntegerField(choices=ORDERSTATUS, default=1, verbose_name='订单状态' ) 

    create_time = models.DateTimeField(auto_now_add=True)  # 订单创建时间
    author_id = models.ForeignKey( 'auth.User', verbose_name='用户id', related_name='orders', on_delete=models.CASCADE)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.title


# https://docs.djangoproject.com/zh-hans/2.2/topics/auth/customizing/#extending-django-s-default-user

class UserProfile(models.Model):
    username = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, verbose_name='昵称', default='')
    phone_number = models.CharField(max_length=20, verbose_name='手机', unique=False, blank=True)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    description = models.CharField(max_length=30, verbose_name='个人简介', default='')
    score = models.BigIntegerField(verbose_name='积分', default=0)

    USERGROUP = (
        (1, "customer"),
        (2, "executor")
    )
    user_group = models.SmallIntegerField(choices=USERGROUP, default=1, verbose_name='用户组' )

    # objects = UserManager()

    @classmethod
    def get_blacklist(cls):
        # seek that is_active = False
        return cls.objects.filter(is_active=False)

    class Meta:
        verbose_name = 'User Profile' 

    # 当生成 user 的时候自动生成 UserProfile
    # 原型是: receiver(signal, **kwargs), 当User产生post_save信号时 
    @receiver(post_save, sender=User)  
    def handler_user_create_content(sender, instance, created, **kwargs):
        # 如果第一次创建
        if created:  
            # 绑定User实例到UserProfile的username字段
            UserProfile.objects.create(username=instance)  
        
    @receiver(post_save, sender=User)  
    def handler_user_save_content(sender, instance, created, **kwargs):
        # profile = UserProfile.objects.create(username=instance)
        # 保存UserProfile的内容 ,profile是username字段外键的related_name名
        instance.profile.save()  

# class ProfileAPI(models.Model):
#     """
#     用户积分
#     """
#     __tablename__ = 'score'
#     score = models.CharField(max_length=10, verbose_name='积分', default='0')
#     owner = models.OneToOneField(
#         'auth.User', related_name="profile_api", on_delete=models.CASCADE)


#     @receiver(post_save, sender=User)
#     def handler_user_create_content(sender, instance, created, **kwargs):
#         if created:
#             ProfileAPI.objects.create(username=instance)

#     @receiver(post_save, sender=User)
#     def handler_user_save_content(sender, instance, created, **kwargs):
#         instance.profile.save()

# class Posts(models.Model):
#     """
#     评论和回复
#     """
#     __tablename__ = 'posts'
#     content = models.CharField(max_length=30, verbose_name='评论内容', default='')
#     create_time = models.DateTimeField(auto_now_add=True)  # 评论回复时间
#     order_id = models.ForeignKey(
#         'Orders', verbose_name='订单id', related_name='art_com', on_delete=models.CASCADE)
#     user_id = models.ForeignKey(
#         'auth.User', verbose_name='评论用户id', related_name='posts_users', on_delete=models.CASCADE)
#     # 如果实现回复需要增加被回复评论id和被回复用户id
#     # user_to_id = models.ForeignKey(
#     #     'auth.User', verbose_name='被回复用户id' related_name='orders', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title