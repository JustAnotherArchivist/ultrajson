import ujson

for _ in range(1000):
	assert ujson.loads(b"123") == 123
	try:
		ujson.loads(memoryview(b"{}"))
	except TypeError as e:
		if 'PyPy' not in str(e):
			raise
	else:
		raise RuntimeError('TypeError not raised')
	assert ujson.loads(bytearray(b"99")) == 99
