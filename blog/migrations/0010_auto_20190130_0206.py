# Generated by Django 2.1.5 on 2019-01-29 17:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190124_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=True, related_name='blog_post_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
