# from flask import Flask, render_template, request
from flask import Flask, render_template, request, make_response,Response, jsonify, redirect
# app = Flask(__name__)
# from flask_cors import CORS, cross_origin
from datetime import datetime
import time
# import dateutil.parser as parser

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#     response.headers.add('Access-Control-Allow-Headers', 'Accept')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
#     return response


@app.route('/dashboard')
def showDashboard() :
    time.sleep(1)
    data = {}
    if len(request.args) == 0:
        data = {'st' : '', 'et' : '', 'app_i' : [], 'app_x' :[]}
        return render_template('dashboard.html',data=data)
    ls_cf_apps_include = request.args.getlist("app_i")
    ls_cf_apps_exclude = request.args.getlist("app_x")
    st = request.args.getlist("st")
    et = request.args.getlist("et")
    if len(st) < 1 or len(et) < 1 :
        return "Timestamp field is required"
    st = str(st[0])[:19]
    et = str(et[0])[:19]
    st1 = datetime.strptime(st, "%Y-%m-%dT%H:%M:%S")
    et1 = datetime.strptime(et, "%Y-%m-%dT%H:%M:%S")
    print(st1)
    print(parser.parse(str(st1)).isoformat())
    mon = "0" + str(st1.month) if st1.month < 10 else str(st1.month)
    day = "0" + str(st1.day) if st1.day < 10 else str(st1.day)
    hour = "0" + str(st1.hour) if st1.hour < 10 else str(st1.hour)
    min = "0" + str(st1.minute) if st1.minute < 10 else str(st1.minute)
    st1 = mon + "/" + day + "/" + str(st1.year) + " " + str(hour) + ":" + str(min)

    mon = "0" + str(et1.month) if et1.month < 10 else str(et1.month)
    day = "0" + str(et1.day) if et1.day < 10 else str(et1.day)
    hour = "0" + str(et1.hour) if et1.hour < 10 else str(et1.hour)
    min = "0" + str(et1.minute) if et1.minute < 10 else str(et1.minute)
    et1 = mon + "/" + day + "/" + str(et1.year) + " " + str(hour) + ":" + str(min)
    data = {'st' : st1, 'et' : et1, 'app_i' : ls_cf_apps_include, 'app_x' :ls_cf_apps_exclude}
    return render_template('dashboard.html', data=data)

@app.route('/fetchdashboard')
def showNewDashboard() :
    
    return render_template('loading.html')




if __name__ == "__main__":
    app.run(debug=True,port=5025)
