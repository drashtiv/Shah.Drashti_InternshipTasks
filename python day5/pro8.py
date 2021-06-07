class schemefun:
    def Scheme(self,scheme_id,scheme_name,outgoing_rate,message_charge):
        self.scheme_id=int(scheme_id)
        self.scheme_name=scheme_name
        self.outgoing_rate=(outgoing_rate)
        self.message_charge=(message_charge)
        print("scheme details ::")
        print("scheme_id :", scheme_id)
        print("scheme_name :", scheme_name)
        print("outgoing_rate :", outgoing_rate)
        print("message_charge :", message_charge)

class customer(schemefun):
    def data(self,cust_id,name,mobile_no):
        self.cust_id=int(cust_id)
        self.name=name
        self.mobile_no=int(mobile_no)
        print("")
        print("customer details ::")
        print("self.cust_id :", self.cust_id)
        print("self.name :", self.name)
        print("self.mobile_no :", self.mobile_no)

c=customer()

c.Scheme(1,"free",33,100000)
c.data(2,"drashti", 1234567890)