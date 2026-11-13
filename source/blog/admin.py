from django import forms
from django.contrib import admin
from django.db import models

from .models import BlogPage, BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'published',
        'created_at',
        'updated_at',
    )
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'description', 'content', 'author')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'rows': 4}),
        },
    }

    fieldsets = (
        ('Content', {
            'fields': (
                'title',
                'slug',
                'description',
                'content',
                'author',
            ),
        }),
        ('Image', {
            'fields': ('picture', 'picture_alt_text'),
        }),
        ('Publishing', {
            'fields': ('published', 'created_at', 'updated_at'),
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': (
                'meta_title',
                'meta_description',
                'canonical_url',
            ),
            'description': (
                'Optional overrides. Leave blank to use the post title, '
                'description and URL.'
            ),
        }),
        ('Social Sharing', {
            'classes': ('collapse',),
            'fields': ('og_image', 'og_image_alt'),
            'description': (
                'Optional sharing image. Leave blank to use the blog picture.'
            ),
        }),
    )


@admin.register(BlogPage)
class BlogPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero', {
            'fields': (
                'hero_title',
                'hero_subtitle',
                'hero_image',
                'hero_image_alt_text',
            ),
        }),
    )

    def has_add_permission(self, request):
        return (
            super().has_add_permission(request)
            and not BlogPage.objects.exists()
        )