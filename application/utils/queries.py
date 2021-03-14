from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def count_by_month():
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT COUNT(id) as Count, strftime("%m", date) as Month '
            'FROM application_application '
            'GROUP BY Month'
        )
        data = dictfetchall(cursor)
    return data


def last_app_for_client():
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT id, MAX(date), phone, product, decision '
            'FROM application_application '
            'GROUP BY phone'
        )
        data = dictfetchall(cursor)
    return data


def new_product():
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT '
        )
        data = dictfetchall(cursor)
    return data