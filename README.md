# Compute web service
Will be a set of language systems (two interpreters and one compiler) behind a web api written in DjangoRestFramework :-)

## example
```python
>>> file = {'scm_file': open('test.scm')}
>>> re = requests.post(url, files=file, auth=auth)
>>> file = {'scm_file': open('test.scm')}
>>> re = requests.post(url, files=file, auth=auth)
>>> file = {'scm_file': open('test.scm')}
>>> re = requests.post(url, files=file, auth=auth)
>>> re.json()
{'input_expression': '(car (cdr (list 3 4 5 6)))\n', 'output_expression': '4', 'created': '2024-03-11T05:05:05.584486Z'}

>>> url = 'http://127.0.0.1:8000/api/scm_exp/22'
>>> re = requests.get(url, auth=auth)
>>> re.json()
{'input_expression': '(car (cdr (list 3 4 5 6)))\n', 'output_expression': '4', 'created': '2024-03-11T05:05:05.584486Z'}
>>> 

```