from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)



@app.route('/dashboard')
def showDashboard() :
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
    mon = "0" + str(st1.month) if st1.month < 10 else str(st1.month)
    day = "0" + str(st1.day) if st1.day < 10 else str(st1.day)
    st1 = mon + "/" + day + "/" + str(st1.year) + " " + str(st1.hour) + ":" + str(st1.minute)

    mon = "0" + str(et1.month) if et1.month < 10 else str(et1.month)
    day = "0" + str(et1.day) if et1.day < 10 else str(et1.day)
    et1 = mon + "/" + day + "/" + str(et1.year) + " " + str(et1.hour) + ":" + str(et1.minute)
    data = {'st' : st1, 'et' : et1, 'app_i' : ls_cf_apps_include, 'app_x' :ls_cf_apps_exclude}
    return render_template('dashboard.html', data=data)

@app.route('/fetchdashboard')
def showNewDashboard() :
    
    return render_template('loading.html')




if __name__ == "__main__":
    app.run(debug=True, port=8138)