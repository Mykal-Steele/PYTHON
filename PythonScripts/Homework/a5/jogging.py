log_book = [
"cycling;time:1,49;distance:2",
"jogging;time:40,11;distance:6",
"swimming;time:1,49;distance:1.2",
"jogging;time:36,25;distance:5.3",
"hiking;time:106,01;distance:8.29"
]

def  jogging_average(activities: list[str]) -> float:
    jogging = []
    distant = []
    timeT = []
    for i in activities:
        if i.split(";")[0] == "jogging":
            jogging.append(i)
    for i in jogging:
        time = i.split(";")[1]
        if len(time) == 10:
            time = int(time[5:7]) * 60 + int(time[8:10])
            timeT.append(time)
        elif len(time) == 9:
            time = int(time[5]) * 60 + int(time[7:9])
            timeT.append(time)
        else:
            "STFU THE FORMAT IS WRONG"
        total_time = sum(int(num) for num in timeT)

        x = i.split(":")[2]
        distant.append(x)
        total_distant = sum(float(num) for num in distant)
                
    output = total_distant * 1000 /total_time
    return output
        
    
def parse_time(line: str) -> int:
    pass    

def parse_dist(line: str) -> float:
    pass

output = jogging_average(log_book)
print(output)