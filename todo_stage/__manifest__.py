{
    'name': 'Add Stages and Tags to To-Dos',
    'description': 'Organize To-Do Tasks using Stages and Tags',
    'author': 'Daniel Reis',
    'depends': ['todo_app', 'mail'],
    'data': [
        # Ch04 Models
        'security/ir.model.access.csv',
        # Ch09 Views
        'views/todo_view.xml',
        # Ch10 Kanban Views
        'views/todo_kanban_view.xml',
        'views/todo_kanban_assets.xml',
        # Ch11 QWeb Reports
        'reports/todo_report.xml',
        'reports/todo_model_report.xml',
    ],
    # Ch05 Demo Data
    'demo': [
        'data/todo.task.csv',
        'data/todo_task.xml',
    ],
}
