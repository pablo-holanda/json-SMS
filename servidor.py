from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    # Get the parsed contents of the form data
    json = request.json
    print(json['remetente'])
    destino = 'var/spool/sms/outgoing/%s.txt' % (json['remetente'])
    # destino = '/Users/pabloholanda/Desktop/%s.txt' % (json['remetente'])
    file = open(destino, 'a')
    file.write("To: %s \n%s" % (json['remetente'], json['menssagem']))
    file.close()
    # Render template
    return jsonify(json)

# Run
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000
    )
