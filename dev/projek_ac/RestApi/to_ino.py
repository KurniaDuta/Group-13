def result_datas(kode, suhu, standar, status, person, last_index):
    send = {}
    send['kode'] = kode
    send['index1'] = is_person(person, kode, status)
    send['index2'] = index_remote(suhu, standar, last_index)
    return send

def is_person(person, kode, status):
    if kode == "m" or status == "off" :
        return "0"
    elif person >= 1 :
        return "1"
    return "0"


def index_remote(suhu, standar, last_index):
    if int(suhu) < int(standar) :
        if int(last_index) + 1 != 15 :
            return str(int(last_index) + 1)
    elif int(suhu) > int(standar) :
        if int(last_index) - 1 != -1 :
            return str(int(last_index) - 1)
    return last_index