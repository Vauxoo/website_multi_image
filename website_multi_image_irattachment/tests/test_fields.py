# coding: utf-8
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: oscar@vauxoo.com
#    planned by: Oscar Alcala <oscar@vauxoo.com>
############################################################################

from openerp.tests.common import TransactionCase


class TestProductAttachments(TransactionCase):
    """
        This test is to know if all the products that were purchased in the
        same order are retrieved to the functional field 'customer_purchased'.
    """

    def setUp(self):
        super(TestProductAttachments, self).setUp()
        self.product_template = self.env.ref(
            'product.product_product_6_product_template')
        self.product_obj = self.env['product.product']
        self.attachment_obj = self.env['ir.attachment']

    def test_attachments(self):
        images = self.product_template.images
        self.assertIsNotNone(images)

    def test_product_product(self):
        product_id = self.product_obj.create(
            {
                'name': 'Test Product',
            })
        att_id = self.attachment_obj.create(
            {
                'name': 'Test Product Attachment 2',
                'res_id': product_id.id,
                'res_model': 'product.product',
            })
        product_id.write({'images': [(6, 0, [att_id.id])]})
        self.assertEqual(len(product_id.product_tmpl_id.images), 1)
