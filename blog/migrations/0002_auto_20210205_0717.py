# Generated by Django 3.1.6 on 2021-02-05 07:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='sections',
            field=wagtail.core.fields.StreamField([('BlogPost', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('post', wagtail.core.blocks.RichTextBlock()), ('gallery', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True))]))], null=True),
        ),
    ]