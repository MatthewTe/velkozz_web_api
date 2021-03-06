# Generated by Django 3.1.5 on 2021-02-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SciencePosts',
            fields=[
                ('id', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(null=True)),
                ('upvote_ratio', models.FloatField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('num_comments', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField()),
                ('stickied', models.BooleanField(null=True)),
                ('over_18', models.BooleanField(null=True)),
                ('spoiler', models.BooleanField(null=True)),
                ('author_is_gold', models.BooleanField(null=True)),
                ('author_mod', models.BooleanField(null=True)),
                ('author_has_verified_email', models.BooleanField(null=True)),
                ('permalink', models.URLField(max_length=300, null=True)),
                ('author', models.CharField(max_length=300)),
                ('author_created', models.DateTimeField()),
                ('comment_karma', models.IntegerField(null=True)),
                ('subreddit', models.CharField(default='science', editable=False, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Science Subreddit Posts',
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WallStreetBetsPosts',
            fields=[
                ('id', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(null=True)),
                ('upvote_ratio', models.FloatField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('num_comments', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField()),
                ('stickied', models.BooleanField(null=True)),
                ('over_18', models.BooleanField(null=True)),
                ('spoiler', models.BooleanField(null=True)),
                ('author_is_gold', models.BooleanField(null=True)),
                ('author_mod', models.BooleanField(null=True)),
                ('author_has_verified_email', models.BooleanField(null=True)),
                ('permalink', models.URLField(max_length=300, null=True)),
                ('author', models.CharField(max_length=300)),
                ('author_created', models.DateTimeField()),
                ('comment_karma', models.IntegerField(null=True)),
                ('subreddit', models.CharField(default='wallstreetbets', editable=False, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'WallStreetBets Subreddit Posts',
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
    ]
