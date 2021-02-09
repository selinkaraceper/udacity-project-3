import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
                      or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
                      or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('\nWould you like to see data for Chicago, New York, or Washington?\n')
        city=city.lower()
        if city not in ['chicago','new york','washington','ch','ny','wa']:
            print('Please choose between Chicago, New York , or Washington (\n')
        else:
             print('\nYou chose {}! You are going to explore its bikeshare data\n'.format(city))
             break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please enter the month you want the data analyzes (all,january,february...,june) :  ')
        month=month.lower()
        if month not in ['all','january','february','march','april','may','june']:
            print('You have not entered the month as either January, February, March, April, May,June or all.Please try enter again\n')
        else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Please enter the week you want the data analyzes (all,monday,tuesday,....,sunday): ')
        day=day.lower()
        if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            print('You have not entered the data as (all,monday,tuesday,wednesday,Thursday,friday, saturday or sunday).Please try enter again\n')
        else:
            break
    print('-'*40)
    return city, month, day
def load_data(city, month, day):
    """
    Loads data by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
        or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
        or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
# filter by day of week 
    if day != all:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print("day")
        
# filter by month
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month] 
        print("month")
        
        return df
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print(common_month)
    
    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
  
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)
    
    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)
    
    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)
    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    start_loc = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        start_loc = start_loc + 5
        print(df.iloc[start_loc:start_loc+5])


def user_stats(df, city):
    """Display statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Distribution for user types:")
    print(user_types)

    if city == 'chicago' or city == 'new_york_city':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print('Earliest birth from the given fitered data is: {}\n'.format(earliest_birth))
        most_recent_birth = df['Birth Year'].max()
        print('Most recent birth from the given fitered data is: {}\n'.format(most_recent_birth))
        most_common_birth = df['Birth Year'].mode()[0]
        print('Most common birth from the given fitered data is: {}\n'.format(most_common_birth)) 
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view 5 indivual trip data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            
if __name__ == "__main__":
    main()