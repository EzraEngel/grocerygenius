# Generated by Django 5.0.2 on 2024-02-16 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ggrid', '0005_category_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
