from flask_restplus import Resource
import json
from flask import jsonify, request, Response
from model.todo import TodoModel
from run import api
import datetime

def validate_new_todo(todo):
    if ('title' in todo and 'body' in todo and 'completed' in todo):
        return True
    else:
        return False

@api.route('/to-do')
class TodoResource(Resource):
    def get(self):
        all_todos = TodoModel().get_todos()
        response = Response(json.dumps({'todos': all_todos}), status=200, mimetype='application/json')
        return response
    
    def post(self):
        request_todo = request.get_json()
        if request_todo is None:
            return Response(json.dumps({'error': 'Enter a valid todo object. Todo must have title, body and completed property'}), status=400, mimetype='application/json')
        if (not validate_new_todo(request_todo)):
            return Response(json.dumps({'error': 'Enter a valid todo object. Todo must have title, body and completed property'}), status=400, mimetype='application/json')
        id = len(TodoModel().get_todos()) + 1
        request_todo['id'] = id
        request_todo['date'] = str(datetime.datetime.now())

        todo = TodoModel().create_todo(request_todo)
        response = Response(json.dumps({'todo': todo}), status=201, mimetype='application/json')
        return response



@api.route('/to-do/<todo_id>')
class TodoSingleResource(Resource):
    def get(self, todo_id):
        todo_id = int(todo_id, base=10)
        todo = TodoModel().get_single_todo(todo_id)
        if (not todo):
            return Response(json.dumps({'error': 'todo not found'}), status=404, mimetype='application/json')
        return Response(json.dumps({'message': 'todo successfully retrieved!', 'todo': todo}), status=200, mimetype='application/json')

    def delete(self, todo_id):
        if (not TodoModel().search_todo(todo_id)):
            return Response(json.dumps({'error': 'todo not found'}), status=404, mimetype='application/json')
        todo = TodoModel().delete_todo(todo_id)
        return Response(json.dumps({'message': 'todo successfully deleted!', 'todo': todo}), status=200, mimetype='application/json')

    def patch(self, todo_id):
        todo_object = request.get_json()
        if (not TodoModel().search_todo(todo_id)):
            return Response(json.dumps({'error': 'todo not found'}), status=404, mimetype='application/json')
        if (todo_object is None) or ('title' not in todo_object) and ('body' not in todo_object) and ('completed' not in todo_object):
            return Response(json.dumps({'error': 'Enter either a title, body or completed'}), status=400, mimetype='application/json')
        todo = TodoModel().update_todo(todo_id, todo_object)
        return Response(json.dumps({'message': 'todo successfully updated!', 'todo': todo}), status=200, mimetype='application/json')
        