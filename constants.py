import enum

class Province(enum.Enum):
    AB = 'AB'
    ON = 'ON'
    QC = 'QC'
    MI = 'MI'
    
    @staticmethod
    def all_members():
        return set([name for name, _ in Province.__members__.items()])
    
    
ProvinceTax = {
    Province.AB : 0.05,
    Province.ON : 0.13,
    Province.QC : 0.14975,
    Province.MI : 0.06
}

OrderDiscount = {
    0: 0.00,
    1000: 0.03,
    5000: 0.05,
    7000: 0.07,
    10000: 0.10,
}