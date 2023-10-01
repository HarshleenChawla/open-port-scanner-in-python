import socket

# Function to scan a target host for open ports
def scan_ports(target_host, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt (adjust as needed)
            socket.setdefaulttimeout(1)

            # Attempt to connect to the target host and port
            result = sock.connect_ex((target_host, port))

            if result == 0:
                open_ports.append(port)

            # Close the socket
            sock.close()

        except KeyboardInterrupt:
            print("Scanning stopped by user.")
            return open_ports

        except socket.error:
            pass

    return open_ports

def main():
    target_host = input("Enter the target host or IP address: ")
    port_range_start = int(input("Enter the start of the port range: "))
    port_range_end = int(input("Enter the end of the port range: "))

    port_range = (port_range_start, port_range_end)

    open_ports = scan_ports(target_host, port_range)

    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_host}.")

if __name__ == "__main__":
    main()
