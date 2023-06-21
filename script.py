import subprocess

def start_remote_shell():
    # Start the remote shell process
    process = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the IP address of the machine
    ip_address = subprocess.check_output(['hostname', '-I']).decode().strip()

    # Get the port number used for the remote shell
    port_number = process.stdout.readline().decode().strip()

    print("Remote shell started.")
    print(f"To connect from a different PC, run the following command:")
    print(f"ssh user@{ip_address} -p {port_number}")

if __name__ == "__main__":
    start_remote_shell()
