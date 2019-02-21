if __name__ == '__main__':
    text = input()
    if text == text[::-1]:
        print("This word is Palindrome, hooray!")
    else:
        print("This is not a palindrome, sorry")
