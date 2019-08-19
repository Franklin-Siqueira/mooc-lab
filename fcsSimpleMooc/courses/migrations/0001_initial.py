# Generated by Django 2.2.3 on 2019-08-19 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Contents')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('shortcut', models.SlugField(verbose_name='Shortcut')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('about', models.TextField(blank=True, verbose_name='About the course')),
                ('startDate', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Image')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Last update')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Number (ordering)')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='courses.Course', verbose_name='Course')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('embedded', models.TextField(blank=True, verbose_name='Vídeo embedded')),
                ('file', models.FileField(blank=True, null=True, upload_to='lessons/materials')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='materials', to='courses.Lesson', verbose_name='Lesson')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='courses.Announcement', verbose_name='Announcement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['created_on'],
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AddField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='announcements', to='courses.Course', verbose_name='Course'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Cancelled')], default=1, verbose_name='Status')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enrollments', to='courses.Course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enrollments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'unique_together': {('user', 'course')},
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
