# Generated by Django 4.1.7 on 2023-08-08 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_conference'),
        ('singup', '0010_paper_status_alter_paper_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='conference',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='papers', to='login.conference'),
        ),
    ]
