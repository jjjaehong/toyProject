# Generated by Django 5.2 on 2025-04-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='password',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
