import requests
from flask import Flask
import time
import re
import json
import pymsteams
#from apscheduler.schedulers.background import BackgroundScheduler
import threading
from mongoConnect2 import mongoConnect2
import os

# link to kibana
template = "https://elk-s3b.dell.com/kibana/app/kibana#/discover?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:curr,to:till))&_a=(columns:!(_source),filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:a45c9220-cf0f-11e9-acc9-e5bbf98ee050,key:cf_app_name,negate:!f,params:(query:IPSDashboard-UX),type:phrase),query:(match:(cf_app_name:(query:IPSDashboard-UX,type:phrase)))),('$state':(store:appState),meta:(alias:!n,disabled:!f,index:a45c9220-cf0f-11e9-acc9-e5bbf98ee050,key:source_type,negate:!f,params:(query:APP%2FPROC%2FWEB),type:phrase),query:(match:(source_type:(query:APP%2FPROC%2FWEB,type:phrase)))),('$state':(store:appState),meta:(alias:!n,disabled:!f,index:a45c9220-cf0f-11e9-acc9-e5bbf98ee050,key:level,negate:!f,params:(query:error),type:phrase),query:(match:(level:(query:error,type:phrase))))),index:a45c9220-cf0f-11e9-acc9-e5bbf98ee050,interval:auto,query:(language:kuery,query:''),sort:!(!(timestamp8601,desc)))"



# apps list
app_list = ["IPSDashboard-UX", "support-ode-ux", "Documents-UX", "Advisories-UX", "guidedPath-ux-prod", "OrderStatusUX", "KbArticle-UX", "article-ux", "flatcontents-ux","ProductSupport-UX","security-portal-ux","masthead-ux","support-home-ux","drivers-ux","sonar-validator-ux"]



# Global params
log_list = []
url = "https://elk-pc1.dell.com/kibana/s/ddsonline/api/console/proxy?path=_search&method=POST"
app = Flask(__name__)


# Update Autorization key using Postman
headers = {
  'kbn-xsrf': 'reporting',
  'Authorization': 'Basic bWFub3Jhbmphbl9tYWhhcmFuYTpXZWxjb21lQDIwMjA=',
  'Content-Type': 'application/json'
}

port = int(os.getenv("PORT"))

# Thread Class
class WorkerThread (threading.Thread):
   def __init__(self, threadID):
      threading.Thread.__init__(self)
      self.threadID = threadID
   def run(self):
      print ("Starting " + self.threadID)
      getResponseFromKibana()
      print('LogList length: ' + str(len(log_list)))
      print ("Exiting " + self.threadID)

class Logs :
    def __init__(self, ts, mess, cf_app):
        self.ts = str(ts)
        self.mess = str(mess)
        self.cf_app = str(cf_app)
    def printLog(self):
        print('Timestamp = ',self.ts)
        print('Message = ',self.mess)
        print('App = ',self.cf_app)
    def time(self):
        return self.ts
    def mess1(self):
        return self.mess
    def name(self):
        return self.cf_app

    def error_clean(df):
    #function for data processing
        x = re.search(r'message-data-start =>(.*)message-data-end',
                    df['message'])
        if x is not None:
            em={"Error_Message": x.group(1)}    
            y = re.search(r'exception-data-start =>(.*)exception-data-end', df['message'])
            if y is not None:
                ed={"Exception_Details":y.group(1)}
                z = re.search(r'exception-data-start => (.*?):', df['message'])
                if z is not None:
                    en={"Exception_Name": z.group(1)}
        else:
            x = re.search(r'Error calling method:(.*)Ex', df['message'])
            if x is not None:
                em={"Error_Message": x.group(1)}
                y = re.search(r'Ex:(.*)', df['message'])
                if y is not None:
                    ed={"Exception_Details":y.group(1)}
                    z = re.search(r'Ex:(.*).', df['message'])
                    if z is not None:
                        pos = z.group(1).find('.')
                        if pos == -1:
                            pos = len(z.group(1))
                        en={"Exception_Name":z.group(1)[:pos]}
            else:
                x = re.search(r'Error(.*)?fromDate', df['message'])
                if x is not None:
                    em={"Error_Message": x.group(1)}
                    y = re.search(r'Exception =(.*)', df_err['message'])
                    if y is not None:
                        ed={"Exception_Details":y.group(1)}
                        z = re.search(r'=>(.*?):', df_err['message'])
                        if z is not None:
                            en={"Exception_Name": z.group(1)}
                else:
                    em = {"Error_Message":"No Data Extracted"} 
                    ed = {"Exception_Details":"No Data Extracted"}
                    en = {"Exception_Name":"Generic Exception"}
        df.update(en)     
        df.update(em) 
        df.update(ed)       
        return df
    
@app.route('/')
def home():
    return "Hello World, Welcome to Kibana Log analyzer and Notifier!!"

@app.route('/results/')
def res():
    return json.dumps(log_list, indent = 4)


