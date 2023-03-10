# Generated by Django 3.2 on 2022-12-31 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ataskaita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ataskaita',
            name='atlyginimas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ataskaita',
            name='bankines_operacijos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ataskaita',
            name='bendrija',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ataskaita', to='home.bendrija'),
        ),
        migrations.AlterField(
            model_name='ataskaita',
            name='pvm_saskaitos_kvitas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ataskaita',
            name='sodra',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ataskaita',
            name='vmi',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
