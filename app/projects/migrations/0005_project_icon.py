# Generated by Django 3.0.7 on 2020-06-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200614_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.CharField(default='university', max_length=50),
            preserve_default=False,
        ),
    ]
