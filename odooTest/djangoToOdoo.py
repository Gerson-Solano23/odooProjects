# En Django (views.py)
from xmlrpc import client

def sync_curso_to_odoo(curso_django):
    odoo = client.ServerProxy('http://localhost:9001/xmlrpc/2/object')
    db = 'nombre_base_de_datos'
    uid = 1  # ID del usuario admin
    password = 'admin'

    # Crear curso en Odoo
    odoo_id = odoo.execute_kw(db, uid, password, 'academia.curso', 'create', [{
        'codigo': curso_django.idCurso,
        'nombre': curso_django.nombre,
        'creditos': curso_django.creditos,
    }])

    # Guardar el ID de Odoo en Django (si es necesario)
    curso_django.odoo_id = odoo_id
    curso_django.save()
