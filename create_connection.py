import socket

def main():
    s = socket.socket(socket.AD_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 5000
    s.connect((host, port))
    print('It works!')

if __name__ == '__main__':
    main()