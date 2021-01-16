
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bbs import views
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls


# 功能     路径             方式
# 创建用户  /usersapi/   POST
# 查看用户  /users/         GET
# 创建订单  /orders       POST
# 查看订单  /orders       GET
# 查看订单  /orders       GET
# 修改订单  /orders         PUT

router = DefaultRouter()
router.register(r'users', views.UserViewSet,  )
router.register(r'usersapi', views.CreateUserViewSet, 'user_api')
router.register(r'orders', views.OrderAPIViewSet, 'orders_list')
# router.register(r'posts', views.UserPostsAPIViewSet, 'posts_list')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    path('docs',include_docs_urls(title='BBS')),
]
