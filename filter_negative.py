

numbs = [34, 55, 65, -7, 90, -43]
positive_numbs =[]
negative_numbs = []

for index in numbs:
  #  positive_numbs = sorted(numbs, key=lambda x: x >= 0) 
  if index >= 0:
    positive_numbs.append(index)
  elif index < 0:
    negative_numbs.append(index)
    



print(positive_numbs)
print(negative_numbs)