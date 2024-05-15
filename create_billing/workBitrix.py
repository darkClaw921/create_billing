from fast_bitrix24 import Bitrix
import os
from dotenv import load_dotenv
from pprint import pprint
from dataclasses import dataclass
from datetime import datetime
# import urllib3
import urllib.request
import time
import asyncio
load_dotenv()
webhook = os.getenv('WEBHOOK')
bit = Bitrix(webhook)
BILLING_ITEM_ID=173
PROJECT_ITEM_ID=158
@dataclass
class Lead:
    userName:str
    title:str='TITLE'
    userID:str='UF_CRM_1709220784686'
    photos:str='UF_CRM_1709223951925'
    urlUser:str='UF_CRM_1709224894080'
    messageURL:str='UF_CRM_1709293438392'

    description:str='COMMENTS'

@dataclass
class Deal:
    id:str='ID'
    title:str='TITLE'
    categoryID:str='CATEGORY_ID'
    statusID:str='STATUS_ID'
    comments:str='COMMENTS'
    responsibleID:str='ASSIGNED_BY_ID'
    department:str=''

@dataclass
class BillingItem:
    id:str='id'
    title:str='title'
    # duration:str='UF_CRM9_1713363122'

    # dateClose:str='ufCrm10_1715010793674'
    dateClose:str='ufCrm_17Date'
    # entityTypeId:str='ENTITY_TYPE_ID 
    # fields:str='FIELDS'
    trydozatrary:str='ufCrm17Duration'
    trydozatratyKoplate:str='ufCrm17Durationbillable'
    stavka:str='None'
    project:str='parentId158'
    assigned:str='assignedById'
# async def te
def find_deal(dealID:str):
    deal = bit.call('crm.deal.get', params={'id': dealID})
    return deal

def find_lead(leadID:str):
    lead = bit.call('crm.lead.get', params={'id': leadID})
    return lead


def get_deals():
    prepareDeal=[]
    deals = bit.call('crm.deal.list', items={'filter': 
                                             {'STAGE_SEMANTIC_ID':'S'}}, raw=True)['result']
    for deal in deals:
        
        product=bit.call('crm.deal.productrows.get', items={'id': int(deal['ID'])}, raw=True)['result']
        
        a={'deal':deal,
            'product':product}
        
        prepareDeal.append(a)
    pprint(prepareDeal)
    return prepareDeal

def get_products():
    products = bit.call('crm.product.list', raw=True)['result']
    pprint(products)
    return products

def get_users():
    prepareUser = []
    # users = bit.call('user.get', items={'filter' :{'ACTIVE':False}})
    users = bit.call('user.get', raw=True)['result']
    # for user in users:
        # prepareUser.append(f'[{user["ID"]}] {user["NAME"]} {user["LAST_NAME"]}')
    # pprint(users)
    # print(prepareUser)
    return users

def get_departments():
    departments = bit.call('department.get', raw=True)['result']
    pprint(departments)
    return departments

def get_billing_item(userID:int, parentID158:int)->list:

    items = bit.get_all('crm.item.list', params={'entityTypeId':BILLING_ITEM_ID,
                                             'filter':
                                                {
                                                # f'>={BillingItem.dateClose}': startDate,
                                                # f'<={BillingItem.dateClose}': endDate,
                                                'parentId158': parentID158,
                                                'assignedById': userID},
                                                # f'!={BillingItem.stage}'
                                            }, )
                                            #
                                            #   }, raw=True)['result']
    projects=[]
    for item in items:
        projects.append([item['title'], f'https://b24-pmzj40.bitrix24.ru/crm/type/{BILLING_ITEM_ID}/details/{item['id']}/'])
        # item['UF_CRM_1621959721'] = datetime.fromtimestamp(item['UF_CRM_1621959721']).strftime('%Y-%m-%d %H:%M:%S')
    # https://b24-pmzj40.bitrix24.ru/crm/type/159/details/3/
    # pprint(items)
    return projects

def get_all_project_item()->list:
    """Получение всех активных проектов"""
    items = bit.get_all('crm.item.list', params={'entityTypeId':PROJECT_ITEM_ID,
                                             'filter':
                                                {
                                                # f'>={BillingItem.dateClose}': startDate,
                                                # f'<={BillingItem.dateClose}': endDate,
                                                "!stageId": ["DT158_21:SUCCESS", "DT158_21:FAIL"],
                                                # 'assignedById': userID
                                                },
                                                # f'!={BillingItem.stage}'
                                            }, )
                                            #
                                            #   }, raw=True)['result']
    # pprint(items)
    projects=[]
    for item in items:
        projects.append([item['title'], item['id']])
        # item['UF_CRM_1621959721'] = datetime.fromtimestamp(item['UF_CRM_1621959721']).strftime('%Y-%m-%d %H:%M:%S')
    # https://b24-pmzj40.bitrix24.ru/crm/type/159/details/3/
    return projects

def get_all_users():
    users = bit.get_all('user.get', params={'filter': {'ACTIVE':True}})
    usersLst=[]
    for user in users:
        usersLst.append([f'{user["NAME"]} {user["LAST_NAME"]}',user['ID'] ])
    return usersLst

def create_billing_item(fields:dict):
    bit.call('crm.item.add', items={'entityTypeId':BILLING_ITEM_ID, 'fields':fields})

if __name__ == '__main__':
    
    users=get_all_users()
    pprint(users)
    # get = get_all_project_item()
    # pprint(get)
    # get = get_billing_item(23, 45)
    # pprint(get)
    # asyncio.run(get_deals())
    # get_deals()\
    # get_products()
    # get_users()
    # get_departments()
    

# async def find_lead(userID:str):
#     lead = await bit.get_all(
#         'crm.deal.list',
#         params={
#             'select': ['*', 'UF_*'],
#             'filter': {Deal.id: f'{userID}'}
#     },)
#     pprint(lead)
#     if lead==[]:
#         return None
#     else:
#         print('лид уже есть')
#         # pprint(lead)
#         lead=lead[-1]
#         return lead




