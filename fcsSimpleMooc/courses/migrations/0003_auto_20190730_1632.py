# Generated by Django 2.2.3 on 2019-07-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190729_0758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='About the course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='shortcut',
            field=models.SlugField(verbose_name='Shortcut'),
        ),
    ]
