"""I have a cat and a dog.
I got them at the same time as kitten/puppy. That was humanYears years ago.
Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:
humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""


def human_years_cat_years_dog_years(human_years):
# Your code here   
  CAT_YEAR_FOR_FIRST_YEAR = 15
  DOG_YEAR_FOR_FIRST_YEAR = 15
  CAT_YEAR_FOR_SECOND_YEAR = 9
  DOG_YEAR_FOR_SECOND_YEAR = 9
  CAT_YEAR_FOR_THIRD_YEAR_AND_SO_ON = 4
  DOG_YEAR_FOR_THIRD_YEAR_AND_SO_ON = 5
  
  cat_years = 0
  dog_years = 0    
  
  if human_years == 1:
      cat_years = CAT_YEAR_FOR_FIRST_YEAR
      dog_years = DOG_YEAR_FOR_FIRST_YEAR
  
      return [human_years, cat_years, dog_years]
  
  if human_years > 1:
      cat_years = CAT_YEAR_FOR_FIRST_YEAR + CAT_YEAR_FOR_SECOND_YEAR
      dog_years = DOG_YEAR_FOR_FIRST_YEAR + DOG_YEAR_FOR_SECOND_YEAR
  
  # for _ in range(2, human_years):
  #     cat_years += CAT_YEAR_FOR_THIRD_YEAR_AND_SO_ON
  #     dog_years += DOG_YEAR_FOR_THIRD_YEAR_AND_SO_ON

  cat_years += CAT_YEAR_FOR_THIRD_YEAR_AND_SO_ON * (human_years - 2)
  dog_years += DOG_YEAR_FOR_THIRD_YEAR_AND_SO_ON * (human_years - 2)
  
  return [human_years, cat_years, dog_years]
print(human_years_cat_years_dog_years(1)) # [1, 15, 15]
print(human_years_cat_years_dog_years(2)) # [2, 24, 24]
print(human_years_cat_years_dog_years(3)) # [3, 28, 29]