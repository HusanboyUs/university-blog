# Generated by Django 4.0.3 on 2022-11-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=15, null=True)),
                ('summary', models.CharField(blank=True, max_length=15, null=True)),
                ('topic', models.TextField(blank=True, max_length=300, null=True)),
                ('posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'ordering': ['posted'],
            },
        ),
    ]
