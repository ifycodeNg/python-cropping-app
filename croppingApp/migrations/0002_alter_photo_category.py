# Generated by Django 4.1.3 on 2022-11-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('croppingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.CharField(choices=[('real', 'real'), ('fake', 'fake')], default=None, max_length=10),
        ),
    ]