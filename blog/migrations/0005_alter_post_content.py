# Generated by Django 4.0.5 on 2022-06-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to='posts/'),
        ),
    ]
