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

#合约创建1：单行合约
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

#合约创建2: 多行合约
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

#合约创建3：通过文件创建
file = open("hello.lua", "r")   #打开文件
context = file.read()          #读取文件
print(context)
pprint(gph.create_contract("contract.pytest.hello3", data=context, con_authority=pub, account="init0"))
'''
执行结果：
function hello() 
    chainhelper:log('Hello World!') 
    chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) 
    chainhelper:log('test end. 2019-08-21 14:35:08') 
end

tx.buffer>>>: {'signatures': ['1f6a7c96c3c1664db6cd6fecd7e6764f3b1c61c1591a1b1ed54448b0055bae5ec508457fbf2f980fe35117982b2ef35f98fe43888d8a8c814bdc4c78ce84b61c07'], 'expiration': '2019-08-21T07:40:25', 'operations': [[43, {'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'owner': '1.2.4', 'name': 'contract.pytest.hello3', 'fee': {'amount': 2178710, 'asset_id': '1.3.0'}, 'extensions': [], 'data': "function hello() \n    chainhelper:log('Hello World!') \n    chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) \n    chainhelper:log('test end. 2019-08-21 14:35:08') \nend\n"}]], 'ref_block_prefix': 2432441567, 'extensions': [], 'ref_block_num': 54369}
tx======>>: {'signatures': ['1f6a7c96c3c1664db6cd6fecd7e6764f3b1c61c1591a1b1ed54448b0055bae5ec508457fbf2f980fe35117982b2ef35f98fe43888d8a8c814bdc4c78ce84b61c07'], 'expiration': '2019-08-21T07:40:25', 'operations': [[43, {'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'owner': '1.2.4', 'name': 'contract.pytest.hello3', 'fee': {'amount': 2178710, 'asset_id': '1.3.0'}, 'extensions': [], 'data': "function hello() \n    chainhelper:log('Hello World!') \n    chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) \n    chainhelper:log('test end. 2019-08-21 14:35:08') \nend\n"}]], 'ref_block_prefix': 2432441567, 'extensions': [], 'ref_block_num': 54369}
transaction>>>: {'signatures': ['1f6a7c96c3c1664db6cd6fecd7e6764f3b1c61c1591a1b1ed54448b0055bae5ec508457fbf2f980fe35117982b2ef35f98fe43888d8a8c814bdc4c78ce84b61c07'], 'expiration': '2019-08-21T07:40:25', 'operations': [[43, {'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'owner': '1.2.4', 'name': 'contract.pytest.hello3', 'fee': {'amount': 2178710, 'asset_id': '1.3.0'}, 'extensions': [], 'data': "function hello() \n    chainhelper:log('Hello World!') \n    chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) \n    chainhelper:log('test end. 2019-08-21 14:35:08') \nend\n"}]], 'ref_block_prefix': 2432441567, 'extensions': [], 'ref_block_num': 54369}
['53a1bcf027ddaf235f26b9987b41feeaa7087d2cf288f5efa76b727df6edfc67',
 {'block': 54370,
  'expiration': '2019-08-21T07:40:25',
  'extensions': [],
  'operation_results': [[2, {'real_running_time': 936, 'result': '1.16.3'}]],
  'operations': [[43,
                  {'contract_authority': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT',
                   'data': 'function hello() \n'
                           "    chainhelper:log('Hello World!') \n"
                           "    chainhelper:log(date('%Y-%m-%dT%H:%M:%S', "
                           'chainhelper:time())) \n'
                           "    chainhelper:log('test end. 2019-08-21 "
                           "14:35:08') \n"
                           'end\n',
                   'extensions': [],
                   'fee': {'amount': 2178710, 'asset_id': '1.3.0'},
                   'name': 'contract.pytest.hello3',
                   'owner': '1.2.4'}]],
  'ref_block_num': 54369,
  'ref_block_prefix': 2432441567,
  'signatures': ['1f6a7c96c3c1664db6cd6fecd7e6764f3b1c61c1591a1b1ed54448b0055bae5ec508457fbf2f980fe35117982b2ef35f98fe43888d8a8c814bdc4c78ce84b61c07']}]
'''



#调用合约: contract.pytest.hello2
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

