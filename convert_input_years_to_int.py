def convert_input_years_to_int(years):
    year_list = []
    if "-" in years:
        years = years.split("-")
        try:
            years[0] = int(years[0])
            years[1] = int(years[1])
        except ValueError:
            print("Your interval doesn't seem quite right, try again")
            return
        if years[0] < 2010 or years[0] > 2024 or years[1] < 2010 or years[1] > 2024:
            print("Invalid interval, try again")
            return
        if years[1] < years[0]:
            temp = years[0]
            years[0] = years[1]
            years[1] = temp
        while years[0] <= years[1]:
            year_list.append(years[0])
            years[0] += 1
    elif len(years) == 4:
        try:
            years = int(years)
            if years < 2010 or years > 2024:
                print("Invalid interval, try again")
                return
        except ValueError:
            print("Your year doesn't seem to be a number, try again")
            return
        year_list.append(years)
    else:
        print("Your year doesn't seem to be formatted correctly, try again.")
    return year_list
