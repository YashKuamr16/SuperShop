# Generated by Django 4.2.4 on 2023-10-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_contact_newslatter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslatter',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
