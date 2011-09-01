from datetime import datetime

def human_time():
    hr = int(datetime.now().hour)
    mi = int(datetime.now().minute)
    
    hours = ["midnight", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "midnight", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven"]
    
    
    if mi < 4:
        human_str = "%s o'clock" % hours[hr] if hr != 0 else hours[hr]
    elif mi > 57:
        human_str = "%s o'clock" % hours[(hr + 1)] if hr + 1 != 0 else hours[(hr + 1)]
    else:
        if mi < 7:
            human_str = "five past %s" % hours[hr]
        elif mi < 15:
            human_str = "nearly quarter past %s" % hours[hr]
        elif mi < 20:
            human_str = "quarter past %s" % hours[hr]
        elif mi < 26:
            human_str = "nearly half past %s" % hours[hr]
        elif mi < 35:
            human_str = "half past %s" % hours[hr]
        elif mi < 43:
            human_str = "twenty to %s" % hours[(hr + 1)]
        elif mi < 49:
            human_str = "quarter to %s" % hours[(hr + 1)]
        else:
            human_str = "five to %s" % hours[(hr + 1)]
    
    return human_str