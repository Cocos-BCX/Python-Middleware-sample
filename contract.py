#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PythonMiddleware.graphene import Graphene
from PythonMiddleware.instance import set_shared_graphene_instance
from pprint import pprint
from PythonMiddleware.account import Account

nodeAddress = "ws://127.0.0.1:8020" 
gph = Graphene(node=nodeAddress, blocking=True) 
set_shared_graphene_instance(gph) 

#创建钱包
#可以通过gph.wallet 直接使用钱包instance，操作钱包的接口。
if gph.wallet.created() is False: 
    gph.newWallet("123456")

#钱包解锁
if gph.wallet.locked() is True:
    gph.wallet.unlock("123456")


#init0 ["COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT", "5JHdMwsWkEXsMozFrQAQKnKwo44CaV77H45S9PsH7QVbFQngJfw"]
pub="COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT"
pprint(gph.wallet.getPrivateKeyForPublicKey(pub))

#合约创建1
data1="function hello() chainhelper:log('Hello World!') end"
pprint(gph.create_contract("contract.pytest.hello", data=data1, con_authority=pub, account="init0"))
'''
执行结果：
tx.buffer>>>: {'extensions': [], 'signatures': ['1f11b53efe5abb9fa5690644b437ce2fe7193b3deeb5bc0f13021241ad914c008019942a45a830253f49410e77537d8739a1f1c629f31938c613085faa8ad82aa9'], 'ref_block_prefix': 695707653, 'ref_block_num': 53573, 'operations': [[43, {'data': "function hello() chainhelper:log('Hello World!') end", 'extensions': [], 'fee': {'asset_id': '1.3.0', 'amount': 2051757}, 'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'owner': '1.2.4', 'name': 'contract.pytest.hello'}]], 'expiration': '2019-08-21T06:34:07'}
tx======>>: {'extensions': [], 'signatures': ['1f11b53efe5abb9fa5690644b437ce2fe7193b3deeb5bc0f13021241ad914c008019942a45a830253f49410e77537d8739a1f1c629f31938c613085faa8ad82aa9'], 'ref_block_prefix': 695707653, 'ref_block_num': 53573, 'operations': [[43, {'data': "function hello() chainhelper:log('Hello World!') end", 'extensions': [], 'fee': {'asset_id': '1.3.0', 'amount': 2051757}, 'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'owner': '1.2.4', 'name': 'contract.pytest.hello'}]], 'expiration': '2019-08-21T06:34:07'}
transaction>>>: {'extensions': [], 'signatures': ['1f11b53efe5abb9fa5690644b437ce2fe7193b3deeb5bc0f13021241ad914c008019942a45a830253f49410e77537d8739a1f1c629f31938c613085faa8ad82aa9'], 'ref_block_prefix': 695707653, 'ref_block_num': 53573, 'operations': [[43, {'data': "function hello() chainhelper:log('Hello World!') end", 'extensions': [], 'fee': {'asset_id': '1.3.0', 'amount': 2051757}, 'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'owner': '1.2.4', 'name': 'contract.pytest.hello'}]], 'expiration': '2019-08-21T06:34:07'}
['66d25d4d1a8fd68fe8d431f1af4b0c11d7d2760777261fc77488033a4c643177',
 {'block': 53574,
  'expiration': '2019-08-21T06:34:07',
  'extensions': [],
  'operation_results': [[2, {'real_running_time': 822, 'result': '1.16.1'}]],
  'operations': [[43,
                  {'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT',
                   'data': "function hello() chainhelper:log('Hello World!') "
                           'end',
                   'extensions': [],
                   'fee': {'amount': 2051757, 'asset_id': '1.3.0'},
                   'name': 'contract.pytest.hello',
                   'owner': '1.2.4'}]],
  'ref_block_num': 53573,
  'ref_block_prefix': 695707653,
  'signatures': ['1f11b53efe5abb9fa5690644b437ce2fe7193b3deeb5bc0f13021241ad914c008019942a45a830253f49410e77537d8739a1f1c629f31938c613085faa8ad82aa9']}]
'''

