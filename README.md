

https://ohmslaw-u2g5rsfcwa-tl.a.run.app/api/v1/f_resistor?source=12.0&component_voltage=5.0

https://ohmslaw-u2g5rsfcwa-tl.a.run.app/api/v1/volts?current=2.0&resistance=6.0

https://ohmslaw-u2g5rsfcwa-tl.a.run.app/api/v1/current?resistance=10.0&volts=5.0

https://ohmslaw-u2g5rsfcwa-tl.a.run.app/api/v1/resistance?volts=12.0&current=2.0



```python
import requests

url = '127.0.0.0:5000/api/v1/f_resistor?source=12.0&component_voltage=5.0'
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print(f'Erro na solicitação: {response.status_code}')

```
