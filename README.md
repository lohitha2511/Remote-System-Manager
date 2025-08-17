# Remote System Management

Remote System Management is a Python-based client–server application that lets you remotely monitor and manage a system. It includes **video streaming** and **keylogging** over a network connection.

## Features

- **Server Mode**  
  Accepts client connections  
  Handles incoming video streams  
  Receives and logs keystrokes  

- **Client Mode**  
  Connects to a remote server  
  Streams the client’s screen/video  
  Captures and transmits keystrokes  

- **Threaded Design**  
  Video streaming and keylogging run in separate threads  
  Core server/client loop manages the main connection  

## Project Structure

    RemoteSystemManagement/
    │
    ├── client/
    │   ├── client.py            # Core client logic
    │   ├── features.py          # Client-side features (video, keylogger)
    │
    ├── server/
    │   ├── server.py            # Core server logic
    │   ├── handlers.py          # Server-side handlers (video, keylogger)
    │
    ├── main.py                  # Entry point (argparse CLI)
    
## Installation

1. **Clone the repository**

       git clone https://github.com/lohitha2511/Remote-System-Manager.git
       cd Remote-System-Manager

2. **Create a virtual environment (optional but recommended)**

       python3 -m venv venv
       source venv/bin/activate   # Linux/macOS
       venv\\Scripts\\activate      # Windows

3. **Install dependencies**

       pip install -r requirements.txt

## Usage

### Start the Server

       python main.py server --host 0.0.0.0 --port 5555 --video_port 9999 --keylogger_port 9998

- --host: Host to bind (default: 0.0.0.0)  
- --port: Main server port (default: 5555)  
- --video_port: Port for video streaming (default: 9999)  
- --keylogger_port: Port for keylogging (default: 9998)  

### Start the Client

       python main.py client --host <SERVER_IP> --port 5555 --video_port 9999 --keylogger_port 9998

Replace <SERVER_IP> with the server’s IP address.  

## Example

Start server:

       python main.py server

Start client (on another machine):

       python main.py client --host 192.168.1.10

## Security Considerations

- Operate only on **trusted networks** and with **explicit authorization**  
- Keylogging captures sensitive data; handle, store, and transmit logs securely
