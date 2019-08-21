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

#查看钱包导入的所有账户信息
pprint(gph.wallet.getAccounts())

#init0 ["COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT", "5JHdMwsWkEXsMozFrQAQKnKwo44CaV77H45S9PsH7QVbFQngJfw"]
pub="COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT"

#获取公钥对应的私钥
pprint(gph.wallet.getPrivateKeyForPublicKey(pub))

#通过公钥获取账号信息
pprint(gph.wallet.getAccount(pub))

#创建账号
try:
    pprint(gph.create_account(account_name="test10", password="123456", proxy_account="init14"))
except Exception as e:
    print(repr(e))
    gph.wallet.removeAccount(None)

#转账1
pprint(gph.transfer('test14', 100, "1.3.0", "test memo", 'init0'))
'''
执行结果：
tx.buffer>>>: {'extensions': [], 'ref_block_num': 52379, 'operations': [[0, {'extensions': [], 'from': '1.2.4', 'memo': {'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h', 'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'nonce': 5901681697903210751, 'message': '8bb2f19b3a3b57cbbf04e539783f3d62'}, 'to': '1.2.17', 'fee': {'amount': 2089843, 'asset_id': '1.3.0'}, 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}}]], 'signatures': ['1f7ebeba7dd6b0efdb9286260a05c426ab476a3ecb5fc8812ccc5dea826b56c5e76024a526ad510f77ff3fd1ac9f6439d4b40aa4e1099fe3676d322d5ffa1a31eb'], 'expiration': '2019-08-21T04:19:45', 'ref_block_prefix': 2924873733}
tx======>>: {'extensions': [], 'ref_block_num': 52379, 'operations': [[0, {'extensions': [], 'from': '1.2.4', 'memo': {'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h', 'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'nonce': 5901681697903210751, 'message': '8bb2f19b3a3b57cbbf04e539783f3d62'}, 'to': '1.2.17', 'fee': {'amount': 2089843, 'asset_id': '1.3.0'}, 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}}]], 'signatures': ['1f7ebeba7dd6b0efdb9286260a05c426ab476a3ecb5fc8812ccc5dea826b56c5e76024a526ad510f77ff3fd1ac9f6439d4b40aa4e1099fe3676d322d5ffa1a31eb'], 'expiration': '2019-08-21T04:19:45', 'ref_block_prefix': 2924873733}
transaction>>>: {'extensions': [], 'ref_block_num': 52379, 'operations': [[0, {'extensions': [], 'from': '1.2.4', 'memo': {'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h', 'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'nonce': 5901681697903210751, 'message': '8bb2f19b3a3b57cbbf04e539783f3d62'}, 'to': '1.2.17', 'fee': {'amount': 2089843, 'asset_id': '1.3.0'}, 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}}]], 'signatures': ['1f7ebeba7dd6b0efdb9286260a05c426ab476a3ecb5fc8812ccc5dea826b56c5e76024a526ad510f77ff3fd1ac9f6439d4b40aa4e1099fe3676d322d5ffa1a31eb'], 'expiration': '2019-08-21T04:19:45', 'ref_block_prefix': 2924873733}

['dee8d42d4e49458b54987cf563e82fa3c941e77580981fd4b8893bde9ad62a4d',
 {'block': 52380,
  'expiration': '2019-08-21T04:19:45',
  'extensions': [],
  'operation_results': [[1, {'real_running_time': 198}]],
  'operations': [[0,
                  {'amount': {'amount': 10000000, 'asset_id': '1.3.0'},
                   'extensions': [],
                   'fee': {'amount': 2089843, 'asset_id': '1.3.0'},
                   'from': '1.2.4',
                   'memo': {'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT',
                            'message': '8bb2f19b3a3b57cbbf04e539783f3d62',
                            'nonce': '5901681697903210751',
                            'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h'},
                   'to': '1.2.17'}]],
  'ref_block_num': 52379,
  'ref_block_prefix': 2924873733,
  'signatures': ['1f7ebeba7dd6b0efdb9286260a05c426ab476a3ecb5fc8812ccc5dea826b56c5e76024a526ad510f77ff3fd1ac9f6439d4b40aa4e1099fe3676d322d5ffa1a31eb']}]
'''

