from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(BaseModel):
    mfo = models.CharField(max_length=255)
    tab_number = models.CharField(max_length=255, unique=True)
    crm_id = models.CharField(max_length=255, unique=True)
    telegram_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    status = models.BooleanField(default=None)

    def __str__(self):
        return str(self.mfo)


class Blank(BaseModel):
    class TicketStatus(models.TextChoices):
        PROMISE_TO_PAY = "promise_to_pay", "To'lashga vada berdi"
        LOST_JOB = "lost_job", "Ishsiz ekan"
        REFUSED_TO_PAY = "refused_to_pay", "To'lashdan bosh tortdi"

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='blanks')
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='photos/')
    payment_amount = models.FloatField(null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=TicketStatus.choices)

    def __str__(self):
        return f"{self.employee}"
