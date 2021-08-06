from datetime import datetime
import calendar

start_time = datetime.now()
print(f'start time: {start_time}')

with open('/Users/yaboong/test_big_data.txt', 'r') as f:
    lines = f.readlines()
    sunday_cnt = 0
    for line in lines:
        line_value = line.strip()
        date = datetime.strptime(line_value, '%Y%m%d')
        weekday = date.weekday()
        sunday_cnt = sunday_cnt + 1 if calendar.day_name[weekday] == 'Sunday' else sunday_cnt

end_time = datetime.now()
print(f'end time: {end_time}')
print(f'SUNDAY COUNT: {sunday_cnt}')
print(f'elapsed time: {end_time - start_time}')