# Generated by Django 5.1.5 on 2025-01-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Legia', '0006_alter_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='games', to='Legia.player'),
        ),
    ]
