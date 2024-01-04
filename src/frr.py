import subprocess

class FRR:
    def __init__(self):
        # Initialize if needed
        pass

    def run_vtysh_command(self, command):
        # Run a vtysh command and return the output
        process = subprocess.Popen(["vtysh", "-c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            print(f"Error executing vtysh command: {error}")
            return f"Error executing vtysh command: {error}"
        return output.decode()

    def new_connection(self,conn_type):
        
        if conn_type == "AZ":
            my_asn = "65000"

            azure_vnet_gateway_ip = "237.84.2.178"
            
            self.run_vtysh_command(f'''
            conf t
            router bgp {asn}
            neighbor {azure_vnet_gateway_ip} remote-as 2



            ''')
            
            
            self.run_vtysh_command(f"show run")
        if conn_type == "RC":
            my_asn = "65000" # fixed - This machine's ASN

            siteb_vti = "237.84.2.178"
            siteb_asn = "65000"
            self.run_vtysh_command(f'''
            conf t
            router bgp {asn}
            neighbor {siteb_vti} remote-as {siteb_asn}

            ''')
            
    def delete_connection(self):
        # Delete a connection from the frr vtysh
        pass



