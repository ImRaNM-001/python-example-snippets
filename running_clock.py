import time

def update_clock() -> None:
    while True:
        now: time.struct_time = time.localtime()
        hours: int = now.tm_hour % 12 or 12                     # the hour '0' should be '12'
        minutes: int = now.tm_min
        seconds: int = now.tm_sec
        am_or_pm: str = 'PM' if now.tm_hour >= 12 else 'AM'
        hours = hours % 12 or 12                                 # the hour '0' should be '12'
        str_time: str = f'{hours}:{minutes:02d}:{seconds:02d} {am_or_pm}'
        print(str_time, end='\r')
        # time.sleep(60 - now.tm_sec)  # wait until the start of the next minute
        time.sleep(1)  # wait for one second

update_clock()