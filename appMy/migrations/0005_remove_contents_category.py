# Generated by Django 4.1.7 on 2023-04-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_rename_categoies_categories_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='category',
        ),
    ]
