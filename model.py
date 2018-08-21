# 교통사고 주/야, 요일 -> 예상 속도
# 6시 ~ 18시 : 주 / 1 ~ 5시, 19시 ~ 24시
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import csv, random

class Dataset:
    def __init__(self):
        self.week_names = ['월', '화', '수', '목', '금', '토', '일']
        self.day_fields = [f'{i:02}' + '시' for i in range(6, 19)]
        self.night_fields = []
        for i in range(1, 25):
            if i not in range(6, 19):
                self.night_fields.append(f'{i:02}' + '시')
        self.data_days = []

    def get_dataset(self, year, month): # 서울시 차량 통행 속도 데이터 
        # ['일자', '요일', '도로명', '링크아이디', '시점명', '종점명', '거리', '방향', '01시', '02시', '03시', '04시','05시', '06시', '07시', '08시', '09시', '10시', '11시', '12시', '13시', '14시', '15시', '16시', '17시', '18시', '19시', '20시', '21시', '22시', '23시', '24시']
        filepath = f'dataset_kor/보조데이터/01.서울시 차량 통행 속도/{str(year)}년 {str(month)}월 통행속도.csv'
        with open(filepath, 'r', encoding='cp949') as f:
            reader = csv.DictReader(f)
            for line in reader:
                record = dict(line)
                weekday = self.week_names.index(record['요일'])
                try:
                    day_speed = [float(record[day]) for day in self.day_fields]
                    day_average = sum(day_speed)/len(day_speed)
                    night_speed = [float(record[night]) for night in self.night_fields]
                    night_average = sum(night_speed)/len(night_speed)
                    self.data_days.append({
                        'weekday' : weekday, # 요일
                        'day' : day_average, # 속도(주)
                        'night' : night_average # 속도(야)
                    })
                except ValueError:
                    continue
        print(f'[+] Loaded csv of {str(year)}.{str(month)}')

    def get_all(self):
        for year in range(2014, 2018):
            for month in range(1, 13):
                self.get_dataset(year, month)

    def generate_dataset(self):
        self.data = []
        for data in self.data_days:
            self.data.append((
                np.array([data['weekday'], 0]), # property
                data['day'] # label
            ))
            self.data.append((
                np.array([data['weekday'], 1]), # property
                data['night'] # label
            ))
        print('[*] Dataset size : ' + str(len(self.data)))
        # random.shuffle(self.data)
        del(self.data_days)

    def load_data(self):
        test_size = int((len(self.data)/100)*20)
        test = self.data[:test_size]
        print('├── Test data size : ' + str(test_size))
        train = self.data[test_size:]
        print('└── Train data size : ' + str(len(train)))
        test = (np.array([data[0] for data in test]), np.array([data[1] for data in test]))
        train = (np.array([data[0] for data in train]), np.array([data[1] for data in train]))
        return train, test

if __name__ == '__main__':
    dataset = Dataset()
    dataset.get_dataset(2014, 1)
    dataset.generate_dataset()

    (train_data, train_labels), (test_data, test_labels) = dataset.load_data()
    order = np.argsort(np.random.random(train_labels.shape))
    train_data = train_data[order]
    train_labels = train_labels[order]
    print("Training set: {}".format(train_data.shape))
    print("Testing set:  {}".format(test_data.shape))

    
    