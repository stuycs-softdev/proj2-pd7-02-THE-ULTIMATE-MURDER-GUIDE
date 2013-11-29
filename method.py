def temperature(a):
    temperature = a[a.find('temp_f'): a.find('temp_c')]
    temperature = "Temperature now = " + temperature[8:12]
    return temperature

def winds(a):
    wind = a[a.find('wind_string'): (a.find ('"wind_dir') - 5)]
    wind = "Winds today = " + wind[14:]
    return wind

def rainfall (a):
    rain = a[a.find('precip_today_string'): (a.find('precip_today_in') - 6)]
    rain = "Rainfall today = " + rain[22:]
    return rain
