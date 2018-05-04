from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from .import forms

def all_article(request):
	title = 'All Articles'
	articles = Article.objects.all().order_by('id')
	return render(request, 'articles/all_article.html', {'articles':articles, 'title':title })

def article_detail(request, slug):
	title = 'Article Detail'
	article = Article.objects.get(slug=slug)
	form = forms.createComment()
	data = {
		'title':title,
		'article':article,
		'form' : form
	}
	return render(request, 'articles/article_detail.html', data)

def add_comment(request,slug):
	if request.method == 'POST':
		article = Article.objects.get(slug=slug)
		form = forms.createComment(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.articleName = article
			instance.save()
			return redirect('articles:article_detail', slug=slug)



@login_required(login_url = '/account/signin')
def create_article(request):
	title = 'New Article'
	if request.method == 'POST':
		form = forms.createArticle(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.auther = request.user
			instance.save()
			return redirect('articles:auther_article')
	else:
		form = forms.createArticle()
	return render(request, 'articles/create_article.html', {'form':form, 'title':title})

@login_required(login_url = '/account/signin')
def auther_article(request):
	title = 'Dashboard'
	auther = request.user
	articles = Article.objects.all().filter(auther=auther)
	return render(request, 'articles/auther_article.html',
	{'articles':articles, 'auther':auther, 'title':title})



