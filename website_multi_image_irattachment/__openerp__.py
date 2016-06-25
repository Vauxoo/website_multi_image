# coding: utf-8
{
    'name': 'Product Multi-Image',
    'category': 'Website',
    'version': '1.0',
    'author': 'Luke Branch, Cristian Sebastian Rocha and Vauxoo',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'sale',
        'website_sale',
        ],
    'data': [
        'views/product_images.xml',
        'views/website_product_image_carousel.xml',
        'views/theme.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo_images.xml',
    ],
    'application': True,
}
