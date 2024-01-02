class Connection:
    def __init__(self, subscription, resource_group, customer_short_name, region, vnet_name, asn):
        self.subscription = subscription
        self.resource_group = resource_group
        self.customer_short_name = customer_short_name
        self.region = region
        self.virtual_network = vnet_name
        self.asn = asn

        # Static fields
        self.gateway_type = "VPN"
        self.sku = "VpnGw1"
        self.generation = "Generation1"
        self.active_active = False
        self.enable_bgp = True
        
    def getConnection(self):
        return {
            "subscription": self.subscription,
            "resource_group": self.resource_group,
            "customer_short_name": self.customer_short_name,
            "region": self.region,
            "virtual_network": self.virtual_network,
            "asn": self.asn,
            "gateway_type": self.gateway_type,
            "sku": self.sku,
            "generation": self.generation,
            "active_active": self.active_active,
            "enable_bgp": self.enable_bgp
        }

    def name(self):
        return f"{self.region}-{self.customer_short_name}"

    def set_public_ip_address(self, public_ip_address):
        self.public_ip_address = public_ip_address
        return public_ip_address

    def get_public_ip_address(self):
        return self.public_ip_address

    # The following methods are placeholders for actual logic to get these values
    def subscription_value(self):
        return self.subscription

    def resource_group_value(self):
        return self.resource_group

    def region_value(self):
        return self.region

    def virtual_network_value(self):
        return self.virtual_network


