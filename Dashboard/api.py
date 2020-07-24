# from flask import Flask, render_template, request
# from flask import Flask, render_template, request, make_response,Response, jsonify, redirect
# from datetime import datetime
import os
import json
from flask.helpers import send_file, send_from_directory
from flask import Flask, render_template, request, make_response,Response, jsonify, redirect
from mongoConnect2 import mongoConnect2
import dateutil.parser as parser
# app = Flask(__name__)
# from flask_cors import CORS, cross_origin
from datetime import datetime
import time
# import dateutil.parser as parser
mc = mongoConnect2()
app_list = ["IPSDashboard-UX", "support-ode-ux", "Documents-UX", "Advisories-UX", "guidedPath-ux-prod", "OrderStatusUX", "KbArticle-UX", "article-ux", "flatcontents-ux","ProductSupport-UX","security-portal-ux","masthead-ux","support-home-ux","drivers-ux","sonar-validator-ux"]
app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Accept')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

def readFromFile(st, et, ls_cf_apps_include, ls_cf_apps_exclude,r) :
    # with open(file_name) as f:
        # data = json.load(f)
    data=r
    print(type(data))
    ls = data
    n_ls = []
    # os.remove(file_name)
    if len(ls_cf_apps_include) == 0 :
        ls_cf_apps_include = app_list
    for item in ls :
        if item['cf_app_name'] in ls_cf_apps_include and item['cf_app_name'] not in ls_cf_apps_exclude :
            start_time = item['timestamp8601']
            start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
            if start_time >= st and start_time <= et :
                mp = {}
                mp['cf_app_name'] = str(item['cf_app_name'])
                mp['timestamp8601'] = str(item['timestamp8601'])
                mp['Exception_Name'] = str(item['Exception_Name'])
                mp['Exception_Details'] = str(item['Exception_Details'])
                mp['Error_Message'] = str(item['Error_Message'])

                n_ls.append(mp)
    return json.dumps(n_ls)
    with open('response.json', 'w') as json_file:
        json.dump(n_ls, json_file)


    
# @app.route('/download')
# def downloadfile1() :
#     print("hello")
#     return send_from_directory('D:\\1705415\\','Air pollution PR.pdf',as_attachment = True)


# @app.route('/getExceptions')
# def getExceptions() :
#     return 'success'


@app.route('/filterData')
def searchDatabase() :
    ls_cf_apps_include = request.args.getlist("app_i")
    ls_cf_apps_exclude = request.args.getlist("app_x")

    ls_except_include = request.args.getlist("except_i")
    ls_except_exclude = request.args.getlist("except_x")
    st = request.args.getlist("st")
    
    et = request.args.getlist("et")
    if len(st) < 1 or len(et) < 1 :
        return "failed to fetch data"
    st = str(st[0])[:19]
    et = str(et[0])[:19]
    print(len(ls_cf_apps_include))
    st1 = datetime.strptime(st, "%Y-%m-%dT%H:%M:%S")
    et1 = datetime.strptime(et, "%Y-%m-%dT%H:%M:%S")
    print(st1)
    print(et1)
    from_date = st1
    to_date = et1
    r=mc.find_document(from_date, to_date)
    return readFromFile(st1, et1, ls_cf_apps_include, ls_cf_apps_exclude,r)



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
    # print(parser.parse(str(st1)).isoformat())
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
    app.run(debug=True,port=5031)
