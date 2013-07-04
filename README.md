install:

virtualenv dh
pip install -r requirements.txt



run:
python server.py



test:
python tests.py



common info:
check tests.py for example implementation

reference: http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

basically - 

1. get "/common_base" for common paint
2. compute mixture for public transmission using pow(2, client_secret, common_paint)
3. send mixture to server and receive server's one in response
4. compute common secret via pow(server_mixture, client_secret, common_paint)
5.(optional) get /check/<common secret> to see if server and client secrets match
