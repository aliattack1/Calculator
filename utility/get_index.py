def action(lis, place):
    count = -1
    index = 1
    for i in lis:
        count += len(i)
        if count == place:
            return index
        index += 1