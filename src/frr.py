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



