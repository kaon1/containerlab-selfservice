#!/usr/bin/python
"""
Kaon Thana 5-31-2023
"""
import re
import dateutil.parser as parser
from datetime import datetime, timezone


class FilterModule:

    @staticmethod
    def filters():
        return {
            'timestamp_differ': FilterModule.timestamp_differ,
        }
    @staticmethod
    def timestamp_differ(timestamp_map):

        return_topos_to_shutdown = set()
        current_datetime = datetime.now().astimezone()
        
        for id in timestamp_map:
            # print("Docker ID: ", id)
            # print("Raw Created Time: ", timestamp_map[id])
            created_datetime = parser.parse(timestamp_map[id])
            
            # print("Created Time Parsed: ", created_datetime)
            # print("Current Time: ", current_datetime)
            
            difference = current_datetime - created_datetime
            
            if int(difference.total_seconds()/3600) < 32 :
                return_topos_to_shutdown.add(id)
            
        
        return list(return_topos_to_shutdown)