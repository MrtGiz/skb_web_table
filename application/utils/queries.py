from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def count_by_month():
    """определяет количество заявок в каждом месяце"""
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT COUNT(id) as Count, strftime("%m", date) as Month '
            'FROM application_application '
            'GROUP BY Month'
        )
        data = dictfetchall(cursor)
    return data


def last_app_for_client():
    """определяет последнюю заявку по клиенту"""
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT id, MAX(date) as date, phone, product, decision '
            'FROM application_application '
            'GROUP BY phone'
        )
        data = dictfetchall(cursor)
    return data


def new_product_after_approve():
    """определяет клиентов, по которым были заведены заявки на другой продукт после одобрения"""
    with connection.cursor() as cursor:
        cursor.execute(
            """
            WITH apps_approved as (
                SELECT * 
                FROM application_application
                WHERE decision = 'approved'
                )
            SELECT * 
            FROM application_application as app JOIN apps_approved as appr
            WHERE app.phone = appr.phone AND app.id > appr.id AND app.product != appr.product
            """
        )
        data = dictfetchall(cursor)
    return data
