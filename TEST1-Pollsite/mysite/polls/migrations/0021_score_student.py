# Generated by Django 3.0.3 on 2020-07-02 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20200702_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Student'),
        ),
    ]