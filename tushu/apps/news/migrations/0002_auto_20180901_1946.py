# Generated by Django 2.1 on 2018-09-01 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '新闻公告', 'verbose_name_plural': '新闻公告'},
        ),
    ]
