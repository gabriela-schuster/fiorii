import articles
from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm
from django.contrib.auth.decorators import login_required


def allArticles(req):
    context = {'articles': Article.objects.order_by('-created')}
    return render(req, 'all-articles.html', context)


def singleArticle(req, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(req, 'single-article.html', context)


@login_required(login_url='user-login')
def createArticle(req):
    profile = req.user.profile

    if req.method == 'POST':
        form = ArticleForm(req.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = profile
            article.save()

            return redirect('all-articles')

    context = {'form': ArticleForm(), 'page': 'create'}
    return render(req, 'form-article.html', context)


@login_required(login_url='user-login')
def editArticle(req, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)

    if req.method == 'POST':
        form = ArticleForm(req.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('all-articles')

    context = {'article': article, 'form': form}
    return render(req, 'form-article.html', context)


@login_required(login_url='user-login')
def deleteArticle(req, pk):
    article = req.user.profile.article_set.get(id=pk)

    if req.method == 'POST':
        article.delete()
        return redirect('all-articles')

    context = {'article': article}
    return render(req, 'delete-article.html', context)
