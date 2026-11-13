from urllib.parse import urljoin
from uuid import uuid4

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class BlogPost(models.Model):
    # Blog content
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(
        help_text="Short summary for the blog listing and SEO fallback.",
    )
    author = models.CharField(
        max_length=255,
        default="Dental Dynamix",
    )
    content = CKEditor5Field(config_name='default', blank=True)

    picture = models.ImageField(
        upload_to='blog_pictures/',
        blank=True,
        default="default/hero_image.webp",
    )
    picture_alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Describe the image for accessibility.",
    )

    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # SEO overrides — leave blank to use the post details
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional search engine title. Aim for around 50–60 characters.",
    )
    meta_description = models.CharField(
        max_length=320,
        blank=True,
        help_text="Optional search description. Aim for around 150–160 characters.",
    )
    canonical_url = models.URLField(
        blank=True,
        help_text="Leave blank to use this post's own URL.",
    )
    og_image = models.ImageField(
        upload_to='blog_seo/',
        blank=True,
        help_text="Optional sharing image. Defaults to the blog picture.",
    )
    og_image_alt = models.CharField(
        max_length=255,
        blank=True,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog_details',
            kwargs={'blog_slug': self.slug},
        )

    def absolute_url(self, path):
        site_url = getattr(
            settings,
            'SITE_URL',
            'https://dentaldynamix.co.uk',
        ).rstrip('/')

        return urljoin(f'{site_url}/', path)

    @property
    def meta(self):
        title = self.meta_title or self.title
        description = self.meta_description or self.description
        canonical_url = (
            self.canonical_url
            or self.absolute_url(self.get_absolute_url())
        )

        image = self.og_image or self.picture
        image_url = self.absolute_url(image.url) if image else ''
        image_alt = (
            self.og_image_alt
            if self.og_image
            else self.picture_alt_text
        )

        return {
            'title': title,
            'description': description,
            'canonical_url': canonical_url,
            'author': self.author,
            'robots': (
                'index, follow, max-image-preview:large'
                if self.published
                else 'noindex, nofollow'
            ),
            'language': 'en-GB',
            'site_name': 'Dental Dynamix',
            'og_title': title,
            'og_description': description,
            'og_type': 'article',
            'og_image': image_url,
            'og_image_alt': image_alt,
            'og_locale': 'en_GB',
            'twitter_card': 'summary_large_image' if image else 'summary',
            'twitter_title': title,
            'twitter_description': description,
            'twitter_image': image_url,
            'twitter_image_alt': image_alt,
        }

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = self._meta.get_field('slug').max_length
            base_slug = slugify(self.title) or f'post-{uuid4().hex[:8]}'
            base_slug = base_slug[:max_length]
            candidate = base_slug
            counter = 1

            while type(self).objects.filter(
                slug=candidate,
            ).exclude(pk=self.pk).exists():
                suffix = f'-{counter}'
                candidate = f'{base_slug[:max_length - len(suffix)]}{suffix}'
                counter += 1

            self.slug = candidate

            if kwargs.get('update_fields') is not None:
                kwargs['update_fields'] = set(kwargs['update_fields']) | {'slug'}

        super().save(*args, **kwargs)
        