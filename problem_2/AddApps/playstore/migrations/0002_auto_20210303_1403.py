# Generated by Django 3.1.7 on 2021-03-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appadmin',
            name='category',
            field=models.CharField(default='Other', max_length=100),
        ),
    ]
