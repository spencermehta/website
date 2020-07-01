# Generated by Django 3.0.7 on 2020-06-13 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('y1', 'UG Year 1 Coursework'), ('y2', 'UG Year 2 coursework'), ('ind', 'Independent project')], default='y1', max_length=20)),
                ('mark', models.IntegerField(null=True)),
                ('github', models.URLField()),
                ('image', models.ImageField(upload_to='project_img/')),
            ],
        ),
    ]
