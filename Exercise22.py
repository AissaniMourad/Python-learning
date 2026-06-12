# Exercise Date & time

import datetime

target_datetime = datetime.datetime(2030, 2, 17, 12, 0, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")

else:
    print("Target date has NOT passed")
