#-*- coding: utf-8 -*-

duration = int(input())
hour_in_seconds = 3600
minutes_in_seconds = 60

hours = duration // hour_in_seconds
duration = duration % hour_in_seconds

minutes = duration // minutes_in_seconds
duration = duration % minutes_in_seconds

print("{}:{}:{}".format(hours, minutes, duration))