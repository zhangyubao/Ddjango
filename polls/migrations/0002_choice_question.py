# Generated by Django 2.0 on 2017-12-11 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Question'),
        ),
    ]
