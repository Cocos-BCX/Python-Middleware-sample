#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PythonMiddleware.graphene import Graphene
from PythonMiddleware.instance import set_shared_graphene_instance
from pprint import pprint
from PythonMiddleware.account import Account

nodeAddress = "ws://127.0.0.1:8020" 
gph = Graphene(node=nodeAddress, blocking=True) 
set_shared_graphene_instance(gph) 

#创建钱包1
#可以通过gph.wallet 直接使用钱包instance，操作钱包的接口。
if gph.wallet.created() is False: 
    gph.newWallet("123456")

#创建钱包2
if gph.wallet.created() is False: 
    gph.wallet.create("123456")

#钱包解锁
gph.wallet.unlock("123456")

#钱包锁住
gph.wallet.lock()

#查看钱包锁定状态
#返回: False 或 True
pprint(gph.wallet.locked())

#更改钱包解锁密码
#钱包需要unlock状态
#gph.wallet.changePassphrase("654321")

#查看钱包导入账户信息
pprint(gph.wallet.getAccounts())

#钱包导入私钥
privateKey="5JWKbGLfkZNtnSAb7fuk1pD4jsdPyMpJz4jyhwgu8RBk9RNzDYA"
pub="COCOS78WwFk5YJVoCVa97NAKVALVZdhnYUdD2oHe2LCiX2KZaYNf4G8"
gph.wallet.addPrivateKey(privateKey) 

#钱包获取导入的私钥
pprint(gph.wallet.getPrivateKeyForPublicKey(pub))

#加密私钥
encWif = gph.wallet.encrypt_wif(privateKey)
pprint(encWif)

#解密私钥
pprint(gph.wallet.decrypt_wif(encWif) == privateKey)

#钱包移除导入的私钥
#gph.wallet.removePrivateKeyFromPublicKey(pub)

#移除导入的账户None
gph.wallet.removeAccount(None)
gph.wallet.removeAccount('test13')

#获取账号的owner private key
pprint(gph.wallet.getOwnerKeyForAccount('test13'))
pprint(gph.wallet.getMemoKeyForAccount('test13'))
pprint(gph.wallet.getActiveKeyForAccount('test13'))

#获取账户ID
pprint(gph.wallet.getAccountFromPrivateKey(privateKey))
pprint(gph.wallet.getAccountFromPublicKey(pub))

#获取账户信息
pprint(gph.wallet.getAccount(pub))

#获取钱包所有账户信息
pprint(gph.wallet.getAccounts())

#获取钱包所有公钥
pprint(gph.wallet.getPublicKeys())

#获取钱包公钥类型
pprint(gph.wallet.getKeyType(Account('test13'), pub))

#清除钱包所有私钥
#  慎用！！！
#gph.wallet.wipe()

