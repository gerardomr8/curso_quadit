# -*- coding: utf-8 -*-
from odoo import http

# class CursoOdoo/odooPracticacurso(http.Controller):
#     @http.route('/curso_odoo/odoo_practicacurso/curso_odoo/odoo_practicacurso/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/curso_odoo/odoo_practicacurso/curso_odoo/odoo_practicacurso/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('curso_odoo/odoo_practicacurso.listing', {
#             'root': '/curso_odoo/odoo_practicacurso/curso_odoo/odoo_practicacurso',
#             'objects': http.request.env['curso_odoo/odoo_practicacurso.curso_odoo/odoo_practicacurso'].search([]),
#         })

#     @http.route('/curso_odoo/odoo_practicacurso/curso_odoo/odoo_practicacurso/objects/<model("curso_odoo/odoo_practicacurso.curso_odoo/odoo_practicacurso"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('curso_odoo/odoo_practicacurso.object', {
#             'object': obj
#         })