# Generated by Django 4.0.5 on 2022-06-14 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to='blog/templates/posts/'),
        ),
    ]
