import os
from flask import Flask, json, jsonify, make_response
from nested_lookup import get_occurrence_of_value

colors = json.load(open(os.path.abspath("/code/test_data.json")))

app = Flask(__name__)

@app.route('/colordata/api/v1.0/all', methods=['GET'])
def get_all():
  return jsonify((colors))

@app.route('/colordata/api/v1.0/version', methods=['GET']) 
def get_version():
  return jsonify({'version': colors['version']})

@app.route('/colordata/api/v1.0/count/<color>', methods=['GET'])
def get_count(color):
  return jsonify({ "count" : 
      str(get_occurrence_of_value(colors['color_data'], 
      value=color)) })

@app.errorhandler(500)
@app.errorhandler(404)
def handle_error(error):
  response = jsonify({ "code" : error.code, "name" : error.name, "msg" : error.description })
  return make_response(response, error.code)


