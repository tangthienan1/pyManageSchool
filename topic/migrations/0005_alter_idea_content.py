# Generated by Django 3.2.9 on 2021-11-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='content',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
