from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    return render(request,'blog/post_list.html',{})
