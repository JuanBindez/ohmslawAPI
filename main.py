
from flask import Flask, jsonify, request
from ohmslaw import Ohms

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        # Obtém os parâmetros da URL
        source = float(request.args.get('source'))
        component_voltage = float(request.args.get('component_voltage'))
        
        # Cria uma instância de Ohms
        o = Ohms()
        
        # Calcula o resistor
        results = o.find_resistor(source=source, component_voltage=component_voltage)
        
        # Cria um dicionário com o resultado
        response = {
            'source': source,
            'component_voltage': component_voltage,
            'results': results,
            'status': 'success'
        }
    except Exception as e:
        response = {
            'error': str(e),
            'status': 'error'
        }
    
    # Retorna o dicionário como JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
