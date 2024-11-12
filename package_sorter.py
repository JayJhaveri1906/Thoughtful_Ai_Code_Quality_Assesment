class PackageSorter():
    def __init__(self):
        """
        Just initializing constant global vars
        """
        self.REF_BULKY_VOL = 1000000    # cm3
        self.REF_BULKY_INDIV_DIM = 150  # cm
        self.REF_HEAVY_WEIGHT = 20      # kg


    def isBulky(self, width, height, length):
        # Checking bulyness
        volume = width * height * length

        if (volume >= self.REF_BULKY_VOL) or \
        (width >= self.REF_BULKY_INDIV_DIM) or \
        (height >= self.REF_BULKY_INDIV_DIM) or \
        (length >= self.REF_BULKY_INDIV_DIM):
            return True
        
        return False
    

    def isHeavy(self, mass):
        # check heavyness
        if mass >= self.REF_HEAVY_WEIGHT:
            return True

        return False


    def sort(self, width, height, length, mass):
        """
        Returns one of {"STANDARD", "SPECIAL", "REJECTED"}
        based on w, h, l (in cms) and mass (in kg)

        ---
        :param float width: in cm
        :param float height: in cm
        :param float length: in cm
        :param float mass: in kg
        """

        # Handling invalid inputs
        try:
            width = float(width)
            height = float(height)
            length = float(length)
            mass = float(mass)
        except:
            return "REJECTED"   # invalid input



        package_bulky = self.isBulky(width, height, length)
        package_heavy = self.isHeavy(mass)
        
        if not package_bulky and not package_heavy:
            return "STANDARD"
        elif package_bulky and package_heavy:
            return "REJECTED"
        else:
            return "SPECIAL"


