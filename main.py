"""This is the main file for organizing the outside classes, HELLO"""
from convert_input_years_to_int import convert_input_years_to_int
from convert_years_to_ceremony_nums import convert_oscar_years_to_ceremony_numbers


def main():

    print("Hello! This is a program for performing statistical analysis on the Oscars, from 2010 to 2024")
    print("Please enter the interval of oscar years you would like to analyze in the form 'year1-year2'")
    print("For example, if you want to analyze from 2020 to 2024, type 2020-2024")
    print("Type a single year if you would like to proceed with just that award season")

    oscar_years = None
    count = 0
    while not oscar_years:
        string_of_oscar_years = input("Your response: ")
        oscar_years = convert_input_years_to_int(string_of_oscar_years)
        count += 1
        if count > 5:
            print("You made a mistake quite a few times now. Are you sure you read the instructions?")

    oscar_ceremony_numbers = convert_oscar_years_to_ceremony_numbers(oscar_years)

    # write_all_oscar_awards_to_file(oscar_award_number)
    # statistical_analysis_manager(oscar_ceremony_numbers)














if __name__ == "__main__":
    main()