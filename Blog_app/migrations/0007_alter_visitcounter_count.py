# Generated by Django 5.0.1 on 2024-05-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0006_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitcounter',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
