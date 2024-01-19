from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

# Create your views here.
def mi_pagina(request):
    return render(request, 'principal.html')


def busqueda(request):
    return render(request, 'listar.html')


def tu_vista(request, codigo_pago):
    with connection.cursor() as cursor:
        # Tu consulta SQL personalizada
        consulta = """
        SELECT
            c."NUMERO_DE_RECIBO" AS cobro_numero_recibo,
            c."DESCRIPCION_COBRO_REALIZAR" AS cobro_descripcion,
            c."IMPORTE_COBRO_CONCEPTO_1" AS cobro_importe,
            c."FECHA_VENCIMIENTO_RECIBO" AS cobro_fecha_vencimiento,
            c."INDICADOR_COBRO_MORA" AS cobro_indicador_mora,
            c."OBSERVACIONES_RECIBO" AS cobro_observaciones
        FROM
            estadosdecuenta_dataconsolidado d
        LEFT JOIN
            estadosdecuenta_cobros c ON d."CODIGO DE PAGO" = c."CODIGO_INTEGRANTE"
        WHERE
            d."CODIGO DE PAGO" = %s;
        """
        cursor.execute(consulta, [codigo_pago])

        # Recuperar los resultados de la consulta
        resultados = cursor.fetchall()

    # Procesar los resultados como desees
    data = [
        {
            'cobro_numero_recibo': row[0],
            'cobro_descripcion': row[1],
            'cobro_importe': row[2],
            'cobro_fecha_vencimiento': row[3],
            'cobro_indicador_mora': row[4],
            'cobro_observaciones': row[5]
        }
        for row in resultados
    ]

    return JsonResponse(data, safe=False)


def tu_vista2(request, codigo_pago):
    with connection.cursor() as cursor:
        # Nueva consulta SQL personalizada
        consulta = """
        SELECT
            c."NUMERO_DE_RECIBO" AS cobro_numero_recibo,
            c."DESCRIPCION_COBRO_REALIZAR" AS cobro_descripcion,
            c."IMPORTE_COBRO_COMPLETO" AS cobro_importe,
            c."FECHA_VENCIMIENTO_RECIBO" AS cobro_fecha_vencimiento,
            c."INDICADOR_COBRO_MORA" AS cobro_indicador_mora
        FROM
            estadosdecuenta_dataconsolidado d
        LEFT JOIN
            estadosdecuenta_cobros c ON d."CODIGO DE PAGO" = c."CODIGO_INTEGRANTE"
        WHERE
            d."CODIGO DE PAGO" = %s;
        """
        cursor.execute(consulta, [codigo_pago])

        # Recuperar los resultados de la consulta
        resultados = cursor.fetchall()

    # Procesar los resultados como desees
    data = [
        {
            'cobro_numero_recibo': row[0],
            'cobro_descripcion': row[1],
            'cobro_importe': row[2],
            'cobro_fecha_vencimiento': row[3],
            'cobro_indicador_mora': row[4]
        }
        for row in resultados
    ]

    return JsonResponse(data, safe=False)