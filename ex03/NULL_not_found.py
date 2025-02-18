def NULL_not_found(obj: any) -> int:
    try:
        if obj is None:
            # print("Nothing: None <class 'NoneType'>")
            print("Nothing: None ",  type(obj))
        elif isinstance(obj, float) and obj != obj:  # Check for NaN
            print("Cheese: nan ", type(obj))
        elif obj == 0 and not isinstance(obj, bool):
            print("Zero: 0 ", type(obj))
        elif obj == '':
            print("Empty: ", type(obj))
        elif obj is False:
            print("Fake: ", type(obj))
        else:
            print("Type not Found")
            return 1
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1