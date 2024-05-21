
# ohmslaw API

```python
import requests

SOURCE = 12
COMPONENT_VOLTS = 5.0

url = f'127.0.0.1:5000/api/v1/f_resistor?source={SOURCE}&component_voltage={COMPONENT_VOLTS}'
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print(f'Erro na solicitação: {response.status_code}')

```
