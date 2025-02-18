# Generated by Django 2.2.19 on 2021-03-19 17:42

from django.db import migrations, models, transaction
import django.db.models.deletion


def migrate_data_from_old_model_to_new_model_up(apps, schema_editor):
    """ Move objects from AptDistribution to NewAptDistribution."""
    AptDistribution = apps.get_model('deb', 'AptDistribution')
    NewAptDistribution = apps.get_model('deb', 'NewAptDistribution')
    for distribution in AptDistribution.objects.all():
        with transaction.atomic():
            NewAptDistribution(
                pulp_id=distribution.pulp_id,
                pulp_created=distribution.pulp_created,
                pulp_last_updated=distribution.pulp_last_updated,
                pulp_type=distribution.pulp_type,
                name=distribution.name,
                base_path=distribution.base_path,
                content_guard=distribution.content_guard,
                remote=distribution.remote,
                publication=distribution.publication
            ).save()
            distribution.delete()


def migrate_data_from_old_model_to_new_model_down(apps, schema_editor):
    """ Move objects from NewAptDistribution to AptDistribution."""
    AptDistribution = apps.get_model('deb', 'AptDistribution')
    NewAptDistribution = apps.get_model('deb', 'NewAptDistribution')
    for distribution in NewAptDistribution.objects.all():
        with transaction.atomic():
            AptDistribution(
                pulp_id=distribution.pulp_id,
                pulp_created=distribution.pulp_created,
                pulp_last_updated=distribution.pulp_last_updated,
                pulp_type=distribution.pulp_type,
                name=distribution.name,
                base_path=distribution.base_path,
                content_guard=distribution.content_guard,
                remote=distribution.remote,
                publication=distribution.publication
            ).save()
            distribution.delete()


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('deb', '0013_aptremote_ignore_missing_package_indices'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewAptDistribution',
            fields=[
                (
                    'distribution_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name='deb_aptdistribution',
                        serialize=False,
                        to='core.Distribution',
                    ),
                ),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.distribution',),
        ),
        migrations.RunPython(
            code=migrate_data_from_old_model_to_new_model_up,
            reverse_code=migrate_data_from_old_model_to_new_model_down,
        ),
        migrations.DeleteModel(
            name='AptDistribution',
        ),
        migrations.RenameModel(
            old_name='NewAptDistribution',
            new_name='AptDistribution',
        ),
    ]
