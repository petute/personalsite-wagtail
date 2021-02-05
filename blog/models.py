from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.

class _S_HeaderBlock(blocks.StructBlock):
    pass


class _S_BlogPostBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    post = blocks.RichTextBlock()

    class Meta:
        template = 'blog/blocks/_S_BlogPost.html'

class _S_BlogBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    posts = blocks.StreamBlock([
        ('post', _S_BlogPostBlock())
    ],null=True)

    class Meta:
        template = 'blog/blocks/_S_Blog.html'

class _S_FooterBlock(blocks.StructBlock):
    pass

class BlogPage(Page):
    sections = StreamField([
        ('Blog', _S_BlogBlock()),
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sections'),
    ]

    template = 'blog/blog_page.html'