class Weather():
    '''
    The Weather class takes a non-empty string for the description
    and a floating point number for the temperature
    '''
    def __init__(self, city, desc, temp):
        self.city = city
        self.desc = desc # make use of the setter methods
        self.temp = temp
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        if type(new_city) == str and len(new_city)>2:
            self.__city = new_city
        else:
            self.__city = 'Athlone'
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        if type(new_desc) == str and new_desc != '':
            self.__desc = new_desc
        else:
            self.__desc = 'fine'
    @property        
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        if type(new_temp) == int or type(new_temp) == float:
            self.__temp = new_temp
        else:
            self.__temp = 12 # a reasonable default
    def __str__(self):
        # output a nicely formatted weather report
        report  = f'The weather in {self.city} is {self.desc} at {self.temp}C'
        return report


if __name__ == '__main__':
    # exercise this module
    w_gen = Weather('Genoa', 'rainy', 9.04)
    w_gal = Weather('Galway', 'windy', 6.70)
    w_kt  = Weather('Kingston', 'sunny', 27.98)
   
    print(w_gen)
    print(w_gal)
    print(w_kt)

    w_default = Weather(False, [], ()) # wrong data types so should fall back to the defaults
    print(w_default)
