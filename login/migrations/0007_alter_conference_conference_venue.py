# Generated by Django 4.1.7 on 2023-08-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_conference_conference_mode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='conference_venue',
            field=models.CharField(default='online', max_length=250, null=True),
        ),
    ]
