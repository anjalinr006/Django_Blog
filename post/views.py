from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import Post

def post_post(request):
    queryset_list=Post.objects.all()
    paginator = Paginator(queryset_list,10)
    page=request.POST.get('page')
    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:

        queryset = paginator.page(paginator.num_pages)

    context={
        "post_list":queryset
    }
    return render(request, "index.html",context)


def post_view(request,id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance":instance
    }
    return render(request, "post_view.html", context)
