from day import result_day
import pymongo
import time

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

def find_standar():
    result_standar = db.room.find({}, {"room5.datas.standar": 1, "_id": 0})
    for result_standar in result_standar:
        if "room5" in result_standar and "datas" in result_standar["room5"]:
            for data in result_standar["room5"]["datas"]:
                if "standar" in data:
                    result_standar = data["standar"]
    return result_standar

query = {
    "room5.datas": {
        "$elemMatch": {
            "time_start": {"$lte": "end_time"}
        }
    }
}

results = db.room.find(query)

for result in results:
    print(result)

def lt8(person, out_data, temperature):
    datas = [
        {
            "ruang": "RT1",
            "servis": "1/1/2024",  # diambil dari data base di dalam data base tanggal bluan tahun dipisah untuk mempermudah dalam penghitubangan 'hari'
            "standar": "22",  # diambil dari database
        }.copy()
        for _ in range(16)
    ]
    datas = loop_suhu(datas, temperature)
    datas = loop_day(datas)
    datas = loop_kode(datas, person)
    datas = loop_status(datas, out_data)
    return datas


def lt6(person, out_data, temperature):
    datas = [
        {
            "ruang": "RT1",
            "servis": "1/3/2024",
            "standar": "22",
        }.copy()
        for _ in range(16)
    ]
    datas = loop_suhu(datas, temperature)
    datas = loop_day(datas)
    datas = loop_kode(datas, person)
    datas = loop_status(datas, out_data)
    return datas


def lt7(person, out_data, temperature):
    datas = [
        {
            "ruang": "RT1",
            "servis": "5/5/2024",
            "standar": "22",
        }.copy()
        for _ in range(16)
    ]
    datas = loop_suhu(datas, temperature)
    datas = loop_day(datas)
    datas = loop_kode(datas, person)
    datas = loop_status(datas, out_data)
    return datas


def lt5(person, out_data, temperature):
    datas = [
        {
            "ruang": "RT1",
            "servis": find_service(),  # diambil dari data base # ada perhitungan lebih lanjut,
            "suhu": temperature[
                0
            ],  # diambil dari database selanjutnya diubah baerdasarkan sensor dht
            "standar": "22",  # diambil dari database # ada perhitungan lebih lanjut
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[1],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[2],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[3],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[4],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[5],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[6],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[7],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[8],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[9],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[10],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[11],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[12],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "5/7/2024",
            "suhu": temperature[13],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[14],
            "standar": "22",
        },
        {
            "ruang": "RT1",
            "servis": "30/12/2022",
            "suhu": temperature[15],
            "standar": "22",
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
    # print(person[0])
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