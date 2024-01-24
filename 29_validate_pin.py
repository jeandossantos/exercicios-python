def validate_pin(pin):
  pin_length = len(pin)
  
  if pin_length != 4 and pin_length != 6:
      return False
  
  if any(not char.isdigit() for char in pin):
      return False
  
  return True

some_pins = ["1234", "a234", "0000", "11111", "34211", "232c"]

for pin in some_pins:
  print(validate_pin(pin))