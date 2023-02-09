import ujson

for _ in range(1000):
	print('ok' if ujson.loads(bytearray(b"99")) == 99 else 'ohno')
