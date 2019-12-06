# Generated by Django 2.2.7 on 2019-12-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Squirel Age', max_length=30),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='approaches',
            field=models.BooleanField(default=True, help_text='Approaches'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='chasing',
            field=models.BooleanField(default=True, help_text='Chasing'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='climbing',
            field=models.BooleanField(default=True, help_text='Climbing'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Squirrel Fur Color', max_length=30),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='eating',
            field=models.BooleanField(default=True, help_text='Eating'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='foraging',
            field=models.BooleanField(default=True, help_text='Foraging'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='indifferent',
            field=models.BooleanField(default=True, help_text='Indifferent'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='kuks',
            field=models.BooleanField(default=True, help_text='Kuks'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='moans',
            field=models.BooleanField(default=True, help_text='Moans'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='quaas',
            field=models.BooleanField(default=True, help_text='Quaas'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='running',
            field=models.BooleanField(default=True, help_text='Running'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='runs_from',
            field=models.BooleanField(default=True, help_text='Runs from'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='tail_flags',
            field=models.BooleanField(default=True, help_text='Tail flags'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='tail_twitches',
            field=models.BooleanField(default=True, help_text='Tail twitches'),
        ),
    ]
