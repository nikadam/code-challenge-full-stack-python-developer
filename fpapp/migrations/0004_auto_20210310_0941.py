# Generated by Django 3.1.7 on 2021-03-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpapp', '0003_favoritelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoritelist',
            name='photo_id',
        ),
        migrations.AlterField(
            model_name='favoritelist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
