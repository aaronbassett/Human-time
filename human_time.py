from datetime import datetime

def human_time(datetime_obj=datetime.now()):
    
    hr = int(datetime_obj.hour)
    mi = int(datetime_obj.minute)
    
    hours = ["midnight", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "noon", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "midnight"]
    
    if mi >= 34:
        hr = hr + 1
    
    if mi <= 1 or mi >= 59:
        if hours[hr] == "noon" or hours[hr] == "midnight":
            human_str = hours[hr]
        else:
            human_str = "%s o'clock" % hours[hr]
    else:
        hours[12] = "twelve"

        if mi <= 4:
            human_str = "just after %s" % hours[hr]
        elif mi <= 6:
            human_str = "five past %s" % hours[hr]
        elif mi <= 9:
            human_str = "nearly ten past %s" % hours[hr]
        elif mi <= 11:
            human_str = "ten past %s" % hours[hr]
        elif mi <= 14:
            human_str = "nearly quarter past %s" % hours[hr]
        elif mi <= 16:
            human_str = "quarter past %s" % hours[hr]
        elif mi <= 19:
            human_str = "nearly twenty past %s" % hours[hr]
        elif mi <= 21:
            human_str = "twenty past %s" % hours[hr]
        elif mi <= 24:
            human_str = "nearly twenty five past %s" % hours[hr]
        elif mi <= 26:
            human_str = "twenty five past %s" % hours[hr]
        elif mi <= 27:
            human_str = "nearly half past %s" % hours[hr]
        elif mi <= 33:
            human_str = "half past %s" % hours[hr]
        elif mi <= 36:
            human_str = "twenty five to %s" % hours[hr]
        elif mi <= 39:
            human_str = "nearly twenty to %s" % hours[hr]
        elif mi <= 41:
            human_str = "twenty to %s" % hours[hr]
        elif mi <= 44:
            human_str = "nearly quarter to %s" % hours[hr]
        elif mi <= 46:
            human_str = "quarter to %s" % hours[hr]
        elif mi <= 49:
            human_str = "nearly ten to %s" % hours[hr]
        elif mi <= 51:
            human_str = "ten to %s" % hours[hr]
        elif mi <= 54:
            human_str = "nearly five to %s" % hours[hr]
        elif mi <= 56:
            human_str = "five to %s" % hours[hr]
        else:
            human_str = "nearly %s" % hours[hr]
    
    return human_str

if __name__ == "__main__":
    print human_time()