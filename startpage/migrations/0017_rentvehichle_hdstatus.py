# Generated by Django 3.0.5 on 2020-07-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0016_auto_20200703_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentvehichle',
            name='hdstatus',
            field=models.CharField(max_length=200, null=True),
        ),
    ]