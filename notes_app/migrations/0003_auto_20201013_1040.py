# Generated by Django 3.1.2 on 2020-10-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_auto_20201013_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
