from django import forms
from django.forms import ModelForm
from app_advertisements.models import Article
from django.core.exceptions import ValidationError

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'price', 'is_auction', 'image']
        title = forms.CharField( max_length=60, validators='?', widget=forms.TextInput(attrs={'class': 'form-control-lg'})) 
        description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control-lg'}))
        price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control-lg'}))
        is_auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control-lg'}))
        image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-lg'}))


article = Article.objects.get(pk=1)
form = ArticleForm(instance=article)

