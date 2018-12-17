#!/usr/bin/env python3

import os
from flowlogs_reader import FlowRecord, FlowLogsReader
import json
from itertools import islice
import jsonpickle
import datetime


log_file = '/Users/me/vpc-flow-log.log'

def file():


        body = open(log_file, 'r').read()
        lines = body.splitlines()

        log_data(lines)

        doc = {
            '_op_type': 'index',
            '_type': 'lamb_type',
        }
        data = json.load(log_data(lines))
        am = data.update(doc)

        print(am)



def log_data(lines):
    for line in islice(lines, 1, None):
        rec = FlowRecord.from_message(line)
        
        json_rec = jsonpickle.encode(rec, unpicklable=False)

        
        print(json_rec)        
        


file()
