# Generated by Django 3.1.4 on 2021-03-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_entry', '0002_stud_rec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='in_out_rp',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]