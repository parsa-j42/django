# Generated by Django 3.0.3 on 2020-06-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20200630_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_date',
            field=models.DateTimeField(verbose_name='exam date'),
        ),
    ]