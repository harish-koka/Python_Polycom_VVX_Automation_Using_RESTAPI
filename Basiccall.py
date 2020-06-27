import json
import requests
import base64
import time

class Phonecall:
    def __init__(self,dutIP,helperIP):
        self.headers = {
            'authorization': "Basic " + (base64.b64encode(bytearray('Polycom:777', 'utf-8'))).decode('utf-8'),
            'content-type': "application/json"
        }
        self.dutIP = dutIP
        self.helperIP = helperIP
        self.callRef = ""


    def placeCall(self):
        #Dialing an IP address from the phone
        url = "http://"+self.dutIP+"/api/v1/callctrl/dial"
        global payload
        payload = "{\"data\":{\"Dest\":\""+self.helperIP+"\",\"Line\":\"1\",\"Type\":\"SIP\"}}"
        response = requests.request("POST", url, headers=self.headers, data = payload)


    def answerCall(self):
        #Get call reference on desination phone to answer the call
        url = "http://"+self.helperIP+"/api/v2/webCallControl/callStatus"
        response = requests.request ("GET", url,headers=self.headers)
        y1 = response.json()
        z=y1["data"][0]
        self.callRef = z["CallHandle"]
        payload = "{\"data\":{\"Ref\":\"" + self.callRef + "\"}}"
        #Answer the call with the call ref on destination
        url = "http://"+self.helperIP+"/api/v1/callctrl/answerCall"
        response = requests.request("POST", url, headers=self.headers, data = payload)
        url = "http://"+self.helperIP+"/api/v1/mgmt/uixml"
        response = requests.request("GET", url, headers=self.headers)
        y1 = response.json()
        z=y1["data"]
        if str(z).__contains__("End Call"):
            print("Call is successfully established")
        else:
            exit("Call is not succefully established")
        time.sleep(5)


    def hasTwowayAudio(self):
        url = "http://"+self.helperIP+"/api/v1/mgmt/media/communicationInfo"
        response = requests.request("GET", url, headers=self.headers)
        y1 = response.json()
        z = y1["data"]["CommunicationType"][0]
        if z == "RxTx":
            print("Call has two-way audio")
        else:
            exit("Call doesn't have two-way audio")


    def holdCall(self):
        #Holding the call with the call ref on destination
        url = "http://"+self.helperIP+"/api/v1/callctrl/holdCall"
        payload = "{\"data\":{\"Ref\":\"" + self.callRef + "\"}}"
        response = requests.request("POST", url, headers=self.headers, data = payload)
        time.sleep(5)


    def resumeCall(self):
        #Resume the call with the call ref on destination
        url = "http://"+self.helperIP+"/api/v1/callctrl/resumeCall"
        payload = "{\"data\":{\"Ref\":\"" + self.callRef + "\"}}"
        response = requests.request("POST", url, headers=self.headers, data = payload)
        time.sleep(5)


    def endCall(self):
        #Ending the call with the call ref on destination
        url = "http://"+self.helperIP+"/api/v1/callctrl/endCall"
        payload = "{\"data\":{\"Ref\":\"" + self.callRef + "\"}}"
        response = requests.request("POST", url, headers=self.headers, data = payload)
        url = "http://" + self.helperIP + "/api/v1/mgmt/uixml"
        response = requests.request("GET", url, headers=self.headers)
        y1 = response.json()
        z = y1["data"]
        if str(z).__contains__("New Call"):
            print("Call is ended successfully")
        else:
            exit("Call is not ended successfully")
        time.sleep(5)

'''
    def uiXmlValidation(self, string):
        self.string = str(string)
        url = "http://"+self.helperIP+"/api/v1/mgmt/uixml"
        response = requests.request("GET", url, headers=self.headers)
        y1 = response.json()
        z=y1["data"]
        if str(z).__contains__(self.string):
            return
        else:
            exit()
'''


