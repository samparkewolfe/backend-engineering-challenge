import pytest
from cli_test_helpers import ArgvContext, EnvironContext
import io

import unbabel_cli

def test_read_json_file_format():
    """
    Can command convert this json format into a list?
    """

    text = """{"timestamp": "2018-12-26 18:11:08.509654", "duration": 20}
{"timestamp": "2018-12-26 18:15:19.903159", "duration": 31}
{"timestamp": "2018-12-26 18:23:19.903159", "duration": 54}
"""
    file = io.StringIO(text)

    result = unbabel_cli.command.parse_input_file(file)

    known_output = [
        {"timestamp": "2018-12-26 18:11:08.509654", "duration": 20},
        {"timestamp": "2018-12-26 18:15:19.903159", "duration": 31},
        {"timestamp": "2018-12-26 18:23:19.903159", "duration": 54},
    ]

    assert known_output == result

def test_write_json_file_format():
    """
    Can command convert the average list into this json format?
    """

    averages = [
        {"date": "2018-12-26 18:11:00", "average_delivery_time": 0},
        {"date": "2018-12-26 18:12:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:13:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:14:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:15:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:22:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:23:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}
    ]

    result = unbabel_cli.command.create_output_text(averages)

    known_output = """{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:22:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:23:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}
"""

    assert known_output == result


def test_calculate_average_delivery_time():
    """
    Does command find the correct averages?
    """

    events = [
        {"timestamp": "2018-12-26 18:11:08.509654", "duration": 20},
        {"timestamp": "2018-12-26 18:15:19.903159", "duration": 31},
        {"timestamp": "2018-12-26 18:23:19.903159", "duration": 54},
    ]

    result = unbabel_cli.command.calculate_average_delivery_time(events, 10)

    known_result = [
        {"date": "2018-12-26 18:11:00", "average_delivery_time": 0},
        {"date": "2018-12-26 18:12:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:13:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:14:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:15:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:22:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:23:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5},
    ]

    assert known_result == result

def test_calculate_average_delivery_time_and_window_size():
    """
    Does command find the correct averages for a different window size?
    """

    events = [
        {"timestamp": "2018-12-26 18:11:08.509654", "duration": 20},
        {"timestamp": "2018-12-26 18:15:19.903159", "duration": 31},
        {"timestamp": "2018-12-26 18:23:19.903159", "duration": 54},
    ]

    result = unbabel_cli.command.calculate_average_delivery_time(events, 5)

    known_result = [
        {"date": "2018-12-26 18:11:00", "average_delivery_time": 0},
        {"date": "2018-12-26 18:12:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:13:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:14:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:15:00", "average_delivery_time": 20},
        {"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5},
        {"date": "2018-12-26 18:17:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:18:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:19:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:20:00", "average_delivery_time": 31},
        {"date": "2018-12-26 18:21:00", "average_delivery_time": 0},
        {"date": "2018-12-26 18:22:00", "average_delivery_time": 0},
        {"date": "2018-12-26 18:23:00", "average_delivery_time": 0},
        {"date": "2018-12-26 18:24:00", "average_delivery_time": 54}
    ]

    assert known_result == result

def test_events_is_empty():
    result = unbabel_cli.command.calculate_average_delivery_time([], 0)
    assert not result