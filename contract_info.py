address_contract_1 = "0x9927E0541ea7986B2FdCAE0B9dA5F5bB91E67A11"
address_contract_2 = "0x53C1bda973E28fD43C0F70343F3Cef723Bd49287"
address_contract_3 = "0x86bC3ac8be1336Da259144f145b5AcabEE4E6A5d"
address_contract_4 = "0x072B3bb0B4eE15c9A4F65f188367eE6212139fbA"
address_contract_5 = "0xB0D78862AEa07d641E5551AB42DE033e01D9437f"



abi = """[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idAd",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "createdAd",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.EstateType",
				"name": "esType",
				"type": "uint8"
			}
		],
		"name": "createdEstate",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idAd",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.AdStatus",
				"name": "adStatus",
				"type": "uint8"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "estatePurchased",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "recipient",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			}
		],
		"name": "fundsBack",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idAd",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.AdStatus",
				"name": "adStatus",
				"type": "uint8"
			}
		],
		"name": "updatedAdStatus",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			}
		],
		"name": "updatedEstateStatus",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "ads",
		"outputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "idAd",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.AdStatus",
				"name": "adStatus",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "balances",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "idAd",
				"type": "uint256"
			}
		],
		"name": "buyEstate",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "createAd",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "addressEstate",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "size",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.EstateType",
				"name": "esType",
				"type": "uint8"
			}
		],
		"name": "createEstate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "estates",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "size",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "addressEstate",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "enum EstateAgency.EstateType",
				"name": "esType",
				"type": "uint8"
			},
			{
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAds",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "buyer",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "idEstate",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "idAd",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "dateTime",
						"type": "uint256"
					},
					{
						"internalType": "enum EstateAgency.AdStatus",
						"name": "adStatus",
						"type": "uint8"
					}
				],
				"internalType": "struct EstateAgency.Advertisement[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getEstates",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "size",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "addressEstate",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "enum EstateAgency.EstateType",
						"name": "esType",
						"type": "uint8"
					},
					{
						"internalType": "bool",
						"name": "isActive",
						"type": "bool"
					},
					{
						"internalType": "uint256",
						"name": "idEstate",
						"type": "uint256"
					}
				],
				"internalType": "struct EstateAgency.Estate[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "idAd",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.AdStatus",
				"name": "adStatus",
				"type": "uint8"
			}
		],
		"name": "updateAdStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			}
		],
		"name": "updateEstateStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withDraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""