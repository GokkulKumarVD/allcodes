# Generated by Django 3.1.4 on 2021-09-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='review_text',
            field=models.TextField(null=True),
        ),
    ]
