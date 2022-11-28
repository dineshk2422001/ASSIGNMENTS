def str_ul(s):
    de = {'upper_case':0, 'lower_case':0}
    for c in s:
        if c.isupper():
            de['upper_case']+=1
        elif c.islower():
            de['lower_case']+=1
        else:
            pass
    print(f"sample string :", s)
    print("no of upper case character: ", de['upper_case'])
    print("no of lower case character: ", de['lower_case'])

str_ul('The quick Brow Fox')
