
#filled string
from turtle import right


filled_string = f'{"":*<50}'
print(filled_string)

#left justified
temp_string= "this is a string"
left_justified = f"{temp_string:-<50}"
print(left_justified)

#center justified
temp_string = "this is a string"
center_justified = f"{temp_string:-^50}"
print(center_justified)

#right justified
temp_string = "this is a string"
right_justified = f"{temp_string:$>50}"
print(right_justified)