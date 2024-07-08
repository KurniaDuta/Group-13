def result_datas(kode, suhu, standar, person, last_index):
    send = {}
    send['kode'] = kode
    send['index1'] = is_person(person, kode)
    send['index2'] = index_remote(suhu, standar, last_index)
    return send

def is_person(person, kode):
    if kode == "m" :
        return "0"
    elif person >= 1 :
        return "1"
    return "0"

def index_remote(suhu, standar, last_index):
    if suhu < standar :
        if int(last_index) + 1 != 10 :
            return str(int(last_index) + 1)
    elif suhu > standar :
        if int(last_index) - 1 != -1 :
            return str(int(last_index) - 1)
    return last_index