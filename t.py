# import pandas as pd
# from sklearn.decomposition import PCA
# # from sklearn.discrimi""t_analysis import LinearDiscrimi""tAnalysis
# import matplotlib.pyplot as plt
#
#
# # lda = LinearDiscrimi""tAnalysis(n_components=15)


# d = pd.read_excel('C:/Users/luna/Desktop/test.xlsx')

# # print(d.head(3))

# d = d.drop(['身份证', 'good'], axis=1)
# d = d.dropna(axis=0, how='any')
# d = d.fillna(0)

# plt.figure()

# print(d.shape)
# pca = PCA(whiten=True)
# m = pca.fit(d)
# print(m)
# print(type(m))
# print(pca.explained_variance_)   # 代表降维后的各主成分的方差值，越大，说明越是重要的主成分
# print(len(pca.explained_variance_))
# print(pca.explained_variance_ratio_)   # 代表降维后的各主成分的方差值占总方差值的比例，这个比例越大，则越是重要的成分、
# print(len(pca.explained_variance_ratio_))
#
# plt.plot(range(50), pca.explained_variance_)
# plt.plot(range(50), pca.explained_variance_ratio_)
# plt.show()
# # print(d.head(3))
# # print(d.columns)
# # d.corr().to_csv('C:/Users/luna/Desktop/bsd/g_b_corr.csv', encoding='ANSI')


# import pymysql
# import pandas as pd
# cnn = pymysql.connect(host="139.196.115.129",
#                        user="root",
#                        password="root",
#                        database="fi""cing_yjk"
#                        )
# d = pd.read_sql_query('select * from app_version', cnn)
# print(d.head())


# from pymongo import MongoClient
# # client = MongoClient('139.196.35.101', 27017)
# client = MongoClient('mongodb://139.196.35.101:27017/')


import json
import pandas as pd
# import demjson


m = []
with open('C:\\Users\\luna\\desktop\\mxdata.json', encoding='utf8') as f:
    for line in f:
        # print(type(line))
        # print(line)
        d = json.loads(line)
        m.append(d)
        # print(type(d))
print(m)

n = pd.DataFrame()
for i,j in enumerate(m):
    n[i] = j.values()

print(n)






















