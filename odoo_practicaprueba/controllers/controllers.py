# -*- coding: utf-8 -*-
from odoo import http

# class CursoOdoo/odooPracticaprueba(http.Controller):
#     @http.route('/curso_odoo/odoo_practicaprueba/curso_odoo/odoo_practicaprueba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/curso_odoo/odoo_practicaprueba/curso_odoo/odoo_practicaprueba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('curso_odoo/odoo_practicaprueba.listing', {
#             'root': '/curso_odoo/odoo_practicaprueba/curso_odoo/odoo_practicaprueba',
#             'objects': http.request.env['curso_odoo/odoo_practicaprueba.curso_odoo/odoo_practicaprueba'].search([]),
#         })

#     @http.route('/curso_odoo/odoo_practicaprueba/curso_odoo/odoo_practicaprueba/objects/<model("curso_odoo/odoo_practicaprueba.curso_odoo/odoo_practicaprueba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('curso_odoo/odoo_practicaprueba.object', {
#             'object': obj
#         })