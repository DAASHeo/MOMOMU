# Generated by Django 3.2.6 on 2021-08-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0007_alter_board_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.CharField(max_length=50),
        ),
    ]
