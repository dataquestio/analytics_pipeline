import time
import sys
import sqlite3
from datetime import datetime

DB_NAME = "db.sqlite"

def get_lines(time_obj):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT time_local,http_user_agent FROM logs WHERE created > ?", [time_obj])
    resp = cur.fetchall()
    return resp

def get_time_and_ip(lines):
    browsers = []
    times = []
    for line in lines:
        times.append(parse_time(line[0]))
        browsers.append(parse_user_agent(line[1]))
    return browsers, times

def parse_time(time_str):
    try:
        time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
    except Exception:
        time_obj = ""
    return time_obj

def parse_user_agent(user_agent):
    browsers = ["Firefox", "Chrome", "Opera", "Safari", "MSIE"]
    for browser in browsers:
        if browser in user_agent:
            return browser
    return "Other"

if __name__ == "__main__":
    browser_counts = {}
    start_time = datetime(year=2017, month=3, day=9)
    while True:
        lines = get_lines(start_time)
        browsers, times = get_time_and_ip(lines)
        if len(times) > 0:
            start_time = times[-1]
        for browser, time_obj in zip(browsers, times):
            if browser not in browser_counts:
                browser_counts[browser] = 0
            browser_counts[browser] += 1

        count_list = browser_counts.items()
        count_list = sorted(count_list, key=lambda x: x[0])
        print("")
        print(datetime.now())
        for item in count_list:
            print("{}: {}".format(*item))

        time.sleep(5)