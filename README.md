## Home task. Work with date, time, and advanced work with strings

#### Task Description

**Task 1**

Create a function **`get_days_from_today(date)`**, which calculates the number of days between the specified date and the current date.

**Requirements for the task:**

- The function takes one parameter: **`date`** — a string representing the date in the format `'YYYY-MM-DD'` (for example, `'2020-10-09'`).
- The function returns an integer that indicates the number of days from the specified date to the current one. If the specified date is later than the current one, the result should be negative.
- Only days should be considered in the calculations, ignoring the time (hours, minutes, seconds).
- Use the **`datetime`** module in Python for working with dates.

**Recommendations for execution:**

1. Import the **`datetime`** module.
2. Convert the date string in the **`'YYYY-MM-DD'`** format to a **`datetime`** object.
3. Get the current date using **`datetime.today()`**.
4. Calculate the difference between the current date and the specified date.
5. Return the difference in days as an integer.

>[!TIP]
>If today is May 5, 2021, calling **`get_days_from_today("2021-10-09")`** should return **`157`**, as October 9, 2021, is 157 days after May 5, 2021.

**Task 2**

To win the main prize in the lottery, several numbers on the lottery ticket must match the numbers randomly drawn within a certain range during the next draw. For example, you need to guess six numbers from 1 to 49 or five numbers from 1 to 36, and so on.

You need to write a function **`get_numbers_ticket(min, max, quantity)`**, which will help generate a set of unique random numbers for such lotteries. It will return a random set of numbers within the specified parameters, with all random numbers in the set being unique.

**Requirements for the task:**

- Function parameters:
  - **`min`** - the minimum possible number in the set (no less than `1`).
  - **`max`** - the maximum possible number in the set (no more than `1000`).
  - **`quantity`** - the number of numbers to select (values between **`min`** and **`max`**).
- The function generates the specified number of unique numbers within the specified range.
- The function returns a list of randomly selected, sorted numbers. Numbers in the set should not repeat. If the parameters do not meet the specified constraints, the function should return an empty list.

**Recommendations for execution:**

1. Ensure that the input parameters meet the specified constraints.
2. Use the **`random`** module to generate random numbers.
3. Use a set or another mechanism to ensure the uniqueness of numbers.
4. Remember that the **`get_numbers_ticket`** function returns a sorted list of unique numbers.

>[!TIP]
>Suppose you need to select `6` unique numbers for a lottery ticket, where numbers should be in the range from `1` to `49`. You can use your function like this:
>```
>lottery_numbers = get_numbers_ticket(1, 49, 6)
>print("Your lottery numbers:", lottery_numbers)
>```
>This code calls the **`get_numbers_ticket`** function with parameters **`min=1`**, **`max=49`**, and **`quantity=6`**. As a result, you'll get a list of 6 random, unique, and sorted numbers, for example, **`[4, 15, 23, 28, 37, 45]`**. Each time you call the function, you'll get a different set of numbers.

**Task 3**

Within your company, an active marketing campaign is being conducted through SMS broadcasts. To do this, you collect customer phone numbers from the database, but often encounter the issue that the numbers are in different formats. For example:
```
" +38(050)123-32-34"
" 0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11 "
```
Your SMS broadcast service can efficiently send messages only when phone numbers are presented in the correct format. Therefore, you need a function that automatically normalizes phone numbers to the required format, removing all unnecessary characters and adding the country's international code if necessary.

Develop the function **`normalize_phone(phone_number)`** that normalizes phone numbers to a standard format, leaving only digits and the `'+'` symbol at the beginning. The function takes one argument - a string with the phone number in any format and converts it to the standard format, leaving only digits and the `'+'` symbol. If the number does not contain an international code, the function automatically adds the `'+38'` code (for Ukraine). This ensures that all numbers will be suitable for SMS sending.

**Requirements for the task:**