#转账2
pprint(gph.transfer('test14', 100, "COCOS", "test memo", 'init0'))
'''
执行结果：
tx.buffer>>>: {'expiration': '2019-08-21T06:14:50', 'ref_block_prefix': 310102910, 'operations': [[0, {'to': '1.2.17', 'memo': {'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h', 'message': '8ba4d671c0736eda127467110ef9043e', 'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'nonce': 6591532363490338807}, 'from': '1.2.4', 'extensions': [], 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}, 'fee': {'amount': 2089843, 'asset_id': '1.3.0'}}]], 'signatures': ['1f16c3c089b96e8c32cdcf530b3542df434a55b3736ac34421fef5e461850c6adf66723dcdb03cd3ed84cc3a5eb8dc158b8aa4c57a368263109fc7e76677059706'], 'extensions': [], 'ref_block_num': 53342}
tx======>>: {'expiration': '2019-08-21T06:14:50', 'ref_block_prefix': 310102910, 'operations': [[0, {'to': '1.2.17', 'memo': {'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h', 'message': '8ba4d671c0736eda127467110ef9043e', 'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'nonce': 6591532363490338807}, 'from': '1.2.4', 'extensions': [], 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}, 'fee': {'amount': 2089843, 'asset_id': '1.3.0'}}]], 'signatures': ['1f16c3c089b96e8c32cdcf530b3542df434a55b3736ac34421fef5e461850c6adf66723dcdb03cd3ed84cc3a5eb8dc158b8aa4c57a368263109fc7e76677059706'], 'extensions': [], 'ref_block_num': 53342}
transaction>>>: {'expiration': '2019-08-21T06:14:50', 'ref_block_prefix': 310102910, 'operations': [[0, {'to': '1.2.17', 'memo': {'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h', 'message': '8ba4d671c0736eda127467110ef9043e', 'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT', 'nonce': 6591532363490338807}, 'from': '1.2.4', 'extensions': [], 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}, 'fee': {'amount': 2089843, 'asset_id': '1.3.0'}}]], 'signatures': ['1f16c3c089b96e8c32cdcf530b3542df434a55b3736ac34421fef5e461850c6adf66723dcdb03cd3ed84cc3a5eb8dc158b8aa4c57a368263109fc7e76677059706'], 'extensions': [], 'ref_block_num': 53342}

['aaa792d7cd0788eb23fdffa8bc2536b37b9733cfb620a092842d04a33a47497f',
 {'block': 53343,
  'expiration': '2019-08-21T06:14:50',
  'extensions': [],
  'operation_results': [[1, {'real_running_time': 201}]],
  'operations': [[0,
                  {'amount': {'amount': 10000000, 'asset_id': '1.3.0'},
                   'extensions': [],
                   'fee': {'amount': 2089843, 'asset_id': '1.3.0'},
                   'from': '1.2.4',
                   'memo': {'from': 'COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT',
                            'message': '8ba4d671c0736eda127467110ef9043e',
                            'nonce': '6591532363490338807',
                            'to': 'COCOS8GY2vkoK8gpLTuDxNfzD6JjwqYDmCRnpoUfZ78J4z8ChdcZi6h'},
                   'to': '1.2.17'}]],
  'ref_block_num': 53342,
  'ref_block_prefix': 310102910,
  'signatures': ['1f16c3c089b96e8c32cdcf530b3542df434a55b3736ac34421fef5e461850c6adf66723dcdb03cd3ed84cc3a5eb8dc158b8aa4c57a368263109fc7e76677059706']}]
'''



