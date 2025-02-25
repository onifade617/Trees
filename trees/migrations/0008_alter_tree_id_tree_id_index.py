# Generated by Django 5.1.6 on 2025-02-25 12:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0007_alter_tree_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='tree',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
