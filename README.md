# Port Scanner

This is a simple web application that scans a specified IP address for open ports. It provides options to scan all ports, all TCP ports, all UDP ports, top 100 ports, a given range of ports, or specific comma-separated ports. The results can be downloaded as a CSV file.

## Features

<ul>
    <li>Scan all ports (1-65535)</li>
    <li>Scan top 100 common ports</li>
    <li>Scan a specific range of ports</li>
    <li>Scan specific comma-separated ports</li>
    <li>Automatically detects the protocol (TCP/UDP) based on the port</li>
    <li>Download scan results as a CSV file</li>
</ul>

## Installation

<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/port_scanner.git
cd port_scanner
        </code></pre>
    </li>
    <li>Install the required packages:
        <pre><code>pip install flask pandas
        </code></pre>
    </li>
    <li>Run the application:
        <pre><code>python port_scanner.py
        </code></pre>
    </li>
    <li>Open your browser and navigate to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</li>
</ol>

## Usage

<ol>
    <li><strong>IP Address</strong>: Enter the IP address you want to scan.</li>
    <li><strong>Ports</strong>: Select the port scanning option:
        <ul>
            <li><strong>All Ports</strong>: Scans all ports from 1 to 65535.</li>
            <li><strong>Top 100 Ports</strong>: Scans the top 100 common ports.</li>
            <li><strong>Range of Ports</strong>: Specify a range of ports (e.g., 20-80).</li>
            <li><strong>Specific Ports</strong>: Specify specific ports as a comma-separated list (e.g., 22,80,443).</li>
        </ul>
    </li>
    <li>Click the "Scan" button to start the scan.</li>
    <li>The results will display open ports along with their protocols.</li>
    <li>Click the "Download Report" button to download the scan results as a CSV file.</li>
</ol>

## Author

<p>Navjot Singh</p>
<p><a href="https://www.linkedin.com/in/njot/">LinkedIn</a></p>

## License

<p>This project is licensed under the MIT License.</p>
