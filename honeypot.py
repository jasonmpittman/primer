

class Honeypot:
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.services = self.getServices()


    def getServices(self):
        #read in the config file for the service list
        f = open("config/services.csv", "r")
        services = f.read().split(",")
        return services
