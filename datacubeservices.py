import requests
import json


class DataCubeServices:
    def __init__(self, api_key, db_name):
        self.base_url = "https://datacube.uxlivinglab.online/db_api/"
        self.api_key = api_key
        self.db_name = db_name

    def perform_request(self, endpoint, method='post', data=None):
        url = self.base_url + endpoint
        headers = {'Content-Type': 'application/json'}

        # If data is None, initialize it as an empty dictionary
        if data is None:
            data = {}

        # Add api_key and db_name to the data
        data['api_key'] = self.api_key
        data['db_name'] = self.db_name
        response = None

        try:
            if method == 'post':
                response = requests.post(url, json=data, headers=headers)
            elif method == 'put':
                response = requests.put(url, json=data, headers=headers)
            elif method == 'delete':
                response = requests.delete(url, json=data, headers=headers)
            
            if response:
                return response.text
            else:
                return "No response received"

        except requests.RequestException as e:
            return f"Request Exception: {str(e)}"

    def fetch_data(self, collection, filters={}, limit=1, offset=0):
        data = {
            "coll_name": collection,
            "operation": "fetch",
            "filters": filters,
            "limit": limit,
            "offset": offset
        }
        return self.perform_request("get_data/", data=data)

    def insert_data(self, collection, data_to_insert):
        data = {
            "coll_name": collection,
            "operation": "insert",
            "data": data_to_insert
        }
        return self.perform_request("crud/", data=data)

    def update_data(self, collection, query, update_data):
        data = {
            "coll_name": collection,
            "operation": "update",
            "query": query,
            "update_data": update_data
        }
        return self.perform_request("crud/", method='put', data=data)

    def delete_data(self, collection, query):
        data = {
            "coll_name": collection,
            "operation": "delete",
            "query": query
        }
        return self.perform_request("crud/", method='delete', data=data)

    def add_collection(self, collection_name, num_collections=1):
        data = {
            "coll_names": collection_name,
            "num_collections": num_collections
        }
        return self.perform_request("add_collection/", data=data)
