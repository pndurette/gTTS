# -*- coding: utf-8 -*
from dataclasses import dataclass
from typing import List
import re


@dataclass
class gBatchPayload:
    rpcid: str
    payload: list


class gBatchExecute():

    def __init__(self, payload: List[gBatchPayload],
                url = None, host = None, user = None, app = None,
                query: dict = None, reqid: int = 0, idx: int = 1, ) -> None:
        
        if not url:
            if not user:
                self.url = f'https://{host}/_/{app}/data/batchexecute'
            else:
                self.url = f'https://{host}/u/{user}/_/{app}/data/batchexecute'
        else:
            self.url = url

        if isinstance(payload, list):
            self.payload = payload
        else:
            self.payload = [payload]

        if not query:
            assert 0 < reqid < 99999, "reqid must be in the 0-99999 range"
            assert idx > 0, "idx must be great than 0"
            self.query = self._query(reqid, idx)
        else:
            self.query = query


    def _query(self, reqid, idx) -> dict:
        return {
            # Comma-deleted string of all rpcids
            'rpcids': ','.join([p.rpcid for p in self.payload]),
            
            # Response type. Always 'c'.
            'rt': 'c',

            # 5-character
            '_reqid': reqid + (idx * 100000),

            # Optionals:

            # Signed 64-bit integer consistant for a single page load
            # e.g. 6781970813608854611
            # 'f.sid': 0,

            # Name and version of the backend software handling the requests
            # e.g. 'boq_translate-webserver_20210217.12_p0'
            #'bl': '',
            
            # 2-character ISO 639–1 language code the UI is in
            # e.g. 'en'
            # 'hl': '',
        }

    def decode(self):
        pass



"""
https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
https://github.com/Boudewijn26/gTTS-token/blob/master/docs/november-2020-translate-changes.md

needs:
* rpcids
* regex matching the result
* payload: [<rpcid>, <payload>]

"""