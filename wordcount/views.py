from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail': details})


def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']

    #fulltext 에 들어있는 것들을 text에 저장해준다. 
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] +=1

        else:
            word_dictionary[word] = 1 
    
    return render(request, 'result.html', {'full' : text, 'count': len(words), 'dictionary' : word_dictionary.items()})
    #render -> 사전형, 

# Create your views here.