#合约创建2
data2 = "function hello() \
    chainhelper:log('Hello World!') \
    chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) \
end "
pprint(gph.create_contract("contract.pytest.hello2", data=data2, con_authority=pub, account="init0"))

'''
执行结果：
tx.buffer>>>: {'extensions': [], 'ref_block_num': 53615, 'ref_block_prefix': 3922499816, 'signatures': ['1f5088ae364efb3b1bbcf59e6adcdd969548d94023564e740631a6b7cbd283a3376533d17c0da90f9f7f4abeb08615f046c056bee4a16d9f6850eb95a325f126be'], 'operations': [[43, {'extensions': [], 'name': 'contract.pytest.hello2', 'data': "function hello()     chainhelper:log('Hello World!')     chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) end ", 'owner': '1.2.4', 'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'fee': {'asset_id': '1.3.0', 'amount': 2122070}}]], 'expiration': '2019-08-21T06:37:37'}
tx======>>: {'extensions': [], 'ref_block_num': 53615, 'ref_block_prefix': 3922499816, 'signatures': ['1f5088ae364efb3b1bbcf59e6adcdd969548d94023564e740631a6b7cbd283a3376533d17c0da90f9f7f4abeb08615f046c056bee4a16d9f6850eb95a325f126be'], 'operations': [[43, {'extensions': [], 'name': 'contract.pytest.hello2', 'data': "function hello()     chainhelper:log('Hello World!')     chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) end ", 'owner': '1.2.4', 'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'fee': {'asset_id': '1.3.0', 'amount': 2122070}}]], 'expiration': '2019-08-21T06:37:37'}
transaction>>>: {'extensions': [], 'ref_block_num': 53615, 'ref_block_prefix': 3922499816, 'signatures': ['1f5088ae364efb3b1bbcf59e6adcdd969548d94023564e740631a6b7cbd283a3376533d17c0da90f9f7f4abeb08615f046c056bee4a16d9f6850eb95a325f126be'], 'operations': [[43, {'extensions': [], 'name': 'contract.pytest.hello2', 'data': "function hello()     chainhelper:log('Hello World!')     chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) end ", 'owner': '1.2.4', 'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'fee': {'asset_id': '1.3.0', 'amount': 2122070}}]], 'expiration': '2019-08-21T06:37:37'}
['dd79a4497506b0d24b0aff5e1896be5d7f2ff875adf08560d84382e128a3b87c',
 {'block': 53616,
  'expiration': '2019-08-21T06:37:37',
  'extensions': [],
  'operation_results': [[2, {'real_running_time': 780, 'result': '1.16.2'}]],
  'operations': [[43,
                  {'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT',
                   'data': "function hello()     chainhelper:log('Hello "
                           "World!')     "
                           "chainhelper:log(date('%Y-%m-%dT%H:%M:%S', "
                           'chainhelper:time())) end ',
                   'extensions': [],
                   'fee': {'amount': 2122070, 'asset_id': '1.3.0'},
                   'name': 'contract.pytest.hello2',
                   'owner': '1.2.4'}]],
  'ref_block_num': 53615,
  'ref_block_prefix': 3922499816,
  'signatures': ['1f5088ae364efb3b1bbcf59e6adcdd969548d94023564e740631a6b7cbd283a3376533d17c0da90f9f7f4abeb08615f046c056bee4a16d9f6850eb95a325f126be']}]
'''

#调用合约
value_list=[]
#调用1
pprint(gph.call_contract_function("contract.pytest.hello2", "hello", value_list=value_list, account="test14"))

