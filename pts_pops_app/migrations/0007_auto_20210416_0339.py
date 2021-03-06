# Generated by Django 3.2 on 2021-04-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pts_pops_app', '0006_auto_20210415_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='good',
            field=models.CharField(choices=[('1', "1 Star: It was okay but you could've done better Justin!!"), ('2', '2 Star: It was really decent for a 3 days worth of code'), ('3', '3 Star: Nice! This was unexpected!')], max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_bio',
            field=models.TextField(blank=True, help_text='This field is not required!!', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_email',
            field=models.EmailField(help_text='This field is not required!!', max_length=254, null=True),
        ),
    ]
