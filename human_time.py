from datetime import datetime

def human_time(datetime_obj=datetime.now()):
    
    hr = int(datetime_obj.hour)
    mi = int(datetime_obj.minute)
    
    hours = ["midnight", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "noon", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "midnight"]
    
    if mi >= 35:
        hr = hr + 1
    
    if mi < 4 or mi > 57:
        if hours[hr] == "noon" or hours[hr] == "midnight":
            human_str = hours[hr]
        else:
            human_str = "%s o'clock" % hours[hr]
    else:
        hours[12] = "twelve"
        
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
            human_str = "twenty to %s" % hours[hr]
        elif mi < 49:
            human_str = "quarter to %s" % hours[hr]
        else:
            human_str = "five to %s" % hours[hr]
    
    return human_str

if __name__ == "__main__":
    print human_time()