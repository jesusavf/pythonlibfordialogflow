from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
import lib

@app.route('/')
def index():
    msj=[]
    msj.append('tet1')
    msj.append('test2')
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
            msj=[]
            msj.append('tet1')
            msj.append('test2')
            return lib.rndmsj(msj)

@app.route('/auth')
def authRouteHandler(): 
    return 'nada'

if __name__ == '__main__':
  app.run(debug=True)
   