#!/usr/bin/python3
import logging
import os
import re
import subprocess
import sys
import yaml


def load_config():
    config_path = os.path.normpath(os.environ['HOME'] + '/.ics_to_gnome')
    with open(config_path, 'r') as file:
        try:
            return yaml.load(file)
        except:
            logging.error(f'Configuration file ~/.ics_to_gnome does not exists or is invalid')
            exit(2)


def do_main():
    config = load_config()
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        logging.error(f'File {file_path}')
        exit(1)

    with open(file_path, 'r') as file_to_add:
        data = file_to_add.read()
        event_data = re.search('BEGIN:VEVENT(.*)END:VEVENT', data, re.DOTALL).group(1)

    with open(config['calendarPath'], 'r') as f:
        calendar_data = f.read()
        appended = calendar_data.replace("END:VCALENDAR", f"BEGIN:VEVENT{event_data}END:VEVENT\nEND:VCALENDAR")

    with open(config['calendarPath'], 'w') as f:
        f.write(appended)

    without_tabs = event_data.replace("\n\t", "")
    event_uid = re.search("UID:(.*)\n", without_tabs).group(1)

    event_uid_in_calendar = f'{config["calendarUid"]}:{event_uid}'

    subprocess.Popen(['gnome-calendar', '-u', event_uid_in_calendar])


if __name__ == '__main__':
    do_main()
