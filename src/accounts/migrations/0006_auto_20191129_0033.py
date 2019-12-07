# Generated by Django 2.2.4 on 2019-11-29 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_emailactivation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailactivation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
