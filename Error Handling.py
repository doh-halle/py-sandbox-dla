try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Your age cannot be 0')
except ValueError:
    print('Invalid value, please enter a number')