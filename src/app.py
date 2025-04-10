from flask import Flask, jsonify, request
app = Flask(__name__)

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"

todos = [ 
    { "done": True, "label": "Sample Todo 1" },
    { "done": True, "label": "Sample Todo 1" }
         ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     request_body = request.json
#     print("Incoming request with the following body", request_body)
#     return 'Response for the POST todo'

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    json_response = jsonify(todos)
    return json_response

# @app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position):
#     print("This is the position to delete:", position)
#     return 'something'

# @app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position):
#     print("This is the position to delete:", position)
#     return 'something'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_todo_list = jsonify(todos)
    return json_todo_list

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)