def lt5() : # ditambah parameter untuk menentukan kode
    # temp = [{}]
    # temp[0]['ruang'] = 'RT1'
    # temp[0]['hari'] = '10 hari'
    # temp[0]['kode'] = 'kode'
    datas = [{
        'ruang' : 'RT1',
        'servis' : '30/12/2022', # diambil dari data base di dalam data base tanggal bluan tahun dipisah untuk mempermudah dalam penghitubangan 'hari'
        'hari' : '10 hari', # ada perhitungan lebih lanjut,
        'suhu' : '22', # diubah berdasarkan sensor dht
        'standar' : '22', # diambil dari database
        'kode' : 'h', # ada perhitungan lebih lanjut
        'status' : 'on' # dimasukkan sendiri
    }.copy() for _ in range(16)]
    #datas[0]['status'] = kode...
    return datas

def lt6() :
    datas = [{
        'ruang' : 'RT1',
        'servis' : '30/12/2022', # diambil dari data base
        'hari' : '10 hari', # ada perhitungan lebih lanjut,
        'suhu' : '22', # diambil dari database selanjutnya diubah baerdasarkan sensor dht
        'standar' : '22', # diambil dari database
        'kode' : 'h', # ada perhitungan lebih lanjut
        'status' : 'on'
    }.copy() for _ in range(16)]
    return datas

def lt7() :
    datas = [{
        'ruang' : 'RT1',
        'servis' : '30/12/2022', # diambil dari data base
        'hari' : '10 hari', # ada perhitungan lebih lanjut,
        'suhu' : '22', # diambil dari database selanjutnya diubah baerdasarkan sensor dht
        'standar' : '22', # diambil dari database
        'kode' : 'h', # ada perhitungan lebih lanjut
        'status' : 'on'
    }.copy() for _ in range(16)]
    return datas

def lt8() :
    datas = [{
        'ruang' : 'RT1',
        'servis' : '30/12/2022', # diambil dari data base
        'hari' : '10 hari', # ada perhitungan lebih lanjut,
        'suhu' : '22', # diambil dari database selanjutnya diubah baerdasarkan sensor dht
        'standar' : '22', # diambil dari database
        'kode' : 'h', # ada perhitungan lebih lanjut
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'k',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'm', # ini contoh tidak valid
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022', # diambil dari data base
        'hari' : '10 hari', # ada perhitungan lebih lanjut,
        'suhu' : '22', # diambil dari database selanjutnya diubah baerdasarkan sensor dht
        'standar' : '22', # diambil dari database
        'kode' : 'h', # ada perhitungan lebih lanjut
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    },
    {
        'ruang' : 'RT1',
        'servis' : '30/12/2022',
        'hari' : '10 hari',
        'suhu' : '22',
        'standar' : '22',
        'kode' : 'h',
    }]
    datas = loopStatus(datas)
    return datas

def loopStatus(datas):
    for i in range(len(datas)) :
        if datas[i]['kode'] == 'm' :
            datas[i]['status'] = 'off'
        else :
            datas[i]['status'] = 'on'
    return datas