import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-akretion-odoo-perf",
    description="Meta package for akretion-odoo-perf Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-perf_account',
        'odoo14-addon-perf_mail',
        'odoo14-addon-perf_mrp',
        'odoo14-addon-perf_multicompany',
        'odoo14-addon-perf_product',
        'odoo14-addon-perf_product_inactive',
        'odoo14-addon-perf_purchase',
        'odoo14-addon-perf_sale',
        'odoo14-addon-perf_sale_stock',
        'odoo14-addon-perf_stock',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
