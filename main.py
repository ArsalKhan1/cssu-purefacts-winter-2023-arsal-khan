
from datetime import datetime, timedelta
import csv


def find_longest_free_time(meetings):
    # combine all meeting times into a single list
    times = []
    for _, start_time, end_time in meetings:
        times.append((start_time, "start"))
        times.append((end_time, "end"))

    # sort the times in ascending order
    times.sort()

    # initialize variables to track the longest free time
    max_start_time = None
    max_duration = 0
    num_attendees = len(meetings)

    # initialize variables to track the current free time
    current_start_time = "09:00"
    current_attendees = 0

    # iterate through the sorted times and track the longest free time
    for time, event_type in times:
        if current_attendees == num_attendees and current_start_time >= "09:00" and time <= "17:00":
            duration = (int(time[:2]) - int(current_start_time[:2])) * 60 + (
                        int(time[3:]) - int(current_start_time[3:]))
            if duration > max_duration:
                max_duration = duration
                max_start_time = current_start_time

        if event_type == "start":
            current_attendees += 1
        else:
            current_attendees -= 1

        if current_attendees == 0:
            current_start_time = time

    if max_start_time is not None:
        return max_start_time, max_duration
    else:
        return "None"


def main(file_path):
    # read the CSV file
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip the header row
        meetings = []
        for row in csv_reader:
            client_id = row[0]
            start_time = row[1]
            end_time = row[2]
            meetings.append((client_id, start_time, end_time))

    # find the largest span of free time
    result = find_longest_free_time(meetings)

    # print the result
    if result == "None":
        print("No free time available for everyone to meet.")
    else:
        start_time, duration = result
        print(f"The largest span of free time is {duration} minutes starting at {start_time}.")


# run the main function for each test file
for i in range(1, 6):
    print(f"--- Test {i} ---")
    main(f"test{i}.csv")
