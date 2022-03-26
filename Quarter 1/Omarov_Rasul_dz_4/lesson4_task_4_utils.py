import requests
from datetime import date

def currency_rates(valute):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    valute_index = response.text.find(valute.upper())
    day, month, year = response.text[60:70].split('.')
    valute_date = date(int(year), int(month), int(day))
    if valute_index != -1:
        value_index_start = response.text.find('<Value>', valute_index)
        value_index_end = response.text.find('</Value>', valute_index)
        value = response.text[value_index_start+7: value_index_end]
        return f"По состоянию на {valute_date} курс {valute.upper()} по отношению к рублю = {float(value.replace(',', '.'))}"
    else:
        return None

