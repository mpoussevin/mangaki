# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-10 19:46
from __future__ import unicode_literals

from django.db import migrations, models

def move_nb_episodes_to_work(apps, schema_editor):
    Anime = apps.get_model("mangaki", "Anime")

    # The nb_episodes field is now in the Work base class, while the deprecated_nb_episodes
    # is in the two derived classes and contains the value of interest.
    for anime in Anime.objects.all():
        anime.nb_episodes = anime.deprecated_nb_episodes
        anime.save()

def move_nb_episodes_from_work(apps, schema_editor):
    Anime = apps.get_model("mangaki", "Anime")

    for anime in Anime.objects.all():
        anime.deprecated_nb_episodes = anime.nb_episodes
        anime.save()

class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0039_auto_20160410_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='nb_episodes',
            new_name='deprecated_nb_episodes',
        ),
        migrations.AddField(
            model_name='work',
            name='nb_episodes',
            field=models.TextField(default='Inconnu', max_length=16),
        ),
        migrations.RunPython(move_nb_episodes_to_work, reverse_code=move_nb_episodes_from_work),
    ]
