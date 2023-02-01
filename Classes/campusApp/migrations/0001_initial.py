# Generated by Django 4.1.5 on 2023-02-01 06:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_Name', models.CharField(blank=True, default='', max_length=60)),
                ('campus_State', models.CharField(blank=True, default='', max_length=2)),
                ('campus_ID', models.IntegerField(blank=True, default='')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
