from datetime import datetime, timedelta

import json


def handle_input_file_and_window_size(file_path, window_size):
    events = []
    with open(file_path, 'r') as file:
        events = parse_input_file(file)
    
    if events:
        averages = calculate_average_delivery_time(events, window_size)

    with open("output_file.json", 'w') as file:
        text = create_output_text(averages)
        print(text)
        file.write(text)


def parse_input_file(file):
    """
    Read the specific format of JSON required for this task
    """
    events = []
    for line in file:
        events.append(json.loads(line))
    return events


def create_output_text(averages):
    """
    Create text in specific format of output for this task
    """
    text = ""
    for line in averages:
        text = text + json.dumps(line) + '\n'
    return text


def calculate_average_delivery_time(events, window_size):
    if not events:
        return []

    # Get the times of the first and last events
    first_event_time = parse_timestamp(events[0]["timestamp"]).replace(second=0, microsecond=0)
    last_event_time = parse_timestamp(events[-1]["timestamp"])

    # Round up last event time to nearest minute
    last_event_time = last_event_time.replace(minute=last_event_time.minute + 1, second=0, microsecond=0)

    # Find total number of minutes between first and last event
    minutes = abs(last_event_time - first_event_time).total_seconds() / 60

    averages = []

    # For each minute between the first and last (incl) events
    for i in range(0, int(minutes) + 1):

        # Find what minute we are in
        current_minute = first_event_time + timedelta(minutes=i)

        # Get all events before this minute within window_size
        window_start_time = current_minute - timedelta(minutes=window_size)
        events_inside_the_window = [event for event in events if parse_timestamp(event["timestamp"]) >= window_start_time and parse_timestamp(event["timestamp"]) < current_minute]

        # Calculate the average duration of events inside the window
        durations = [event["duration"] for event in events_inside_the_window]
        average_duration = sum(durations) / len(durations) if durations else 0

        # Cast duration int if it's a whole number to get exactly the same output as the example
        if average_duration.is_integer():
            average_duration = int(average_duration)

        averages.append({"date": current_minute.strftime("%Y-%m-%d %H:%M:%S"), "average_delivery_time": average_duration})

    return averages


def parse_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")