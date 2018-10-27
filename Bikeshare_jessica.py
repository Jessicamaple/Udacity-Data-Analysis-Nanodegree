
# coding: utf-8

# In[1]:


# %load bikeshare.py
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new-york-city.csv',
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
    
    valid_city = ["chicago", "new york city", "washington"]
    valid_month = ["all", "january", "february", "march", "april", "may", "june"]
    valid_day_of_week = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_city = input("Please choose the city you want to explore among chicago, new york city and washington. ").lower()
    
    while input_city not in valid_city:
        print("Please input a valid city.")
        input_city = input().lower()
    
    while input_city in valid_city:
        city = input_city
        break
                         
    # TO DO: get user input for month (all, january, february, ... , june)
    input_month = input("Which month do you want to explore? ").lower()
                                        
    while input_month not in valid_month:
        print("Please input a valid month.")
        input_month = input().lower()
    
    while input_month in valid_month:
        month = input_month
        break
                         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    input_day_of_week = input("Which day of week do you want to explore? ").lower()
                                        
    while input_day_of_week not in valid_day_of_week:
        print("Please input a valid day of week.")
        input_day_of_week = input().lower()
    
    while input_day_of_week in valid_day_of_week:
        day = input_day_of_week
        break

    print('-'*40)
    print(city, month, day)
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
    # load data file into a dataframe and add "Gender" and "Birth Year" columns to washington filling with 'na' 
    if city == "washington":
        df = pd.read_csv(CITY_DATA[city])    
        df['Gender'] = 'na'
        df['Birth Year'] = 'na'
    else:
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    df['day of week'] = df['Start Time'].dt.day
    popular_day_of_week = df['day of week'].mode()[0]
    print('Most Popular Start Day Of Week:', popular_day_of_week)

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
    common_start_station = df['Start Station'].mode()[0] 
    print('Most commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0] 
    print('Most commonly used end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('Most fequent combination of start and end station trip:',common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time: {} sec.".format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean travel time: {} sec.".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
        
    """Displays statistics on bikeshare users."""
            
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types: ",user_types)

    # TO DO: Display counts of gender
    genders = df['Gender'].value_counts()
    print("Counts of genders: ",genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_yob = df['Birth Year'].min()
    print("The earliest year of birth: ", earliest_yob)

    recent_yob = df['Birth Year'].max()
    print("The most recent year of birth: ", recent_yob)

    common_yob= df['Birth Year'].mode()[0]
    print("The most common year of birth: ", common_yob)

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

