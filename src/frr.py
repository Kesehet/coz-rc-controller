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
        return output.decode()

    def new_connection(self,conn_type):
        variable = "conf t"
        if conn_type == "AZ":
            
            self.run_vtysh_command(f'''


            {variable}
            router bgp 1
            neighbor 10.1.1.1 remote-as 2


            ''')
            
            
            self.run_vtysh_command(f"show run")




