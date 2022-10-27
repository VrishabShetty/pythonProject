class BrakeCalculator:
    _Gravity: float = 9.81
    _Friction: float = 0.7
    _PI = 3.14

    def __init__(self):
        self.bT: tuple = (0, 0)
        self.bF: tuple = (0, 0)
        self.wD: tuple = (0, 0)
        self.wT: float = 0


    # h: Height of center of gravity; l: Wheelbase; W: Mass

    def weight_transfer(self, h: int, l: float, w: int):
        self.wT = self._Friction * h * w / l

    def dynamic_load(self, front_s_load: float, rear_s_load: float):
        wFD = front_s_load + self.wT
        wRD = rear_s_load - self.wT

        self.wD = wFD, wRD

    def brakingForce(self):
        bFF = self._Friction * self.wD[0] * self._Gravity
        bFR = self._Friction * self.wD[1] * self._Gravity

        self.bF = bFF, bFR

    def brakingTorque(self, r_w: float):
        bTF = self.bF[0] * r_w
        bTR = self.bF[1] * r_w

        self.bT = bTF, bTR

    def pressure_master_cylinder(self, pedalRatio: float, fP: float, d: float, r: float):
        fMC = fP * pedalRatio
        pMC = fMC * 4 / (self._PI * d * d)
        fC = pMC * self._PI * r * r / 4
        fDisc = 0.35 * fC
        bT = fDisc * 2*r

        return pMC, fDisc, bT