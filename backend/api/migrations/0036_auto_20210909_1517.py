# Generated by Django 3.2.6 on 2021-09-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_item_property'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tier',
            name='id',
        ),
        migrations.AlterField(
            model_name='item_match_performance',
            name='tier',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tier',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
