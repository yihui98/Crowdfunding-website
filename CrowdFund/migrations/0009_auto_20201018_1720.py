# Generated by Django 3.1.2 on 2020-10-18 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CrowdFund', '0008_auto_20201018_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newproject',
            name='donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
