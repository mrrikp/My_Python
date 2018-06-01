import requests
import json
import time

## define functions

## function to get the sun rise and set times
def suntimes():
    sun = requests.get("https://api.sunrise-sunset.org/json?lat=51.476132&lng=-1.447958&date=today&formatted=0")
    ##print (sun.status_code)
    ##print (sun.content)
    oksun = "[" + bytes.decode(sun.content) + "]"
    ##print (oksun)
    sun_dict_list = json.loads(oksun)
    sun_dict = sun_dict_list[0]['results']
    return sun_dict
## function to say how long to sleep and if it is dawn dusk or night
def sleeptime(timenow, sun_dict):
    CT_end = sun_dict['civil_twilight_end']
    CT_begin = sun_dict['civil_twilight_begin']
    DCT_end = time.mktime(time.strptime(CT_end,'%Y-%m-%dT%H:%M:%S+00:00'))
    DCT_begin = time.mktime(time.strptime(CT_begin,'%Y-%m-%dT%H:%M:%S+00:00'))
    if (timenow > DCT_end) :
         sleep = 1.0
         tod = "night"
    elif (timenow > DCT_begin) :
         sleep = DCT_end-timenow
         tod = "dusk"
    else:   
         sleep = timenow - DCT_begin
         tod = "dawn"
    sleep =int(abs(sleep))
    return [sleep, tod]

## main body
timenow = time.time()
sun_dict = suntimes()
sleeplist = sleeptime(timenow,sun_dict)
tod = sleeplist[1]
sleep = sleeplist[0]
print (sleep)
print (tod)

time.sleep(sleep)

if tod == "dawn" :
    print ("camera on")
    sleeplist = sleeptime(timenow,sun_dict)
    tod = sleeplist[1]
    sleep = sleeplist[0]
    time.sleep(sleep)
if tod == "dusk" :
    print ("camera off")


   

