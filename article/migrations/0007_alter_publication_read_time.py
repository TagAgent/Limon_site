# Generated by Django 5.0.7 on 2024-08-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_publication_read_time_publication_update_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='read_time',
            field=models.PositiveSmallIntegerField(default=4, verbose_name='время для чтения'),
        ),
    ]