# Generated by Django 5.1.3 on 2024-11-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_comment_counter_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
