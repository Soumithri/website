# Generated by Django 2.2.3 on 2019-07-25 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20190725_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('github_link', models.URLField(blank=True, max_length=250, null=True)),
                ('linkedIn_link', models.URLField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='docs/')),
            ],
        ),
    ]