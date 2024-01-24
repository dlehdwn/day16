import random
from datetime import *
import pandas as pd
from faker import Faker
fake = Faker('ko_KR')

movieList = ['웡카','시민덕희','도그맨','너의 이름은','라라랜드','상견니','외게인']
snackList = ['일반','카라멜','치즈','오징어','핫도그','나초','프레즐']
drinkList = ['콜라','사이다','스프라이트','환타']

cgvData = {
    'customers':[fake.name() for i in range(500)],
    'movie':[random.choice(movieList) for i in range(500)],
    'snack':[random.choice(snackList) for i in range(500)],
    'drink':[random.choice(drinkList) for i in range(500)]
}

cgv_df = pd.DataFrame(cgvData)
now = datetime.now()
cgv_df.to_csv(f'0124 cgv.csv',index=False)
