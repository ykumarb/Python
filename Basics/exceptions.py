# Raise exceptions
# raise Exception('Exception is raised')

try:
    x = 7/0
except Exception as e:
    print(e)
finally:
    print("finally")