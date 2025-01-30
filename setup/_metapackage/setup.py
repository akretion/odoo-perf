import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-akretion-odoo-perf",
    description="Meta package for akretion-odoo-perf Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-account_index',
        'odoo8-addon-base_no_needaction',
        'odoo8-addon-mrp_index',
        'odoo8-addon-purchase_index',
        'odoo8-addon-purchase_performance',
        'odoo8-addon-sale_stock_index',
        'odoo8-addon-stock_picking_wave_index',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 8.0',
    ]
)
