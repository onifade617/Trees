# Generated by Django 5.1.6 on 2025-02-17 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0003_rename_book_review_tree'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='farmer',
        ),
    ]
