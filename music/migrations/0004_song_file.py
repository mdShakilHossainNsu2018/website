# Generated by Django 3.0.1 on 2019-12-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190305_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(default=1, upload_to='musics/'),
            preserve_default=False,
        ),
    ]
