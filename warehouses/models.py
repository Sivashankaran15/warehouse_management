from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

def validate_max_10_rows(value):
    if value > 10:
        raise ValidationError(
            _('Maximum rows exceeded.'),
            params={'value': value},
        )

class WarehouseQ(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseQ.objects.count())

class WarehouseT(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseT.objects.count())

class WarehouseY(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseY.objects.count())

class WarehouseZ(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseA0(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseN(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseU(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseG(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseX(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())
        
class WarehouseJ(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseV(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseH(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseR(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseHR(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseA(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseC(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class WarehouseK(models.Model):
    id = models.AutoField(primary_key=True)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    def clean(self):
        validate_max_10_rows(WarehouseZ.objects.count())

class CommonTracking(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=1)  # A, B, C, D
    in_time = models.DateTimeField(default=timezone.now)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
    out_time = models.DateTimeField(null=True, blank=True)  # Update to allow null values
    def clean(self):
        warehouses_count = WarehouseQ.objects.count() + WarehouseT.objects.count() + WarehouseY.objects.count()
        validate_max_10_rows(warehouses_count)


class OutTimeTracking(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=1)  # A, B, C, D
    out_time = models.DateTimeField(default=timezone.now)
    product_status = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)  # Add product_name field
