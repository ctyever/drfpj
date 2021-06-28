from django.db import models
import pandas as pd
import numpy as np
from algo.common.models import FileDTO
from algo.common.models import Reader, Printer

'''
<인구 소멸 지역의 정의>
65세 이상 노인 인구와 20~39세 여성 인구를 비교해서 젊은 여성 인구가 노인 인구의 절반에 미달할 경우, 인구 소멸 위험 지역으로 분류한다
위 방법에 따라 분류를 하려면 먼저 각 지역별 20~30대 여성 인구수를 파악하고, 65세 이상 노인 인구수를 파악해야 한다
그리고 해당 지역이 인구 소멸 위기 지역인지 파악해야 한다
https://gist.github.com/HyeongWookKim/9ae79f06de0c2e8dd4f66d58db3f8087
'''


class Service(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()

    def organize_population_data(self):
        f = self.f
        r = self.r
        p = self.p
        f.context = './data/'
        f.fname = '05_population_raw_data'
        population = r.xls(f, 1, None)
        # p.dframe(population)
        population.fillna(method='pad', inplace=True)
        population.rename(columns={'행정구역(동읍면)별(1)': '광역시도',
                                   '행정구역(동읍면)별(2)': '시도',
                                   '계': '인구수'}, inplace=True)
        population = population[(population['시도'] != '소계')]
        p.dframe(population)

        population.is_copy = False

        population.rename(columns={'항목': '구분'}, inplace=True)

        population.loc[population['구분'] == '총인구수 (명)', '구분'] = '합계'
        population.loc[population['구분'] == '남자인구수 (명)', '구분'] = '남자'
        population.loc[population['구분'] == '여자인구수 (명)', '구분'] = '여자'

        population.to_csv('./saved_data/population.csv')

    def calculate_areas_risk_organize_data(self):

        f = self.f
        r = self.r
        p = self.p
        f.context = './saved_data/'
        f.fname = 'population'
        population = r.csv(f)


        population['20-39세'] = population['20 - 24세'] + population['25 - 29세'] + \
                               population['30 - 34세'] + population['35 - 39세']

        population['65세이상'] = population['65 - 69세'] + population['70 - 74세'] + \
                              population['75 - 79세'] + population['80 - 84세'] + \
                              population['85 - 89세'] + population['90 - 94세'] + \
                              population['95 - 99세'] + population['100+']

        pop = pd.pivot(population,
                             index=['광역시도', '시도'],
                             columns=['구분'],
                             values=['20-39세', '65세이상', '인구수'])

        pop['소멸비율'] = pop['20-39세', '여자'] / (pop['65세이상', '합계'] / 2)
        pop['소멸위기지역'] = pop['소멸비율'] < 1.0
        # p.dframe(pop)
        pop[pop['소멸위기지역'] == True].index.get_level_values(1)
        pop.reset_index(inplace=True)
        p.dframe(pop)

        tmp_columns = [pop.columns.get_level_values(0)[n] + \
                        pop.columns.get_level_values(1)[n]
                       for n in range(0, len(pop.columns.get_level_values(0)))]

        pop.columns = tmp_columns
        # pop.to_csv('./saved_data/pop.csv')

        #print(pop.head())
        #print(pop.info())

    def create_regional_unique_IDs_for_map_visualization(self):

        f = self.f
        r = self.r
        p = self.p
        f.context = './saved_data/'
        f.fname = 'pop'
        pop = r.csv(f)

        pop['시도'].unique()

        si_name = [None] * len(pop)

        tmp_gu_dict = {'수원': ['장안구', '권선구', '팔달구', '영통구'],
                       '성남': ['수정구', '중원구', '분당구'],
                       '안양': ['만안구', '동안구'],
                       '안산': ['상록구', '단원구'],
                       '고양': ['덕양구', '일산동구', '일산서구'],
                       '용인': ['처인구', '기흥구', '수지구'],
                       '청주': ['상당구', '서원구', '흥덕구', '청원구'],
                       '천안': ['동남구', '서북구'],
                       '전주': ['완산구', '덕진구'],
                       '포항': ['남구', '북구'],
                       '창원': ['의창구', '성산구', '진해구', '마산합포구', '마산회원구'],
                       '부천': ['오정구', '원미구', '소사구']}

        for n in pop.index:
            # '광역시도'에 있는 이름의 끝 세 글자가 '광역시', '특별시', '자치시'로 끝나지 않으면
            # ==> 일반 시 혹은 군으로 처리
            if pop['광역시도'][n][-3:] not in ['광역시', '특별시', '자치시']:

                # '강원도 고성군'과 '경상남도 고성군'을 구분 후, 처리해주는 작업
                if pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '강원도':
                    si_name[n] = '고성(강원)'

                elif pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '경상남도':
                    si_name[n] = '고성(경남)'

                else:
                    si_name[n] = pop['시도'][n][:-1]

                for keys, values in tmp_gu_dict.items():
                    if pop['시도'][n] in values:

                        if len(pop['시도'][n]) == 2:
                            si_name[n] = keys + ' ' + pop['시도'][n]

                        elif pop['시도'][n] in ['마산합포구', '마산회원구']:
                            si_name[n] = keys + ' ' + pop['시도'][n][2:-1]

                        else:
                            si_name[n] = keys + ' ' + pop['시도'][n][:-1]

            elif pop['광역시도'][n] == '세종특별자치시':
                si_name[n] = '세종'

            else:
                if len(pop['시도'][n]) == 2:
                    si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n]

                else:
                    si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n][:-1]







# Service().organize_population_data()
Service().calculate_areas_risk_organize_data()
