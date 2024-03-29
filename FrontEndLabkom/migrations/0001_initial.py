# Generated by Django 3.0.2 on 2020-01-30 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('email', models.EmailField(default='nama@web.com', max_length=254)),
                ('alamat', models.CharField(max_length=100)),
                ('waktu_posting', models.DateTimeField(auto_now_add=True)),
                ('kategori', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
