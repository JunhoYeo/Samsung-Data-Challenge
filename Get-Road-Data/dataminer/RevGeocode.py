from shapely.geometry import Polygon
import csv, json, requests
import pkg_resources as pkg_r

class csv_parser:
    
    def __init__(self):
        self.coordinates = []
        
    # def parse(self, idx):
    #     filepath = pkg_r.resource_filename(__name__, 'dataset/' + str(idx) + '.csv')
    #     with open(filepath, 'r', encoding='cp949') as dataset:
    #         reader = csv.reader(dataset)
    #         size = sum(1 for line in open(filepath, encoding='cp949'))
    #         first = True
    #         for line in reader:
    #             if first is True: first = False; continue
    #             if '서울' not in line[4]: continue
    #             corrected = line[14].replace('}}', '}').replace('][', '],[').replace('"Polygon"coordinates', '"Polygon","coordinates"')
    #             try:
    #                 data = json.loads(corrected, encoding='cp949')
    #             except json.decoder.JSONDecodeError:
    #                 continue
    #             self.coordinates.append(data['coordinates'][0])

    def parse(self, idx):
        filepath = pkg_r.resource_filename(__name__, 'dataset/' + str(idx) + '.csv')
        with open(filepath, 'r', encoding='cp949') as dataset:
            reader = csv.reader(dataset)
            size = sum(1 for line in open(filepath, encoding='cp949'))
            first = True
            for line in reader:
                if first is True: first = False; continue
                if '서울' not in line[4]: continue
                self.coordinates.append(f'{line[13]}, {line[12]}')

    def result(self):
        return self.coordinates

class parser:
    
    def __init__(self, YOUR_API_KEY):
        self.API_KEY = YOUR_API_KEY
    
    def check_key(self):
        print('[*] API_KEY : ' + self.API_KEY)
    
    # def find_center(self, border_coord):
    #     poly = Polygon([[point[1], point[0]] for point in border_coord])
    #     return f'{poly.centroid.x}, {poly.centroid.y}'
    
    # def load_result(self, centroid):
    #     print('[*] CENTROID : ' + centroid)
    #     URL = 'https://maps.googleapis.com/maps/api/geocode/json'
    #     params = {
    #         'latlng' : centroid,
    #         'language' : 'ko',
    #         'key' : self.API_KEY
    #     }
    #     return requests.get(URL, params=params).json()

    def result(self, coord):
        URL = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'latlng' : coord,
            'language' : 'ko',
            'key' : self.API_KEY
        }
        r = requests.get(URL, params=params)
        # print(r.url)
        return r.json()

class roadname:

    def __init__(self):
        self.json_data = {}
        self.load()
    
    def load(self):
        filepath = pkg_r.resource_filename(__name__, 'SeoulRoadNameInfo.json')
        with open(filepath, encoding='utf-8') as f:
            data = f.read()
        self.json_data = json.loads(data)['DATA']

    def search(self, query):
        for data in self.json_data:
            # print(query)
            # print(data['road_nm'])
            if query == data['road_nm']:
                print(data)
                
            
# if __name__ == '__main__':
#     roadname = roadname()
#     roadname.load()
#     roadname.search('삼양로')
