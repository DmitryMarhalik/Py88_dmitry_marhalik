# Generated by Django 4.2.1 on 2023-06-06 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=20, unique=True)),
                ('content', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pesron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('message', models.TextField(max_length=300)),
                ('rating', models.IntegerField()),
                ('article_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_articles.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_articles.author'),
        ),
    ]
