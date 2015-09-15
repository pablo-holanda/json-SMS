from flask import Flask, request, jsonify
import time
import logging

# Initialize the Flask application
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    # Get the parsed contents of the form data
    json = request.json
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    logging.warning('Para: ' + json['remetente'] + ' | Menssagem: ' + json['mensagem'])
    # print time.strftime("%d/%m/%Y") + " - " + time.strftime("%H:%M:%S") + " | Para: " + json['remetente'] +\
    #       " - Mensagem: " + json['mensagem']
    destino = '/var/spool/sms/outgoing/%s.txt' % (json['remetente'])
    # destino = '/Users/pabloholanda/Desktop/%s.txt' % (json['remetente'])
    file = open(destino, 'a')
    file.write("To: %s \n\n%s" % (json['remetente'], json['mensagem']))
    file.close()
    # Render template
    return jsonify(json)

# Run
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000
    )
