# Generated by Django 3.1.5 on 2021-02-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210216_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiapplication',
            name='app_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='apiapplication',
            name='module_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]