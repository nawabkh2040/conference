# Generated by Django 4.1.7 on 2023-08-19 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0003_remove_reviewer_data_password_reviewer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewer_data',
            old_name='reviewer_email',
            new_name='email',
        ),
    ]