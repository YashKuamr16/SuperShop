# Generated by Django 4.2.4 on 2023-09-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_brand_name_alter_maincategory_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=10),
        ),
    ]