from django.db import models

# Create your models here.
# モデルはデータベースのレコードをオブジェクトに割り当てる
# オブジェクトでデータベースを操作する方法をＯＲマッパーという

# 記事のテーブルを操作するためのモデル
class Article(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null = True) #null = Trueはカラムを追加する際に必須。空のデータを許可する必要があるため

    def __str__(self):
        return self.content