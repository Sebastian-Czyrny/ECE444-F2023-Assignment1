class Utils:

    # take in a number (int) and return that number reversed (int)
    def reversed(self, num):
        # check if input was an int
        if type(num) != int:
            return None

        # convert number to string if not already
        num_str = str(num)

        # reverse the string
        num_str_rev = num_str[::-1]

        # convert back to int and return
        return int(num_str_rev)

    
    # take in a number (int) and then return it in base 2 AND base 8
    def formatter(self, num):
        # check if input was an int
        if type(num) != int:
            return None
    
        # convert to base 2
        num_base_2 = self.__baseX(num, base=2)

        # convert to baee 8
        num_base_8 = self.__baseX(num, base=8)

        # return base 2 and 8 representations
        return num_base_2, num_base_8
    
    def __baseX(self,num, base=10):
            num_basex_str = ""
            while num != 0:
                 num_basex_str = str(num % base) +  num_basex_str  
                 num = num // base
            return int(num_basex_str)
                 

        
