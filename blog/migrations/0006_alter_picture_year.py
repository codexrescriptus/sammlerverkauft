# Generated by Django 3.2 on 2023-02-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_picture_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='year',
            field=models.CharField(blank=True, db_index=True, max_length=200),
        ),
    ]