# m = {
#     "mobile": "15757155137",
#     "code": 0,
#     "message": "正常",
#     "name": "胡汉三",
#     "idcard": "",
#     "carrier": "CHINA_MOBILE",
#     "province": "浙江",
#     "city": "杭州",
#     "level": "三星级",
#     "state": "开机",
#     "address": "浙江省杭州市余杭",
#     "imsi": "460077577222222",
#     "email": "",
#     "reliability": "1",
#     "packages": [
#         {
#             "items": [
#                 {
#                     "item": "VPMN个人产品763",
#                     "total": "16666666",
#                     "used": "0",
#                     "unit": "分"
#                 },
#                 {
#                     "item": "光棍节幸福1+1赠送流量",
#                     "total": "1048576",
#                     "used": "0",
#                     "unit": "KB"
#                 },
#                 {
#                     "item": "光棍节幸福1+1赠送流量",
#                     "total": "1048576",
#                     "used": "315",
#                     "unit": "KB"
#                 },
#                 {
#                     "item": "飞享套餐18元基本模组（含50分钟）",
#                     "total": "50",
#                     "used": "35",
#                     "unit": "分"
#                 },
#                 {
#                     "item": "光棍节幸福1+1赠送流量",
#                     "total": "1048576",
#                     "used": "1048576",
#                     "unit": "KB"
#                 },
#                 {
#                     "item": "光棍节幸福1+1赠送流量",
#                     "total": "1048576",
#                     "used": "0",
#                     "unit": "KB"
#                 },
#                 {
#                     "item": "光棍节幸福1+1赠送流量",
#                     "total": "1048576",
#                     "used": "1048576",
#                     "unit": "KB"
#                 },
#                 {
#                     "item": "手机上网自选100元包(3GB)",
#                     "total": "3145728",
#                     "used": "2658987",
#                     "unit": "KB"
#                 }
#             ],
#             "bill_start_date": "2017-11-01",
#             "bill_end_date": "2017-11-30"
#         },
#         {
#             "items": [
#                 {
#                     "item": "飞享套餐18元基本模组（含50分钟）#国内语音主叫时长",
#                     "total": "50",
#                     "used": "4",
#                     "unit": "分"
#                 },
#                 {
#                     "item": "手机上网自选100元包(3GB)#国内数据流量",
#                     "total": "3145728",
#                     "used": "0",
#                     "unit": "KB"
#                 },
#                 {
#                     "item": "手机上网自选100元包(3GB)#国内数据流量-结转",
#                     "total": "3087216",
#                     "used": "316604",
#                     "unit": "KB"
#                 },
#                 {
#                     "item": "随意玩5元流量包#夜间省内流量-结转",
#                     "total": "853960",
#                     "used": "5699",
#                     "unit": "KB"
#                 }
#             ],
#             "bill_start_date": "2018-01-01",
#             "bill_end_date": "2018-01-31"
#         }
#     ],
#     "families": [
#         {
#             "family_num": "",
#             "items": []
#         }
#     ],
#     "recharges": [
#         {
#             "amount": 5000,
#             "type": "神州行充值卡",
#             "details_id": "4bfc3d645963647ea8077d278a4ad9f30",
#             "recharge_time": "2018-03-06 16:20:09"
#         },
#         {
#             "amount": 4800,
#             "type": "现金",
#             "details_id": "f677c0bcf22c45d3c360ee0bcaa9ca480",
#             "recharge_time": "2018-02-21 03:29:14"
#         },
#         {
#             "amount": 3000,
#             "type": "现金",
#             "details_id": "e38ce1999a7b088272ca89dad33a3ff20",
#             "recharge_time": "2018-02-21 03:10:26"
#         },
#         {
#             "amount": 3000,
#             "type": "现金",
#             "details_id": "c7b41547bc61bf473cc3c677500acb7e0",
#             "recharge_time": "2018-01-21 03:52:28"
#         }
#     ],
#     "bills": [
#         {
#             "point": 566,
#             "bill_month": "2018-02",
#             "bill_start_date": "2018-02-01",
#             "bill_end_date": "2018-02-28",
#             "base_fee": 16300,
#             "extra_service_fee": 1100,
#             "voice_fee": 0,
#             "sms_fee": 70,
#             "web_fee": 0,
#             "extra_fee": 0,
#             "total_fee": 17470,
#             "discount": 6000,
#             "extra_discount": 0,
#             "actual_fee": 11470,
#             "paid_fee": 0,
#             "unpaid_fee": 0,
#             "last_point": 336,
#             "related_mobiles": "",
#             "notes": ""
#         },
#         {
#             "point": "",
#             "bill_month": "2018-03",
#             "bill_start_date": "2018-03-01",
#             "bill_end_date": "2018-03-22",
#             "base_fee": 11790,
#             "extra_service_fee": 962,
#             "voice_fee": 0,
#             "sms_fee": 90,
#             "web_fee": 0,
#             "extra_fee": 0,
#             "total_fee": 12842,
#             "discount": 4617,
#             "extra_discount": 0,
#             "actual_fee": 8225,
#             "paid_fee": 0,
#             "unpaid_fee": 0,
#             "last_point": "",
#             "related_mobiles": "",
#             "notes": ""
#         },
#         {
#             "point": "",
#             "bill_month": "2017-11",
#             "bill_start_date": "2017-11-01",
#             "bill_end_date": "2017-11-30",
#             "base_fee": 16300,
#             "extra_service_fee": 764,
#             "voice_fee": 0,
#             "sms_fee": 90,
#             "web_fee": 0,
#             "extra_fee": 0,
#             "total_fee": 22818,
#             "discount": 0,
#             "extra_discount": 0,
#             "actual_fee": 22818,
#             "paid_fee": 0,
#             "unpaid_fee": 0,
#             "last_point": "",
#             "related_mobiles": "",
#             "notes": ""
#         },
#         {
#             "point": 2605,
#             "bill_month": "2017-12",
#             "bill_start_date": "2017-12-01",
#             "bill_end_date": "2017-12-31",
#             "base_fee": 16900,
#             "extra_service_fee": 1100,
#             "voice_fee": 0,
#             "sms_fee": 100,
#             "web_fee": 0,
#             "extra_fee": 0,
#             "total_fee": 18100,
#             "discount": 6000,
#             "extra_discount": 0,
#             "actual_fee": 12100,
#             "paid_fee": 0,
#             "unpaid_fee": 0,
#             "last_point": 2363,
#             "related_mobiles": "",
#             "notes": ""
#         },
#         {
#             "point": "",
#             "bill_month": "2017-10",
#             "bill_start_date": "2017-10-01",
#             "bill_end_date": "2017-10-31",
#             "base_fee": 13700,
#             "extra_service_fee": 600,
#             "voice_fee": 0,
#             "sms_fee": 10,
#             "web_fee": 2000,
#             "extra_fee": 0,
#             "total_fee": 21810,
#             "discount": 0,
#             "extra_discount": 0,
#             "actual_fee": 21810,
#             "paid_fee": 0,
#             "unpaid_fee": 0,
#             "last_point": "",
#             "related_mobiles": "",
#             "notes": ""
#         },
#         {
#             "point": "",
#             "bill_month": "2017-09",
#             "bill_start_date": "2017-09-01",
#             "bill_end_date": "2017-09-30",
#             "base_fee": 14600,
#             "extra_service_fee": 600,
#             "voice_fee": 0,
#             "sms_fee": 20,
#             "web_fee": 1000,
#             "extra_fee": 0,
#             "total_fee": 16220,
#             "discount": 7500,
#             "extra_discount": 0,
#             "actual_fee": 8720,
#             "paid_fee": 0,
#             "unpaid_fee": 0,
#             "last_point": "",
#             "related_mobiles": "",
#             "notes": ""
#         },
#         {
#             "point": 336,
#             "bill_month": "2018-01",
#             "bill_start_date": "2018-01-01",
#             "bill_end_date": "2018-01-31",
#             "base_fee": 16300,
#             "extra_service_fee": 1100,
#             "voice_fee": 0,
#             "sms_fee": 110,
#             "web_fee": 0,
#             "extra_fee": 0,
#             "total_fee": 17510,
#             "discount": 6000,
#             "extra_discount": 0,
#             "actual_fee": 11510,
#             "paid_fee": 0,
#             "unpaid_fee": 0,
#             "last_point": 2605,
#             "related_mobiles": "",
#             "notes": ""
#         }
#     ],
#     "calls": [
#         {
#             "bill_month": "2018-03",
#             "total_size": 14,
#             "items": [
#                 {
#                     "time": "2018-03-09 11:38:29",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "60c1af378b0fc3772f1eaa94a843e44e0",
#                     "peer_number": "057195014911",
#                     "location_type": "国内被叫",
#                     "duration": 5,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-03-09 11:06:50",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "4caa9814d27e714be38c6a6316539dd30",
#                     "peer_number": "13221011135",
#                     "location_type": "国内被叫",
#                     "duration": 9,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-03-09 09:57:24",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "fb4d2d293b2f14269e533282a358f2100",
#                     "peer_number": "15114099710",
#                     "location_type": "国内被叫",
#                     "duration": 2000,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-03-09 08:08:44",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "8a5606c1365823675c094fa99c0ebb510",
#                     "peer_number": "18661166142",
#                     "location_type": "国内被叫",
#                     "duration": 20,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-03-07 12:26:35",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "64c9791859f910b6ec655b65b31e60230",
#                     "peer_number": "18011713984",
#                     "location_type": "国内被叫",
#                     "duration": 6,
#                     "dial_type": "DIALED"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2018-02",
#             "total_size": 29,
#             "items": [
#                 {
#                     "time": "2018-02-28 22:06:30",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "0d49b2d6bd859fd56261a5ae84b02d4f0",
#                     "peer_number": "18661191241",
#                     "location_type": "国内被叫",
#                     "duration": 6,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-02-28 10:43:02",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "ca686379ebf8db6c98a48283f8e6d5d50",
#                     "peer_number": "18511961950",
#                     "location_type": "国内被叫",
#                     "duration": 1078,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-02-27 18:49:59",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "ded6b0fe66f958416127663da71fabe90",
#                     "peer_number": "125911818001",
#                     "location_type": "国内被叫",
#                     "duration": 10,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-02-26 15:15:44",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "29b0e8eb02121a27de2b02b8fa2bf3c10",
#                     "peer_number": "13675813262",
#                     "location_type": "本地主叫本地",
#                     "duration": 64,
#                     "dial_type": "DIAL"
#                 },
#                 {
#                     "time": "2018-02-24 11:36:53",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "56d258c340897c290e480d47411ce1350",
#                     "peer_number": "057125295655",
#                     "location_type": "国内被叫",
#                     "duration": 227,
#                     "dial_type": "DIALED"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2018-01",
#             "total_size": 60,
#             "items": [
#                 {
#                     "time": "2018-01-31 22:28:09",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "33ffca899d909954b84bcd16ca09dc970",
#                     "peer_number": "18329216227",
#                     "location_type": "本地主叫本地",
#                     "duration": 98,
#                     "dial_type": "DIAL"
#                 },
#                 {
#                     "time": "2018-01-30 22:08:56",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "0a3090add4aa1f30e8aea91201f630f40",
#                     "peer_number": "18668116636",
#                     "location_type": "本地主叫本地",
#                     "duration": 8,
#                     "dial_type": "DIAL"
#                 },
#                 {
#                     "time": "2018-01-30 22:08:31",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "b077d8100506aa6d1716ff315838b2680",
#                     "peer_number": "18662116346",
#                     "location_type": "国内被叫",
#                     "duration": 1,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-01-30 17:18:34",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "584095f5d010ee6598374c3abac2467d0",
#                     "peer_number": "18515626552",
#                     "location_type": "国内被叫",
#                     "duration": 485,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2018-01-30 16:30:09",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "ac6c4b2aa5278e19b2f6c850114291c30",
#                     "peer_number": "18515542552",
#                     "location_type": "国内被叫",
#                     "duration": 165,
#                     "dial_type": "DIALED"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-12",
#             "total_size": 45,
#             "items": [
#                 {
#                     "time": "2017-12-30 11:41:49",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "892c2fadbbf29d8df26b4fa3e6e516030",
#                     "peer_number": "15967162152",
#                     "location_type": "国内被叫",
#                     "duration": 150,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-12-29 21:21:04",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "d2e8fc9dae578c8d229fd52ce7bac01d0",
#                     "peer_number": "18668087941",
#                     "location_type": "国内被叫",
#                     "duration": 8,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-12-29 19:37:13",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "235cdeff59be635f62c490affb3c2c1b0",
#                     "peer_number": "18957646673",
#                     "location_type": "小区优惠",
#                     "duration": 47,
#                     "dial_type": "DIAL"
#                 },
#                 {
#                     "time": "2017-12-29 19:00:18",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "1cfdf4d2302ded1e86a288382c472bf90",
#                     "peer_number": "18657283746",
#                     "location_type": "小区优惠",
#                     "duration": 28,
#                     "dial_type": "DIAL"
#                 },
#                 {
#                     "time": "2017-12-29 18:42:23",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "761fbf302984399a6aa8a99a34169c660",
#                     "peer_number": "18692851248",
#                     "location_type": "国内被叫",
#                     "duration": 34,
#                     "dial_type": "DIALED"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-11",
#             "total_size": 117,
#             "items": [
#                 {
#                     "time": "2017-11-30 21:57:44",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "0de78a083a60ff8af4aa95f6b98a9ac10",
#                     "peer_number": "18659871843",
#                     "location_type": "国内被叫",
#                     "duration": 10,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-11-30 19:36:01",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "c5b462978aa7811efeb157c822feb5890",
#                     "peer_number": "057156229008",
#                     "location_type": "国内被叫",
#                     "duration": 25,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-11-29 22:16:33",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "6aa2f782c48c56bf2105a3c1bd3ac7ce0",
#                     "peer_number": "18698527307",
#                     "location_type": "国内被叫",
#                     "duration": 6,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-11-29 20:51:24",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "26b2332f80b0c520e59e1c6e282c105c0",
#                     "peer_number": "057110086",
#                     "location_type": "国内被叫",
#                     "duration": 10,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-11-29 12:31:18",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "b611193444f749a9087071da8087c2130",
#                     "peer_number": "13582983695",
#                     "location_type": "国内被叫",
#                     "duration": 8,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-11-28 22:13:06",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "d986bc9c643ffbb93302b2dff939b0d80",
#                     "peer_number": "18662373148",
#                     "location_type": "国内被叫",
#                     "duration": 16,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-11-28 10:22:05",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "e8106b30b57e63585211700b55d21fd80",
#                     "peer_number": "057128939871",
#                     "location_type": "国内被叫",
#                     "duration": 61,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-11-27 21:57:47",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "db8f999cd1710d47393d6c221c5874f70",
#                     "peer_number": "18626234943",
#                     "location_type": "国内被叫",
#                     "duration": 9,
#                     "dial_type": "DIALED"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-10",
#             "total_size": 44,
#             "items": [
#                 {
#                     "time": "2017-10-31 15:37:17",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "182cf2c641bd3643893962858bdd83f20",
#                     "peer_number": "057128167266",
#                     "location_type": "本地主叫本地",
#                     "duration": 19,
#                     "dial_type": "DIAL"
#                 },
#                 {
#                     "time": "2017-10-31 15:36:36",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "60459410923551a733c620d696f70a960",
#                     "peer_number": "057128167266",
#                     "location_type": "国内被叫",
#                     "duration": 23,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-10-28 14:22:47",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "0ce13b593e70094c3228a7e1150a0c8d0",
#                     "peer_number": "057186903377",
#                     "location_type": "国内被叫",
#                     "duration": 30,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-10-27 22:35:04",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "06ab706f1fac65260b791e9e13fedda90",
#                     "peer_number": "18767120297",
#                     "location_type": "国内被叫",
#                     "duration": 41,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-10-27 21:26:11",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "fa07c2aa1d8ff3c790bccd280114214b0",
#                     "peer_number": "18667027415",
#                     "location_type": "国内被叫",
#                     "duration": 41,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-10-27 21:03:04",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "0a4ae4684c445e8ffeaf353ba40edf9a0",
#                     "peer_number": "15967185152",
#                     "location_type": "国内被叫",
#                     "duration": 9,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-10-27 20:58:01",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "8545f7176714bd34cc57ceaa8b4e40c70",
#                     "peer_number": "15967185152",
#                     "location_type": "国内被叫",
#                     "duration": 29,
#                     "dial_type": "DIALED"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-09",
#             "total_size": 16,
#             "items": [
#                 {
#                     "time": "2017-09-30 12:51:16",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "2651ccc98ff67df1082018c564cb2d830",
#                     "peer_number": "18158442798",
#                     "location_type": "国内被叫",
#                     "duration": 14,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-09-24 13:53:22",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "8bac50c91b18d212362e8eeef0c3d4e50",
#                     "peer_number": "057110086",
#                     "location_type": "国内被叫",
#                     "duration": 7,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-09-19 10:48:48",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "fa157bf4b6d67a6c4c4bd50fed32b2e80",
#                     "peer_number": "057110086",
#                     "location_type": "国内被叫",
#                     "duration": 29,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-09-18 11:05:24",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "32c4b51eedcbcfcc38320ee74e9d18a50",
#                     "peer_number": "18601761407",
#                     "location_type": "国内被叫",
#                     "duration": 24,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-09-16 10:36:53",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "3e2a918432c75d9badb912db64cff4b50",
#                     "peer_number": "02138784988",
#                     "location_type": "本地主叫异地",
#                     "duration": 70,
#                     "dial_type": "DIAL"
#                 },
#                 {
#                     "time": "2017-09-15 17:01:23",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "0dc6465133bfb4592c547cd06265af2f0",
#                     "peer_number": "057126204277",
#                     "location_type": "国内被叫",
#                     "duration": 13,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-09-15 12:20:38",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "2718ab3ef0eac7a9cfdecb2f47cae0490",
#                     "peer_number": "13757788598",
#                     "location_type": "国内被叫",
#                     "duration": 58,
#                     "dial_type": "DIALED"
#                 },
#                 {
#                     "time": "2017-09-14 11:46:12",
#                     "location": "杭州",
#                     "fee": 0,
#                     "details_id": "049f35f44a63a720240b6de2c9f6a1700",
#                     "peer_number": "4000895558",
#                     "location_type": "国内被叫",
#                     "duration": 87,
#                     "dial_type": "DIALED"
#                 }
#             ]
#         }
#     ],
#     "smses": [
#         {
#             "bill_month": "2018-03",
#             "total_size": 142,
#             "items": [
#                 {
#                     "time": "2018-03-09 16:51:33",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "366cf6f6c3440e5fe19aa32ef569ed4d0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-03-09 16:51:32",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "2f10b7de0fecf6f4faaa2d1328ec5db60",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-03-09 16:51:31",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "bb56e217482514e0e9f65f81005699aa0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-03-09 16:51:30",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "75afc69c676d0b77961fee6cef9f48230",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-03-09 16:51:29",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "daeb36c449bfc7460e916c22eb4d13cb0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-03-09 16:51:28",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "ad4534ea2c9f72561a2f8779b44f70820",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-03-09 16:51:27",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "eb31ea17f5e01849f15d81f64d70967c0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2018-02",
#             "total_size": 152,
#             "items": [
#                 {
#                     "time": "2018-02-28 22:24:02",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "833540f15b8faafd3054b66cd221865f0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-02-28 22:24:01",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "cdf73343d2fbae77a338e6614f1a4f410",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-02-28 22:24:00",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "1217746031500a5bbd26cf330a84ce710",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-02-28 22:23:50",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "115caedbee56691233cea20620dd48410",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-02-28 22:23:49",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "b9a2e166a56e484f0962c3b8f9d17bb80",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-02-28 22:23:48",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "5c1fa1c1f4e69655c59f5ff29f35a2210",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2018-01",
#             "total_size": 277,
#             "items": [
#                 {
#                     "time": "2018-01-31 18:57:46",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "1692a66b7ccfa4251808aa7456b6cc510",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-01-31 18:57:45",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "0a90f6e680191978184e3866534dbdc30",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-01-31 15:40:45",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "fefc1812d9b6e58733f5120bd0e6e59a0",
#                     "peer_number": "1069103833669370503",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-01-31 13:10:15",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "79063e75c290b441b18fcf9790f1aca10",
#                     "peer_number": "10690529043768",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-01-29 17:00:25",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "e7437fa010d1c629075cea6ea655debc0",
#                     "peer_number": "10086703",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-01-29 17:00:24",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "5f7231ad5f0a16cd8e9ba4a2ea1febfe0",
#                     "peer_number": "10086703",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2018-01-29 17:00:23",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "d8a44a26b1731c78b25badea02b2a8580",
#                     "peer_number": "10086703",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-12",
#             "total_size": 221,
#             "items": [
#                 {
#                     "time": "2017-12-31 08:48:43",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "d08f5b5f7ad14c072af1fb9548de49110",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-12-31 08:48:42",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "52ffc25ba243bff625556ec502d1126c0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-12-31 08:48:41",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "a1f5c3615ebceee6d54447b2c15ff5af0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-12-30 08:58:41",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "d0278c039055d45fdc08af025a80dee50",
#                     "peer_number": "1065712079481016",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-12-29 15:10:45",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "44b42237417149c1474fd1e5a8435d8f0",
#                     "peer_number": "106575262195566",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-12-29 15:10:19",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "37a5975836fe6ce8ab736e63dc6b24b70",
#                     "peer_number": "10690092200320031",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-12-29 15:10:03",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "c548c51c0963d528a71171fc8161c0b20",
#                     "peer_number": "106907985944",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-12-29 15:09:52",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "ed1aa9f6a7f87a02b6ac751bf01f84fe0",
#                     "peer_number": "106916312121",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-11",
#             "total_size": 416,
#             "items": [
#                 {
#                     "time": "2017-11-30 15:31:21",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "a76f64645a1265044735a8af38b520b90",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-30 15:31:20",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "5b99dae0986ebc7cdce625ce794fa3bb0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-30 15:31:19",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "ad00311d2f5b0e7aa9f8dfb03dd48ec80",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-30 15:31:14",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "0bcd1748065ceddbcb34d75e538283a0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-30 15:31:13",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "94b1b3381e25e9fb4afb22ccfef50df50",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-30 15:30:30",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "6051cb66c05f9edf1c7b4a8a0decd8f30",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-30 15:30:29",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "bd26223e70f4b3fc0cd321dbb05d97df0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-29 14:35:37",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "4879b019f660d629e0258a7677dd131f0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-29 14:35:35",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "e2e860b86ed632af6069a2a7c562d0de0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 },
#                 {
#                     "time": "2017-11-29 14:34:03",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "3bcb9de104259384ddf3f641fb73cf0c0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "梦网业务"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-10",
#             "total_size": 76,
#             "items": [
#                 {
#                     "time": "2017-10-31 08:11:52",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "3e45d0161b44f023bad3b31f58fff5a70",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-29 16:50:39",
#                     "location": "国内（不含港澳台）",
#                     "fee": 10,
#                     "details_id": "4d03878ebadf23de80415c6b216e53280",
#                     "peer_number": "17757191261",
#                     "send_type": "SEND",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-28 14:49:21",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "c5abe4e8d0c623438ea1f57c9c94f1000",
#                     "peer_number": "17757191261",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-28 14:49:20",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "ee432d60fca73194cb05e1c3ec5d368d0",
#                     "peer_number": "17757191261",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-28 11:51:12",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "77e55c10dd03d083afe8a49c4e38c5dd0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-28 11:51:11",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "c98e3c927b7548ce222887cba8204ca70",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-28 11:51:10",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "e2727fdddb9c4c4758a01d5181ffd6a50",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-27 15:18:02",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "998e17985e01d1eaf3fa844e1057aa940",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-10-27 14:43:59",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "82ff800fe66e804d564784012fe4622e0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-09",
#             "total_size": 89,
#             "items": [
#                 {
#                     "time": "2017-09-29 19:20:55",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "6bdc467ca2b9f40c8e6f1921e37e664f0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-29 19:20:53",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "a5e16d1108a034a5d5c07eea67260c180",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-29 19:20:52",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "d2111eb7e81fb57806a88de72dcfb3c90",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-29 18:10:31",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "4a727762c30a58557c1a843342fe01600",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-29 18:10:30",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "fb61a47eaffceb3bce68ac5a8b07cc5e0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-29 18:10:29",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "64be2b560ceacfa51a6679a096a5377e0",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-29 14:11:26",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "66d124e80764a7557b5ab36a9f6055d20",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-29 14:11:25",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "0e0030294e1d3619190fd70d49c3f9a80",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 },
#                 {
#                     "time": "2017-09-28 17:57:44",
#                     "location": "国内（不含港澳台）",
#                     "fee": 0,
#                     "details_id": "19eda1410523b3fb0d7e1ad79b6fc3b60",
#                     "peer_number": "10086",
#                     "send_type": "RECEIVE",
#                     "msg_type": "SMS",
#                     "service_name": "短信"
#                 }
#             ]
#         }
#     ],
#     "nets": [
#         {
#             "bill_month": "2018-03",
#             "total_size": 60,
#             "items": [
#                 {
#                     "time": "2018-03-02 12:26:57",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "0f784ee97bfa222fb51d7c3b904bab3d0",
#                     "duration": "",
#                     "subflow": "36535.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2018-03-01 00:04:24",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "c2a616d7cc36780f0e542ca0e239eda00",
#                     "duration": "",
#                     "subflow": "56578.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2018-03-02 00:48:10",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "58f032c962ba1cf36b2109b444e919ff0",
#                     "duration": "",
#                     "subflow": "13603.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-哔哩哔哩 "
#                 },
#                 {
#                     "time": "2018-03-04 19:27:55",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "6cab464c50d260a15981d4ccbe7d13140",
#                     "duration": "",
#                     "subflow": "7.00",
#                     "net_type": "4g ",
#                     "service_name": "流量核减-volte ut接口 "
#                 },
#                 {
#                     "time": "2018-03-04 19:27:51",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "9e3b59afeed9a60c3fbb33d82f624f920",
#                     "duration": "",
#                     "subflow": "1.00",
#                     "net_type": "4g ",
#                     "service_name": "流量核减-volte ut接口 "
#                 },
#                 {
#                     "time": "2018-03-02 12:48:05",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "b331f8c3840b0b8bc43a05c97224e41f0",
#                     "duration": "",
#                     "subflow": "7.00",
#                     "net_type": "4g ",
#                     "service_name": "流量核减-volte ut接口 "
#                 },
#                 {
#                     "time": "2018-03-04 00:30:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "37c443b2feff30c2e96eb29f6d003deb0",
#                     "duration": "",
#                     "subflow": "5.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 }
#             ]
#         },
#         {
#             "bill_month": "2018-02",
#             "total_size": 139,
#             "items": [
#                 {
#                     "time": "2018-02-17 08:51:19",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "d4245cb3328c6890db7872ae4ee0308f0",
#                     "duration": "",
#                     "subflow": "3929.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2018-02-22 10:28:20",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "86880f9901bc56b8e45be34243317c9d0",
#                     "duration": "",
#                     "subflow": "106.00",
#                     "net_type": "4g ",
#                     "service_name": "cmwap缺省流量，不包含所有业务的信令流量 "
#                 },
#                 {
#                     "time": "2018-02-06 00:59:14",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "4ddb3d2e728275273fbfddba90ce20a60",
#                     "duration": "",
#                     "subflow": "56270.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2018-02-01 21:38:54",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "d18724b6f95f872dae09e1b324565a8f0",
#                     "duration": "",
#                     "subflow": "4.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2018-02-22 09:44:02",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "8126339392e355e69cc894f7ceb510520",
#                     "duration": "",
#                     "subflow": "4799.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-爱奇艺 "
#                 },
#                 {
#                     "time": "2018-02-13 09:30:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "9ea7e864369dd140cf7abffc992b50780",
#                     "duration": "",
#                     "subflow": "686.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2018-02-07 18:36:23",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "c2e9e4c5747317f7c0ac1ded6bd280510",
#                     "duration": "",
#                     "subflow": "192.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 }
#             ]
#         },
#         {
#             "bill_month": "2018-01",
#             "total_size": 129,
#             "items": [
#                 {
#                     "time": "2018-01-03 18:13:41",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "b8931741899bc4782853159f2b3c5fff0",
#                     "duration": "",
#                     "subflow": "693.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2018-01-04 09:28:28",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "46414bb45eb96396ecb583b402000a640",
#                     "duration": "",
#                     "subflow": "7.00",
#                     "net_type": "4g ",
#                     "service_name": "流量核减-volte ut接口 "
#                 },
#                 {
#                     "time": "2018-01-05 00:00:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "d13c490e7ac7532a36b5bdc199edddda0",
#                     "duration": "",
#                     "subflow": "6244.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2018-01-25 18:46:02",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "0310895d6ea1bc6571a019cedb719eb00",
#                     "duration": "",
#                     "subflow": "139.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2018-01-26 14:33:55",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "f82fc66407e3f2264ed332216305c38f0",
#                     "duration": "",
#                     "subflow": "7.00",
#                     "net_type": "4g ",
#                     "service_name": "流量核减-volte ut接口 "
#                 },
#                 {
#                     "time": "2018-01-23 15:41:59",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "b658f1f93ce426a45b920b8626b9d1f70",
#                     "duration": "",
#                     "subflow": "14.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2018-01-22 22:08:31",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "9ddb793880e35081cd8ff65a63ac98d30",
#                     "duration": "",
#                     "subflow": "14.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-12",
#             "total_size": 128,
#             "items": [
#                 {
#                     "time": "2017-12-14 12:28:09",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "aef0c9654e2d8836cc197ca899f3bc930",
#                     "duration": "",
#                     "subflow": "694.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2017-12-05 00:00:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "c592e195b6283e3ef24837da231baa0d0",
#                     "duration": "",
#                     "subflow": "10134.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-12-09 05:13:31",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "9de8d70c799f6615f100b7f2ceaaa0230",
#                     "duration": "",
#                     "subflow": "7076.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2017-12-09 07:20:12",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "9474d4c52710b31ae9e9d284112e1c090",
#                     "duration": "",
#                     "subflow": "6769.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-12-09 19:42:42",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "81d9b621c486dcd7efad34553fd46e7e0",
#                     "duration": "",
#                     "subflow": "90.00",
#                     "net_type": "2g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-12-08 10:08:50",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "894e261bdf1db736a70e3c5bbd18f8470",
#                     "duration": "",
#                     "subflow": "94775.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-12-28 00:00:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "83b35370d5a03596897f929280f8c6c10",
#                     "duration": "",
#                     "subflow": "50111.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-12-06 17:38:41",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "2634137f7da52fd6989cd2130051fa550",
#                     "duration": "",
#                     "subflow": "7.00",
#                     "net_type": "4g ",
#                     "service_name": "流量核减-volte ut接口 "
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-11",
#             "total_size": 129,
#             "items": [
#                 {
#                     "time": "2017-11-22 08:13:48",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "443ea08fb22a395c928dbeba319344f20",
#                     "duration": "",
#                     "subflow": "5152.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-11-23 00:04:02",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "474bc2a694d28568df49bdfe36296de10",
#                     "duration": "",
#                     "subflow": "85987.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-11-03 11:17:31",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "d023559c9217d4407aa5d202acc68ff50",
#                     "duration": "",
#                     "subflow": "518.00",
#                     "net_type": "4g ",
#                     "service_name": "前向定向-腾讯视频 "
#                 },
#                 {
#                     "time": "2017-11-19 08:30:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "49c92a04f19f3c09b4b5748f5af134d30",
#                     "duration": "",
#                     "subflow": "712262.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-11-03 20:47:12",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "29f7b4d65ed58a02fc21489a3356e8d90",
#                     "duration": "",
#                     "subflow": "13.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-11-02 00:00:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "1875ed73530dbbb2a9f60c00eb76add20",
#                     "duration": "",
#                     "subflow": "36.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-11-18 00:12:01",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "89ec748791845519dca6ccab3f176f530",
#                     "duration": "",
#                     "subflow": "5013.00",
#                     "net_type": "4g ",
#                     "service_name": "cmnet流量 "
#                 },
#                 {
#                     "time": "2017-11-01 12:00:00",
#                     "location": "浙江省",
#                     "fee": 0,
#                     "details_id": "69b2a9844ad3d145322fb4e76fa2ea2d0",
#                     "duration": "",
#                     "subflow": "1756.00",
#                     "net_type": "4g ",
#                     "service_name": "掌上营业厅 "
#                 }
#             ]
#         },
#         {
#             "bill_month": "2017-10",
#             "total_size": 0,
#             "items": []
#         },
#         {
#             "bill_month": "2017-09",
#             "total_size": 0,
#             "items": []
#         }
#     ],
#     "open_time": "2012-09-03",
#     "package_name": "4G飞享套餐",
#     "available_balance": 14087,
#     "real_balance": "",
#     "last_modify_time": "2018-03-22 09:56:55",
#     "month_info": {
#         "month_list": {
#             "201709": 16,
#             "201710": 44,
#             "201711": 117,
#             "201712": 45,
#             "201801": 60,
#             "201802": 29,
#             "201803": 14
#         },
#         "phone_no": "15757666637",
#         "month_count": 7,
#         "miss_month_count": 0,
#         "no_call_month": 0,
#         "user_id": "青云上仙"
#     }
# }

