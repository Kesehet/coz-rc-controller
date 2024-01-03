from .database import DB
from .frr import FRR

class Connection:
    def __init__(self, customer_short_name, region, asn):
        self.DB = DB("connection_db.json")

        self.customer_short_name = customer_short_name
        self.region = region

        self.vti_ip = None
        
        self.asn = asn
        self.type = "VPN"
        
    def getConnection(self):
        return {
            "key": "name",
            "value": self.name(),
            "customer_short_name": self.customer_short_name,
            "region": self.region,
            "asn": self.asn,
            "type": self.type
        }
    
    def start(self):
        successful = True
        #FRR Config write
        print(FRR.run_vtysh_command(f"show run"))
        #LibreSwan Config write
        if(successful):
            self.DB.insert_row(self.getConnection())
            return "Connected"
        return "Connection Failed"

    def stop(self):
        successful = True
        #FRR Config write
        #LibreSwan Config write
        if(successful):
            self.DB.delete_row(self.getConnection())
            return "Disconnected"
        return "Disconnected"

# __________________________________________________ NAME ___________________________________________________

    def name(self):
        self.name = f"{self.region}-{self.customer_short_name}"
        return self.name

    def vti_name(self):
        self.vti_name = f"{self.region}-{self.customer_short_name}-vti"
        return self.vti_name

# ____________________________________________________ PUBLIC IP ADDRESSS ___________________________________________________
    def set_public_ip_address(self, public_ip_address):
        self.public_ip_address = public_ip_address
        return public_ip_address

    def get_public_ip_address(self):
        return self.public_ip_address

# ____________________________________________________ PRIVATE IP ADDRESSS ___________________________________________________

    def set_private_ip_address(self, private_ip_address):
        self.private_ip_address = private_ip_address
        return private_ip_address

    def get_private_ip_address(self):
        return self.private_ip_address

# ____________________________________________________ VTI IP ADDRESSS __________________________________

    def set_vti_ip(self, vti_ip):
        self.vti_ip = vti_ip

    def get_vti_ip(self):
        return self.vti_ip

