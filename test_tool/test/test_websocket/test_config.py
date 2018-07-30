# -*- coding: utf-8 -*-
import sys
import os

sys.path.append('..')
sys.path.append('../..')

from utils.config import Config

class test_config():
	(contract_addr, contract_tx_hash) = ("", "")
	block_height = 0
	block_hash = ""
	signed_data = ""

	HEIGHT_CORRECT = 0
	HEIGHT_BORDER = 0
	HEIGHT_INCORRECT_1 = -1
	HEIGHT_INCORRECT_2 = 0
	HEIGHT_INCORRECT_3 = "abc"

	BLOCK_HASH_CORRECT = ""
	BLOCK_HASH_INCORRECT_1 = "" # NULL
	BLOCK_HASH_INCORRECT_2 = ""
	BLOCK_HASH_INCORRECT_3 = ""
	BLOCK_HASH_INCORRECT_4 = 1234

	TX_HASH_CORRECT = ""
	TX_HASH_INCORRECT_1 = "" # NULL
	TX_HASH_INCORRECT_2 = "" # TX HASH NOT EXISTENT
	TX_HASH_INCORRECT_3 = ""
	TX_HASH_INCORRECT_4 = 1234

	RAW_TRANSACTION_DATA_CORRECT = ""
	RAW_TRANSACTION_DATA_INCORRECT_1 = "" # NULL
	RAW_TRANSACTION_DATA_INCORRECT_2 = "11111111" + signed_data + "1111111111" # INCORRECT SERIALIZE
	RAW_TRANSACTION_DATA_INCORRECT_3 = 1234

	ACCOUNT_ADDRESS_CORRECT = Config.NODES[0]['address']
	ACCOUNT_ADDRESS_INCORRECT_1 = "" # NULL
	ACCOUNT_ADDRESS_INCORRECT_2 = Config.NODES[0]['address'] + "11" # NOT EXISTENT
	ACCOUNT_ADDRESS_INCORRECT_3 = "abc"
	ACCOUNT_ADDRESS_INCORRECT_4 = 1234

	CONTRACT_ADDRESS_CORRECT = ""
	CONTRACT_ADDRESS_INCORRECT_1 = "" # NULL
	CONTRACT_ADDRESS_INCORRECT_2 = "" # NOT EXISTENT
	CONTRACT_ADDRESS_INCORRECT_3 = "abc"
	CONTRACT_ADDRESS_INCORRECT_4 = 1234

	KEY_CORRECT = ""
	KEY_INCORRECT_1 = "" # NULL
	KEY_INCORRECT_2 = "" # NOT EXISTENT
	KEY_INCORRECT_3 = "abc"
	KEY_INCORRECT_4 = 1234 
