# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from .models import Orders , UserProfile#, Posts
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view



class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    """订单序列"""
    author_id = serializers.ReadOnlyField(source='author_id.username')

    status = serializers.ChoiceField(choices=Orders.ORDERSTATUS, source="get_status_display", read_only=True)

    class Meta:
        model = Orders
        fields = [ 'id', 'author_id', 'body', 'create_time', 'title', 'status']

    # def validate(self, attrs):
 	# 	# 撤销以后不可以再改为New
    #     if self['status'] != '2':
    #         return attrs

    # def update(self, instance, validated_data):
    #     instance.status = validated_data['status']
    #     instance.save()
    #     return instance

    # @api_view(['PUT'])
    # def changestatus(request):
    #     id = request.GET['id']
    #     datas=Orders.objects.filter(id=id)
    #     postdata = PostsSerializer(datas,many=False)
    #     return Response({'data':PostsSerializer.data})

# class ProfileAPISerializer(serializers.HyperlinkedModelSerializer):
#     """用户积分序列"""
#     lookup_field = 'id'
#     class Meta:
#         model = ProfileAPI
#         fields = ['url','score', 'owner']
#     extra_kwargs = {
#         'url': {'lookup_field': 'id'},
#         'owner': {'lookup_field': 'id'}
#         }

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    # other = OtherSerializer(read_only=True, many=True)
    # class Meta:
    #     fields = (..., 'other',)
    user_group = serializers.ChoiceField(choices=UserProfile.USERGROUP, source="get_user_group_display", read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'nickname', 'phone_number', 'description', 'createtime', 'score', 'user_group']

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    """创建用户序列"""

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password']
    
    def validate(self, attrs):
 		# 对密码进行加密 
        attrs['password'] = make_password(attrs['password'])
        return attrs

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """用户序列"""
    # orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Orders.objects.all())
    orders = OrdersSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'orders' ]


# class PostsSerializer(serializers.ModelSerializer):
#     """评论序列"""
 
#     class Meta:
#         model = Posts
#         fields = ['id', 'content', 'create_time', 'order_id', 'user_id']

#     @api_view(['GET'])
#     def showdata(request):
#         id = request.GET['id']
#         datas=Posts.objects.filter(order_id=id)
#         postdata = PostsSerializer(datas,many=True)
#         return Response({'data':PostsSerializer.data})

