# Generated by Django 3.1.1 on 2020-09-28 06:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted', models.DateTimeField(default=datetime.datetime.now)),
                ('form_name', models.CharField(max_length=64)),
                ('address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='map_image',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='map_url',
        ),
        migrations.CreateModel(
            name='CkanOrgSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_form_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Modal Form')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]