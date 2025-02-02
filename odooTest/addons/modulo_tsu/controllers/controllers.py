
from odoo import http


class ModuloTsu(http.Controller):
    @http.route('/modulo_tsu/modulo_tsu', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/modulo_tsu/modulo_tsu/objects', auth='public')
    def list(self, **kw):
        return http.request.render('modulo_tsu.listing', {
            'root': '/modulo_tsu/modulo_tsu',
            'objects': http.request.env['modulo_tsu.modulo_tsu'].search([]),
        })

    @http.route('/modulo_tsu/modulo_tsu/objects/<model("modulo_tsu.modulo_tsu"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('modulo_tsu.object', {
            'object': obj
        })

