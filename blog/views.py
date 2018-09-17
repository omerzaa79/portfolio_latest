from django.shortcuts import render

def blog(request):
	return render(request, 'blog/blogs.html')


def detail(request):
	return render(request, 'blog/detail.html')
