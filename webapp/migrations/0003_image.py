# Generated by Django 3.1.7 on 2021-07-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webapp', '0002_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(max_length=200)),
                ('photo', models.ImageField(upload_to='myimage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]