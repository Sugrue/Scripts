import re

def meraki_parser(string):
    #REGEX:
    DATE_RE = r'(?P<date>\w+\s\d+)'
    TIME_RE = r'(?P<time>[\d:]+)'
    SOURCE_RE = r'(?P<source>(?:[\d.]+){4})'
    LEVEL_RE = r'(?P<level>\d)'
    TIMESTAMP_RE = r'(?P<timestamp>(?:[\d.]+){2})'
    DEVICE_NAME_RE = r'(?P<device_name>[^\s]+)'
    TYPE_RE = r'(?P<type>[\d\w]+)'
    #SUB_TYPE = r'(?P<sub_type>[\w_-]+)?'
    MSG_RE = r'(?P<msg>.*)'

    DELIM_RE = r'\s+'
    START_RE = r'^'
    END_RE = r'$'


    REGEX = START_RE + DATE_RE + DELIM_RE + \
            TIME_RE + DELIM_RE + \
            SOURCE_RE + DELIM_RE + \
            LEVEL_RE + DELIM_RE + \
            TIMESTAMP_RE + DELIM_RE + \
            DEVICE_NAME_RE + DELIM_RE + \
            TYPE_RE + DELIM_RE + \
            MSG_RE  + END_RE



    parsed = re.match(REGEX, string)
    if parsed:
        return parsed.groupdict()
    else:
        raise ValueError('MERAKI PARSER FAILED TO PARSE LOGGING MESSAGE')


