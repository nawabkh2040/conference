# Generated by Django 4.1.7 on 2023-08-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0004_alter_paper_paper_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paper_upload',
            field=models.FileField(upload_to='papers/'),
        ),
    ]