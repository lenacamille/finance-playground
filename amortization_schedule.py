class AmSchedule: 
    def __init__(self, P, N, i):
        """Initializes a fixed-rate amortization schedule, which assumes that the compounding convention is consistent with the periodicity of the payments
        Inputs: 
            P = principal loan amount
            i = periodic rate of interest stated in decimals, e.g. 0.02 = 2% (for monthly periodicity, divide the APR by 12)
            N = number of payments / the term of the loan
        Calculated:
            PMT = constant periodic payment
            I = total interest paid
        """
        self.N = N
        self.P = P
        self.i = i
        self.PMT = P * ( (1-(1+i)) / (1-((1+i)**N)) + i)
        self.I = 0
        monthly_balance = P
        for n in range(0,N):
            monthly_interest_paid = monthly_balance * i
            monthly_principal_paid = self.PMT - monthly_interest_paid
            self.I = self.I + monthly_interest_paid
            monthly_balance = monthly_balance - monthly_principal_paid
    
    def presentValue(self, discount_rate):
        """Takes as input a constant discount rate
        Generates compound discount factors which are used to calculate present value
        Returns present value stated as a % of the loan amount, e.g. 98.5 returned means 98.5% of P
        """
        CDF = 1
        PV = 0
        for n in range (0, self.N):
            CDF = CDF / (1+discount_rate)
            PV = PV + CDF * self.PMT
        PV_pts = PV / self.P *100
        return PV_pts

myAmSchedule = AmSchedule(235000,360,.0375/12)
print("PMT: "+str(myAmSchedule.PMT))
print("Total Interest Paid: "+str(myAmSchedule.I))
print("Present Value (5 pct discount rate): "+str(round(myAmSchedule.presentValue(.05/12),4)))