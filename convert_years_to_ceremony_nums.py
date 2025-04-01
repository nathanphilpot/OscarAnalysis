years_to_ceremony_nums = {
    "2024": "97",
    "2023": "96",
    "2022": "95",
    "2021": "94",
    "2020": "93",
    "2019": "92",
    "2018": "91",
    "2017": "90",
    "2016": "89",
    "2015": "88",
    "2014": "87",
    "2013": "86",
    "2012": "85",
    "2011": "84",
    "2010": "83",
}

def convert_oscar_years_to_ceremony_numbers(years):
    new_years = []
    for year in years:
        new_years.append(int(years_to_ceremony_nums[str(year)]))
    return new_years