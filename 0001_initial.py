# Generated by Django 5.0 on 2023-12-06 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=100, verbose_name='인사말')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일 주소')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='책 제목')),
                ('publication_date', models.DateField(verbose_name='출판날짜')),
                ('authors', models.ManyToManyField(to='books.author', verbose_name='저자')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.publisher')),
            ],
        ),
    ]
