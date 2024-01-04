import os

class LibreSwanManager:
    def __init__(self, config_path='/etc/ipsec.conf'):
        self.config_path = config_path

    def add_connection(self, conn_name, conn_params):
        # Add a new connection to the ipsec.conf file
        with open(self.config_path, 'a') as file:
            file.write(f"\nconn {conn_name}\n")
            for param, value in conn_params.items():
                file.write(f"    {param}={value}\n")

    def delete_connection(self, conn_name):
        # Delete a connection from the ipsec.conf file
        with open(self.config_path, 'r') as file:
            lines = file.readlines()
        
        with open(self.config_path, 'w') as file:
            connection_block = False
            for line in lines:
                if line.startswith(f"conn {conn_name}"):
                    connection_block = True
                    continue
                if connection_block and line.startswith("    "):
                    continue
                connection_block = False
                file.write(line)

    def restart_ipsec_service(self):
        # Restart the IPSec service to apply changes
        os.system('sudo ipsec restart')

    # Additional methods as needed
