try:
    print("outer try block")
    try:
        print('inner try block')
        print(10 / 0)
    except ZeroDivisionError:
        print('')
    finally:
        print('')
except:
    print('')
finally:
    print('')
