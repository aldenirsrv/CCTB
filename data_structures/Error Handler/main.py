import time
products = [12,34,23,56,73,22,19,89]

# for i in range(20):
#     if i == 15:
#         try:
#             print(i/2)
#         except:
#             print("An error ocorred.{e}")
#     print(f"{i} is the  current number")
#     time.sleep(1)

def errorhandlerTest():
    try:
        for i in range(20):
            if i == 15:
                print(i/0)
            print(f"\n{i+1} is the  current number")
            print(f"The price of {i+1} product is: {products[i]}")
            time.sleep(0.5)
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError:  {zde}")
    except IndexError as ie:
        print(f"IndexError:  {ie}")
    except Exception as e:
        print(f"Exception:  {e}")
    finally:
        print("This will be executed anyway")
errorhandlerTest()