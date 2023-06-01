# Generated by Django 3.2.7 on 2022-12-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResilientIncidentsData',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('resilient_host', models.CharField(db_index=True, max_length=10000)),
                ('incident_id', models.IntegerField(db_index=True)),
                ('incident_name', models.CharField(db_index=True, max_length=10000)),
                ('siem_rule_name', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('date_created', models.IntegerField(blank=True, db_index=True)),
                ('last_update_by_client', models.BooleanField(blank=True, db_index=True)),
                ('incident_is_work_in_progress_flag', models.BooleanField(blank=True, db_index=True)),
                ('incident_level', models.TextField(blank=True, db_index=True)),
                ('incident_handler_triag', models.CharField(db_index=True, max_length=10000)),
                ('phase', models.CharField(db_index=True, max_length=10000)),
                ('severity', models.CharField(blank=True, db_index=True, max_length=10000, null=True)),
                ('org', models.CharField(db_index=True, max_length=10000)),
                ('status', models.CharField(db_index=True, max_length=10000)),
                ('open_url', models.CharField(db_index=True, max_length=10000)),
                ('asignee_email', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
            ],
        ),
    ]
