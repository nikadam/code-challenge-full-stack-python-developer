# Generated by Django 3.1.7 on 2021-03-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpapp', '0004_auto_20210310_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritelist',
            name='secret',
            field=models.CharField(max_length=256),
        ),
    ]
