import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(user_email):
    if validators.email(user_email) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()