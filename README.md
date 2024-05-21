
# ohmslaw API

```python
import requests

SOURCE = 12
COMPONENT_VOLTS = 5.0

url = f'127.0.0.1:5000/api/v1/f_resistor?source={SOURCE}&component_voltage={COMPONENT_VOLTS}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')

```
