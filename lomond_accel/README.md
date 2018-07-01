Lomond Accel
------------

A Python lib that contains Cython extensions for use with [Lomond](https://github.com/wildfoundry/dataplicity-lomond)

```python
from lomond_accel import mask
key = b'1234'
payload = bytearray('Hello, World')

masked_payload = mask(key, payload)
unmasked_payload = mask(key, masked_payload)

```