{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Erfan Ahammed',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """Hospital Management system""",
    'depends': [
        'mail', 'product'
    ],
    'data': [

        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'data/appointment_sequence_data.xml',
        'wizard/cancel_appointment_wizard.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',

    ],
    'demo': [],
    'installable': True,
    "application": True,
    'auto_install': False,
    'license': 'LGPL-3',

}
