from __future__ import unicode_literals

import avro.schema
import csv
import os
import json
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

##Defining DJDNA Snapshots Schema May 22,2018
djdna_avro_schema = {
"type":"record",
"name":"Delivery",
"namespace":"com.dowjones.dna.avro",
"doc":"Avro schema for extraction content used by Dow Jones' SyndicationHub",
"fields":[
    {"name":"an","type":["string","null"]},
    {"name":"modification_datetime","type":["long","null"]},
    {"name":"ingestion_datetime","type":["long","null"]},
    {"name":"publication_date","type":["long","null"]},
    {"name":"publication_datetime","type":["long","null"]},
    {"name":"snippet","type":["string","null"]},
    {"name":"body","type":["string","null"]},
    {"name":"art","type":["string","null"]},
    {"name":"action","type":["string","null"]},
    {"name":"credit","type":["string","null"]},
    {"name":"byline","type":["string","null"]},
    {"name":"document_type","type":["string","null"]},
    {"name":"language_code","type":["string","null"]},
    {"name":"title","type":["string","null"]},
    {"name":"copyright","type":["string","null"]},
    {"name":"dateline","type":["string","null"]},
    {"name":"source_code","type":["string","null"]},
    {"name":"modification_date","type":["long","null"]},
    {"name":"section","type":["string","null"]},
    {"name":"company_codes","type":["string","null"]},
    {"name":"publisher_name","type":["string","null"]},
    {"name":"region_of_origin","type":["string","null"]},
    {"name":"word_count","type":["int","null"]},
    {"name":"subject_codes","type":["string","null"]},
    {"name":"region_codes","type":["string","null"]},
    {"name":"industry_codes","type":["string","null"]},
    {"name":"person_codes","type":["string","null"]},
    {"name":"currency_codes","type":["string","null"]},
    {"name":"market_index_codes","type":["string","null"]},
    {"name":"company_codes_about","type":["string","null"]},
    {"name":"company_codes_association","type":["string","null"]},
    {"name":"company_codes_lineage","type":["string","null"]},
    {"name":"company_codes_occur","type":["string","null"]},
    {"name":"company_codes_relevance","type":["string","null"]},
    {"name":"source_name","type":["string","null"]}
]
}

read_schema = avro.schema.parse(json.dumps(djdna_avro_schema))


from argparse import ArgumentParser

arguments = ArgumentParser()
arguments.add_argument('--j', type=int, default=0)
args = arguments.parse_args()
j=args.j

import sys
reload(sys)
sys.setdefaultencoding('utf8')

## define function to write dictionary into file
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))    
    return   

dir_name = '/scratch/ab7325/Factiva/o6umiw3a11/o6umiw3a11'
i_s = str(j).zfill(12)
reader = DataFileReader(open("{1}-{0}.avro".format(i_s, dir_name), "rb"), DatumReader(read_schema))
new_schema = reader.get_meta("avro.schema")
users = []
for user in reader:
    users.append(user)
reader.close()
##extracting columns for header
if users:
    csv_columns = [str(i) for i in users[0].keys()]

    ##defining csv full path and filename
    csv_file = "{1}-{0}.csv".format(i_s, dir_name)

    ##writting filw
    WriteDictToCSV(csv_file,csv_columns,users)

## Returning to default
reload(sys)
sys.setdefaultencoding('ascii')
