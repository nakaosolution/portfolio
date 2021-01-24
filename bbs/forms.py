from django import forms

class SearchForm(forms.Form):
    # viewsやテンプレートででこのクラスを使用する
    keyword = forms.CharField(label='検索', max_length=100)