@app.route('/getLogs/')
def getResponseFromKibana():
    # calculating timestamps
    print("Getting data from Kibana....")
    curr = int(time.time() * 1000) #- 18000000
    lte = str(curr)
    gte = str(curr - int(15*60*1000))
    
    # sending requests
    payload = "{\r\n    \"from\": 0,\r\n    \"query\": {\r\n        \"bool\": {\r\n            \"filter\": [\r\n                {\r\n                    \"terms\": {\r\n                        \"origin\": [\r\n                            \"rep\"\r\n                        ]\r\n                    }\r\n                },\r\n                {\r\n                    \"term\": {\r\n                        \"level\": \"error\"\r\n                    }\r\n                },\r\n                {\r\n                    \"range\": {\r\n                        \"timestamp\": {\r\n                            \"gte\": \"" + gte + "\",\r\n                            \"lte\": \"" + lte + "\"\r\n                        }\r\n                    }\r\n                }\r\n            ]\r\n        }\r\n    },\r\n    \"size\": 10000\r\n}"
    response = requests.request("POST", url, headers=headers, data = payload, verify = False)
    
    # response handling
    if response.status_code != 200:
      return "Failed to fetch data"
    
    # filtering the data for given app name
    ls = response.json()['hits']['hits']
    #print(response.json())
    logs = []
    ind = []
    index = 0
    print("hello")
    time_ls = []
    for item in response.json()['hits']['hits'] :
        time_ls.append(str(item['_source']['timestamp8601']))
        if item['_source']['cf_app_name'] not in app_list or item['_source']['source_type'] != "APP/PROC/WEB" :
            ind.append(index)
        index = index + 1
        
    ind.reverse()
    time_ls.sort()
    for item in ind:
        del ls[int(item)]

    print("here")
    print(len(ls))
    out_json = response.json()
    out_json['hits'].update({'hits' : ls})

    # initialize dictionary and message
    d = {} 
    # msg="nothing"
    # iterating through the elements of list 
    for i in app_list: 
        d[i] = 0  
    
    logs = []
    # creating list of object(s)
    print("Processing logs...")
    for item in out_json['hits']['hits'] :
      res_mp = {}
      res_mp['timestamp8601'] = str(item['_source']['timestamp8601'])
      res_mp['cf_app_name'] = str(item['_source']['cf_app_name'])
      res_mp['message'] = str(item['_source']['@message'])
      res_mp['level'] = str(item['_source']['level'])
      res_mp = Logs.error_clean(res_mp)
      #print(res_mp)
      log_list.append(res_mp)
      logs.append(res_mp)#possible duplication of log_list var
      d[res_mp['cf_app_name']]+=1
    # if(len(msg)>0):
    msg = ""
    sum=0
    # for k,v  in d.items():
    #     if v>0:
    #         sum+=v
    #         v=str(v)
    #         tup=(k, ' : ', v)
    #         msg=msg+"".join(tup)+"<br>"
                # msg=msg+"Total number of errors in the last 15 minutes="+str(sum)+"<br><br>"
    # if sum>0:
    topapps=[]
    toperr=[]
    p=""
        #collecting top 5 app names and error occurences
    for i in range(0,len(d)):
        m_val=0
        for k,v in d.items():
            if v>0:
                sum+=v
            if(v>m_val):
                m_val=v
                p=k
        d[p]=0
        topapps.append(p)
        toperr.append(m_val)
        
        #putting the app names in msg in descending order
    for i in range(0,len(d)):
        tup=(topapps[i], ' : ', str(toperr[i]))
        lk = template
        lk = lk.replace('curr',"\'"+str(time_ls[0])+"\'")
        lk = lk.replace("till","\'"+str(time_ls[-1])+"\'")
        lk = lk.replace('IPSDashboard-UX',str(topapps[i]))
        msg=msg+"".join(tup)+"\t\t\t<a href=\"" + lk + "\">See details here</a><br>"
            
        


    print("Done processing...\nDumping Logs...")

    mc = mongoConnect2()
    mc.push_to_db(logs)
    print("Done dumping...")
    print(msg)
    
    time.sleep(2)
    print("Sending Alert....")
    myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/f831df10-5cba-44bb-9126-38d017bd6d11@945c199a-83a2-4e80-9f8c-5a91be5752dd/IncomingWebhook/bc676eaf4afe43bc8146729e1cf3486f/bac75b88-988d-461d-a871-e229d7449a72")

    myTeamsMessage.title("ALERT !")
    myTeamsMessage.color("#FF4040")
    msg="<b>There is a spike observed in the number of errors that are logged in Kibana.<br>"+ "Total number of errors in the last 15 minutes= "+str(sum)+"<br> Following are the details:<br></b>"+msg
    if sum>0:
        myTeamsMessage.text(msg)
        myTeamsMessage.addLinkButton("Redirect to Dashboard", "https://elk-s3b.dell.com/kibana/app/kibana#")
    
        myTeamsMessage.send()
    # for getting the response
    return out_json

def scheduler(a, b):
    index = 0
    while True :
        log_list.clear()
        getResponseFromKibana()
        time.sleep(20*60)
        # worker_thread = WorkerThread('Thread-' + str(index))        
        # worker_thread.start()
        # worker_thread.join()
        # index = index + 1
        # time.sleep(20*60)

# sched = BackgroundScheduler(daemon=True)
# sched.add_job(getResponseFromKibana,'interval', minutes=3)
# sched.start()

if __name__ == '__main__':
    thread = threading.Thread(target=scheduler, args = (1, 2))
    thread.daemon = True
    thread.start()
    app.run(host='0.0.0.0', port=port)
    #app.run(debug = True, use_reloader=False)
    #scheduler()
        
