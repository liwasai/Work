# Generated by Django 2.2.6 on 2020-02-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_rank',
            field=models.IntegerField(default=0),
        ),
    ]