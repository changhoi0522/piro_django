# Generated by Django 2.1.5 on 2019-01-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdraw')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]
