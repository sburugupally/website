# Generated by Django 2.1 on 2018-08-30 07:48

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
                ('name', models.TextField(max_length=30)),
                ('email', models.TextField(max_length=30)),
                ('nationality', models.TextField(max_length=25)),
            ],
        ),
    ]
