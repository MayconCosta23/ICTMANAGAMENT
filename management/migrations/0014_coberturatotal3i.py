# Generated by Django 4.1.3 on 2022-12-14 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_delete_compstatusn50s_coberturatotaln50s_boardname'),
    ]

    operations = [
        migrations.CreateModel(
            name='coberturatotal3i',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeds', models.IntegerField()),
                ('testable', models.IntegerField()),
                ('tested', models.IntegerField()),
                ('boardname', models.CharField(max_length=30)),
            ],
        ),
    ]