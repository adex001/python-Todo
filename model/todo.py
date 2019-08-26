from .db import todos

class TodoModel:

    def get_todos(self):
        return todos

    def get_single_todo(self, todo_id):
        single_todo = [todo for todo in todos if todo['id'] == todo_id]
        print(single_todo)
        if single_todo:
            return single_todo[0]
        return False
    
    def create_todo(self, todo_object):
        todos.insert(0, todo_object)
        return todo_object


    def delete_todo(self, todo_id):
        todo_id = int(todo_id, base=10)
        single_todo = [todos.remove(todo) for todo in todos if todo['id'] == todo_id]
        if single_todo:
            return todos
        return False
            
    
    def search_todo(self, todo_id):
        todo_id = int(todo_id, base=10)
        todo = [todo for todo in todos if todo['id'] == todo_id]
        if todo:
            print(todo)
            return True
        return False

    def update_todo(self, todo_id, todo_object):
        todo_id = int(todo_id, base=10)
        for todo in todos:
            if todo['id'] == todo_id:
                if 'title' in todo_object:
                    todo['title'] = todo_object['title']
                if 'body' in todo_object:
                    todo['body'] = todo_object['body']
                if 'completed' in todo_object:
                    todo['completed'] = todo_object['completed']
                return todo
