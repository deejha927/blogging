# Generated by Django 3.0.8 on 2020-08-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200818_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
