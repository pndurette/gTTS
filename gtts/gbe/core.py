# -*- coding: utf-8 -*
from dataclasses import dataclass
from urllib.parse import quote, urlencode
from typing import List
import json
import re


@dataclass
class gBatchPayload:
    rpcid: str
    data: list


class gBatchExecuteException(Exception):
    pass


class gBatchExecuteDecodeException(gBatchExecuteException):
    pass


class gBatchExecute():

    def __init__(self, payload: List[gBatchPayload],
                url = None, host = None, user = None, app = None,
                query: dict = None, reqid: int = 0, idx: int = 1, **kwargs) -> None:
        
        # TODO: Handle extra optionals w/ **kwargs

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

        self.data = self._data()

        self.headers = self._headers()


    def _query(self, reqid, idx) -> dict:
        # TODO: Clean optionals

        query = {
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

        return urlencode(query)


    def _data(self, at: str = None):
        # TODO: at (for auth)

        data = {
            'f.req': self._freq()
        }

        return urlencode(data)


    def _freq(self):

        freq = []

        for idx, p in enumerate(self.payload, start=1):

            if len(self.payload) == 1:
                idx = 0

            freq.append(self._envelope(p, idx))

        freq = [freq]
        return json.dumps(freq, separators=(',', ':'))


    def _envelope(self, payload: gBatchPayload, idx: int = 0):

        return [
            payload.rpcid,
            json.dumps(payload.data, separators=(',', ':')),
            None,
            idx if idx > 0 else 'generic'
        ]


    def _headers(self):
        # TODO: Cookie (for auth)

        return {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        }


    def decode(self, raw: str):

        # TODO: Can't find any example of a reponse with more than
        #   than one rpcid response. This method will always assume
        #   that there was only one rpcid (first one).

        rpcid = self.payload[0].rpcid

        """
        Raw response to decode, e.g.:

            )]}'
            2593
            [["wrb.fr","rptSGc","[[[\"c8351307351755208604\", ... \n]\n]\n]\n",null,null,null,"generic"]
            ]
            57
            [["di",79]
            ,["af.httprm",79,"246063832929204055",128]
            ]
            27
            [["e",4,null,null,2691]
            ]

        """

        # Split on digits following with a newline
        # ('content-lenght' of what follows)
        resps = re.split(r'\d+\n', raw)

        # Json Decode second element to json, i.e.:
        #   [["wrb.fr", "<rpcid>", "<data>", null, null, null, "generic"]]
        decoded_resp = json.loads(resps[1])

        if decoded_resp[0][1] != rpcid:
            pass
            # raise gBatchExecuteDecodeException('rpcid not found in resp.')

        # The <data> of the reponse itself is a json string
        decoded_data = json.loads(decoded_resp[0][2])

        return [(rpcid, decoded_data)]



"""
https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
https://github.com/Boudewijn26/gTTS-token/blob/master/docs/november-2020-translate-changes.md

needs:
* rpcids
* regex matching the result
* payload: [<rpcid>, <payload>]

re.search(r'jQ1olc","\[\\"(.*)\\"]', decoded_line)

"""
"""
parameter = [text, self.lang, self.speed, "null"]
escaped_parameter = json.dumps(parameter, separators=(',', ':'))

rpc = [[[self.GOOGLE_TTS_RPC, escaped_parameter, None, "generic"]]]
espaced_rpc = json.dumps(rpc, separators=(',', ':'))
return f"f.req={quote(espaced_rpc)}&"
"""

"""

[[["rptSGc","[[\"c8351307351755208604\"]]",null,"generic"]]]

[[["jQ1olc","[\"test\",\"en\",true,\"null\"]",null,"generic"]]]
[[["jQ1olc","[\"test\",\"en\",true,\"null\"]",null,"generic"]]]

[[["jQ1olc","[\"test\",\"en\",null,\"null\"]",null,"generic"]]]
[[["jQ1olc","[\"test\",\"en\",true,\"null\"]",null,"generic"]]]

f.req=%5B%5B%5B%22jQ1olc%22%2C%22%5B%5C%22test%5C%22%2C%5C%22en%5C%22%2Cnull%2C%5C%22null%5C%22%5D%22%2Cnull%2C%22generic%22%5D%5D%5D
f.req=%5B%5B%5B%22jQ1olc%22%2C%22%5B%5C%22test%5C%22%2C%5C%22en%5C%22%2Ctrue%2C%5C%22null%5C%22%5D%22%2Cnull%2C%22generic%22%5D%5D%5D


curl 'https://translate.google.com/_/TranslateWebserverUi/data/batchexecute' \
-X 'POST' \
-H 'Content-Type: application/x-www-form-urlencoded;charset=utf-8' \
-d 'f.req=%5B%5B%5B%22jQ1olc%22%2C%22%5B%5C%22test%5C%22%2C%5C%22en%5C%22%2Cnull%2C%5C%22null%5C%22%5D%22%2Cnull%2C%22generic%22%5D%5D%5D'
"""