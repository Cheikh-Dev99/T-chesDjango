# Generated by Django 5.1.1 on 2024-10-28 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0003_rename_auteur_livre_auteur_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livre',
            old_name='auteur_id',
            new_name='auteur',
        ),
    ]
