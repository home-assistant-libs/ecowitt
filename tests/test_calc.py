"""Test for calulcated values from calc.py"""

from aioecowitt import calc

from .const import EASYWEATHER_DATA, GW2000A_DATA


def test_gw2000a_v2():
    """Test Calculated values from GW2000A_V2"""
    values = calc.weather_datapoints(GW2000A_DATA)

    assert values == {
        "PASSKEY": "345544D8EAF42E1B8824A86D8250D5A3",
        "baromabshpa": 944.2,
        "baromabsin": 27.885,
        "baromrelhpa": 944.2,
        "baromrelin": 27.885,
        "dateutc": "2022-07-15 15:26:14",
        "dewpointc": 13.0,
        "dewpointf": 55.3,
        "dewpointinc": 15.7,
        "dewpointinf": 60.2,
        "drain_piezo": 0.0,
        "drain_piezomm": 0.0,
        "erain_piezo": 0.0,
        "erain_piezomm": 0.0,
        "freq": "868M",
        "hrain_piezo": 0.0,
        "hrain_piezomm": 0.0,
        "humidity": 34,
        "humidityin": 53,
        "maxdailygust": 12.53,
        "maxdailygustkmh": 20.2,
        "model": "GW2000A",
        "mrain_piezo": 0.0,
        "mrain_piezomm": 0.0,
        "rrain_piezo": 0.0,
        "rrain_piezomm": 0.0,
        "runtime": "188738",
        "solarradiation": 530.62,
        "solarradiation_lux": 67167.1,
        "stationtype": "GW2000A_V2.1.5",
        "tempc": 30.6,
        "tempf": 87.08,
        "tempfeelsc": 29.7,
        "tempfeelsf": 85.5,
        "tempinc": 26.0,
        "tempinf": 78.8,
        "uv": 4,
        "wh90batt": 2.74,
        "windchillc": None,
        "windchillf": None,
        "winddir": 289,
        "windgustkmh": 5.0,
        "windgustmph": 3.13,
        "windspeedkmh": 4.7,
        "windspeedmph": 2.91,
        "wrain_piezo": 0.0,
        "wrain_piezomm": 0.0,
        "leaf_batt1": 1.78,
        "leafwetness_ch1": 14,
        "leak_ch1": 0,
        "leakbatt1": 100,
        "ws90_ver": "119",
        "ws90cap_volt": 5.4,
        "yrain_piezo": 0.0,
        "yrain_piezomm": 0.0,
    }


def test_easyweather():
    """Test EasyWeather station."""
    values = calc.weather_datapoints(EASYWEATHER_DATA)

    assert values == {
        "PASSKEY": "34271334ED1FADA6D8B988B14267E55D",
        "baromabshpa": 967.8,
        "baromabsin": 28.583,
        "baromrelhpa": 967.8,
        "baromrelin": 28.583,
        "dailyrainin": 0.0,
        "dailyrainmm": 0.0,
        "dateutc": "2020-05-04 14:34:26",
        "dewpointc": 3.9,
        "dewpointf": 39.1,
        "dewpointinc": 8.6,
        "dewpointinf": 47.4,
        "eventrainin": 0.0,
        "eventrainmm": 0.0,
        "freq": "915M",
        "humidity": 32,
        "humidityin": 33,
        "model": "HP3500_V1.6.2",
        "monthlyrainin": 0.079,
        "monthlyrainmm": 2.0,
        "rainratein": 0.0,
        "rainratemm": 0.0,
        "solarradiation": 205.52,
        "solarradiation_lux": 26015.2,
        "stationtype": "EasyWeatherV1.4.9",
        "tempc": 21.3,
        "tempf": 70.3,
        "tempfeelsc": 21.3,
        "tempfeelsf": 70.3,
        "tempinc": 26.1,
        "tempinf": 79.0,
        "uv": 2,
        "weeklyrainin": 0.079,
        "weeklyrainmm": 2.0,
        "windchillc": None,
        "windchillf": None,
        "winddir": 200,
        "windgustkmh": 1.8,
        "windgustmph": 1.1,
        "windspeedkmh": 0.6,
        "windspeedmph": 0.4,
        "yearlyrainin": 0.079,
        "yearlyrainmm": 2.0,
    }
