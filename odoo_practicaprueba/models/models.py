# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class res_partner(models.Model):
	_name='res.partner'
	_inherit='res.partner'
	company_type = fields.Selection(selection_add=[('is_school', 'Escuela'),('student', 'Estudiante')])
	student = fields.Many2one(
		'academia.student',
		'Estudiante')

class academia_student(models.Model):
	_inherit = ['portal.mixin', 'mail.thread','mail.activity.mixin']

	_name = 'academia.student'
	_description = 'Modelo para formulario de estudiantes'
	name = fields.Char('Nombre', size = 128, required=True, track_visibility="onchange")
	last_name = fields.Char('Apellido', size = 128)
	#Inicia video 4
	photo = fields.Binary('Fotografia')
	create_date = fields.Datetime('Fecha de creacion', readonly=True)
	#Inica video 5
	note = fields.Html('Comentarios')
	active = fields.Boolean('Activo')
	age = fields.Integer('Edad')
	curp = fields.Char('curp', size =18)
	state = fields.Selection([('draf', 'Documento borrador'),
							('process', 'Proceso'), 
							('done', 'Egresado'),], 'Estado')
	#Relaciones 

	partner_id = fields.Many2one('res.partner','Escuela')

	calificaciones_id = fields.One2many(
		'academia.calificacion',
		'student_id',
		'Calificaciones') 

	country = fields.Many2one('res.country', 'Pais', related='partner_id.country_id')

	invoice_ids = fields.Many2many('account.invoice',
									'student_invoice_rel',
									'student_id', 'invoice_id',
									'Facturas')

	@api.one 
	@api.constrains('curp')
	def _check_lines(self):
		if len(self.curp) < 18:
			raise exceptions.ValidationError("Curp debe tener 18 caracteres")


	@api.model
	def create(self, values):
		if values['name']:
			nombre = values['name']
			exist_ids = self.env['academia.student'].search([('name', '=', self.name)])
			if exist_ids:
				values.update({
					'name': values['name']+"(copia)",
					})
			res = super(academia_student, self).create(values)
			partner_obj = self.env['res.partner']
			vals_to_partner = {
				'name': res['name']+" "+res['last_name'],
				'company_type': 'student',
				'student_id': res['id'],
				}
			print (vals_to_partner)
			partner_id = partner_obj.create(vals_to_partner)
			print ("===>partner_id", partner_id)
			return res
	
	@api.multi
	def unlink(self):
		partner_obj = self.env['res.partner']
		partner_ids = partner_obj.search([('student','in',self.ids)])
		print ("Partnet ##### >>>>>",partner_ids)
		if partner_ids:	
			for partner in partner_ids:
				partner.unlink()
		res = super(academia_student, self).unlink()
		return res


	_order = 'name'
	_default = {
		'status': 'draf',
		'active': True, 
	}




# class curso_odoo/odoo_practicaprueba(models.Model):
#     _name = 'curso_odoo/odoo_practicaprueba.curso_odoo/odoo_practicaprueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100