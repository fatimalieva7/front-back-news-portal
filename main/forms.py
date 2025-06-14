from django import forms
from .models import News,  NewsImage, NewsSport, NewsCulture
from django.utils.text import slugify

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image', 'category']
        wigdets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug:
            instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
class NewsImageForm(forms.ModelForm):
    class Meta:
        model = NewsImage
        fields = '__all__'

class NewsSportForm(forms.ModelForm):
    class Meta:
        model = NewsSport
        fields = '__all__'

class NewsCultureForm(forms.ModelForm):
    class Meta:
        model = NewsCulture
        fields = '__all__'