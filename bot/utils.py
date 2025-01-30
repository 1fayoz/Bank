from asgiref.sync import sync_to_async

from apps.common import models


@sync_to_async
def get_employee(telegram_id):
    return models.Employee.objects.filter(telegram_id=telegram_id).first()


@sync_to_async
def update_or_create_employee(telegram_id, mfo, tab_number, crm_id):
    employee = models.Employee.objects.filter(telegram_id=telegram_id).first()
    if employee:
        employee.status = True
        employee.save()
    else:
        models.Employee.objects.create(
            telegram_id=telegram_id,
            mfo=mfo,
            status=True,
            tab_number=tab_number,
            crm_id=crm_id
        )



