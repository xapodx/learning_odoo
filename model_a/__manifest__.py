{
    'name': "Model A",
    'author': "Abdulrahman",
    'version': '17.0.0.1',
    'category': '',
    'depends': ['base','mail','hr'],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/jobs_view.xml',
        'views/property_view.xml',
        'views/hr_view.xml',

    ],
    'assets':{
        'web.assets_backend':[
            'model_a\static\src\css\property.css'
        ]
    },

    'application': True,

}
