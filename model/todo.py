import datetime
import json
from run import db

class TodoModel(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(80))
    completed = db.Column(db.Boolean)
    date = db.Column(db.Date, default=datetime.datetime.now())

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'completed': self.completed,
            'date': str(self.date)
        }

    def get_todos(self):
        return [TodoModel.json(todo) for todo in TodoModel.query.all()]

    def get_single_todo(self, todo_id):
        single_todo = TodoModel.query.filter_by(id=todo_id).first()
        if single_todo:
            return TodoModel.json(single_todo)
        return False
    
    def create_todo(self, todo_object):
        new_todo = TodoModel(title=todo_object['title'], body=todo_object['body'], completed=todo_object['completed'])
        db.session.add(new_todo)
        db.session.commit()
        return TodoModel.json(new_todo)


    def delete_todo(self, todo_id):
        todo_id = int(todo_id, base=10)
        single_todo = TodoModel.query.filter_by(id=todo_id).delete()
        db.session.commit()
        if single_todo:
            return TodoModel().get_todos()
        return False
            
    def search_todo(self, todo_id):
        todo = TodoModel.query.filter_by(id=todo_id).first()
        if todo:
            return todo
        return False

    def update_todo(self, todo_id, todo_object):
        todo_id = int(todo_id, base=10)
        todo_to_update = TodoModel().search_todo(todo_id)
        if (not todo_to_update):
            return False
        if 'title' in todo_object:
            todo_to_update.title = todo_object['title']

        if 'body' in todo_object:
            todo_to_update.body = todo_object['body']

        if 'completed' in todo_object:
            todo_to_update.completed = todo_object['completed']

        db.session.commit()
        return TodoModel.json(todo_to_update)
