import re

#MM-DD-YYYY to DD-MM-YYYY, preserve file extension

def rename(original):

  #check input validity
  try:
    str(original)
  except (ValueError, TypeError, AttributeError):
    return("Please provide filename in convetional form of MM-DD-YYYY.extension")

  #defining regex
  object = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)\.(\w+)')

  result = object.search(original)

  #checking if no matches
  print(result)
  if result == [] or result == None:
    return("Please provide filename in convetional form of MM-DD-YYYY.extension")

  #assembling reformated filename
  new_file_name = result.group(2) + "-"+ result.group(1) + "-" + result.group(3) + "." + result.group(4)

  return new_file_name

#code for testing
new = rename('10-31-2019.jpg')
print(new)

new2 = rename('12-24-2018.png')
print(new2)

while True:
  print("Provide file name")
  x = input()
  y = rename(x)
  print(y)