import dataminer.RevGeocode as geoparser
from progress.bar import Bar
import json, time

# API_KEY = open('./API.key').read().strip('\n')

# csv_parser = geoparser.csv_parser()
# csv_data = []
# for idx in range(1, 6):
#     csv_parser.parse(idx)
#     csv_data += csv_parser.result()

# parser = geoparser.parser(API_KEY)
# parser.check_key()

# road_name = []
# print('\n[*] Reverse-geocoding coordinate data...')
# bar = Bar('Processing', max=len(csv_data), suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')
# for coord in csv_data:
#     result_json = parser.result(coord)
#     roadname = result_json['results'][1]['address_components'][0]['long_name']
#     if '로' not in roadname: continue
#     # print('[x] ' + roadname)
#     bar.next()
#     road_name.append(roadname)
# bar.finish()

# with open('roadnames.txt', 'w') as f:
#     for roadname in road_name:
#         f.write(roadname + '\n')

# $ python3 app.py
# [*] API_KEY : AIzaSyAlSSUu9PMXmVMVORq3ikCIp0PhWakEAPY

# [*] Reverse-geocoding coordinate data...
# Processing |#########################       | 4590/5862 - 78.3% - 829s

road_name = [line.strip('\n') for line in open('roadnames.txt').readlines()]
print('[*] Searching road names...')
roadname = geoparser.roadname()
roadname.load()
for road in road_name:
    roadname.search(road)
