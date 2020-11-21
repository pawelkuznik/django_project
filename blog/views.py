from django.shortcuts import render

posts = [
    {
        'author': 'Pawel',
        'title': 'Blog post 1',
        'content':'Pierwsz post',
        'date_posted': 'November 21, 2020'
    },
    {
        'author': 'Andrzej',
        'title': 'Blog post 2',
        'content':'Drugi post',
        'date_posted': 'November 22, 2020'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
