import requests


def currency_rates(valute):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    valute_index = response.text.find(valute.upper())
    if valute_index != -1:
        value_index_start = response.text.find('<Value>', valute_index)
        value_index_end = response.text.find('</Value>', valute_index)
        value = response.text[value_index_start+7: value_index_end]
        return f"Курс {valute.upper()} по отношению к рублю = {float(value.replace(',', '.'))}"
    else:
        return None

print(currency_rates('usd'))