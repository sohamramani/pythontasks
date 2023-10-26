import datetime


def get_time_from_user():
    try:
        time_from_user = input("Enter time in HH:MM:SS\n").split(":")
        if len(time_from_user) != 3:
            raise ValueError("Invalid input. Use HH:MM:SS format.")
        hours, minutes, seconds = map(int, time_from_user)   
        return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    except ValueError as e:
        print(f"Error: {e}")

def increase_time(time, unit, value):
    if unit == "H":
        return time + datetime.timedelta(hours=value)
    elif unit == "M":
        return time + datetime.timedelta(minutes=value)
    elif unit == "S":
        return time + datetime.timedelta(seconds=value)
    else:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")
  
def main():
        user_input = get_time_from_user()
        
        if user_input is None:
            return
        while True:
            print(
                "\n1. increase \n"
                "2. add\n"
                "3. difference:\n"
                "4. Quit\n"
            )
            operation = input("Choose operation: ")

            if operation == "1":
                unit = input("Enter unit (S for second)(M for minute)(H for hour): ").strip()
                value = int(input("Enter value to increase by: "))  
                result = increase_time(user_input, unit, value)
                print(f"Result: {result}")
            elif operation == "2":
                time2 = get_time_from_user()
                if time2 is not None:
                    result = user_input + time2
                    print(f"Result: {result}")

            elif operation == "3":
                time2 = get_time_from_user()
                if time2 is not None:
                    result = user_input - time2
                    print(f"Result: {result}")
            elif operation == "4":
                break
            else:
                print("Invalid operation. Use '1', '2', '3', or '4'.")

main()