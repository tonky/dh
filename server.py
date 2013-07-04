from random import getrandbits
from flask import Flask
app = Flask(__name__)

print(">>>", app)


g = 2
prime = 7919
bits = 32

a = getrandbits(bits)
server_public = pow(g, a, prime)

client_public = 0

@app.route('/common_base')
def show_key():
    return str(prime)

@app.route('/public/<int:key>')
def set_client_public(key):
    global client_public

    client_public = key
    print("client public", client_public)
    return str(server_public)

@app.route("/check/<int:client_key>")
def check_common_secret(client_key):
    global client_public
    # b = getrandbits(bits)
    # B = pow(g, b, prime)

    common = pow(client_public, a, prime)

    print("sp, cp", server_public, client_public)

    if(common == client_key):
        return("Shared secret matches: %d" % common)

    return("No match!")

if __name__ == "__main__":
    app.run(debug=True)
