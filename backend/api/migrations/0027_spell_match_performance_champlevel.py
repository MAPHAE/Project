# Generated by Django 3.1.2 on 2021-09-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20210907_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell_match_performance',
            name='champLevel',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0),
        ),
    ]
