# Generated by Django 3.0.5 on 2020-05-13 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_item', '0004_auto_20200504_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listitem',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='listitem',
            unique_together=set(),
        ),
    ]