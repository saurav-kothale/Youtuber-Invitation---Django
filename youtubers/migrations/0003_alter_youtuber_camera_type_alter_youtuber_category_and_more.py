# Generated by Django 4.1.4 on 2022-12-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_alter_youtuber_camera_type_alter_youtuber_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('Canon', 'Canon'), ('Nikon', 'Nikon'), ('Sony', 'Sony'), ('Red', 'Red'), ('Fuji', 'Fuji'), ('Panasonic', 'Panasonic'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('Code', 'Code'), ('Mobile_review', 'Mobile_review'), ('Vlogs', 'Vlogs'), ('Comedy', 'Comedy'), ('Gaming', 'Gaming'), ('Roasting', 'Roasting'), ('Cooking', 'Cooking')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('Solo', 'Solo'), ('Small', 'Small'), ('Large', 'Large')], max_length=255),
        ),
    ]