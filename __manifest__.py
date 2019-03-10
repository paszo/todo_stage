{
  'name': 'Add Stages and Tags to To Do-Dos',
  'description': 'Organize To-Do Tasks using Stages and Tags',
  'author': 'Daniel Reis',
  'depends': ['todo_app', 'mail', 'contacts'],
  'data': [
    'security/ir.model.access.csv',
    'views/todo_menu.xml',
    'views/todo_view.xml',
    'views/todo_kanban_view.xml',
    'views/todo_kanban_assets.xml',
  ],
  'demo': [
    'data/todo.task.csv',
    'data/todo_task.xml',
  ]
}
