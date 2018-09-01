# 사상자수, 도로형태, 당사자1/2종 -> 사고유형
import csv
from pprint import pprint

class Dataset:
    def __init__(self):
        filepath = f'../dataset_kor/교통사망사고정보/Kor_Train_교통사망사고정보(12.1~17.6).csv'
        self.data_days = []
        with open(filepath, 'r', encoding='cp949') as f:
            reader = csv.DictReader(f)
            for line in reader:
                record = dict(line)
                # print(record)
                # exit()
                self.data_days.append({
                    'casualties' : record['사상자수'],
                    'road_type' : record['도로형태'],
                    'party1' : record['당사자종별_1당'],
                    'party2' : record['당사자종별_2당'],
                    'accident_type' : record['사고유형']
                })
        # pprint(self.data_days[:10])
        # self.road_type_names = self.field_kinds('road_type')
        self.road_type_names = [
            '기타단일로', '교차로부근', '교량위', '교차로내', '고가도로위', 
            '교차로횡단보도내', '기타', '지하차도(도로)내', '주차장', '터널안', 
            '불명', '횡단보도상', '횡단보도부근', '기타/불명', '지하도로내', 
            '건널목'
        ]
        # self.accident_type_names = self.field_kinds('accident_type')
        self.accident_type_names = [
            '횡단중', '추돌', '차도통행중', '측면충돌', '기타', 
            '전도', '도로이탈 기타', '길가장자리구역통행중','공작물충돌', '정면충돌', 
            '도로이탈 추락', '전도전복', '전복', '보도통행중', '후진중충돌', 
            '주/정차차량 충돌', '진행중 추돌', '측면직각충돌', '주정차중 추돌', '차단기돌파', 
            '직전진행', '경보기 무시'
        ]
        # self.parties_names = self.parties_field_kinds()
        self.parties_names = [
            '승용차', '이륜차', '화물차', '자전거', '특수차', 
            '승합차', '원동기장치자전거', '사륜오토바이(ATV)','건설기계', '농기계', 
            '개인형이동수단(PM)', '중형', '대형', '소형', '경형', 
            '사발이', '불명', '보행자', '없음', '열차'
        ]

    def field_kinds(self, field, log=True):
        kind = []
        for data in self.data_days:
            if data[field] not in kind:
                kind.append(data[field])
        if log: print('[*] ' + field + ' : ' + str(kind))
        return kind

    def parties_field_kinds(self):
        kind = self.field_kinds('party1', log=False)
        for data in self.field_kinds('party2', log=False):
            if data not in kind:
                kind.append(data)
        print('[*] parties kinds : ' + str(kind))
        return kind
    
if __name__ == '__main__':
    dataset = Dataset()
