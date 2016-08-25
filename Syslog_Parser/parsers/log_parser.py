from .vendors import *
from .meraki import *


class log_parser():


    def __init__(self, string, vendor):
        parsers = {
            VENDOR_MERAKI: meraki_parser
        }

        self.parsed = {}
        if vendor in parsers:
            self.parsed = parsers[vendor](string)
        else:
            raise ValueError("UNKOWN VENDOR: " + str(vendor))

    def get_parsed(self):
        return self.parsed
