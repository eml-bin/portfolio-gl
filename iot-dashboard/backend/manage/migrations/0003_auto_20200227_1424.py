# Generated by Django 2.1 on 2020-02-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0002_auto_20200226_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='anon', max_length=15, null=True, verbose_name='Usuario'),
        ),
    ]
