# Generated by Django 3.2.9 on 2021-11-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sondageapp', '0004_alter_questionnaire_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='code_commercial',
            field=models.CharField(default='t1', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='customer',
            field=models.CharField(max_length=200),
        ),
    ]