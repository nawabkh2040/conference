# Generated by Django 4.1.7 on 2023-08-24 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0029_paper_reviewer_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='reviewer_comments',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='resubmit_papers',
            old_name='reviewer_comments',
            new_name='comments',
        ),
    ]
