def add_time(start, duration, weekday = ''):
    
    def find_hour(time):
        hour = ''
        for i in range(len(time)):
            if time[i] == ':':
                break
            hour += time[i]
        return int(hour)

    def find_minute(time):
        minute = ''
        for i in range(len(time)):
            if time[i] == ':':
                minute += time[i+1]
                minute += time[i+2]
        return int(minute)
    
    def find_daytime(time):
        am_pm = ''
        for i in range(len(time)):
            if time[i].isalpha():
                am_pm += time[i]
        return am_pm

    start_hour = find_hour(start)
    start_minute = find_minute(start)
    start_daytime = find_daytime(start)
    duration_hour = find_hour(duration)
    duration_minute = find_minute(duration)


    def adding_time(new_hour, new_minute, daytime, duration_hour, duration_minute, weekday):
        next_day = 0
        new_daytime = ''

        for i in range(duration_minute):
            new_minute += 1
            if new_minute == 60:
                new_hour += 1
                new_minute = 0
                if new_hour == 12:
                    if daytime == 'AM':
                        daytime = 'PM'
                    elif daytime == 'PM':
                        daytime = 'AM'
                        next_day += 1
        
        for i in range(duration_hour):
            new_hour += 1
            if new_hour == 12:
                if daytime == 'AM':
                    daytime = 'PM'
                elif daytime == 'PM':
                    daytime = 'AM'
                    next_day += 1
                    
            if new_hour == 13:
                new_hour = 1

        if weekday:
            weekday = weekday.capitalize()
            day = 0
            match weekday:
                case 'Monday':
                    day = 1
                case 'Tuesday':
                    day = 2
                case 'Wednesday':
                    day = 3
                case 'Thursday':
                    day = 4
                case 'Friday':
                    day = 5
                case 'Saturday':
                    day = 6
                case 'Sunday':
                    day = 7

            for i in range(next_day):
                day += 1
                if day == 8:
                    day = 1

            match day:
                case  1:
                    new_weekday = 'Monday'
                case 2:
                    new_weekday = 'Tuesday'
                case 3:
                    new_weekday = 'Wednesday'
                case 4:
                    new_weekday = 'Thursday'
                case 5:
                    new_weekday = 'Friday'
                case 6:
                    new_weekday = 'Saturday'
                case 7:
                    new_weekday = 'Sunday'
        
        if new_minute < 10:
            new_minute = '0'+str(new_minute)


        new_time = str(new_hour) + ':' + str(new_minute) + ' ' + daytime
        if weekday:
            new_time += ', ' + new_weekday
        if next_day == 1:
            new_time += ' (next day)'
        elif next_day > 1:
            new_time += f' ({next_day} days later)'

        return(new_time)

    new_time = adding_time(start_hour, start_minute, start_daytime, duration_hour, duration_minute, weekday)
    print(new_time)
    return new_time

add_time('11:55 AM', '12:07', 'Monday')