# Generated by Django 3.1.6 on 2021-02-04 15:09

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210204_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([], blank=True, null=True)), ('about', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('picture', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('contacts', wagtail.core.blocks.StreamBlock([('contact', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.core.blocks.URLBlock())]))]))], blank=True, null=True)), ('footer', wagtail.core.blocks.StructBlock([], blank=True, null=True))], null=True),
        ),
    ]