#调用2
pprint(gph.call_contract_function("1.16.2", "hello", value_list=value_list, account="test14"))
'''
执行结果：
value_list:>>> []
value_list:>>> []
tx.buffer>>>: {'ref_block_num': 53792, 'expiration': '2019-08-21T06:52:24', 'operations': [[44, {'value_list': [], 'function_name': 'hello', 'caller': '1.2.17', 'fee': {'asset_id': '1.3.0', 'amount': 2007812}, 'contract_id': '1.16.2', 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 1080919947, 'signatures': ['200e225780dc4381daeb9322a81733d2a085b68d41d5c5468794b106f2f21a3679228fcbc97035aa992c37570f1a548a6ed764a84d479b06cf5cf6adb70ce5d1a1', '203d5a926b2777f092c6659838c80c71521a37bf549edf221778b9aa7763fa97167d0f679123e4078b77371c58f15bccc01cc2ea4155ef322d8f0221af36e3126b']}
tx======>>: {'ref_block_num': 53792, 'expiration': '2019-08-21T06:52:24', 'operations': [[44, {'value_list': [], 'function_name': 'hello', 'caller': '1.2.17', 'fee': {'asset_id': '1.3.0', 'amount': 2007812}, 'contract_id': '1.16.2', 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 1080919947, 'signatures': ['200e225780dc4381daeb9322a81733d2a085b68d41d5c5468794b106f2f21a3679228fcbc97035aa992c37570f1a548a6ed764a84d479b06cf5cf6adb70ce5d1a1', '203d5a926b2777f092c6659838c80c71521a37bf549edf221778b9aa7763fa97167d0f679123e4078b77371c58f15bccc01cc2ea4155ef322d8f0221af36e3126b']}
transaction>>>: {'ref_block_num': 53792, 'expiration': '2019-08-21T06:52:24', 'operations': [[44, {'value_list': [], 'function_name': 'hello', 'caller': '1.2.17', 'fee': {'asset_id': '1.3.0', 'amount': 2007812}, 'contract_id': '1.16.2', 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 1080919947, 'signatures': ['200e225780dc4381daeb9322a81733d2a085b68d41d5c5468794b106f2f21a3679228fcbc97035aa992c37570f1a548a6ed764a84d479b06cf5cf6adb70ce5d1a1', '203d5a926b2777f092c6659838c80c71521a37bf549edf221778b9aa7763fa97167d0f679123e4078b77371c58f15bccc01cc2ea4155ef322d8f0221af36e3126b']}
['6a73a9d7dc3e56fd6087d17592ce55e5c8453f21c268c1f66ef0055759b943f3',
 {'block': 53794,
  'expiration': '2019-08-21T06:52:24',
  'extensions': [],
  'operation_results': [[4,
                         {'additional_cost': {'amount': 637109,
                                              'asset_id': '1.3.0'},
                          'contract_affecteds': [[3,
                                                  {'affected_account': '1.2.17',
                                                   'message': 'Hello World!'}],
                                                 [3,
                                                  {'affected_account': '1.2.17',
                                                   'message': '2019-08-21T05:52:25'}]],
                          'contract_id': '1.16.2',
                          'existed_pv': False,
                          'process_value': '',
                          'real_running_time': 600}]],
  'operations': [[44,
                  {'caller': '1.2.17',
                   'contract_id': '1.16.2',
                   'extensions': [],
                   'fee': {'amount': 2007812, 'asset_id': '1.3.0'},
                   'function_name': 'hello',
                   'value_list': []}]],
  'ref_block_num': 53792,
  'ref_block_prefix': 1080919947,
  'signatures': ['200e225780dc4381daeb9322a81733d2a085b68d41d5c5468794b106f2f21a3679228fcbc97035aa992c37570f1a548a6ed764a84d479b06cf5cf6adb70ce5d1a1',
                 '203d5a926b2777f092c6659838c80c71521a37bf549edf221778b9aa7763fa97167d0f679123e4078b77371c58f15bccc01cc2ea4155ef322d8f0221af36e3126b']}]
'''



