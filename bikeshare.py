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
    city = input('Would you like to see data for Chicago, New York, or Washington? \n')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Would month ? January, February, March, April, May, or June?Enter integer number.\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.strftime("%B")
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)
    # TO DO: display the most common day of week
    df['day of week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day of week'].mode()[0]
    print('Most Popular day of the week:', popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
   """Displays statistics on the most popular stations and trip."""
   print('\nCalculating The Most Popular Stations and Trip...\n')
   start_time = time.time()
    # TO DO: display most commonly used start station
   popular_Start_Station=df['Start Station'].mode()[0]
   print('Most commonly used start station:',popular_Start_Station)

   # TO DO: display most commonly used end station
   popular_end_Station=df['End Station'].mode()[0]
   print('Most commonly used end station: ',popular_end_Station)

    # TO DO: display most frequent combination of start station and end station trip
   df['Combined Station']=df['Start Station']+' & '+df['End Station']
   popular_startend_station = df['Combined Station'].mode()[0]
   print('Most frequent start & end station: \n',popular_startend_station)

   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum(axis =0)
    print('Total travel time :', total_tt)

   # TO DO: display mean travel time
    mean_tt = df['Trip Duration'].mean(axis =0)
    print('mean travel time :',mean_tt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

   # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types:\n', user_types)
    # need if/else condition
   # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_type = df['Gender'].value_counts()
        print('\nCounts for each gender type:\n',gender_type)
    else:
        print("No Gender data available for Washington.")

    # need if condition
   # TO DO: Display earliest, most recent, and most common year of birth
    min_year=df['Birth Year'].min()
    print('\nEarliest year: ',min_year)
    max_year=df['Birth Year'].max()
    print('\nMost recent year: ',max_year)
    popular_year=df['Birth Year'].mode()[0]
    print('\nMost common year: \n',popular_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

    raw_data = input('\nWould you like to see 5 rows of raw data? y or n: ').lower()
    if raw_data != 'n':
        i = 0
        print(df.iloc[i:i+5])
        restart1 = input('\nWould you like to restart? Enter yes or no. \n')
        if restart1.lower() != 'yes':
            break
    else:
        restart2 = input('\nWould you like to restart? Enter yes or no. \n')
        if restart2.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
