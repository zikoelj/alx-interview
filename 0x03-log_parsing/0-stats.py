#!/usr/bin/python3


import sys


def print_msg(status_code, total_file_size):
    """reads stdin line by line and computes metrics.
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in status_code.keys()):
                    status_code[code] += 1

            if (counter == 10):
                print_msg(status_code, total_file_size)
                counter = 0

finally:
    print_msg(status_code, total_file_size)
