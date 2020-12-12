from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Movies
# Create your views here.

def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html', locals())

def search(request):
    if request.method == "GET":
        title = request.GET.get('q')
        if title:
            pass
        else:
            # 如果前端传参为空，默认展示《肖申克的救赎》
            title = Movies.objects.get(id=1).movie_title

    all_evaluate = Movies.objects.values_list('short_evaluate').filter(movie_title=title)
    short_evaluate = []
    star_l = []

    # 判断评论星级
    for i in range(len(all_evaluate)):
        if Movies.objects.get(short_evaluate=all_evaluate[i][0]).star in ['力荐','推荐','一般']:
            short_evaluate.append(all_evaluate[i])
            star = Movies.objects.get(short_evaluate=all_evaluate[i][0]).star
            star_l.append(star)
        else:
            pass
    # print(title)
    return render(request, 'index.html', locals())