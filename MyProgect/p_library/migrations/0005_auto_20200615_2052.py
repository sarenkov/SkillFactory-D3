# Generated by Django 2.2.6 on 2020-06-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200615_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='books',
            field=models.ManyToManyField(related_name='books', to='p_library.Book'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='friend',
        ),
        migrations.AddField(
            model_name='book',
            name='friend',
            field=models.ManyToManyField(to='p_library.Friend'),
        ),
    ]