#合约调用：调用通过文件创建的合约：contract.pytest.hello3
pprint(gph.call_contract_function("contract.pytest.hello3", "hello", value_list=value_list, account="test14"))
'''
合约执行：
value_list:>>> []
value_list:>>> []
tx.buffer>>>: {'ref_block_num': 54396, 'ref_block_prefix': 398433404, 'extensions': [], 'operations': [[44, {'value_list': [], 'extensions': [], 'contract_id': '1.16.3', 'function_name': 'hello', 'caller': '1.2.17', 'fee': {'amount': 2007812, 'asset_id': '1.3.0'}}]], 'expiration': '2019-08-21T07:42:41', 'signatures': ['20312321ead5eefee489d55868fad2b3782f3b39fdf9fcf79a229e4967a1a49f0460e658e3d14fde1162a78f4707ac7ffd14a0c98f132723e72856bed6d75721c0', '203afda066ec1969e9eb5b37e015744011aff225ae0674692b3e0f505d21d64b352e9e51b8fffdf66cec6ec1bd9233cfefae8226b159b5673744304068172017a2']}
tx======>>: {'ref_block_num': 54396, 'ref_block_prefix': 398433404, 'extensions': [], 'operations': [[44, {'value_list': [], 'extensions': [], 'contract_id': '1.16.3', 'function_name': 'hello', 'caller': '1.2.17', 'fee': {'amount': 2007812, 'asset_id': '1.3.0'}}]], 'expiration': '2019-08-21T07:42:41', 'signatures': ['20312321ead5eefee489d55868fad2b3782f3b39fdf9fcf79a229e4967a1a49f0460e658e3d14fde1162a78f4707ac7ffd14a0c98f132723e72856bed6d75721c0', '203afda066ec1969e9eb5b37e015744011aff225ae0674692b3e0f505d21d64b352e9e51b8fffdf66cec6ec1bd9233cfefae8226b159b5673744304068172017a2']}
transaction>>>: {'ref_block_num': 54396, 'ref_block_prefix': 398433404, 'extensions': [], 'operations': [[44, {'value_list': [], 'extensions': [], 'contract_id': '1.16.3', 'function_name': 'hello', 'caller': '1.2.17', 'fee': {'amount': 2007812, 'asset_id': '1.3.0'}}]], 'expiration': '2019-08-21T07:42:41', 'signatures': ['20312321ead5eefee489d55868fad2b3782f3b39fdf9fcf79a229e4967a1a49f0460e658e3d14fde1162a78f4707ac7ffd14a0c98f132723e72856bed6d75721c0', '203afda066ec1969e9eb5b37e015744011aff225ae0674692b3e0f505d21d64b352e9e51b8fffdf66cec6ec1bd9233cfefae8226b159b5673744304068172017a2']}

['2bc05435b5d4eac3f69da12b5917eb9d29f2825db0dc152ee96415e03294f046',
 {'block': 54397,
  'expiration': '2019-08-21T07:42:41',
  'extensions': [],
  'operation_results': [[4,
                         {'additional_cost': {'amount': 701359,
                                              'asset_id': '1.3.0'},
                          'contract_affecteds': [[3,
                                                  {'affected_account': '1.2.17',
                                                   'message': 'Hello World!'}],
                                                 [3,
                                                  {'affected_account': '1.2.17',
                                                   'message': '2019-08-21T06:42:40'}],
                                                 [3,
                                                  {'affected_account': '1.2.17',
                                                   'message': 'test end. '
                                                              '2019-08-21 '
                                                              '14:35:08'}]],
                          'contract_id': '1.16.3',
                          'existed_pv': False,
                          'process_value': '',
                          'real_running_time': 633}]],
  'operations': [[44,
                  {'caller': '1.2.17',
                   'contract_id': '1.16.3',
                   'extensions': [],
                   'fee': {'amount': 2007812, 'asset_id': '1.3.0'},
                   'function_name': 'hello',
                   'value_list': []}]],
  'ref_block_num': 54396,
  'ref_block_prefix': 398433404,
  'signatures': ['20312321ead5eefee489d55868fad2b3782f3b39fdf9fcf79a229e4967a1a49f0460e658e3d14fde1162a78f4707ac7ffd14a0c98f132723e72856bed6d75721c0',
                 '203afda066ec1969e9eb5b37e015744011aff225ae0674692b3e0f505d21d64b352e9e51b8fffdf66cec6ec1bd9233cfefae8226b159b5673744304068172017a2']}]
'''
