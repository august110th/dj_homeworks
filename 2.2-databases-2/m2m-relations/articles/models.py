from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    objects = models.Manager
    scopes = models.ManyToManyField('Scope', related_name='article', through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager
    is_main = models.BooleanField(verbose_name='Главный раздел', default=False)

    class Meta:
        ordering = ['-is_main']

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    scopes = models.ForeignKey(Scope, on_delete=models.CASCADE)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.scopes} {self.articles}'
