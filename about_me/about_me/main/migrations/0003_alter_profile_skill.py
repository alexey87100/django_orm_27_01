# Generated by Django 3.2.18 on 2024-01-27 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='main.skill'),
        ),
    ]
