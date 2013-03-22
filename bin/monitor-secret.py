#!/usr/bin/python

import base64
import struct

AES_128_KEY_TYPE = 1
AES_128_KEY_LEN = 16

def encode(created_nsec, use_entropy):
    NANO = 1000000000
    secs, nsecs = divmod(created_nsec, NANO)
    assert len(use_entropy) == AES_128_KEY_LEN
    s = struct.pack(
        '<HLLH16s',
        AES_128_KEY_TYPE,
        secs,
        nsecs,
        AES_128_KEY_LEN,
        use_entropy,
        )
    assert len(s) == 28
    return base64.b64encode(s)

if __name__ == '__main__':
    import random
    import time

    entropy = struct.pack(
        'QQ',
        random.getrandbits(64),
        random.getrandbits(64),
        )
    print encode(
        created_nsec=int(time.time() * 1e9),
        use_entropy=entropy,
        )
