time1 = int(input())
dict_date = dict(day="0", hours="0", minutes="0", seconds="0")
if 0 <= time1 <= 8640000:
    day_count = time1 // (24 * 60 * 60)
    hours_count = time1 % (24 * 60 * 60) // (60 * 60)
    minutes_count = time1 % (60 * 60) // 60
    seconds_count = time1 % 60

    if day_count == 0:
        dict_date["day"] = "0"
    else:
        dict_date["day"] = str(day_count)

    if hours_count == 0:
        dict_date["hours"] = "00"
    else:
        dict_date["hours"] = str(hours_count)

    if minutes_count == 0:
        dict_date["minutes"] = "00"
    else:
        dict_date["minutes"] = str(minutes_count)

    if seconds_count == 0:
        dict_date["seconds"] = "00"
    else:
        dict_date["seconds"] = str(seconds_count)


else:
    exit("error number")

print("{} days, {}:{}:{}".format(dict_date["day"], dict_date["hours"], dict_date["minutes"], dict_date["seconds"]))
