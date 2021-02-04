from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

# Sections

class _S_HeaderBlock(blocks.StructBlock):
    pass

class _S_About_ContactBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    image = ImageChooserBlock()
    url = blocks.URLBlock()

    class Meta:
        template = 'home/blocks/_S_About_Contact.html'

class _S_AboutBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    picture = ImageChooserBlock()
    description = blocks.RichTextBlock()
    contacts = blocks.StreamBlock([
        ('contact', _S_About_ContactBlock()),
    ])

    class Meta:
        template = 'home/blocks/_S_About.html'

class _S_FooterBlock(blocks.StructBlock):
    pass

class HomePage(Page):
    sections = StreamField([
        ('header', _S_HeaderBlock(null=True, blank=True)),
        ('about', _S_AboutBlock(null=True, blank=True)),
        ('footer', _S_FooterBlock(null=True, blank=True)),
    ],null=True, blank=False)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sections'),
    ]

    template = 'home/home_page.html'