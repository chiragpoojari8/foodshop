# Generated by Django 5.0.7 on 2024-09-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_rename_category_loginform_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Loginform',
        ),
        migrations.AlterField(
            model_name='foodimages',
            name='images',
            field=models.ImageField(upload_to='Food/'),
        ),
    ]