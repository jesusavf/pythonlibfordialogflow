from flask import Flask, request, make_response, jsonify
from flask_ngrok import run_with_ngrok
from waitress import serve
app = Flask(__name__)
import lib

@app.route('/')
def index():
    msj=[]
    msj.append('ssss')
    msj.append('puta')
    return lib.rndmsj(msj)

@app.route('/web', methods=['GET', 'POST'])
def web():
    lib.credenciales(request.authorization["username"],request.authorization["password"],'test','testo')
    if lib.instancia('h gato'):
        a=lib.variable('any')
        return lib.msj(a)
    else:
        if lib.origenes()=='FACEBOOK':
            t = {"titulo":[],"boton":[]}
            t['titulo'].append('deseas seguir')
            t['boton'].append('si')
            t['boton'].append('no')
            return lib.enviarrespuestasrapidas(t,lib.origenes())
        else:
            return lib.msj(lib.acciones())

@app.route('/auth')
def authRouteHandler(): 
    return 'nada'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)
   