# m = json.dumps(m)
# print(type(m))
# print(m)
#
# print(m.keys())
# print(len(m.keys()))
# print(m.values())
# print(len(m.values()))

# d = {
#     "report": [
#         {
#             "key": "data_type",
#             "value": "运营商"
#         },
#         {
#             "key": "source_name",
#             "value": "chinamobilezj"
#         },
#         {
#             "key": "source_name_zh",
#             "value": "浙江移动"
#         },
#         {
#             "key": "data_gain_time",
#             "value": "2017-10-13"
#         },
#         {
#             "key": "task_id",
#             "value": "78c15210-afbb-11e7-8963-00163e0e0050"
#         },
#         {
#             "key": "update_time",
#             "value": "2017-10-13 10:08:57"
#         },
#         {
#             "key": "version",
#             "value": "1.0"
#         }
#     ],
#     "user_basic": [
#         {
#             "key": "name",
#             "value": "张三"
#         },
#         {
#             "key": "id_card",
#             "value": "371521199305281420"
#         },
#         {
#             "key": "gender",
#             "value": "男"
#         },
#         {
#             "key": "age",
#             "value": "24"
#         },
#         {
#             "key": "constellation",
#             "value": "双子座"
#         },
#         {
#             "key": "province",
#             "value": "山东省"
#         },
#         {
#             "key": "city",
#             "value": "聊城市"
#         },
#         {
#             "key": "region",
#             "value": "阳谷县"
#         },
#         {
#             "key": "native_place",
#             "value": "山东省聊城市阳谷县"
#         }
#     ],
#     "cell_phone": [
#         {
#             "key": "mobile",
#             "value": "13100000000"
#         },
#         {
#             "key": "carrier_name",
#             "value": "李四"
#         },
#         {
#             "key": "carrier_idcard",
#             "value": "运营商未提供身份证"
#         },
#         {
#             "key": "reg_time",
#             "value": "2013-09-21 00:00:00"
#         },
#         {
#             "key": "in_time",
#             "value": "50"
#         },
#         {
#             "key": "email",
#             "value": "运营商未提供邮箱"
#         },
#         {
#             "key": "address",
#             "value": "运营商未提供通讯地址"
#         },
#         {
#             "key": "reliability",
#             "value": "实名认证"
#         },
#         {
#             "key": "phone_attribution",
#             "value": "浙江绍兴"
#         },
#         {
#             "key": "live_address",
#             "value": "杭州"
#         },
#         {
#             "key": "available_balance",
#             "value": "4286"
#         },
#         {
#             "key": "package_name",
#             "value": "4G飞享套餐"
#         },
#         {
#             "key": "bill_certification_day",
#             "value": "2017-10-13"
#         }
#     ],
#     "basic_check_items": [
#         {
#             "result": "无数据",
#             "comment": "",
#             "check_item": "idcard_check"
#         },
#         {
#             "result": "未提供邮箱",
#             "comment": "",
#             "check_item": "email_check"
#         },
#         {
#             "result": "未提供通讯地址",
#             "comment": "",
#             "check_item": "address_check"
#         },
#         {
#             "result": "通话记录正常",
#             "comment": "",
#             "check_item": "call_data_check"
#         },
#         {
#             "result": "运营商未提供身份证",
#             "comment": "",
#             "check_item": "idcard_match"
#         },
#         {
#             "result": "匹配失败",
#             "comment": "",
#             "check_item": "name_match"
#         },
#         {
#             "result": "否",
#             "comment": "",
#             "check_item": "is_name_and_idcard_in_court_black"
#         },
#         {
#             "result": "否",
#             "comment": "",
#             "check_item": "is_name_and_idcard_in_finance_black"
#         },
#         {
#             "result": "否",
#             "comment": "",
#             "check_item": "is_name_and_mobile_in_finance_black"
#         },
#         {
#             "result": "3",
#             "comment": "",
#             "check_item": "mobile_silence_3m"
#         },
#         {
#             "result": "3",
#             "comment": "",
#             "check_item": "mobile_silence_6m"
#         },
#         {
#             "result": "0",
#             "comment": "",
#             "check_item": "arrearage_risk_3m"
#         },
#         {
#             "result": "0",
#             "comment": "",
#             "check_item": "arrearage_risk_6m"
#         },
#         {
#             "result": "0",
#             "comment": "",
#             "check_item": "binding_risk"
#         }
#     ],
#     "application_check": [
#         {
#             "app_point": "contact",
#             "check_points": {
#                 "relationship": "",
#                 "key_value": "13777777777",
#                 "contact_name": "111",
#                 "check_mobile": "无该联系人电话的通话记录",
#                 "check_xiaohao": "该联系人号码非临时小号"
#             }
#         },
#         {
#             "app_point": "contact",
#             "check_points": {
#                 "relationship": "",
#                 "key_value": "138888888",
#                 "contact_name": "111",
#                 "check_mobile": "无该联系人电话的通话记录",
#                 "check_xiaohao": "该联系人号码非临时小号"
#             }
#         }
#     ],
#     "behavior_check": [
#         {
#             "result": "朋友圈主要活跃在杭州地区(居住地)",
#             "evidence": "杭州地区通话时间占比为21%",
#             "score": 2,
#             "check_point": "regular_circle",
#             "check_point_cn": "朋友圈在哪里"
#         },
#         {
#             "result": "长期使用（24个月以上，包含24）",
#             "evidence": "根据号码[15715848975]运营商提供的认证时间,推算该号码使用50个月",
#             "score": 1,
#             "check_point": "phone_used_time",
#             "check_point_cn": "号码使用时间"
#         },
#         {
#             "result": "180天内有6天无通话记录",
#             "evidence": "根据运营商通话详单数据，连续三天以上无通话记录0次",
#             "score": 2,
#             "check_point": "phone_silent",
#             "check_point_cn": "手机静默情况"
#         },
#         {
#             "result": "关机共6天",
#             "evidence": "根据运营商详单数据，180天内关机6天，连续三天以上关机0次",
#             "score": 2,
#             "check_point": "phone_power_off",
#             "check_point_cn": "关机情况"
#         },
#         {
#             "result": "数量正常（10 - 100）",
#             "evidence": "互通过电话的号码有49个，比例为13%，其中未被标记号码49个，被标记号码0个",
#             "score": 1,
#             "check_point": "contact_each_other",
#             "check_point_cn": "互通过电话的号码数量"
#         },
#         {
#             "result": "无通话记录",
#             "evidence": "未发现与澳门地区电话通话记录",
#             "score": 1,
#             "check_point": "contact_macao",
#             "check_point_cn": "与澳门地区电话通话情况"
#         },
#         {
#             "result": "无通话记录",
#             "evidence": "未发现与110电话通话记录",
#             "score": 1,
#             "check_point": "contact_110",
#             "check_point_cn": "与110电话通话情况"
#         },
#         {
#             "result": "无通话记录",
#             "evidence": "未发现与120电话通话记录",
#             "score": 1,
#             "check_point": "contact_120",
#             "check_point_cn": "与120电话通话情况"
#         },
#         {
#             "result": "无通话记录",
#             "evidence": "未发现与律师电话通话记录",
#             "score": 1,
#             "check_point": "contact_lawyer",
#             "check_point_cn": "与律师电话通话情况"
#         },
#         {
#             "result": "无通话记录",
#             "evidence": "未发现与法院电话通话记录",
#             "score": 1,
#             "check_point": "contact_court",
#             "check_point_cn": "与法院电话通话情况"
#         },
#         {
#             "result": "无该类号码记录",
#             "evidence": "[总计]主叫0次共0分钟；被叫0次共0分钟；号码数0个",
#             "score": 1,
#             "check_point": "contact_loan",
#             "check_point_cn": "与贷款类号码联系情况"
#         },
#         {
#             "result": "无该类号码记录",
#             "evidence": "[总计]主叫0次共0分钟；被叫0次共0分钟；号码数0个",
#             "score": 1,
#             "check_point": "contact_bank",
#             "check_point_cn": "与银行类号码联系情况"
#         },
#         {
#             "result": "无该类号码记录",
#             "evidence": "[总计]主叫0次共0分钟；被叫0次共0分钟；号码数0个",
#             "score": 1,
#             "check_point": "contact_credit_card",
#             "check_point_cn": "与信用卡类号码联系情况"
#         },
#         {
#             "result": "无该类号码记录",
#             "evidence": "[总计]主叫0次共0分钟；被叫0次共0分钟；号码数0个",
#             "score": 1,
#             "check_point": "contact_collection",
#             "check_point_cn": "与催收类号码联系情况"
#         },
#         {
#             "result": "很少夜间活动（低于20%)",
#             "evidence": "晚间活跃频率占全天的0.1%",
#             "score": 1,
#             "check_point": "contact_night",
#             "check_point_cn": "夜间活动情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "dwell_used_time",
#             "check_point_cn": "居住地本地（省份）地址在电商中使用时长"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "ebusiness_info",
#             "check_point_cn": "总体电商使用情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "person_ebusiness_info",
#             "check_point_cn": "申请人本人电商使用情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "virtual_buying",
#             "check_point_cn": "虚拟商品购买情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "lottery_buying",
#             "check_point_cn": "彩票购买情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "person_addr_changed",
#             "check_point_cn": "申请人本人地址变化情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供学信网数据",
#             "score": 0,
#             "check_point": "school_status",
#             "check_point_cn": "申请人的学籍状态是否为在校学生"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供学历数据",
#             "score": 0,
#             "check_point": "education_info",
#             "check_point_cn": "申请人的学历情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "work_addr_info",
#             "check_point_cn": "申请人本人最近使用工作地址情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "live_addr_info",
#             "check_point_cn": "申请人本人最近使用居住地址情况"
#         },
#         {
#             "result": "无数据",
#             "evidence": "未提供电商数据",
#             "score": 0,
#             "check_point": "school_addr_info",
#             "check_point_cn": "申请人本人最近使用学校地址情况"
#         },
#         {
#             "result": "数量众多（100以上，不含100）",
#             "evidence": "[总计]号码数384个；主叫228次共434分钟；被叫431次共490分钟，联系列表：[中介]号码数1个；主叫0次共0分钟；被叫1次共0分钟，[快递公司]号码数10个；主叫2次共0分钟；被叫9次共2分钟，[通信服务机构]号码数5个；主叫20次共32分钟；被叫11次共8分钟",
#             "score": 1,
#             "check_point": "phone_call",
#             "check_point_cn": "号码通话情况"
#         }
#     ],
#     "friend_circle": {
#         "summary": [
#             {
#                 "key": "friend_num_3m",
#                 "value": "183"
#             },
#             {
#                 "key": "good_friend_num_3m",
#                 "value": "2"
#             },
#             {
#                 "key": "friend_city_center_3m",
#                 "value": "杭州"
#             },
#             {
#                 "key": "is_city_match_friend_city_center_3m",
#                 "value": "否"
#             },
#             {
#                 "key": "inter_peer_num_3m",
#                 "value": "22"
#             },
#             {
#                 "key": "friend_num_6m",
#                 "value": "384"
#             },
#             {
#                 "key": "good_friend_num_6m",
#                 "value": "4"
#             },
#             {
#                 "key": "friend_city_center_6m",
#                 "value": "杭州"
#             },
#             {
#                 "key": "is_city_match_friend_city_center_6m",
#                 "value": "否"
#             },
#             {
#                 "key": "inter_peer_num_6m",
#                 "value": "49"
#             }
#         ],
#         "peer_num_top_list": [
#             {
#                 "key": "peer_num_top3_3m",
#                 "top_item": [
#                     {
#                         "peer_number": "13101111111",
#                         "peer_num_loc": "贵阳",
#                         "group_name": "未知",
#                         "company_name": "未知",
#                         "call_cnt": 35,
#                         "call_time": 5582,
#                         "dial_cnt": 12,
#                         "dialed_cnt": 23,
#                         "dial_time": 1755,
#                         "dialed_time": 3827
#                     },
#                     {
#                         "peer_number": "13102222222",
#                         "peer_num_loc": "温州",
#                         "group_name": "未知",
#                         "company_name": "未知",
#                         "call_cnt": 20,
#                         "call_time": 2252,
#                         "dial_cnt": 19,
#                         "dialed_cnt": 1,
#                         "dial_time": 2210,
#                         "dialed_time": 42
#                     },
#                     {
#                         "peer_number": "13103333333",
#                         "peer_num_loc": "宁波",
#                         "group_name": "未知",
#                         "company_name": "未知",
#                         "call_cnt": 10,
#                         "call_time": 522,
#                         "dial_cnt": 5,
#                         "dialed_cnt": 5,
#                         "dial_time": 251,
#                         "dialed_time": 271
#                     }
#                 ]
#             },
#             {
#                 "key": "peer_num_top3_6m",
#                 "top_item": [
#                     {
#                         "peer_number": "13101111111",
#                         "peer_num_loc": "温州",
#                         "group_name": "未知",
#                         "company_name": "未知",
#                         "call_cnt": 41,
#                         "call_time": 3808,
#                         "dial_cnt": 26,
#                         "dialed_cnt": 15,
#                         "dial_time": 2862,
#                         "dialed_time": 946
#                     },
#                     {
#                         "peer_number": "13102222222",
#                         "peer_num_loc": "贵阳",
#                         "group_name": "未知",
#                         "company_name": "未知",
#                         "call_cnt": 37,
#                         "call_time": 6094,
#                         "dial_cnt": 13,
#                         "dialed_cnt": 24,
#                         "dial_time": 2186,
#                         "dialed_time": 3908
#                     },
#                     {
#                         "peer_number": "057110086",
#                         "peer_num_loc": "杭州",
#                         "group_name": "通信服务机构",
#                         "company_name": "中国移动客服热线",
#                         "call_cnt": 12,
#                         "call_time": 1320,
#                         "dial_cnt": 12,
#                         "dialed_cnt": 0,
#                         "dial_time": 1320,
#                         "dialed_time": 0
#                     }
#                 ]
#             }
#         ],
#         "location_top_list": [
#             {
#                 "key": "location_top3_3m",
#                 "top_item": [
#                     {
#                         "location": "杭州",
#                         "peer_number_cnt": 124,
#                         "call_cnt": 173,
#                         "call_time": 5373,
#                         "dial_cnt": 56,
#                         "dialed_cnt": 117,
#                         "dial_time": 2880,
#                         "dialed_time": 2493
#                     },
#                     {
#                         "location": "贵阳",
#                         "peer_number_cnt": 1,
#                         "call_cnt": 35,
#                         "call_time": 5582,
#                         "dial_cnt": 12,
#                         "dialed_cnt": 23,
#                         "dial_time": 1755,
#                         "dialed_time": 3827
#                     },
#                     {
#                         "location": "温州",
#                         "peer_number_cnt": 9,
#                         "call_cnt": 35,
#                         "call_time": 3178,
#                         "dial_cnt": 29,
#                         "dialed_cnt": 6,
#                         "dial_time": 2971,
#                         "dialed_time": 207
#                     }
#                 ]
#             },
#             {
#                 "key": "location_top3_6m",
#                 "top_item": [
#                     {
#                         "location": "杭州",
#                         "peer_number_cnt": 235,
#                         "call_cnt": 326,
#                         "call_time": 11847,
#                         "dial_cnt": 98,
#                         "dialed_cnt": 228,
#                         "dial_time": 5544,
#                         "dialed_time": 6303
#                     },
#                     {
#                         "location": "绍兴",
#                         "peer_number_cnt": 57,
#                         "call_cnt": 87,
#                         "call_time": 2505,
#                         "dial_cnt": 20,
#                         "dialed_cnt": 67,
#                         "dial_time": 653,
#                         "dialed_time": 1852
#                     },
#                     {
#                         "location": "温州",
#                         "peer_number_cnt": 13,
#                         "call_cnt": 64,
#                         "call_time": 7531,
#                         "dial_cnt": 40,
#                         "dialed_cnt": 24,
#                         "dial_time": 6264,
#                         "dialed_time": 1267
#                     }
#                 ]
#             }
#         ]
#     },
#     "cell_behavior": [
#         {
#             "behavior": [
#                 {
#                     "sms_cnt": 70,
#                     "cell_phone_num": "13100000000",
#                     "net_flow": 0,
#                     "total_amount": 3899,
#                     "cell_mth": "2017-10",
#                     "cell_loc": "浙江绍兴",
#                     "cell_operator_zh": "浙江移动",
#                     "cell_operator": "chinamobilezj",
#                     "call_cnt": 40,
#                     "call_time": 1336,
#                     "dial_cnt": 18,
#                     "dial_time": 673,
#                     "dialed_cnt": 22,
#                     "dialed_time": 663,
#                     "rechange_cnt": 1,
#                     "rechange_amount": 5000
#                 },
#                 {
#                     "sms_cnt": 176,
#                     "cell_phone_num": "13100000000",
#                     "net_flow": 0,
#                     "total_amount": 10776,
#                     "cell_mth": "2017-09",
#                     "cell_loc": "浙江绍兴",
#                     "cell_operator_zh": "浙江移动",
#                     "cell_operator": "chinamobilezj",
#                     "call_cnt": 107,
#                     "call_time": 12909,
#                     "dial_cnt": 40,
#                     "dial_time": 5462,
#                     "dialed_cnt": 67,
#                     "dialed_time": 7447,
#                     "rechange_cnt": 4,
#                     "rechange_amount": 12000
#                 },
#                 {
#                     "sms_cnt": 285,
#                     "cell_phone_num": "13100000000",
#                     "net_flow": 0,
#                     "total_amount": 8751,
#                     "cell_mth": "2017-08",
#                     "cell_loc": "浙江绍兴",
#                     "cell_operator_zh": "浙江移动",
#                     "cell_operator": "chinamobilezj",
#                     "call_cnt": 81,
#                     "call_time": 10353,
#                     "dial_cnt": 41,
#                     "dial_time": 5654,
#                     "dialed_cnt": 40,
#                     "dialed_time": 4699,
#                     "rechange_cnt": 2,
#                     "rechange_amount": 2000
#                 },
#                 {
#                     "sms_cnt": 115,
#                     "cell_phone_num": "13100000000",
#                     "net_flow": 0,
#                     "total_amount": 11414,
#                     "cell_mth": "2017-07",
#                     "cell_loc": "浙江绍兴",
#                     "cell_operator_zh": "浙江移动",
#                     "cell_operator": "chinamobilezj",
#                     "call_cnt": 164,
#                     "call_time": 14319,
#                     "dial_cnt": 60,
#                     "dial_time": 7036,
#                     "dialed_cnt": 104,
#                     "dialed_time": 7283,
#                     "rechange_cnt": 4,
#                     "rechange_amount": 20000
#                 },
#                 {
#                     "sms_cnt": 116,
#                     "cell_phone_num": "13100000000",
#                     "net_flow": 0,
#                     "total_amount": 7860,
#                     "cell_mth": "2017-06",
#                     "cell_loc": "浙江绍兴",
#                     "cell_operator_zh": "浙江移动",
#                     "cell_operator": "chinamobilezj",
#                     "call_cnt": 115,
#                     "call_time": 9998,
#                     "dial_cnt": 35,
#                     "dial_time": 5761,
#                     "dialed_cnt": 80,
#                     "dialed_time": 4237,
#                     "rechange_cnt": 2,
#                     "rechange_amount": 6000
#                 },
#                 {
#                     "sms_cnt": 56,
#                     "cell_phone_num": "13100000000",
#                     "net_flow": 0,
#                     "total_amount": 8800,
#                     "cell_mth": "2017-05",
#                     "cell_loc": "浙江绍兴",
#                     "cell_operator_zh": "浙江移动",
#                     "cell_operator": "chinamobilezj",
#                     "call_cnt": 108,
#                     "call_time": 5252,
#                     "dial_cnt": 28,
#                     "dial_time": 1254,
#                     "dialed_cnt": 80,
#                     "dialed_time": 3998,
#                     "rechange_cnt": 2,
#                     "rechange_amount": 10000
#                 }
#             ],
#             "phone_num": "13100000000"
#         }
#     ],
#     "call_contact_detail": [
#         {
#             "city": "温州",
#             "p_relation": "",
#             "peer_num": "13101111111",
#             "group_name": "未知",
#             "company_name": "未知",
#             "call_cnt_1w": 1,
#             "call_cnt_1m": 3,
#             "call_cnt_3m": 20,
#             "call_cnt_6m": 41,
#             "call_time_3m": 2252,
#             "call_time_6m": 3808,
#             "dial_cnt_3m": 19,
#             "dial_cnt_6m": 26,
#             "dial_time_3m": 2210,
#             "dial_time_6m": 2862,
#             "dialed_cnt_3m": 1,
#             "dialed_cnt_6m": 15,
#             "dialed_time_3m": 42,
#             "dialed_time_6m": 946,
#             "call_cnt_morning_3m": 3,
#             "call_cnt_morning_6m": 7,
#             "call_cnt_noon_3m": 1,
#             "call_cnt_noon_6m": 1,
#             "call_cnt_afternoon_3m": 4,
#             "call_cnt_afternoon_6m": 9,
#             "call_cnt_evening_3m": 12,
#             "call_cnt_evening_6m": 24,
#             "call_cnt_night_3m": 0,
#             "call_cnt_night_6m": 0,
#             "call_cnt_weekday_3m": 11,
#             "call_cnt_weekday_6m": 21,
#             "call_cnt_weekend_3m": 6,
#             "call_cnt_weekend_6m": 13,
#             "call_cnt_holiday_3m": 3,
#             "call_cnt_holiday_6m": 7,
#             "call_if_whole_day_3m": "fls",
#             "call_if_whole_day_6m": "fls",
#             "trans_start": "2017-04-18 19:29:38",
#             "trans_end": "2017-10-07 07:48:15",
#             "max_call_time_6m": 298,
#             "min_call_time_6m": 7,
#             "avg_call_time_6m": 92
#         },
#         {
#             "city": "北京",
#             "p_relation": "",
#             "peer_num": "13102222222",
#             "group_name": "未知",
#             "company_name": "未知",
#             "call_cnt_1w": 0,
#             "call_cnt_1m": 0,
#             "call_cnt_3m": 35,
#             "call_cnt_6m": 37,
#             "call_time_3m": 5582,
#             "call_time_6m": 6094,
#             "dial_cnt_3m": 12,
#             "dial_cnt_6m": 13,
#             "dial_time_3m": 1755,
#             "dial_time_6m": 2186,
#             "dialed_cnt_3m": 23,
#             "dialed_cnt_6m": 24,
#             "dialed_time_3m": 3827,
#             "dialed_time_6m": 3908,
#             "call_cnt_morning_3m": 6,
#             "call_cnt_morning_6m": 6,
#             "call_cnt_noon_3m": 3,
#             "call_cnt_noon_6m": 3,
#             "call_cnt_afternoon_3m": 2,
#             "call_cnt_afternoon_6m": 2,
#             "call_cnt_evening_3m": 22,
#             "call_cnt_evening_6m": 23,
#             "call_cnt_night_3m": 2,
#             "call_cnt_night_6m": 3,
#             "call_cnt_weekday_3m": 27,
#             "call_cnt_weekday_6m": 28,
#             "call_cnt_weekend_3m": 8,
#             "call_cnt_weekend_6m": 9,
#             "call_cnt_holiday_3m": 0,
#             "call_cnt_holiday_6m": 0,
#             "call_if_whole_day_3m": "fls",
#             "call_if_whole_day_6m": "fls",
#             "trans_start": "2017-07-14 23:58:20",
#             "trans_end": "2017-08-23 23:12:15",
#             "max_call_time_6m": 894,
#             "min_call_time_6m": 30,
#             "avg_call_time_6m": 164
#         },
#         {
#             "city": "杭州",
#             "p_relation": "",
#             "peer_num": "057110086",
#             "group_name": "通信服务机构",
#             "company_name": "中国移动客服热线",
#             "call_cnt_1w": 0,
#             "call_cnt_1m": 2,
#             "call_cnt_3m": 7,
#             "call_cnt_6m": 12,
#             "call_time_3m": 736,
#             "call_time_6m": 1320,
#             "dial_cnt_3m": 7,
#             "dial_cnt_6m": 12,
#             "dial_time_3m": 736,
#             "dial_time_6m": 1320,
#             "dialed_cnt_3m": 0,
#             "dialed_cnt_6m": 0,
#             "dialed_time_3m": 0,
#             "dialed_time_6m": 0,
#             "call_cnt_morning_3m": 2,
#             "call_cnt_morning_6m": 5,
#             "call_cnt_noon_3m": 2,
#             "call_cnt_noon_6m": 2,
#             "call_cnt_afternoon_3m": 1,
#             "call_cnt_afternoon_6m": 2,
#             "call_cnt_evening_3m": 2,
#             "call_cnt_evening_6m": 3,
#             "call_cnt_night_3m": 0,
#             "call_cnt_night_6m": 0,
#             "call_cnt_weekday_3m": 6,
#             "call_cnt_weekday_6m": 7,
#             "call_cnt_weekend_3m": 1,
#             "call_cnt_weekend_6m": 5,
#             "call_cnt_holiday_3m": 0,
#             "call_cnt_holiday_6m": 0,
#             "call_if_whole_day_3m": "fls",
#             "call_if_whole_day_6m": "fls",
#             "trans_start": "2017-06-10 07:58:44",
#             "trans_end": "2017-09-25 09:50:34",
#             "max_call_time_6m": 351,
#             "min_call_time_6m": 1,
#             "avg_call_time_6m": 110
#         }
#     ],
#     "sms_contact_detail": [
#         {
#             "peer_num": "10086",
#             "sms_cnt_1w": 63,
#             "sms_cnt_1m": 160,
#             "sms_cnt_3m": 566,
#             "sms_cnt_6m": 780,
#             "send_cnt_3m": 8,
#             "send_cnt_6m": 14,
#             "receive_cnt_3m": 558,
#             "receive_cnt_6m": 766
#         },
#         {
#             "peer_num": "10086700",
#             "sms_cnt_1w": 0,
#             "sms_cnt_1m": 0,
#             "sms_cnt_3m": 10,
#             "sms_cnt_6m": 18,
#             "send_cnt_3m": 1,
#             "send_cnt_6m": 3,
#             "receive_cnt_3m": 9,
#             "receive_cnt_6m": 15
#         }
#     ],
#     "contact_region": [
#         {
#             "key": "contact_region_3m",
#             "desc": "联系人手机号码归属地 (近3月联系次数降序)",
#             "region_list": [
#                 {
#                     "region_loc": "杭州",
#                     "region_uniq_num_cnt": 124,
#                     "region_call_cnt": 173,
#                     "region_call_time": 5373,
#                     "region_dial_cnt": 56,
#                     "region_dial_time": 2880,
#                     "region_dialed_cnt": 117,
#                     "region_dialed_time": 2493,
#                     "region_avg_dial_time": 51,
#                     "region_avg_dialed_time": 21,
#                     "region_dial_cnt_pct": 0.32,
#                     "region_dial_time_pct": 0.54,
#                     "region_dialed_cnt_pct": 0.68,
#                     "region_dialed_time_pct": 0.46
#                 },
#                 {
#                     "region_loc": "贵阳",
#                     "region_uniq_num_cnt": 1,
#                     "region_call_cnt": 35,
#                     "region_call_time": 5582,
#                     "region_dial_cnt": 12,
#                     "region_dial_time": 1755,
#                     "region_dialed_cnt": 23,
#                     "region_dialed_time": 3827,
#                     "region_avg_dial_time": 146,
#                     "region_avg_dialed_time": 166,
#                     "region_dial_cnt_pct": 0.34,
#                     "region_dial_time_pct": 0.31,
#                     "region_dialed_cnt_pct": 0.66,
#                     "region_dialed_time_pct": 0.69
#                 },
#                 {
#                     "region_loc": "北海",
#                     "region_uniq_num_cnt": 1,
#                     "region_call_cnt": 1,
#                     "region_call_time": 4,
#                     "region_dial_cnt": 0,
#                     "region_dial_time": 0,
#                     "region_dialed_cnt": 1,
#                     "region_dialed_time": 4,
#                     "region_avg_dial_time": 0,
#                     "region_avg_dialed_time": 4,
#                     "region_dial_cnt_pct": 0,
#                     "region_dial_time_pct": 0,
#                     "region_dialed_cnt_pct": 1,
#                     "region_dialed_time_pct": 1
#                 }
#             ]
#         }
#     ],
#     "call_risk_analysis": [
#         {
#             "analysis_item": "110",
#             "analysis_desc": "110",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "120",
#             "analysis_desc": "120",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "loan",
#             "analysis_desc": "贷款",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "credit_card",
#             "analysis_desc": "信用卡",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "macao",
#             "analysis_desc": "澳门地区",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "collection",
#             "analysis_desc": "催收公司",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "lawyer",
#             "analysis_desc": "律师",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "agency",
#             "analysis_desc": "中介",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 1,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0.17,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 41,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 7,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 1,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0.17,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 41,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 7
#                 }
#             }
#         },
#         {
#             "analysis_item": "fraud",
#             "analysis_desc": "诈骗电话",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "nuisance",
#             "analysis_desc": "骚扰电话",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 2,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0.33,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 16,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 3,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 2,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0.33,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 16,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 3
#                 }
#             }
#         },
#         {
#             "analysis_item": "court",
#             "analysis_desc": "法院",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         }
#     ],
#     "main_service": [
#         {
#             "service_num": "057110086",
#             "group_name": "通信服务机构",
#             "company_name": "中国移动客服热线",
#             "total_service_cnt": 12,
#             "service_details": [
#                 {
#                     "interact_mth": "2017-09",
#                     "interact_cnt": 4,
#                     "interact_time": 159,
#                     "dial_cnt": 4,
#                     "dialed_cnt": 0,
#                     "dial_time": 159,
#                     "dialed_time": 0
#                 },
#                 {
#                     "interact_mth": "2017-08",
#                     "interact_cnt": 2,
#                     "interact_time": 226,
#                     "dial_cnt": 2,
#                     "dialed_cnt": 0,
#                     "dial_time": 226,
#                     "dialed_time": 0
#                 },
#                 {
#                     "interact_mth": "2017-07",
#                     "interact_cnt": 1,
#                     "interact_time": 351,
#                     "dial_cnt": 1,
#                     "dialed_cnt": 0,
#                     "dial_time": 351,
#                     "dialed_time": 0
#                 },
#                 {
#                     "interact_mth": "2017-06",
#                     "interact_cnt": 5,
#                     "interact_time": 584,
#                     "dial_cnt": 5,
#                     "dialed_cnt": 0,
#                     "dial_time": 584,
#                     "dialed_time": 0
#                 }
#             ]
#         },
#         {
#             "service_num": "10000",
#             "group_name": "通信服务机构",
#             "company_name": "中国电信综合服务",
#             "total_service_cnt": 6,
#             "service_details": [
#                 {
#                     "interact_mth": "2017-09",
#                     "interact_cnt": 4,
#                     "interact_time": 492,
#                     "dial_cnt": 4,
#                     "dialed_cnt": 0,
#                     "dial_time": 492,
#                     "dialed_time": 0
#                 },
#                 {
#                     "interact_mth": "2017-08",
#                     "interact_cnt": 2,
#                     "interact_time": 31,
#                     "dial_cnt": 2,
#                     "dialed_cnt": 0,
#                     "dial_time": 31,
#                     "dialed_time": 0
#                 }
#             ]
#         },
#         {
#             "service_num": "10010",
#             "group_name": "通信服务机构",
#             "company_name": "中国联通客服热线",
#             "total_service_cnt": 1,
#             "service_details": [
#                 {
#                     "interact_mth": "2017-09",
#                     "interact_cnt": 1,
#                     "interact_time": 6,
#                     "dial_cnt": 1,
#                     "dialed_cnt": 0,
#                     "dial_time": 6,
#                     "dialed_time": 0
#                 }
#             ]
#         },
#         {
#             "service_num": "057510086",
#             "group_name": "通信服务机构",
#             "company_name": "中国移动客服热线",
#             "total_service_cnt": 11,
#             "service_details": [
#                 {
#                     "interact_mth": "2017-10",
#                     "interact_cnt": 1,
#                     "interact_time": 12,
#                     "dial_cnt": 0,
#                     "dialed_cnt": 1,
#                     "dial_time": 0,
#                     "dialed_time": 12
#                 },
#                 {
#                     "interact_mth": "2017-09",
#                     "interact_cnt": 1,
#                     "interact_time": 11,
#                     "dial_cnt": 0,
#                     "dialed_cnt": 1,
#                     "dial_time": 0,
#                     "dialed_time": 11
#                 },
#                 {
#                     "interact_mth": "2017-08",
#                     "interact_cnt": 1,
#                     "interact_time": 90,
#                     "dial_cnt": 0,
#                     "dialed_cnt": 1,
#                     "dial_time": 0,
#                     "dialed_time": 90
#                 },
#                 {
#                     "interact_mth": "2017-07",
#                     "interact_cnt": 1,
#                     "interact_time": 7,
#                     "dial_cnt": 0,
#                     "dialed_cnt": 1,
#                     "dial_time": 0,
#                     "dialed_time": 7
#                 },
#                 {
#                     "interact_mth": "2017-06",
#                     "interact_cnt": 7,
#                     "interact_time": 511,
#                     "dial_cnt": 1,
#                     "dialed_cnt": 6,
#                     "dial_time": 105,
#                     "dialed_time": 406
#                 }
#             ]
#         }
#     ],
#     "call_service_analysis": [
#         {
#             "analysis_item": "bank",
#             "analysis_desc": "银行",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "railway_airway",
#             "analysis_desc": "航旅机构",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "special_service",
#             "analysis_desc": "特种服务",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "express",
#             "analysis_desc": "快递公司",
#             "analysis_point": {
#                 "call_cnt_1m": 1,
#                 "call_cnt_3m": 6,
#                 "call_cnt_6m": 11,
#                 "avg_call_cnt_3m": 2,
#                 "avg_call_cnt_6m": 1.83,
#                 "call_time_1m": 18,
#                 "call_time_3m": 102,
#                 "call_time_6m": 167,
#                 "avg_call_time_3m": 34,
#                 "avg_call_time_6m": 28,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 1,
#                     "call_dial_cnt_3m": 2,
#                     "call_dial_cnt_6m": 2,
#                     "avg_call_dial_cnt_3m": 0.67,
#                     "avg_call_dial_cnt_6m": 0.33,
#                     "call_dial_time_1m": 18,
#                     "call_dial_time_3m": 41,
#                     "call_dial_time_6m": 41,
#                     "avg_call_dial_time_3m": 14,
#                     "avg_call_dial_time_6m": 7
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 4,
#                     "call_dialed_cnt_6m": 9,
#                     "avg_call_dialed_cnt_3m": 1.33,
#                     "avg_call_dialed_cnt_6m": 1.5,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 61,
#                     "call_dialed_time_6m": 126,
#                     "avg_call_dialed_time_3m": 20,
#                     "avg_call_dialed_time_6m": 21
#                 }
#             }
#         },
#         {
#             "analysis_item": "ins_fin",
#             "analysis_desc": "保险公司",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "car_firm",
#             "analysis_desc": "汽车公司",
#             "analysis_point": {
#                 "call_cnt_1m": 0,
#                 "call_cnt_3m": 0,
#                 "call_cnt_6m": 0,
#                 "avg_call_cnt_3m": 0,
#                 "avg_call_cnt_6m": 0,
#                 "call_time_1m": 0,
#                 "call_time_3m": 0,
#                 "call_time_6m": 0,
#                 "avg_call_time_3m": 0,
#                 "avg_call_time_6m": 0,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 0,
#                     "call_dial_cnt_3m": 0,
#                     "call_dial_cnt_6m": 0,
#                     "avg_call_dial_cnt_3m": 0,
#                     "avg_call_dial_cnt_6m": 0,
#                     "call_dial_time_1m": 0,
#                     "call_dial_time_3m": 0,
#                     "call_dial_time_6m": 0,
#                     "avg_call_dial_time_3m": 0,
#                     "avg_call_dial_time_6m": 0
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 0,
#                     "call_dialed_cnt_3m": 0,
#                     "call_dialed_cnt_6m": 0,
#                     "avg_call_dialed_cnt_3m": 0,
#                     "avg_call_dialed_cnt_6m": 0,
#                     "call_dialed_time_1m": 0,
#                     "call_dialed_time_3m": 0,
#                     "call_dialed_time_6m": 0,
#                     "avg_call_dialed_time_3m": 0,
#                     "avg_call_dialed_time_6m": 0
#                 }
#             }
#         },
#         {
#             "analysis_item": "carrier",
#             "analysis_desc": "通信服务机构",
#             "analysis_point": {
#                 "call_cnt_1m": 8,
#                 "call_cnt_3m": 18,
#                 "call_cnt_6m": 31,
#                 "avg_call_cnt_3m": 6,
#                 "avg_call_cnt_6m": 5.17,
#                 "call_time_1m": 515,
#                 "call_time_3m": 1385,
#                 "call_time_6m": 2487,
#                 "avg_call_time_3m": 462,
#                 "avg_call_time_6m": 415,
#                 "call_analysis_dial_point": {
#                     "call_dial_cnt_1m": 7,
#                     "call_dial_cnt_3m": 14,
#                     "call_dial_cnt_6m": 20,
#                     "avg_call_dial_cnt_3m": 4.67,
#                     "avg_call_dial_cnt_6m": 3.33,
#                     "call_dial_time_1m": 503,
#                     "call_dial_time_3m": 1265,
#                     "call_dial_time_6m": 1954,
#                     "avg_call_dial_time_3m": 422,
#                     "avg_call_dial_time_6m": 326
#                 },
#                 "call_analysis_dialed_point": {
#                     "call_dialed_cnt_1m": 1,
#                     "call_dialed_cnt_3m": 4,
#                     "call_dialed_cnt_6m": 11,
#                     "avg_call_dialed_cnt_3m": 1.33,
#                     "avg_call_dialed_cnt_6m": 1.83,
#                     "call_dialed_time_1m": 12,
#                     "call_dialed_time_3m": 120,
#                     "call_dialed_time_6m": 533,
#                     "avg_call_dialed_time_3m": 40,
#                     "avg_call_dialed_time_6m": 89
#                 }
#             }
#         }
#     ],
#     "active_degree": [
#         {
#             "item": {
#                 "item_1m": "28",
#                 "item_3m": "86",
#                 "item_6m": "174",
#                 "avg_item_3m": "28.67",
#                 "avg_item_6m": "29.00"
#             },
#             "app_point": "call_day",
#             "app_point_zh": "通话活跃天数"
#         },
#         {
#             "item": {
#                 "item_1m": "19",
#                 "item_3m": "55",
#                 "item_6m": "104",
#                 "avg_item_3m": "18.33",
#                 "avg_item_6m": "17.33"
#             },
#             "app_point": "sms_day",
#             "app_point_zh": "短信活跃天数"
#         },
#         {
#             "item": {
#                 "item_1m": "3",
#                 "item_3m": "9",
#                 "item_6m": "15",
#                 "avg_item_3m": "3.00",
#                 "avg_item_6m": "2.50"
#             },
#             "app_point": "recharge_cnt",
#             "app_point_zh": "充值次数"
#         },
#         {
#             "item": {
#                 "item_1m": "94",
#                 "item_3m": "326",
#                 "item_6m": "659",
#                 "avg_item_3m": "108.67",
#                 "avg_item_6m": "109.83"
#             },
#             "app_point": "call_cnt",
#             "app_point_zh": "通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "70",
#                 "item_3m": "183",
#                 "item_6m": "384",
#                 "avg_item_3m": "61.00",
#                 "avg_item_6m": "64.00"
#             },
#             "app_point": "peer_num_cnt",
#             "app_point_zh": "通话号码数目"
#         },
#         {
#             "item": {
#                 "item_1m": "13",
#                 "item_3m": "27",
#                 "item_6m": "43",
#                 "avg_item_3m": "9.00",
#                 "avg_item_6m": "7.17"
#             },
#             "app_point": "peer_loc_cnt",
#             "app_point_zh": "通话号码归属地总数"
#         },
#         {
#             "item": {
#                 "item_1m": "37",
#                 "item_3m": "136",
#                 "item_6m": "228",
#                 "avg_item_3m": "45.33",
#                 "avg_item_6m": "38.00"
#             },
#             "app_point": "dial_cnt",
#             "app_point_zh": "主叫次数"
#         },
#         {
#             "item": {
#                 "item_1m": "57",
#                 "item_3m": "190",
#                 "item_6m": "431",
#                 "avg_item_3m": "63.33",
#                 "avg_item_6m": "71.83"
#             },
#             "app_point": "dialed_cnt",
#             "app_point_zh": "被叫次数"
#         },
#         {
#             "item": {
#                 "item_1m": "27",
#                 "item_3m": "72",
#                 "item_6m": "129",
#                 "avg_item_3m": "24.00",
#                 "avg_item_6m": "21.50"
#             },
#             "app_point": "dial_peer_num_cnt",
#             "app_point_zh": "主叫号码数"
#         },
#         {
#             "item": {
#                 "item_1m": "48",
#                 "item_3m": "133",
#                 "item_6m": "304",
#                 "avg_item_3m": "44.33",
#                 "avg_item_6m": "50.67"
#             },
#             "app_point": "dialed_peer_num_cnt",
#             "app_point_zh": "被叫号码数"
#         },
#         {
#             "item": {
#                 "item_1m": "167",
#                 "item_3m": "605",
#                 "item_6m": "842",
#                 "avg_item_3m": "201.67",
#                 "avg_item_6m": "140.33"
#             },
#             "app_point": "sms_cnt",
#             "app_point_zh": "短信次数"
#         },
#         {
#             "item": {
#                 "item_1m": "6572",
#                 "item_3m": "31748",
#                 "item_6m": "55455",
#                 "avg_item_3m": "10583",
#                 "avg_item_6m": "9243"
#             },
#             "app_point": "call_time",
#             "app_point_zh": "通话时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "2748",
#                 "item_3m": "15098",
#                 "item_6m": "26055",
#                 "avg_item_3m": "5033",
#                 "avg_item_6m": "4343"
#             },
#             "app_point": "dial_time",
#             "app_point_zh": "主叫时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "3824",
#                 "item_3m": "16650",
#                 "item_6m": "29400",
#                 "avg_item_3m": "5550",
#                 "avg_item_6m": "4900"
#             },
#             "app_point": "dialed_time",
#             "app_point_zh": "被叫时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "59973632",
#                 "item_3m": "278659835",
#                 "item_6m": "417738630",
#                 "avg_item_3m": "92886612",
#                 "avg_item_6m": "69623105"
#             },
#             "app_point": "net_total",
#             "app_point_zh": "流量套餐总量（KB）"
#         },
#         {
#             "item": {
#                 "item_1m": "9297202",
#                 "item_3m": "43858552",
#                 "item_6m": "128377549",
#                 "avg_item_3m": "14619517",
#                 "avg_item_6m": "21396258"
#             },
#             "app_point": "net_used",
#             "app_point_zh": "流量套餐使用量（KB）"
#         },
#         {
#             "item": {
#                 "item_1m": "70",
#                 "item_3m": "97",
#                 "item_6m": "84",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "avg_call_time",
#             "app_point_zh": "均次通话时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "12",
#                 "item_3m": "30",
#                 "item_6m": "73",
#                 "avg_item_3m": "10.00",
#                 "avg_item_6m": "12.17"
#             },
#             "app_point": "no_dial_day",
#             "app_point_zh": "无呼出天数"
#         },
#         {
#             "item": {
#                 "item_1m": "0.40",
#                 "item_3m": "0.33",
#                 "item_6m": "0.41",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "no_dial_day_pct",
#             "app_point_zh": "无呼出天数占比"
#         },
#         {
#             "item": {
#                 "item_1m": "2",
#                 "item_3m": "4",
#                 "item_6m": "6",
#                 "avg_item_3m": "1.33",
#                 "avg_item_6m": "1.00"
#             },
#             "app_point": "no_call_day",
#             "app_point_zh": "无通话天数"
#         },
#         {
#             "item": {
#                 "item_1m": "0.07",
#                 "item_3m": "0.04",
#                 "item_6m": "0.03",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "no_call_day_pct",
#             "app_point_zh": "无通话天数占比"
#         },
#         {
#             "item": {
#                 "item_1m": "14",
#                 "item_3m": "35",
#                 "item_6m": "77",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "max_power_on_day",
#             "app_point_zh": "最大连续开机天数"
#         },
#         {
#             "item": {
#                 "item_1m": "2",
#                 "item_3m": "4",
#                 "item_6m": "6",
#                 "avg_item_3m": "1.33",
#                 "avg_item_6m": "1.00"
#             },
#             "app_point": "power_off_day",
#             "app_point_zh": "关机天数"
#         },
#         {
#             "item": {
#                 "item_1m": "0.07",
#                 "item_3m": "0.04",
#                 "item_6m": "0.03",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "power_off_day_pct",
#             "app_point_zh": "关机天数占比"
#         },
#         {
#             "item": {
#                 "item_1m": "0",
#                 "item_3m": "0",
#                 "item_6m": "0",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "continue_power_off_cnt",
#             "app_point_zh": "连续3天以上关机次数"
#         }
#     ],
#     "consumption_detail": [
#         {
#             "item": {
#                 "item_1m": "3899",
#                 "item_3m": "42837",
#                 "item_6m": "74511",
#                 "avg_item_3m": "14279",
#                 "avg_item_6m": "12419"
#             },
#             "app_point": "total_fee",
#             "app_point_zh": "消费总金额（分）"
#         },
#         {
#             "item": {
#                 "item_1m": "0",
#                 "item_3m": "0",
#                 "item_6m": "0",
#                 "avg_item_3m": "0",
#                 "avg_item_6m": "0"
#             },
#             "app_point": "net_fee",
#             "app_point_zh": "网络流量消费金额（分）"
#         },
#         {
#             "item": {
#                 "item_1m": "10",
#                 "item_3m": "1417",
#                 "item_6m": "2823",
#                 "avg_item_3m": "472",
#                 "avg_item_6m": "471"
#             },
#             "app_point": "voice_fee",
#             "app_point_zh": "通话消费金额（分）"
#         },
#         {
#             "item": {
#                 "item_1m": "0",
#                 "item_3m": "120",
#                 "item_6m": "210",
#                 "avg_item_3m": "40",
#                 "avg_item_6m": "35"
#             },
#             "app_point": "sms_fee",
#             "app_point_zh": "短信消费金额（分）"
#         },
#         {
#             "item": {
#                 "item_1m": "214",
#                 "item_3m": "1214",
#                 "item_6m": "2714",
#                 "avg_item_3m": "405",
#                 "avg_item_6m": "452"
#             },
#             "app_point": "vas_fee",
#             "app_point_zh": "增值业务消费金额（分）"
#         },
#         {
#             "item": {
#                 "item_1m": "0",
#                 "item_3m": "6589",
#                 "item_6m": "10189",
#                 "avg_item_3m": "2196",
#                 "avg_item_6m": "1698"
#             },
#             "app_point": "extra_fee",
#             "app_point_zh": "其它消费金额（分）"
#         },
#         {
#             "item": {
#                 "item_1m": "11000",
#                 "item_3m": "29000",
#                 "item_6m": "55000",
#                 "avg_item_3m": "9667",
#                 "avg_item_6m": "9167"
#             },
#             "app_point": "recharge_amount",
#             "app_point_zh": "充值金额（分）"
#         },
#         {
#             "item": {
#                 "item_1m": "5000",
#                 "item_3m": "5000",
#                 "item_6m": "5000",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "max_single_recharge",
#             "app_point_zh": "单次充值最大金额（分）"
#         }
#     ],
#     "call_time_detail": [
#         {
#             "item": {
#                 "item_1m": "642",
#                 "item_3m": "1825",
#                 "item_6m": "2243",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "max_single_time",
#             "app_point_zh": "单次通话最长时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "1",
#                 "item_3m": "1",
#                 "item_6m": "1",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "min_single_time",
#             "app_point_zh": "单次通话最短时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "77",
#                 "item_3m": "233",
#                 "item_6m": "499",
#                 "avg_item_3m": "77.67",
#                 "avg_item_6m": "83.17"
#             },
#             "app_point": "cnt_1min_within",
#             "app_point_zh": "时长在1min内的通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "8",
#                 "item_3m": "65",
#                 "item_6m": "118",
#                 "avg_item_3m": "21.67",
#                 "avg_item_6m": "19.67"
#             },
#             "app_point": "cnt_1min_5min",
#             "app_point_zh": "时长在1min-5min内的通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "8",
#                 "item_3m": "20",
#                 "item_6m": "26",
#                 "avg_item_3m": "6.67",
#                 "avg_item_6m": "4.33"
#             },
#             "app_point": "cnt_5min_10min",
#             "app_point_zh": "时长在5min-10min内的通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "1",
#                 "item_3m": "8",
#                 "item_6m": "16",
#                 "avg_item_3m": "2.67",
#                 "avg_item_6m": "2.67"
#             },
#             "app_point": "cnt_10min_over",
#             "app_point_zh": "时长在10min以上的通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "93",
#                 "item_3m": "324",
#                 "item_6m": "657",
#                 "avg_item_3m": "108.00",
#                 "avg_item_6m": "109.50"
#             },
#             "app_point": "daytime_cnt",
#             "app_point_zh": "白天(7:00-0:00)通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "1",
#                 "item_3m": "2",
#                 "item_6m": "2",
#                 "avg_item_3m": "0.67",
#                 "avg_item_6m": "0.33"
#             },
#             "app_point": "night_cnt",
#             "app_point_zh": "夜晚(0:00-7:00)通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "6567",
#                 "item_3m": "31690",
#                 "item_6m": "55397",
#                 "avg_item_3m": "10563",
#                 "avg_item_6m": "9233"
#             },
#             "app_point": "daytime_time",
#             "app_point_zh": "白天(7:00-0:00)通话时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "5",
#                 "item_3m": "58",
#                 "item_6m": "58",
#                 "avg_item_3m": "19",
#                 "avg_item_6m": "10"
#             },
#             "app_point": "night_time",
#             "app_point_zh": "夜晚(0:00-7:00)通话时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "2",
#                 "item_3m": "2",
#                 "item_6m": "99",
#                 "avg_item_3m": "0.67",
#                 "avg_item_6m": "16.50"
#             },
#             "app_point": "local_cnt",
#             "app_point_zh": "本机号码归属地通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "92",
#                 "item_3m": "324",
#                 "item_6m": "560",
#                 "avg_item_3m": "108.00",
#                 "avg_item_6m": "93.33"
#             },
#             "app_point": "remote_cnt",
#             "app_point_zh": "本机号码归属地以外通话次数"
#         },
#         {
#             "item": {
#                 "item_1m": "12",
#                 "item_3m": "12",
#                 "item_6m": "4331",
#                 "avg_item_3m": "4",
#                 "avg_item_6m": "722"
#             },
#             "app_point": "local_time",
#             "app_point_zh": "本机号码归属地通话时长（秒）"
#         },
#         {
#             "item": {
#                 "item_1m": "6560",
#                 "item_3m": "31736",
#                 "item_6m": "51124",
#                 "avg_item_3m": "10579",
#                 "avg_item_6m": "8521"
#             },
#             "app_point": "remote_time",
#             "app_point_zh": "本机号码归属地以外通话时长（秒）"
#         }
#     ],
#     "call_family_detail": [
#         {
#             "item": {
#                 "item_1m": "是",
#                 "item_3m": "是",
#                 "item_6m": "是",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "is_family_member",
#             "app_point_zh": "是否为亲情网用户"
#         },
#         {
#             "item": {
#                 "item_1m": "否",
#                 "item_3m": "否",
#                 "item_6m": "否",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "is_family_master",
#             "app_point_zh": "是否为亲情网户主"
#         },
#         {
#             "item": {
#                 "item_1m": "1",
#                 "item_3m": "3",
#                 "item_6m": "6",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "continue_recharge_month_cnt",
#             "app_point_zh": "连续充值月数"
#         },
#         {
#             "item": {
#                 "item_1m": "否",
#                 "item_3m": "否",
#                 "item_6m": "否",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "is_address_match_attribution",
#             "app_point_zh": "常联系地址是否为手机归属地"
#         },
#         {
#             "item": {
#                 "item_1m": "否",
#                 "item_3m": "否",
#                 "item_6m": "否",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "call_cnt_less",
#             "app_point_zh": "通话次数 小于 使用月数＊1次"
#         },
#         {
#             "item": {
#                 "item_1m": "否",
#                 "item_3m": "否",
#                 "item_6m": "否",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "call_cnt_more",
#             "app_point_zh": "通话次数 大于 使用月数＊300次"
#         },
#         {
#             "item": {
#                 "item_1m": "0",
#                 "item_3m": "0",
#                 "item_6m": "0",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "unpaid_month_cnt",
#             "app_point_zh": "连续欠费月数"
#         },
#         {
#             "item": {
#                 "item_1m": "1",
#                 "item_3m": "1",
#                 "item_6m": "3",
#                 "avg_item_3m": "",
#                 "avg_item_6m": ""
#             },
#             "app_point": "live_month_cnt",
#             "app_point_zh": "本机号码归属地使用月数"
#         }
#     ],
#     "call_duration_detail": [
#         {
#             "key": "call_duration_detail_3m",
#             "desc": "通话时段（近三月）",
#             "duration_list": [
#                 {
#                     "item": {
#                         "total_cnt": 9,
#                         "uniq_num_cnt": 4,
#                         "total_time": 769,
#                         "dial_cnt": 3,
#                         "dialed_cnt": 6,
#                         "dial_time": 416,
#                         "dialed_time": 353,
#                         "latest_call_time": "20171007-074815",
#                         "farthest_call_time": "20170717-080443"
#                     },
#                     "time_step": "morning",
#                     "time_step_zh": "早晨[5:30-9:00]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 45,
#                         "uniq_num_cnt": 27,
#                         "total_time": 6007,
#                         "dial_cnt": 19,
#                         "dialed_cnt": 26,
#                         "dial_time": 2449,
#                         "dialed_time": 3558,
#                         "latest_call_time": "20171013-094156",
#                         "farthest_call_time": "20170716-093935"
#                     },
#                     "time_step": "forenoon",
#                     "time_step_zh": "上午[9:00-11:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 62,
#                         "uniq_num_cnt": 49,
#                         "total_time": 4087,
#                         "dial_cnt": 15,
#                         "dialed_cnt": 47,
#                         "dial_time": 1122,
#                         "dialed_time": 2965,
#                         "latest_call_time": "20171012-125349",
#                         "farthest_call_time": "20170718-123731"
#                     },
#                     "time_step": "noon",
#                     "time_step_zh": "中午[11:30-13:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 52,
#                         "uniq_num_cnt": 34,
#                         "total_time": 10587,
#                         "dial_cnt": 33,
#                         "dialed_cnt": 19,
#                         "dial_time": 5861,
#                         "dialed_time": 4726,
#                         "latest_call_time": "20171007-153228",
#                         "farthest_call_time": "20170716-150533"
#                     },
#                     "time_step": "afternoon",
#                     "time_step_zh": "下午[13:30-17:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 62,
#                         "uniq_num_cnt": 47,
#                         "total_time": 3658,
#                         "dial_cnt": 23,
#                         "dialed_cnt": 39,
#                         "dial_time": 1697,
#                         "dialed_time": 1961,
#                         "latest_call_time": "20171012-180027",
#                         "farthest_call_time": "20170717-183651"
#                     },
#                     "time_step": "dusk",
#                     "time_step_zh": "傍晚[17:30-19:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 88,
#                         "uniq_num_cnt": 53,
#                         "total_time": 6490,
#                         "dial_cnt": 40,
#                         "dialed_cnt": 48,
#                         "dial_time": 3449,
#                         "dialed_time": 3041,
#                         "latest_call_time": "20171012-221205",
#                         "farthest_call_time": "20170716-203358"
#                     },
#                     "time_step": "evening",
#                     "time_step_zh": "晚上[19:30-23:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 8,
#                         "uniq_num_cnt": 7,
#                         "total_time": 150,
#                         "dial_cnt": 3,
#                         "dialed_cnt": 5,
#                         "dial_time": 104,
#                         "dialed_time": 46,
#                         "latest_call_time": "20170930-000849",
#                         "farthest_call_time": "20170721-235611"
#                     },
#                     "time_step": "daybreak",
#                     "time_step_zh": "凌晨[23:30-1:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 0,
#                         "uniq_num_cnt": 0,
#                         "total_time": 0,
#                         "dial_cnt": 0,
#                         "dialed_cnt": 0,
#                         "dial_time": 0,
#                         "dialed_time": 0,
#                         "latest_call_time": "该时段无通话记录",
#                         "farthest_call_time": "该时段无通话记录"
#                     },
#                     "time_step": "midnight",
#                     "time_step_zh": "深夜[1:30-5:30]"
#                 }
#             ]
#         },
#         {
#             "key": "call_duration_detail_6m",
#             "desc": "通话时段（近六月）",
#             "duration_list": [
#                 {
#                     "item": {
#                         "total_cnt": 17,
#                         "uniq_num_cnt": 11,
#                         "total_time": 1108,
#                         "dial_cnt": 5,
#                         "dialed_cnt": 12,
#                         "dial_time": 624,
#                         "dialed_time": 484,
#                         "latest_call_time": "20171007-074815",
#                         "farthest_call_time": "20170418-084334"
#                     },
#                     "time_step": "morning",
#                     "time_step_zh": "早晨[5:30-9:00]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 79,
#                         "uniq_num_cnt": 51,
#                         "total_time": 8345,
#                         "dial_cnt": 32,
#                         "dialed_cnt": 47,
#                         "dial_time": 3902,
#                         "dialed_time": 4443,
#                         "latest_call_time": "20171013-094156",
#                         "farthest_call_time": "20170420-101850"
#                     },
#                     "time_step": "forenoon",
#                     "time_step_zh": "上午[9:00-11:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 126,
#                         "uniq_num_cnt": 97,
#                         "total_time": 10054,
#                         "dial_cnt": 34,
#                         "dialed_cnt": 92,
#                         "dial_time": 3238,
#                         "dialed_time": 6816,
#                         "latest_call_time": "20171012-125349",
#                         "farthest_call_time": "20170419-120846"
#                     },
#                     "time_step": "noon",
#                     "time_step_zh": "中午[11:30-13:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 114,
#                         "uniq_num_cnt": 78,
#                         "total_time": 14273,
#                         "dial_cnt": 49,
#                         "dialed_cnt": 65,
#                         "dial_time": 6999,
#                         "dialed_time": 7274,
#                         "latest_call_time": "20171007-153228",
#                         "farthest_call_time": "20170423-164502"
#                     },
#                     "time_step": "afternoon",
#                     "time_step_zh": "下午[13:30-17:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 149,
#                         "uniq_num_cnt": 114,
#                         "total_time": 7307,
#                         "dial_cnt": 47,
#                         "dialed_cnt": 102,
#                         "dial_time": 2952,
#                         "dialed_time": 4355,
#                         "latest_call_time": "20171012-180027",
#                         "farthest_call_time": "20170417-191601"
#                     },
#                     "time_step": "dusk",
#                     "time_step_zh": "傍晚[17:30-19:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 165,
#                         "uniq_num_cnt": 102,
#                         "total_time": 13787,
#                         "dial_cnt": 57,
#                         "dialed_cnt": 108,
#                         "dial_time": 7805,
#                         "dialed_time": 5982,
#                         "latest_call_time": "20171012-221205",
#                         "farthest_call_time": "20170417-203653"
#                     },
#                     "time_step": "evening",
#                     "time_step_zh": "晚上[19:30-23:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 9,
#                         "uniq_num_cnt": 7,
#                         "total_time": 581,
#                         "dial_cnt": 4,
#                         "dialed_cnt": 5,
#                         "dial_time": 535,
#                         "dialed_time": 46,
#                         "latest_call_time": "20170930-000849",
#                         "farthest_call_time": "20170714-235820"
#                     },
#                     "time_step": "daybreak",
#                     "time_step_zh": "凌晨[23:30-1:30]"
#                 },
#                 {
#                     "item": {
#                         "total_cnt": 0,
#                         "uniq_num_cnt": 0,
#                         "total_time": 0,
#                         "dial_cnt": 0,
#                         "dialed_cnt": 0,
#                         "dial_time": 0,
#                         "dialed_time": 0,
#                         "latest_call_time": "该时段无通话记录",
#                         "farthest_call_time": "该时段无通话记录"
#                     },
#                     "time_step": "midnight",
#                     "time_step_zh": "深夜[1:30-5:30]"
#                 }
#             ]
#         }
#     ],
#     "roam_analysis": [
#         {
#             "roam_location": "杭州",
#             "roam_day_cnt_3m": 78,
#             "roam_day_cnt_6m": 146,
#             "continue_roam_cnt_3m": 5,
#             "continue_roam_cnt_6m": 11,
#             "max_roam_day_cnt_3m": 34,
#             "max_roam_day_cnt_6m": 60
#         },
#         {
#             "roam_location": "温州",
#             "roam_day_cnt_3m": 7,
#             "roam_day_cnt_6m": 12,
#             "continue_roam_cnt_3m": 1,
#             "continue_roam_cnt_6m": 2,
#             "max_roam_day_cnt_3m": 7,
#             "max_roam_day_cnt_6m": 7
#         },
#         {
#             "roam_location": "丽水",
#             "roam_day_cnt_3m": 0,
#             "roam_day_cnt_6m": 2,
#             "continue_roam_cnt_3m": 0,
#             "continue_roam_cnt_6m": 1,
#             "max_roam_day_cnt_3m": 0,
#             "max_roam_day_cnt_6m": 2
#         },
#         {
#             "roam_location": "湖州",
#             "roam_day_cnt_3m": 1,
#             "roam_day_cnt_6m": 1,
#             "continue_roam_cnt_3m": 0,
#             "continue_roam_cnt_6m": 0,
#             "max_roam_day_cnt_3m": 1,
#             "max_roam_day_cnt_6m": 1
#         }
#     ],
#     "roam_detail": [
#         {
#             "roam_day": "2017-10-12",
#             "roam_location": "杭州"
#         },
#         {
#             "roam_day": "2017-10-6",
#             "roam_location": "杭州"
#         }
#     ],
#     "collection_contact": [
#         {
#             "phone_num": "13777777777",
#             "contact_name": "111",
#             "relationship": "",
#             "phone_num_loc": "",
#             "call_cnt": 0,
#             "call_time": 0,
#             "dial_cnt": 0,
#             "dial_time": 0,
#             "dialed_cnt": 0,
#             "dialed_time": 0,
#             "trans_start": "",
#             "trans_end": "",
#             "sms_cnt": 0
#         },
#         {
#             "phone_num": "138888888",
#             "contact_name": "111",
#             "relationship": "",
#             "phone_num_loc": "",
#             "call_cnt": 0,
#             "call_time": 0,
#             "dial_cnt": 0,
#             "dial_time": 0,
#             "dialed_cnt": 0,
#             "dialed_time": 0,
#             "trans_start": "",
#             "trans_end": "",
#             "sms_cnt": 0
#         }
#     ],
#     "user_info_check": [
#         {
#             "check_search_info": {
#                 "searched_org_cnt": 0,
#                 "searched_org_type": [],
#                 "idcard_with_other_names": [
#                     "李子",
#                     "王五"
#                 ],
#                 "idcard_with_other_phones": [
#                     "13882288228",
#                     "13992299229"
#                 ],
#                 "phone_with_other_names": [
#                     "王五",
#                     "鲁华"
#                 ],
#                 "phone_with_other_idcards": [
#                     "610424199303060488"
#                 ],
#                 "register_org_cnt": 0,
#                 "register_org_type": [],
#                 "arised_open_web": []
#             },
#             "check_black_info": {
#                 "phone_gray_score": 61,
#                 "contacts_class1_blacklist_cnt": 0,
#                 "contacts_class2_blacklist_cnt": 21,
#                 "contacts_class1_cnt": 381,
#                 "contacts_router_cnt": 9,
#                 "contacts_router_ratio": 0.02
#             }
#         }
#     ],
#     "trip_info": [
#         {
#             "trip_dest": "温州",
#             "trip_start_time": "2017-04-28 11:08:18",
#             "trip_end_time": "2017-04-28 21:36:10",
#             "trip_leave": "杭州",
#             "trip_type": "工作日"
#         },
#         {
#             "trip_dest": "丽水",
#             "trip_start_time": "2017-04-28 21:36:10",
#             "trip_end_time": "2017-04-30 15:50:12",
#             "trip_leave": "温州",
#             "trip_type": "节假日"
#         },
#         {
#             "trip_dest": "杭州",
#             "trip_start_time": "2017-10-07 15:32:28",
#             "trip_end_time": "2017-10-12 22:12:05",
#             "trip_leave": "温州",
#             "trip_type": "节假日"
#         }
#     ]
# }
# print(d['active_degree'])
# print(pd.DataFrame(d['active_degree'][0]))



