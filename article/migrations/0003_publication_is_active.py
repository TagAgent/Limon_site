# Generated by Django 5.0.7 on 2024-07-31 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_publication_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]