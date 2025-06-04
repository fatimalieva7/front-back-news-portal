from django.shortcuts import render, get_object_or_404
from django.views.generic import  UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm
from django.db.models import Q
from django.shortcuts import redirect



def index(request):
    categories = Category.objects.all()
    latest_news = News.objects.filter(slug__isnull=False).exclude(slug='').order_by('-published_date')[:5]
    return render(request, 'main/index.html', {
        'categories': categories,
        'news_list': latest_news
    })

def category_view(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    news_list = News.objects.filter(
    category=category,
    slug__isnull=False).exclude(slug='').order_by('-published_date')
    return render(request, 'main/category.html', {'category': category, 'news_list': news_list, 'categories': categories})

def news_detail(request, slug):
    categories = Category.objects.all()
    news = get_object_or_404(News, slug=slug)
    return render(request, 'main/news_detail.html', {'news': news, 'categories': categories})
    
    try:
        news = News.objects.get(slug=slug)
    except News.DoesNotExist:
        raise Http404("Новость не найдена")

def search(request):
    query = request.GET.get('q')
    results = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)) if query else []
    return render(request, 'main/search.html', {'query': query, 'results': results})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:index') 
    else:
        form = NewsForm()
    return render(request, 'main/create_news.html', {'form': form})


    
class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'main/create_news.html'
    success_url = reverse_lazy('main:index')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'main/delete_news.html'
    context_object_name = 'new'
    success_url = reverse_lazy('main:index')


def news_delete_view(request, pk):
    new = News.objects.get(pk=pk)
    new.delete()
    return redirect('main:index')