- The function parameter **`phone_number`** is a string with the phone number in various formats.
- The function removes all characters except digits and the `'+'` symbol.
- If the international code is absent, the function adds the `'+38'` code. This accounts for cases where the number starts with `'380'` (only `'+'` is added) and when the number starts without a code (`'+38'` is added).
- The function returns the normalized phone number as a string.

**Recommendations for execution:**

1. Use the **`re`** module for regular expressions to remove unnecessary characters.
2. Check if the number starts with `'+'`, and adjust the prefix accordingly.
3. Remove all characters except digits and `'+'` from the phone number.
4. Don't forget to return the normalized phone number from the function.

>[!TIP]
>```
>raw_numbers = [
>    "067\\t123 4567",
>    "(095) 234-5678\\n",
>    "+380 44 123 4567",
>    "380501234567",
>    "    +38(050)123-32-34",
>    "     0503451234",
>    "(050)8889900",
>    "38050-111-22-22",
>    "38050 111 22 11   ",
>]
>
>sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
>print("Normalized phone numbers for SMS broadcast:", sanitized_numbers)
>```
>As a result, you should get a list of numbers in the standard format, ready for use in SMS broadcasting.
>```
>Normalized phone numbers for SMS broadcast:
>['+380671234567', '+380952345678', '+380441234567',
>'+380501234567', '+380501233234', '+380503451234',
>'+380508889900', '+380501112222', '+380501112211']
>```

**Task 4**

Within your organization, you are responsible for organizing birthday greetings for colleagues. To optimize this process, you need to create a function **`get_upcoming_birthdays`**, which will help you determine who needs to be greeted among colleagues. The function should return a list of all colleagues whose birthdays are within the next 7 days, including the current day.

You have a list of **`users`**, each element of which contains information about the user's name and their birthday. Since colleagues' birthdays may fall on weekends, your function should also consider this and move the greeting date to the next working day if necessary.

**Requirements for the task:**

- The function parameter **`users`** is a list of dictionaries, where each dictionary contains the keys **`name`** (user's name, string) and **`birthday`** (birthday, string in the format 'year.month.day').
- The function should determine whose birthdays fall within the next 7 days, including the current day. If the birthday falls on a weekend, the greeting date should be moved to the next Monday.
- The function returns a list of dictionaries, where each dictionary contains information about the user (key **`name`**) and the congratulation date (key **`congratulation_date`**, data in the format string 'year.month.day').

**Recommendations for execution:**

1. Assume that you have received a list of **`users`**, where each dictionary contains **`name`** (user's name) and **`birthday`** (date of birth in the format string 'year.month.day'). You should convert the birth dates from strings to **`datetime`** objects. Convert the birth date from a string to a **`datetime object`** - `datetime.strptime(user["birthday"], "%Y.%m.%d").date()`. Since only the **`date`** is needed (without time), use .date() to get only the date.
2. Determine the current system date using **`datetime.today().date()`**.
3. Iterate through the list of **`users`** and analyze the birthdays of each user (**`for user in users:`**).
4. Check if the birthday has already passed this year (**`if birthday_this_year < today`**). If so, consider the date for the next year.
5. Determine the difference between the birthday and the current date to determine birthdays for the next week.
6. Check if the birthday falls on a weekend. If so, move the greeting date to the next Monday.
7. Create a data structure that stores the user's name and the corresponding congratulation date if the birthday occurs within the next week.
8. Output the collected data as a list of dictionaries with user names and congratulation dates.

>[!TIP]
>Suppose you have a list of **`users`**:
>```
>users = [
>    {"name": "John Doe", "birthday": "1985.01.23"},
>    {"name": "Jane Smith", "birthday": "1990.01.27"}
>]
>```
>Using the **`get_upcoming_birthdays`** function:
>```
>upcoming_birthdays = get_upcoming_birthdays(users)
>print("List of greetings for this week:", upcoming_birthdays)
>```
>If today is `2024.01.22`, the result could be:
>```
>[
>   {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
>    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
>]
>```
>This list contains information about whom and when to greet with a birthday.
