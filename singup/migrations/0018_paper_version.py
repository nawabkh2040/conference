# Generated by Django 4.1.7 on 2023-08-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0017_alter_paper_other_auth_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
    ]