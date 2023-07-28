from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorPersona import ControladorPersona
from Controladores.ControladorProveedor import ControladorProveedor
from Controladores.ControladorProducto import ControladorProducto
from Controladores.ControladorInventario import ControladorInventario

app = Flask(__name__)
cors = CORS(app)


miControladorPersona = ControladorPersona()
miControladorProveedor = ControladorProveedor()
miControladorProducto = ControladorProducto()
miControladorInventario = ControladorInventario()




#########################EndPoint de persona##########################################
@app.route("/personas",methods=['GET'])
def getPersonas():
    json=miControladorPersona.index()
    return jsonify(json)

@app.route("/personas",methods=['POST'])
def crearPersonas():
    data = request.get_json()
    json=miControladorPersona.create(data)
    return jsonify(json)

@app.route("/personas/<string:id>",methods=['GET'])
def getPersona(id):
    json=miControladorPersona.show(id)
    return jsonify(json)

@app.route("/personas/<string:id>",methods=['PUT'])
def modificarPersona(id):
    data = request.get_json()
    json=miControladorPersona.update(id,data)
    return jsonify(json)

@app.route("/personas/<string:id>",methods=['DELETE'])
def eliminarPersona(id):
    json=miControladorPersona.delete(id)
    return jsonify(json)


#########################EndPoint de proveerdor##########################################
@app.route("/proveedores", methods=['GET'])
def getProveedores():
    json = miControladorProveedor.index()
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['GET'])
def getProveedor(id):
    json = miControladorProveedor.show(id)
    return jsonify(json)

#Que hace esta ruta???????????????????????????
@app.route("/proveedores/<string:id>/productos", methods=['GET'])
def getProductosInventario(id):
    json = miControladorProveedor.getProductos(id)
    return jsonify(json)


@app.route("/proveedores", methods=['POST'])
def crearProveedor():
    data = request.get_json()
    json = miControladorProveedor.create(data)
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['PUT'])
def modificarProveerdor(id):
    data = request.get_json()
    json = miControladorProveedor.update(id, data)
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['DELETE'])
def eliminarDepartamento(id):
    json = miControladorProveedor.delete(id)
    return jsonify(json)

#########################EndPoint de producto##########################################
@app.route("/productos", methods=['GET'])
def getProductos():
    json = miControladorProducto.index()
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['GET'])
def getProducto(id):
    json = miControladorProducto.show(id)
    return jsonify(json)


@app.route("/productos", methods=['POST'])
def crearProducto():
    data = request.get_json()
    json = miControladorProducto.create(data)
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json = miControladorProducto.update(id, data)
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['DELETE'])
def eliminarProducto(id):
    json = miControladorProducto.delete(id)
    return jsonify(json)

##Funciona normal la asignacion de proveedor a producto
@app.route("/productos/<string:id>/proveedor/<string:id_proveedor>", methods=['PUT'])
def asignarProveedorProducto(id, id_proveedor):
    json = miControladorProducto.asignarProveedor(id, id_proveedor)
    return jsonify(json)


#########################EndPoint de inventario##########################################
@app.route("/inventarios", methods=['GET'])
def getInventarios():
    json = miControladorInventario.index()
    return jsonify(json)


@app.route("/inventarios/<string:id>", methods=['GET'])
def getInventario(id):
    json = miControladorInventario.show(id)
    return jsonify(json)

#####obtener un solo campo#####
#@app.route("/inventarios/<string:id>/cantidadProducto", methods=['GET'])
#def getUnProducto(id, cantidadProducto):
#    json = miControladorInventario.getUnProducto(id, cantidadProducto)
#    return jsonify(json)


@app.route("/inventarios/persona/<string:id_persona>/producto/<string:id_producto>", methods=['POST'])
def crearInventario(id_persona, id_producto):
    data = request.get_json()
    json = miControladorInventario.create(data, id_persona, id_producto)
    return jsonify(json)


## Funciona normal
@app.route("/inventarios/<string:id_inventario>/persona/<string:id_persona>/producto/<string:id_producto>", methods=['PUT'])
def modificarInventario(id_inventario, id_persona, id_producto):
    data = request.get_json()
    json = miControladorInventario.update(id_inventario, data, id_persona, id_producto)
    return jsonify(json)


@app.route("/inventarios/<string:id_inventario>", methods=['DELETE'])
def eliminarInventario(id_inventario):
    json = miControladorInventario.delete(id_inventario)
    return jsonify(json)


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)




#es un método leer el archivo de configuración del proyecto, en últimas este retornará un
#diccionario el cual posee la información dentro del JSON
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data




if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
