# Generated by Django 4.2.6 on 2023-10-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y%m%d/background_images'),
        ),
    ]
