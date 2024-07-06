def result(lantai5, lantai6, lantai7, lantai8):
    info = {}
    info['fifth'] = loop(lantai5)
    info['sixth'] = loop(lantai6)
    info['seventh'] = loop(lantai7)
    info['eighth'] = loop(lantai8)
    return info


def loop(lt):
    temp = ''
    for i in range(len(lt)):
        if lt[i]['kode'] == 'm' :
            return 'm'
        else :
            temp = 'h'
    return temp
