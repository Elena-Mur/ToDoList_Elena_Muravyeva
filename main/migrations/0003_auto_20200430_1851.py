# Generated by Django 3.0.5 on 2020-04-30 15:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_listmodel_priority'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='listmodel',
            unique_together={('name', 'user')},
        ),
    ]