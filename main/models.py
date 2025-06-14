from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    content = models.TextField(max_length=1400, verbose_name='Контент')
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='Изображение')
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            while News.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

class NewsImage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    description = models.TextField(max_length=1400, blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            while NewsImage.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class NewsSport(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='Изображение')
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1400, blank=True, null=True, verbose_name='Описание')

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            while NewsSport.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class NewsCulture(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='Изображение')
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1400, blank=True, null=True, verbose_name='Описание')

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            while NewsCulture.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
