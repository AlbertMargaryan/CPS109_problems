def can_balance(items):
  for i, v in enumerate(items):
    listBefore = (items[:i])[::-1]
    listAfter = items[i+1:]
    
    beforeSum = 0
    afterSum = 0
    
    for j, a in enumerate(listBefore):
      beforeSum += a*(j+1)
    for k, b in enumerate(listAfter):
      afterSum += b*(k+1)

    if beforeSum == afterSum:
      return i
  return -1
