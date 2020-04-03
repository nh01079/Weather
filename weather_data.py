#weather_data.py
#   Handling of the weather data
#   Two classess
#   1. WeatherData ==> data set access
#   2. WeatherDataItem ==> single data data access

class WeatherData:
    '''To access the csv file constaining WeatherData'''
    def __init__(self):
        "To perform read operation on the csv file"
        self.filename = input("CSV file location\n")
        self.nDays = 0
        self.dataItems = []
        self.dataSize  = 0
        "load the data"
        self.load(self.filename)
        self.dataSize = self.size()

    def load(self, filename):
        "Takes a string(file_name) as a parameter"
        try:
            onfile = open(filename, mode = 'r')
        except:
            print("No such filename!")
            self.__init__()
        # skip the first line
        onfile.readline()
        for line in onfile:
            param = line.split(',')
            try:
                if len(param) == 11:
                    dataItem = WeatherDataItem(param)
                    self.dataItems.append(dataItem)
                else:
                    # not enough input arguments
                    raise IndexError
            except (IndexError, ValueError):
                print("Data error!")
                onfile.close()
                self.__init__()
        onfile.close()

    def get_data(self, nDays):
        "The number of days of data to return"
        return self.dataItems[self.dataSize-nDays:]

    def size(self):
        "Size of self.dataItems"
        return len(self.dataItems)


class WeatherDataItem:
    "To store the weather data of a single day"
    def __init__(self, param):
        "Transfer the list of data into instance variables."
        self.date = param[0]
        self.temp = list(map(float, param[1:3]))
        self.rain = float(param[3])
        self.sun  = float(param[4])
        self.humid = float(param[5])
        self.cloud = float(param[6])
        self.wind  = [param[7]] + list(map(float,param[8:10]))
        self.pressure = float(param[10])

def main():
    test_data = WeatherData()
    sample = test_data.get_data(5)
    pass

if __name__ == '__main__':
    main()
