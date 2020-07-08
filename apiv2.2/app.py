from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Log 
import json
import Preprocessing

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/error-logs'
}

initialize_db(app)

@app.route('/')
def get_logs():
    logs = Log.objects().to_json()
    return Response(logs, mimetype="application/json", status=200)
    # return "<h2>hello %s</h2>" %user

@app.route('/', methods=['POST'])
def add_logs():
    body = request.get_data().decode('utf-8')
    d = json.loads(body)
    for obj in d:
        obj2=Preprocessing.error_clean(obj)
        log =  Log(**obj2).save()
        id =log.id
        # return {'id': str(id)}, 200
    return "ok"

@app.route('/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Log.objects.get(id=id).update(**body)
    return '', 200

@app.route('/<id>', methods=['DELETE'])
def delete_log(id):
    movie = Log.objects.get(id=id).delete()
    return '', 200


@app.route('/<id>')
def get_log(id):
    logs = Log.objects.get(id=id).to_json()
    return Response(logs, mimetype="application/json", status=200)
# if __name__=="__main__":
app.run()

