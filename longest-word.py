
def is_order(s):
   for k in range(len(s)-1):
      if s[k] > s[k+1]:
         return False
   return True

input_string = input("Please enter a string: ")
longest_length = 0
longest_string = ""

for i in range(len(input_string)+1):
   for j in range(i+2, len(input_string)+1):
      if is_order(input_string[i:j]):
         if len(input_string[i:j]) > longest_length:
            longest_string = input_string[i:j]
            longest_length = len(input_string[i:j])
         else:
            continue

print(longest_string)
