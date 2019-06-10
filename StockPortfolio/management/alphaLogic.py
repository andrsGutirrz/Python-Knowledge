
"""
 Welcome to Alpha Vantage! Your API key is: JGSKX4CM3I3QFT5D.
 Please record this API key for future access to Alpha Vantage.
 https://github.com/RomelTorres/alpha_vantage
"""

from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='JGSKX4CM3I3QFT5D')

def getInfo(value):
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_intraday(value)
    #Find a way to return data & meta_data
    #Join data, meta_data into a single object
    allData = {**meta_data,**data}
    #print(type(meta_data))
    return allData
