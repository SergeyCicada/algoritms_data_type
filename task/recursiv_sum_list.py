def sum(data):
    total = data.pop(0)
    if len(data) == 0:
        return total
    else:
        return total + sum(data)


