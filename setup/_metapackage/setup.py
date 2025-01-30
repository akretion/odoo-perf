import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-akretion-odoo-perf",
    description="Meta package for akretion-odoo-perf Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-perf_account>=16.0dev,<16.1dev',
        'odoo-addon-perf_mail>=16.0dev,<16.1dev',
        'odoo-addon-perf_mrp>=16.0dev,<16.1dev',
        'odoo-addon-perf_multicompany>=16.0dev,<16.1dev',
        'odoo-addon-perf_product>=16.0dev,<16.1dev',
        'odoo-addon-perf_product_inactive>=16.0dev,<16.1dev',
        'odoo-addon-perf_purchase>=16.0dev,<16.1dev',
        'odoo-addon-perf_sale>=16.0dev,<16.1dev',
        'odoo-addon-perf_sale_stock>=16.0dev,<16.1dev',
        'odoo-addon-perf_stock>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
