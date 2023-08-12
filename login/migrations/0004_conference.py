# Generated by Django 4.1.7 on 2023-08-06 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_login_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_name', models.CharField(max_length=80)),
                ('conference_descriptions', models.CharField(max_length=600)),
                ('conference_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('conference_end_date', models.DateField()),
            ],
        ),
    ]
