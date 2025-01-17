import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-sale-promotion",
    description="Meta package for oca-sale-promotion Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-sale_coupon_auto_refresh',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
