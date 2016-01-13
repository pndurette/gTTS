# -*- coding: utf-8 -*-
import calendar, time, math

class gToken:
    """ gToken (Google Translate Token)
    Generate the current token key and allows generation of tokens (tk) with it
    Python version of `token-script.js` itself from translate.google.com
    """

    SALT_1 = "+-a^+6"
    SALT_2 = "+-3^+b+-f"

    def __init__(self):
        # The current token key (hours since unix epoch)
        timestamp = calendar.timegm(time.gmtime())
        hours = int(math.floor(timestamp / 3600))
        self.token_key = hours

    def calculate_token(self, text, seed=None):
        """ Calculate the request token (`tk`) of a string """

        e = 0
        f = 0
        d = [None] * len(text)
        for c in text:
            g = ord(c)
            if 128 > g:
                d[e] = g
                e += 1
            elif 2048 > g:
                d[e] = g >> 6 | 192
                e += 1
            else:
                if 55296 == (g & 64512) and f + 1 < len(text) and 56320 == (ord(text[f + 1]) & 64512):
                    f += 1
                    g = 65536 + ((g & 1023) << 10) + (ord(text[f]) & 1023)
                    d[e] = g >> 18 | 240
                    e += 1
                    d[e] = g >> 12 & 63 | 128
                    e += 1
                else:
                    d[e] = g >> 12 | 224
                    e += 1
                    d[e] = g >> 6 & 63 | 128
                    e += 1
                    d[e] = g & 63 | 128
                    e += 1

        a = seed if seed is not None else self.token_key
        if seed is None:
            seed = self.token_key
        for value in d:
            a += value
            a = self._work_token(a, self.SALT_1)
        a = self._work_token(a, self.SALT_2)
        if 0 > a:
            a = (a & 2147483647) + 2147483648
        a %= 1E6
        a = int(a)
        return str(a) + "." + str(a ^ seed)

    """ Functions used by the token calculation algorithm """
    def _rshift(self, val, n): return val>>n if val >= 0 else (val+0x100000000)>>n
    def _work_token(self, a, seed):
        for i in range(0, len(seed) - 2, 3):
            char = seed[i + 2]
            d = ord(char[0]) - 87 if char >= "a" else int(char)
            d = self._rshift(a, d) if seed[i + 1] == "+" else a << d
            a = a + d & 4294967295 if seed[i] == "+" else a ^ d
        return a

if __name__ == "__main__":
        pass
