# Generated by Django 3.0.5 on 2020-04-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
