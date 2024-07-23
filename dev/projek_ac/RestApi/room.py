from day import result_day
import pymongo
import time
import datetime

client = pymongo.MongoClient(
    "mongodb+srv://dutaka2945:6XvyLNT9JZj1z6TN@iot13.t2mqlae.mongodb.net/"
)
db = client["IoT_AC"]


def find_service():
    result = db.room.find({}, {"room5.service": 1, "_id": 0})
    for result in result:
        if "room5" in result and "service" in result["room5"]:
            result = result["room5"]["service"]
    return result

def find_standar(person):
    result = "24"
    current = current_time()
    datas = list(db.room.find({}, {"room5.datas": 1, "_id": 0}))
    datas = datas[0]['room5']['datas']
    for i in datas:
        if i['day'] == current[1] and (time_standar(i['time_start']) <= current[0] and time_standar(i['end_time']) > current[0]) and (person >= int(i['min_people']) and person <= int(i['max_people'])):
            result = i['standar']
    return result
            
def current_time():
    localtime = time.localtime(time.time())
    minute = str(localtime.tm_min)
    if len(minute) == 1 :
        minute = "0" + minute
    hour = int(str(localtime.tm_hour) + minute)
    day = datetime.datetime(localtime.tm_year, localtime.tm_mon, localtime.tm_mday)
    return [hour, day.strftime("%A")]

def time_standar(t):
    result = t.split(":")
    return int(result[0] + result[1])

def lt8(person, out_data, temperature):
    datas = [
        {
            "servis": "1/1/2024",
            "standar": "27",
        }.copy()
        for _ in range(16)
    ]
    room = ['RL6', 'RL7', 'RL8', 'RL9', 'RH1', 'RH2', 'RH3', 'RH4', 'RH5', 'RH6', 'RH7', 'RH8', 'RH9', 'RS1', 'RS2', 'RS3']
    datas = loop_room(datas, room)
    datas = loop_suhu(datas, temperature)
    datas = loop_day(datas)
    datas = loop_kode(datas, person)
    datas = loop_status(datas, out_data)
    return datas


def lt6(person, out_data, temperature):
    datas = [
        {
            "servis": "1/3/2024",
            "standar": "27",
        }.copy()
        for _ in range(16)
    ]
    room = ['RD1', 'RD2', 'RD3', 'RD4', 'RD5', 'RD6', 'RA', 'RJ', 'LS1', 'LS2', 'LS3', 'LS4', 'LS5', 'LS6', 'LS7', 'LS8']
    datas = loop_room(datas, room)
    datas = loop_suhu(datas, temperature)
    datas = loop_day(datas)
    datas = loop_kode(datas, person)
    datas = loop_status(datas, out_data)
    return datas


def lt7(person, out_data, temperature):
    datas = [
        {
            "servis": "5/5/2024",
            "standar": "27",
        }.copy()
        for _ in range(16)
    ]
    room = ['LS9', 'LP1', 'LP2', 'LP3', 'LP4', 'LP5', 'LP6', 'LP7', 'LP8', 'LP9', 'PRP', 'RL1', 'RL2', 'RL3', 'RL4', 'RL5']
    datas = loop_room(datas, room)
    datas = loop_suhu(datas, temperature)
    datas = loop_day(datas)
    datas = loop_kode(datas, person)
    datas = loop_status(datas, out_data)
    return datas


def lt5(person, out_data, temperature):
    datas = [
        {
            "ruang": "RT1",
            "servis": find_service(),
            "suhu": temperature[0], 
            "standar": find_standar(person[0]), 
        },
        {
            "ruang": "RT2",
            "servis": "1/3/2024",
            "suhu": temperature[1],
            "standar": "27",
        },
        {
            "ruang": "RT3",
            "servis": "1/3/2024",
            "suhu": temperature[2],
            "standar": "27",
        },
        {
            "ruang": "RT4",
            "servis": "1/3/2024",
            "suhu": temperature[3],
            "standar": "27",
        },
        {
            "ruang": "RT5",
            "servis": "1/3/2024",
            "suhu": temperature[4],
            "standar": "27",
        },
        {
            "ruang": "RT6",
            "servis": "1/3/2024",
            "suhu": temperature[5],
            "standar": "27",
        },
        {
            "ruang": "RT7",
            "servis": "1/3/2024",
            "suhu": temperature[6],
            "standar": "27",
        },
        {
            "ruang": "RT8",
            "servis": "1/3/2024",
            "suhu": temperature[7],
            "standar": "27",
        },
        {
            "ruang": "RT9",
            "servis": "1/3/2024",
            "suhu": temperature[8],
            "standar": "27",
        },
        {
            "ruang": "RP1",
            "servis": "1/3/2024",
            "suhu": temperature[9],
            "standar": "27",
        },
        {
            "ruang": "RP2",
            "servis": "1/3/2024",
            "suhu": temperature[10],
            "standar": "27",
        },
        {
            "ruang": "RP3",
            "servis": "1/3/2024",
            "suhu": temperature[11],
            "standar": "27",
        },
        {
            "ruang": "RP4",
            "servis": "1/3/2024",
            "suhu": temperature[12],
            "standar": "27",
        },
        {
            "ruang": "RP5",
            "servis": "5/7/2024",
            "suhu": temperature[13],
            "standar": "27",
        },
        {
            "ruang": "RP6",
            "servis": "1/3/2024",
            "suhu": temperature[14],
            "standar": "27",
        },
        {
            "ruang": "RP7",
            "servis": "1/3/2024",
            "suhu": temperature[15],
            "standar": "27",
        },
    ]
    datas = loop_day(datas)
    datas = loop_kode(datas, person)
    datas = loop_status(datas, out_data)
    return datas


def loop_suhu(datas, temperature):
    for i in range(len(datas)):
        datas[i]["suhu"] = temperature[i]
    return datas


def loop_status(datas, out_data):
    for i in range(len(datas)):
        if datas[i]["kode"] == "m":
            datas[i]["status"] = "off"
        else:
            datas[i]["status"] = out_data[i]
    return datas


def loop_kode(datas, person):
    for i in range(len(datas)):
        difference = abs(int(datas[i]["suhu"]) - int(datas[i]["standar"]))
        if difference < 4 or person[i] == 0:
            datas[i]["kode"] = "h"
        elif difference < 7:
            datas[i]["kode"] = "k"
        else:
            datas[i]["kode"] = "m"
    return datas


def loop_day(datas):
    for i in range(len(datas)):
        datas[i]["hari"] = result_day(datas[i]["servis"])
    return datas

def loop_room(datas, room):
    for i in range(len(datas)):
        datas[i]["ruang"] = room[i]
    return datas