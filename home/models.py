from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

# Sections

class _S_Header(blocks.StructBlock):
    pass

class _S_AboutBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    picture = ImageChooserBlock()
    description = blocks.RichTextBlock()

    class Meta:
        tempate = 'home/blocks/_S_About.html'

class _S_Footer(blocks.StructBlock):
    pass

class HomePage(Page):
    sections = StreamField([
        ('about', _S_AboutBlock(null=True, blank=True))
    ],null=True, blank=False)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sections'),
    ]

    template = 'home/home_page.html'