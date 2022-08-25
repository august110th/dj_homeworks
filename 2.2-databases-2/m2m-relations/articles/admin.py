from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super(ArticleScopeInlineFormset, self).clean()
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
            if count > 1:
                raise ValidationError('Может быть только 1 базовый тег')
            elif count < 1:
                raise ValidationError('Тут всегда ошибка')
            return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]
