# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2014 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from openerp.osv import orm, fields


class FinancierFund(orm.Model):

    _name = 'financier.fund'
    _description = 'Financier Fund'
    _rec_name = 'code'
    _columns = {
        # Nombre
        'code': fields.char('Code', size=64, required=True),
        # Nombre
        'name': fields.char('Name', size=64, required=True),
        # Tipo
        'type': fields.selection([('view', 'View'),
                                  ('normal', 'Normal')], 'Type'),
        # Padre
        'parent_id': fields.many2one('financier.fund', 'Parent'),
        # Recursos Propios
        'own_fund': fields.boolean('Own Fund')
    }

    _defaults = {
        'type': lambda *a: 'normal',
    }
