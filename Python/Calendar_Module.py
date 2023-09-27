import calendar

day_list = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']
b = input() #mm dd yyyy
a = calendar.weekday(int(b[5:10]),int(b[0:2]), int(b[3:5])) #yyyy mm dd
print(day_list[a])

'''You are given a date  in MM DD YYYY format. Your task is to find what the day is on that date.'''