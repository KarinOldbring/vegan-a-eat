# Generated by Django 3.2.13 on 2022-06-12 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['created_on']},
        ),
    ]
