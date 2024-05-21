import os

from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, jsonify, request
from ohmslaw import Ohms


load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')


@app.route('/api/v1/f_resistor', methods=['GET'])
def api_find_resistor():
    try:
        source = float(request.args.get('source'))
        component_voltage = float(request.args.get('component_voltage'))
        
        o = Ohms()
        results = o.find_resistor(source=source, component_voltage=component_voltage)
        
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
    
    return jsonify(response)


@app.route('/api/v1/volts', methods=['GET'])
def api_volts():
    try:
        current = float(request.args.get('current'))
        resistance = float(request.args.get('resistance'))

        o = Ohms()
        results = o.volts(I=current, R=resistance)

        response = {
            'current': current,
            'resistance': resistance,
            'results': results,
            'status': 'success'
        }
    except Exception as e:
        response = {
            'error': str(e),
            'status': 'error'
        }
    
    return jsonify(response)


@app.route('/api/v1/current', methods=['GET'])
def api_current():
    try:
        resistance = float(request.args.get('resistance'))
        volts = float(request.args.get('volts'))

        o = Ohms()
        results = o.current(R=resistance, V=volts)

        response = {
            'resistance': resistance,
            'volts': volts,
            'results': results,
            'status': 'success'
        }
    except Exception as e:
        response = {
            'error': str(e),
            'status': 'error'
        }
        
    return jsonify(response)


@app.route('/api/v1/resistance')
def api_resistance():
    try:
        volts = float(request.args.get('volts'))
        current = float(request.args.get('current'))

        o = Ohms()
        results = o.resistance(V=volts, I=current)

        response = {
            'volts': volts,
            'current': current,
            'results': results,
            'status': 'success'
        }
    except Exception as e:
        response = {
            'error': str(e),
            'status': 'error'
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run()