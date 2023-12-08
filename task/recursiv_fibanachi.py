def fibanachi (data):
    data.append(data[-1] + data[-2])
    if len(data) == 10:
        return data
    return fibanachi(data)





