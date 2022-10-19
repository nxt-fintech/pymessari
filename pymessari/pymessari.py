#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   pymessari.py
@Time    :   2022/10/19 14:50:19
@Author  :   Next Finance Tech
@Version :   0.0.1
@License :   (C)Copyright 2022 Next Finance Tech
"""


import json
import time
import urllib
from enum import Enum

import requests


class Method(Enum):
    GET = 1
    POST = 2


class API:
    def __init__(self, api_key, timeout=None):
        self.api_url = "https://data.messari.io/api"
        self.api_key = api_key
        self.timeout = timeout

    def request(self, endpoint, method=Method.GET, params=None):
        url = self.api_url + endpoint
        headers = {
            "Accept": "application/json",
            "x-messari-api-key": self.api_key,
        }

        print(url)
        try:
            with requests.Session() as s:
                s.headers.update(headers)
                if method == Method.GET:
                    response = s.get(url, params=params, timeout=self.timeout)
                elif method == Method.POST:
                    response = s.post(url, data=json.dumps(params), timeout=self.timeout)
        except requests.RequestException as e:
            raise e

        return API.process_response(response)

    @staticmethod
    def process_response(response):
        result = {"status_code": response.status_code}
        if len(response.content) > 0:
            result["body"] = response.json()

        return result

    @staticmethod
    def join_id(protocol_id, network_id):
        if network_id:
            protocol_id = "{protocol_id}/networks/{network_id}"
        return protocol_id

    def get_total_revenue(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/total-revenue-usd/time-series"

        return self.request(endpoint, params=params)

    def get_protocol_side_revenue(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/protocol-side-revenue-usd/time-series"

        return self.request(endpoint, params=params)

    def get_supply_side_revenue(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/supply-side-revenue-usd/time-series"

        return self.request(endpoint, params=params)

    def get_total_deposits_balance(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/total-deposits-balance-usd/time-series"

        return self.request(endpoint, params=params)

    def get_num_deposits(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/num-deposits/time-series"

        return self.request(endpoint, params=params)

    def get_deposits(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/deposits-usd/time-series"

        return self.request(endpoint, params=params)

    def get_total_borrows_balance(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/total-borrows-balance-usd/time-series"

        return self.request(endpoint, params=params)

    def get_num_borrow(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/num-borrows/time-series"

        return self.request(endpoint, params=params)

    def get_borrows(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/borrows-usd/time-series"

        return self.request(endpoint, params=params)

    def get_num_liquidates(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/num-liquidates/time-series"

        return self.request(endpoint, params=params)

    def get_liquidates(self, protocol_id, network_id=None, **params):
        joined_ids = API.join_id(protocol_id, network_id)
        endpoint = f"/v1/protocols/{joined_ids}/metrics/liquidates-usd/time-series"

        return self.request(endpoint, params=params)
