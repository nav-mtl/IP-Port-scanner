import socket
from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

# Common ports and their protocols
COMMON_PORTS = {
    'tcp': [20, 21, 22, 23, 25, 53, 80, 110, 119, 143, 161, 194, 443, 465, 587, 993, 995, 3389],
    'udp': [53, 67, 68, 69, 123, 161, 162, 500, 514, 520, 631, 1434]
}

# Function to scan a single port
def scan_port(ip, port, protocol):
    try:
        if protocol == 'tcp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False

# Function to scan multiple ports and return the open ones
def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        for protocol in ['tcp', 'udp']:
            if port in COMMON_PORTS[protocol] and scan_port(ip, port, protocol):
                open_ports.append((port, protocol))
                break
    return open_ports

# Function to parse port ranges or comma-separated ports
def parse_ports(ports_string):
    if '-' in ports_string:
        start, end = map(int, ports_string.split('-'))
        return list(range(start, end + 1))
    return list(map(int, ports_string.split(',')))

# Function to get the top 100 common ports
def get_top_100_ports():
    return list(range(1, 101))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form['ip']
        ports_option = request.form['ports_option']
        
        # Determine which ports to scan based on user input
        if ports_option == 'all':
            ports = range(1, 65536)
        elif ports_option == 'top100':
            ports = get_top_100_ports()
        elif ports_option == 'range':
            ports = parse_ports(request.form['range_ports'])
        elif ports_option == 'specific':
            ports = parse_ports(request.form['specific_ports'])
        else:
            ports = range(1, 1024)  # Default to scanning well-known ports if no option is specified

        open_ports = scan_ports(ip, ports)
        
        # Save results to a CSV file
        report_filename = 'port_scan_report.csv'
        df = pd.DataFrame(open_ports, columns=['Port', 'Protocol'])
        df.to_csv(report_filename, index=False)
        
        return render_template('index.html', open_ports=open_ports, ip=ip, report_filename=report_filename)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
