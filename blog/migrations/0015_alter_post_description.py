# Generated by Django 5.1.3 on 2024-12-01 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_image1_post_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
