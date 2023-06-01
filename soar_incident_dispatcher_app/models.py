from django.db import models

# Create your models here.
class ResilientIncidentsData(models.Model):
    record_id = models.AutoField(blank=False, primary_key=True)
    resilient_host = models.CharField(blank=False, db_index=True, max_length=10000)
    incident_id = models.BigIntegerField(blank=False, db_index=True)
    incident_name = models.CharField(blank=False, db_index=True, max_length=10000)
    siem_rule_name = models.TextField(blank=True, db_index=True, max_length=10000, null=True)
    date_created = models.BigIntegerField(blank=True, db_index=True)
    last_update_by_client = models.BooleanField(db_index=True, blank=True, null=True, max_length=15)
    incident_is_work_in_progress_flag = models.BooleanField(db_index=True, blank=True, null=True, max_length=15)
    incident_level = models.CharField(blank=True, db_index=True, null=True, max_length=50)
    incident_handler_triag = models.CharField(blank=False, db_index=True, max_length=10000)
    phase = models.CharField(blank=False, db_index=True, max_length=10000)
    severity = models.CharField(blank=True, null=True, db_index=True, max_length=10000)
    org = models.CharField(blank=False, db_index=True, max_length=10000)
    status = models.CharField(blank=False, db_index=True, max_length=10000)
    open_url = models.CharField(blank=False, db_index=True, max_length=10000)
    asignee_email = models.CharField(blank=True, null=True, db_index=True, max_length=200)
    
    def __str__(self):
        return "{}-{}".format(self.resilient_host, self.incident_id)