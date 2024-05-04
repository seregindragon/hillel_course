time1 = int(input())
if 0 <= time1 <= 8640000:
    day_count = time1 // (24 * 60 * 60)
    hours_count = time1 % (24 * 60 * 60) // (60 * 60)
    minutes_count = time1 % (60 * 60) // 60
    seconds_count = time1 % 60

    if day_count % 10 == 1 and day_count != 11:
        print("{} день, {}:{}:{}".format(str(day_count), str(hours_count).zfill(2), str(minutes_count).zfill(2),
                                         str(seconds_count).zfill(2)))
    elif (day_count % 10 == 1 or day_count % 10 == 3 or day_count % 10 == 4 or day_count % 10 == 2) and day_count != 11:
        print("{} дні, {}:{}:{}".format(str(day_count), str(hours_count).zfill(2), str(minutes_count).zfill(2),
                                        str(seconds_count).zfill(2)))
    else:
        print("{} днів, {}:{}:{}".format(str(day_count), str(hours_count).zfill(2), str(minutes_count).zfill(2),
                                         str(seconds_count).zfill(2)))

else:
    exit("error number")
