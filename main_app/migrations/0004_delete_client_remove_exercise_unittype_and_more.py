# Generated by Django 4.1.3 on 2022-11-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_client_exercise_unittype_alter_exercise_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='unitType',
        ),
        migrations.AlterField(
            model_name='clientexercise',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='picture',
            field=models.CharField(max_length=100),
        ),
    ]