# Solved by: Ali Helmi
# Email: ahelmi365@gmail.com
# Program: Programming for Data Science Nanodegree
# By: UDACITY

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york city': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    list_city = ['chicago', 'new york city', 'washington']
    city = ''
    while city not in list_city:
        city = input("Please enter name of the city ('chicago', 'new york city', 'washington') to analyze:\n")
        city = city.lower()

    print()
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    month = ''

    while month not in month_list and month != "all":
        month = input("Please enter name of the month (from january to june) to filter by, or (all) to apply no month filter:\n")
        month = month.lower()

    print()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    day= ''
    while day not in day_list and day != "all":
        day = input("Please enter name of the day of week to filter by, or (all) to apply no day filter:\n")
        day = day.lower()

    print('-'*60)
    print()
    print()
    print()
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month:
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week:
    # extract month from the Start Time column to create an month column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # find the most popular day_of_week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day_of_week)

    # TO DO: display the most common start hour:
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    print()
    print()
    print()


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)
    print()

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print("Most frequent combination of startstation end station trip:")
    print("    1.", popular_start_end_station[0])
    print("    2.", popular_start_end_station[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    print()
    print()
    print()


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = int(df['Trip Duration'].sum())
    print("Total travel time in seconds:", total_time)
    print("Total travel time in minutes:", int(total_time // 60))
    if total_time >= 3600:
        print("Total travel time in hours:", int((total_time // 60)//60))
    print()

    # TO DO: display mean travel time
    total_time = int(df['Trip Duration'].mean())
    print("Mean travel time in seconds:", total_time)
    print("Mean travel time in minutes:", int(total_time // 60))
    if total_time >= 3600:
        print("Mean travel time in hours:", int((total_time // 60)//60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    print()
    print()
    print()


def user_stats(df, city):
    """Displays statistics on bikeshare users.
        Args:
        1. dataframe
        2. City name, because data of washington is different than data in chicago and New York city.
        Washington does not have two columns (Gender and Birth Year)
        So we will not calc some stats here if the city is Washington
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types:
    df['Number of Users'] = 1  # this new column to be used in groupby()
    count_user_type = df.groupby(['User Type']).count()[['Number of Users']]
    print(count_user_type)
    print()

    # TO DO: Display counts of gender
    # To get the city entered by the user
    if city != "washington":  # Beacuse washington doesn't have Gender nor Birth Year
        count_gender = df.groupby(['Gender']).count()[['Number of Users']]
        print(count_gender)
        print()

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth:", int(df['Birth Year'].min()))
        print("The most recent year of birth:", int(df['Birth Year'].max()))
        print("The most common year of birth:", int(df['Birth Year'].mode()[0]))
        print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    print()
    print()
    print()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print()
            print()
            print()
            break


if __name__ == "__main__":
	main()
