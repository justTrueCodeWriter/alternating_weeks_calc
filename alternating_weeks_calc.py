from datetime import datetime, date

things = ["direction1", "direction2", "direction3"]

weeks_by_things = [[] for _ in range(len(things))]

current_date = datetime.now()
last_week = date(current_date.year, 12, 28).isocalendar().week

things_counter = 0
for week_number in range(1, last_week+1):
    weeks_by_things[things_counter].append(week_number)

    things_counter += 1
    if things_counter == len(weeks_by_things):
        things_counter = 0

things_counter = 0
for thing_weeks in weeks_by_things:
    if (current_date.isocalendar().week in thing_weeks):
        print(things[things_counter])
    things_counter += 1
