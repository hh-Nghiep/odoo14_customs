# -*- coding: utf-8 -*-
{
    'name': "Enmasys Project Study",

    'summary': "Enmasys Project Study Github",

    'description': "Enmasys Project Study Github",

    'author': "Huynh Hoang Nghiep",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_access_data.xml',
        'data/menu.xml',
        'views/models.xml',
        'views/project.xml',
        'views/staff.xml',
        'views/customer.xml',
        'views/task2.xml',
    ],
    'application': 'true',
}
