time1 = int(input())
if 0 <= time1 <= 8640000:
    day_count = time1 // (24 * 60 * 60)
    hours_count = time1 % (24 * 60 * 60) // (60 * 60)
    minutes_count = time1 % (60 * 60) // 60
    seconds_count = time1 % 60

    print("{} days, {}:{}:{}".format(str(day_count), str(hours_count).zfill(2), str(minutes_count).zfill(2),
                                     str(seconds_count).zfill(2)))


else:
    exit("error number")
