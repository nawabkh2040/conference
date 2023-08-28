# Generated by Django 4.1.7 on 2023-08-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_conference_has_uploaded_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='conference_mode',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline'), ('hybrid', 'Hybrid')], default='online', max_length=20),
        ),
        migrations.AddField(
            model_name='conference',
            name='conference_venue',
            field=models.CharField(default='online', max_length=250),
        ),
    ]
