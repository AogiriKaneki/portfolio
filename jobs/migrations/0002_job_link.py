# Generated by Django 2.0.2 on 2019-10-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(default='https://debian.com', max_length=1000),
            preserve_default=False,
        ),
    ]