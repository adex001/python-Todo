# python-Todo

## API Endpoints
| ROUTES                              |  METHOD  |         DESCRIPTION                      |
|-------------------------------------|----------|------------------------------------------|
|`/api/v1/to-do`                      | `POST`   | `Creates a new Todo`                     |
|`/api/v1/to-do`                      | `GET`    | `Retrieves all todos`                    |
| `/api/v1/to-do/<to-do>`             | `GET`    | `Retrieves a specific todo `             | 
| `/api/v1/to-do/<to-do>`             | `PATCH`  | `Updates a specific todo `               |
| `/api/v1/to-do/<to-do>`             | `DELETE` | `Deletes a specific todo `               |
|

## Requirements
- [Python 3](https://www.python.org/)
- [Postman](https://www.getpostman.com/downloads/)


#### Installation steps
- Clone the git repo
```
$ https://github.com/adex001/python-Todo.git
```
- Cd into project folder
```
$ cd python-Todo
```
- Install pipenv for virtual environment
```
$ pip install pipenv
```
- Activate it
```
$ pipenv shell
```
- Install dependencies
```
$ pipenv install
```
- Install devDependencies
```
$ pipenv install --dev
```
- Environment Setup 
```
FLASK_APP="run.py" 
FLASK_ENV=development
```
- Run the app
``` 
$ flask run 
```
- Test the app
```
$ pytest
```
