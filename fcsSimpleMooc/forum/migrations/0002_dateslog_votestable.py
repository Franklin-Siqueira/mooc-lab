# Generated by Django 2.2.3 on 2019-08-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatesLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Last update')),
            ],
        ),
        migrations.CreateModel(
            name='VotesTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votePositives', models.IntegerField(blank=True, default=0, verbose_name='PositiveVotes')),
                ('voteNegatives', models.IntegerField(blank=True, default=0, verbose_name='NegativeVotes')),
            ],
        ),
    ]
