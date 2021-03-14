import csv
import xlwt
from datetime import datetime
from django.http import HttpResponse

from application.models import Application


class Export:
    def __init__(self, filename=f'data_{datetime.now().date()}', model=Application):
        self.filename = filename
        self.model = model

    def _get_data(self):
        queryset = self.model.objects.all()
        return queryset

    def _get_model_fields(self):
        field_names = [field.name for field in self.model._meta.fields]
        return field_names

    def export_to_csv(self):
        field_names = self._get_model_fields()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={self.filename}.csv'
        writer = csv.writer(response, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)

        for instance in self.model.objects.all():
            writer.writerow([getattr(instance, field) for field in field_names])

        return response

    def export_to_excel(self):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{self.filename}.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(self.model.__name__)

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = self._get_model_fields()
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = self.model.objects.all().values_list()

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if isinstance(row[col_num], datetime):
                    ws.write(row_num, col_num, row[col_num].strftime("%Y-%m-%d %H:%M"), font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response
