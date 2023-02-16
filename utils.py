import json
import requests


class CurrenciesConverter:
    def convert(self, inputCurrency: str, outputCurrency: str, amount: float) -> float:
        todayCourses = self.__get_today_courses()
        convertAmount =  \
            (todayCourses['Valute'][inputCurrency]['Value'] * todayCourses['Valute'][outputCurrency]['Nominal']) / \
            (todayCourses['Valute'][outputCurrency]['Value'] * todayCourses['Valute'][inputCurrency]['Nominal']) * \
            amount

        return round(convertAmount, 2)

    @staticmethod
    def __get_today_courses() -> dict:
        r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        todayCourses = json.loads(r.content)
        todayCourses["Valute"]["RUB"] = {
            "ID": "1",
            "NumCode": "1",
            "CharCode": "RU",
            "Name": "Рубль",
            "Value": 1,
            "Nominal": 1
        }

        return todayCourses


c = CurrenciesConverter()
