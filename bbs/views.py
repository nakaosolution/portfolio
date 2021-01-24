from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm

# 掲示板一覧ページ
def index(request):
    # return HttpResponse('HelloWorld')
    
    # もしサーチフォームに正常なデータがあればキーワードのデータを代入して
    # DBから該当のデータを取り出す
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        # DBからすべての投稿をとりだし、articles変数に代入
        articles = Article.objects.all()

    context = {
        'message': 'Welcome my bbs',
        'articles': articles,
        'searchForm': searchForm,
    }

    # renderはデータとテンプレートを組み合わせてWebページを返すショートカット関数、第三引数に辞書型を渡すとテンプレートを呼び出すことができる。
    return render(request, 'bbs/index.html', context)


# 掲示板詳細ページ
def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message': 'Show Article' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)


# 記事投稿ページ
def create(request):
    # contentがHello BBS user_nameが名無しさんのデータをDBに保存
    article = Article(content='Hello BBS',user_name='名無しさん')
    article.save()

    articles = Article.objects.all()
    context = {
        'message': 'Welcome my bbs',
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)


# 記事削除ページ
def delete(request, id):
    # データを呼び出し、削除
    article = get_object_or_404(Article, pk=id)
    article.delete()

    # 記事一覧を呼び出す
    articles = Article.objects.all()
    context = {
        'message': 'Delete Article' + str(id),
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)