from xlsxwriter.workbook import Workbook
from django.http import HttpResponse

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

from ficha.models import *


def create_xls(request):
    # your view logic here
    services  = Servicio.objects.all().order_by('id')

    # create a workbook in memory
    output = StringIO.StringIO()

    book = Workbook(output)
    sheet = book.add_worksheet('test')

    bold = book.add_format()
    bold.set_bold()

    sheet.write(0, 0, 'Servicio'        ,bold)
    sheet.write(0, 1, 'Estado Ficha'    ,bold)
    sheet.write(0, 2, 'Solicitud'       ,bold)
    sheet.write(0, 3, 'Nombre'          ,bold)
    sheet.write(0, 4, 'Apellido'        ,bold)


    for i, service in enumerate(services):
        sheet.write(i+1, 0, service.id)
        sheet.write(i+1, 1, service.estado_ficha)
        sheet.write(i+1, 2, service.solicitud)
        sheet.write(i+1, 3, service.ficha.nombre)
        sheet.write(i+1, 4, service.ficha.apellido)
    

    book.close()

    # construct response
    output.seek(0)
    response = HttpResponse(output.read(), 
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=test.xlsx"

    return response