# Generated by Django 2.1 on 2018-08-31 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '图书分类', 'verbose_name_plural': '图书分类'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='root',
            new_name='room',
        ),
    ]
