def format_duration(seconds):
    answer = ""
    year = 31_536_000
    day = 86_400
    hour = 3_600
    minute = 60
    second = 1
    time = {"second": 0,
            "minute": 0,
            "hour": 0,
            "day": 0,
            "year": 0}
    
    while seconds > 0:
        if seconds >= year:
            seconds-=year
            time["year"] += 1
        elif seconds >= day:
            seconds-=day
            time["day"] += 1
        elif seconds >= hour:
            seconds -= hour
            time["hour"] += 1
        elif seconds >= minute:
            time["minute"] += 1
            seconds -= minute
        elif seconds >= second:
            time["second"] = seconds
            seconds = 0

    i = 0
    for d, val in time.items():
        if val == 1:
            answer = f"{val} {d}" + answer
        elif val > 1:
            answer = f"{val} {d}s" + answer
        if i == 0 and answer != "":
            answer = " and " + answer 
            i += 1
        elif i > 0 and val != 0:
            answer = ", " + answer

            i += 1
            
    if answer.startswith(" and "):
        answer = answer[5:]
    if answer.startswith(','):
        answer = answer[1:]
    if answer.startswith(" "):
        answer = answer[1:]
    if answer.endswith(" and "):
        answer = answer[:-5]
    if answer.endswith(','):
        answer = answer[:-1]
    if answer.endswith(" "):
        answer = answer[:-1]
    if answer == "":
        answer = "now"
    return answer

print(format_duration(2790120))