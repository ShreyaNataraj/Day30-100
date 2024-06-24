def missing_number(arr,n):
  total_sum = n*(n+1)//2
  arr_sum = sum(arr)
  missing = total_sum-arr_sum
  return missing
print(missing_number([1,2,3,4,6],6))