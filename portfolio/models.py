from django.db import models
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

# Create your models here.

# Sections

class _S_HeaderBlock(blocks.StructBlock):
    pass

class _S_AboutBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    name = blocks.CharBlock()
    description = blocks.CharBlock()
    description = blocks.RichTextBlock()
    picture = ImageChooserBlock()

    class Meta:
        template = 'portfolio/blocks/_S_About.html'

class _S_Projects_Project_ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    description = blocks.RichTextBlock()
    
    class Meta:
        template = 'portfolio/blocks/_S_Projects_Project_Image.html'

class _S_Projects_ProjectBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.RichTextBlock()
    gallery = blocks.StreamBlock([
        ('image', _S_Projects_Project_ImageBlock())
    ])

    class Meta:
        template = 'portfolio/blocks/_S_Projects_Project.html'

class _S_ProjectsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    foreword = blocks.RichTextBlock()
    projects = blocks.StreamBlock([
        ('project', _S_Projects_ProjectBlock())
    ])

    class Meta:
        template = 'portfolio/blocks/_S_Projects.html'

class _S_FooterBlock(blocks.StructBlock):
    pass

class PortfolioPage(Page):
    sections = StreamField([
        ("header", _S_HeaderBlock(null=True, blank=True)),
        ("about", _S_AboutBlock(null=True, blank=True)),
        ("projects",_S_ProjectsBlock(null=True, blank=True)),
        ("footer", _S_FooterBlock(null=True, blank=True)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sections'),
    ]
    template = 'portfolio/portfolio_page.html'