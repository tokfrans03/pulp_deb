# Generated by Django 4.2.9 on 2024-03-22 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deb', '0029_distributedpublication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aptdistribution',
            options={'default_related_name': '%(app_label)s_%(model_name)s', 'permissions': [('manage_roles_aptdistribution', 'Can manage roles on an APT distribution')]},
        ),
        migrations.AlterModelOptions(
            name='aptpublication',
            options={'default_related_name': '%(app_label)s_%(model_name)s', 'permissions': [('manage_roles_aptpublication', 'Can manage roles on an APT publication')]},
        ),
        migrations.AlterModelOptions(
            name='aptremote',
            options={'default_related_name': '%(app_label)s_%(model_name)s', 'permissions': [('manage_roles_aptremote', 'Can manage roles on an APT remote')]},
        ),
        migrations.AlterModelOptions(
            name='aptrepository',
            options={'default_related_name': '%(app_label)s_%(model_name)s', 'permissions': [('manage_roles_aptrepository', 'Can manage roles on APT repositories'), ('modify_content_aptrepository', 'Add content to, or remove content from a repository'), ('repair_aptrepository', 'Copy an APT repository'), ('sync_aptrepository', 'Sync an APT repository'), ('delete_aptrepository_version', 'Delete a repository version')]},
        ),
        migrations.AlterModelOptions(
            name='verbatimpublication',
            options={'default_related_name': '%(app_label)s_%(model_name)s', 'permissions': [('manage_roles_verbatimpublication', 'Can manage roles on a verbatim publication')]},
        ),
    ]
