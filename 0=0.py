Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\requests\models.py", line 974, in json
    return complexjson.loads(self.text, **kwargs)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python312\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python312\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python312\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Lenovo\Desktop\新建文件夹\demo1.py", line 7, in <module>
    data=response.json()['data']['result']
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python312\Lib\site-packages\requests\models.py", line 978, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

