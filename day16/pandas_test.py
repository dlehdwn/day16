#pandas
#엑셀을 데이터화
#판다스 데이터 타입 : series, dataframe
#series : 엑셀에서 하나의 열
#dataframe : 엑셀 그 자체

import pandas as pd
from faker import Faker

nlist = [5,12,24,13,17]
series = pd.Series(nlist)
print(series.mean())


# coffeeList = ['아아','라떼','카푸치노']
# series = pd.Series(coffeeList)
# print(series)
#
# coffeeData = {
#     "menu":['americano','latte','mocha'],
#     "price":[2000,2500,3000],
#     "caffein":[120,100,130]
# }
#
# df = pd.DataFrame(coffeeData)
# print(df)

fake = Faker()
print(fake.name()) # Joshua Love

carData = {
    'carname':['k5','k7','avante'],
    'owner':[fake.name() for i in range(3)]
}
df = pd.DataFrame(carData)
df.to_csv('car.csv',index=False)










