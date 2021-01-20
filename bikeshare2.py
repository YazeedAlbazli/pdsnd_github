import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
        city = input("Please type a city among chicago, new york city, or washington:\n").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Invalid city. Please type a city among chicago, new york city, or washington.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:    
        month = input("Please type a month among the first six months you'd like to see or type 'all':\n").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("invalid month. Please type a month among the first six months or type 'all'.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please type which day of the week you'd like to see or type 'all':\n").lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("invalid day. Please type a day of the week or type 'all'.")
            continue
        else:
            break

    print('-'*40)
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
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The Most Common Month is:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The Most Common Day of Week is:", most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The Most Common Hour is:", most_common_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print("The Most commonly used Start Station is:", popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("The Most commonly used End Station is:", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combined_stations = df.groupby(['Start Station', 'End Station']).count()
    print("The most frequent combination of start station and end station trip is:", combined_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print("The Trip Time Total is:", travel_time_total) 
    
    # TO DO: display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print("The Travel Time Mean is:", travel_time_mean) 

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The User Types are:", user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("Here are the Gender Counts:", gender_counts)
    except KeyError:
        print("Unavailable data.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df["Birth Year"].min()
        print("The Earliest Birth Year is:", earliest_birth_year)
    except KeyError:
        print("Unavailable data.")

    try:
        latest_birth_year = df["Birth Year"].max()
        print("The Most Recent Birth Year is:", latest_birth_year)
    except KeyError:
        print("Unavailable data.")

    try:
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        print("The Most Common Year of Birth is:", common_birth_year)
    except KeyError:
        print("Unavailable data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    x = 1
    while True:
        raw_data = input('\nWould you like to see some raw data? Enter yes or no.\n').lower()
        if raw_data == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
