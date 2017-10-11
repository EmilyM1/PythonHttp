from flask import Flask, jsonify,request
app = Flask(__name__)
#Creating a RESTFul API With Flask [1 of 4] - Get Requests

languages = [{'name': 'Python'}, {'name': 'go'}, {'name': 'java'} ]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'working'})

@app.route('/lang/', methods=['GET'])
def returnAll():
	return jsonify({'languagesssss' : languages})

@app.route('/lang/<name>', methods=['GET'])
def returnOne(name):
	return jsonify({'languages' : name})

@app.route('/lang', methods=['POST']) #append more languages to list
def addLang():
	language = {'name': request.json['name']} #returns name users posts,
	#creates dictionary name is key, json'ed returned from reuqest name is value
	#extracts json object send
	languages.append(language)
	#append your add the the globa list
	return jsonify({'languagesssss' : languages})
@app.route('/lang/<name>', methods=['PUT'])
def editJava(name):
	languages[2]['name'] = request.json['name']
	return jsonify({'languages' :languages[2]})



if __name__ == '__main__': #direct run from this script
	app.run(debug=True)