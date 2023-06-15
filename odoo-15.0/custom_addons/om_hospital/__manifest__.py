{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Erfan Ahammed',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """Hospital Management system""",
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',

    ],
    'demo': [],
    'installable': True,
    "application": True,
    'auto_install': False,
    'license': 'LGPL-3',

}
