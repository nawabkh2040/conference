# Generated by Django 4.1.7 on 2023-08-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0014_alter_paper_conference'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='has_uploaded_paper',
            field=models.BooleanField(default=False),
        ),
    ]
