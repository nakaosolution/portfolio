from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    # bbs以降が空欄の場合はviews.pyのindex関数を呼び出す
    path('', views.index, name='index'),
    # bbs以降が整数の場合はviews.pyのdetail関数を呼び出す
    path('<int:id>', views.detail, name='detail'),
    path('new', views.new, name="new"),
    path('<int:id>/edit', views.edit, name="edit"),
    path('<int:id>/update', views.update, name="update"),
    path('create', views.create, name='create'),
    path('<int:id>/delete', views.delete, name='delete'),
]