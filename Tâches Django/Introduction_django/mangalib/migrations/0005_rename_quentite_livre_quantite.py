# Generated by Django 5.1.1 on 2024-10-30 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0004_rename_auteur_id_livre_auteur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livre',
            old_name='quentite',
            new_name='quantite',
        ),
    ]
