# Generated by Django 3.2 on 2021-04-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('picture', models.ImageField(blank=True, default=None, upload_to='uploaded_img')),
                ('date_of_entry', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]