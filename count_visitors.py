import time
import sys
import sqlite3
from datetime import datetime

DB_NAME = "db.sqlite"

def get_lines(time_obj):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT remote_addr,time_local FROM logs WHERE created > ?", [time_obj])
    resp = cur.fetchall()
    return resp

def get_time_and_ip(lines):
    ips = []
    times = []
    for line in lines:
        ips.append(line[0])
        times.append(parse_time(line[1]))
    return ips, times

def parse_time(time_str):
    try:
        time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
    except Exception:
        time_obj = ""
    return time_obj

if __name__ == "__main__":
    unique_ips = {}
    counts = {}
    start_time = datetime(year=2017, month=3, day=9)
    while True:
        lines = get_lines(start_time)
        ips, times = get_time_and_ip(lines)
        if len(times) > 0:
            start_time = times[-1]
        for ip, time_obj in zip(ips, times):
            day = time_obj.strftime("%d-%m-%Y")
            if day not in unique_ips:
                unique_ips[day] = set()
            unique_ips[day].add(ip)

        for k, v in unique_ips.items():
            counts[k] = len(v)

        count_list = counts.items()
        count_list = sorted(count_list, key=lambda x: x[0])

        print("")
        print(datetime.now())
        for item in count_list:
            print("{}: {}".format(*item))

        time.sleep(5)