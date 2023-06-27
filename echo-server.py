from src.echo_server.app import app

HOST='0.0.0.0'
PORT=8080
DEBUG=True


if __name__ == '__main__':
    app.run(host=HOST,port=PORT,debug=DEBUG)