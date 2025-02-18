{
    'name': "Grade System",
    'author': "Abdulrahman",
    'version': '17.0.0.1',
    'category': '',
    'depends': ['base','mail','hr'],
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/jobs_view.xml',
        'views/grade_view.xml',
        'views/hr_view.xml',
        'data\sequence.xml',
        'wizard\change_state_view.xml'

    ],
    'assets':{
        'web.assets_backend':[
        'model_a\static\src\css\property.css'
        ]
    },

    'application': True,

}
