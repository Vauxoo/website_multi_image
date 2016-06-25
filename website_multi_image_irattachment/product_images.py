# coding: utf-8
from openerp import models, fields, api


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    _order = 'name asc'

    product_tmpl_id = fields.Many2one('product.template', string='Images')
    product_id = fields.Many2one('product.product', string='Images')
    sequence = fields.Integer(
        'Sequence',
        help="Dragging and dropping an image at te beggining of the list of"
             "images will make the picture on top the default image to be"
             "shown if there is no main image in the product form.")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('ir.attachment', 'product_tmpl_id',
                             string='Images')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    images = fields.One2many('ir.attachment', 'product_id',
                             string='Images',
                             compute='_get_tmpl_attachments',
                             inverse='_set_tmpl_attachments',
                             store=True)

    @api.multi
    @api.depends('product_tmpl_id.images')
    def _get_tmpl_attachments(self):
        for record in self:
            record.images = record.images or record.product_tmpl_id.images

    @api.multi
    def _set_tmpl_attachments(self):
        for record in self:
            if not record.product_tmpl_id.images:
                record.product_tmpl_id.images = record.images
