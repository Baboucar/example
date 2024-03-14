import pandas as pd


mydataset = {
  'cars': ["BMW", "Volvo", "Ford","BYD"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)