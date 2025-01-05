import json
import os
from typing import Any


class JSONHelper:

    def get_parse_json_body(self) -> bool:
        json_path = self.get_json_path()
        parse_json = self.decode_json_body(json_path=json_path)
        return parse_json


    def decode_json_body(self,json_path) -> Any:
        try:
            with open(json_path,'r',encoding='utf-8') as json_content:
                data = json.load(json_content)
                return data if data is not None else None
        except json.decoder.JSONDecodeError as json_decode_error:
            print(f'Error Decoding The JSON Content...., Error: {json_decode_error}')
            return
        except Exception as error:
            print(f'An Unknown Error has been Encountered while Decoding the JSON Body , Error : {error}')


    def get_json_path(self):
        acutal_json_path = os.path.join(os.getcwd(),'TestData','Credentials.json')
        try:
            return acutal_json_path
        except FileNotFoundError as file_error:
            print(f'{acutal_json_path} Does not Exists on your System')
            return