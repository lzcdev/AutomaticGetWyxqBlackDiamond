#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

# 领取黑钻的请求
def getCollectCoins(serialNumber):
	cookies = {
   		'mp_MA-9E66-C87EFACB60BC_hubble': 'xxx',
    	'_ga': 'xxx',
    	'_gat': 'xxx',
    	'NTES_YD_SESS': 'xxx',
    	'STAR_YD_SESS': 'xxx',
    	'STAREIG': 'xxx',
	}

	headers = {
    	'Host': 'star.8.163.com',
    	'Accept': 'application/json, text/plain, */*',
    	'X-Requested-With': 'XMLHttpRequest',
    	'Accept-Language': 'en-us',
    	'Content-Type': 'application/json;charset=UTF-8',
    	'Origin': 'https://star.8.163.com',
    	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.3.1",accountId: "f737c09d14618b486b90fa7d6c21c017c193ce0ff4284f8da24aad2833caea21"}star_client_info_end',
    	'Referer': 'https://star.8.163.com/m',
 	}
	data = '{"serialNumber": \"%s\"}' % serialNumber
	response = requests.post('https://star.8.163.com/api/starUserCoin/collectUserCoin', headers=headers, cookies=cookies, data=data)
	print(response.json())

	

def main():
	cookies = {
  		'mp_MA-9E66-C87EFACB60BC_hubble': 'xxx',
   		'NTES_YD_SESS': 'xxx',
    	'STAR_YD_SESS': 'xxx',
    	'_ga': 'xxx',
    	'_gat': 'xxx',
    	'STAREIG': 'xxx',
	}

	headers = {
    	'Host': 'star.8.163.com',
    	'Accept': 'application/json, text/plain, */*',
    	'X-Requested-With': 'XMLHttpRequest',
    	'Accept-Language': 'en-us',
    	'Content-Type': 'application/json;charset=UTF-8',
    	'Origin': 'https://star.8.163.com',
    	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.3.1",accountId: "f737c09d14618b486b90fa7d6c21c017c193ce0ff4284f8da24aad2833caea21"}star_client_info_end',
    	'Referer': 'https://star.8.163.com/m',
	}

	data = '{"type":0}'

	# 获取黑钻的请求
	response = requests.post('https://star.8.163.com/api/home/v2/userInfoAndCollectCoins', headers=headers, cookies=cookies, data=data)
	collectCoins = response.json()['data']['collectCoins']
	# print(collectCoins)
	if len(collectCoins) == 0:
		print('当前没有黑钻可以领取');
	else:
		for collectCoinsItem in collectCoins:
			print(collectCoinsItem)	
			getCollectCoins(collectCoinsItem['serialNumber'])	


main()			







