import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

regs = []

def in_dictlist(key, value, my_dictlist):
    for entry in my_dictlist:
        if entry[key] == value:
            return entry
    return False

def getLastId(regs):
	if len(regs) > 0:
		return regs[-1]['id'] + 1
	return 1

@app.route('/demo/register', methods=['POST'])
def register():
	id_count = 1
	name = request.form['name']
	lang = request.form['lang']
	regs.append({
		'id': getLastId(regs),
		'name':name,
		'lang': lang
		})
	id_count += 1
	return jsonify({'status':True,'response':'Añadido usuario ' + name + ' con idioma ' + lang})

@app.route('/demo/greeting/<name>', methods=['GET'])
def saludo(name):
	reg = in_dictlist('name',name,regs)
	if reg:
		return jsonify({'id':reg['id'],'content':'Hello, ' + reg['name'] + '!'})
	else:
		return jsonify({'status':False,'response':'Usuario no registrado'})

@app.route('/demo/list', methods=['GET'])
def listar():
	if len(regs) > 0:
		return jsonify(regs)
	else:
		return jsonify({'status':False,'response':'No se encuentran usuarios'})

app.run()