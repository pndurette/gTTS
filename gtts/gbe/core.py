# -*- coding: utf-8 -*
from dataclasses import dataclass
from urllib.parse import quote, urlencode
from typing import List
import json
import re


@dataclass
class gBatchPayload:
    rpcid: str
    args: list


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
        # TODO: return urlencode

        data = {
            'f.req': self._freq()
        }

        return data
        # return urlencode(data)


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
            json.dumps(payload.args, separators=(',', ':')),
            None,
            str(idx) if idx > 0 else 'generic'
        ]


    def _headers(self):
        # TODO: Cookie (for auth)

        return {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        }


    def decode(self, raw: str, strict: bool = False):

        # Regex pattern to extract raw data responses (frames)
        p = re.compile(
            pattern=r"""
                (\d+\n)         # <number><\n>
                (?P<frame>.+?)  # 'frame': anything incl. <\n> (re.DOTALL)
                (?=\d+\n|$)     # until <number><\n> or <end>
            """,
            flags=re.DOTALL | re.VERBOSE
        )

        # TODO: decode charset here?
        # TODO: except if rpcid not found
        # TODO: except if data is empty

        decoded = []

        for item in p.finditer(raw):

            # A 'frame' group is a json string
            # e.g.: '[["wrb.fr","jQ1olc","[\"/abc\"]\n",null,null,null,"generic"]]'
            #          ^^^^^^^^  ^^^^^^   ^^^^^^^^^^^^                 ^^^^^^^^^
            #          [0][0]    [0][1]   [0][2]                       [0][6]
            #          constant  rpc id   rpc response                 frame index or
            #          (str)     (str)    (json str)                   "generic" if single frame
            #                                                          (str)
            frame_raw = item.group('frame')
            frame = json.loads(frame_raw)

            # Ignore frames that don't have 'wrb.fr' at [0][0]
            # (they're not rpc reponses but analytics etc.)
            if frame[0][0] != 'wrb.fr':
                continue

            # index (at [0][6], string)
            # index is 1-based
            # index is "generic" if the response contains a single frame
            if frame[0][6] == 'generic':
                index = 1
            else:
                index = int(frame[0][6])

            # rpcid (at [0][1])
            # rpcid's response (at [0][2], a json string)
            rpcid = frame[0][1]
            data = json.loads(frame[0][2])

            if strict and data == []:
                raise gBatchExecuteDecodeException("empty data")

            # Append as tuple
            decoded.append(
                (index, rpcid, data)
            )

        # Sort responses by index ([0])
        decoded = sorted(decoded, key=lambda frame: frame[0])

        if strict:
            in_rpcids = [p.rpcid for p in self.payload]
            out_rpcids = [rpcid for rpcid, data in decoded]

            in_len = len(in_rpcids)
            out_len = len(out_rpcids)

            if in_len != out_len:
                raise gBatchExecuteDecodeException("in/out not same len")

            if set(in_rpcids) != set(out_rpcids):
                raise gBatchExecuteDecodeException("items not the same")

        return decoded



"""
https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
https://github.com/Boudewijn26/gTTS-token/blob/master/docs/november-2020-translate-changes.md
"""