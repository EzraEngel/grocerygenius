# Generated by Django 5.0.2 on 2024-02-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ggrid', '0004_keystroke'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(default='apple.jpg', upload_to=''),
        ),
    ]