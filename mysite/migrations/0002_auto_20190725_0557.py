# Generated by Django 2.2.3 on 2019-07-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sample_doc',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
    ]