from datetime import datetime

def convertTo24(m2):
    in_time = datetime.strptime(m2, "%I:%M %p")
    out_time = datetime.strftime(in_time, "%H:%M")
    return out_time


def get_F_hour(hour):
    if hour.startswith("0"):
        hour = hour[1:]
        return hour
        
    else:
        return hour    
  