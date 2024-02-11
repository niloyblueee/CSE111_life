#task2
def pricecalc(food,place="Mohakhali"):
  menu={"BBQ Chicken Cheese Burger":250,
        "Beef Burger":170,
        "Naga Drums":200}
  total_price=0
  total_price+=menu[food]+(menu[food]*.08)
  if place!='Mohakhali':
    total_price+=60
  else:
    total_price+=40
  print( total_price )


pricecalc('Beef Burger','Dhanmondi')
pricecalc("Beef Burger")
pricecalc("Naga Drums","Dhanmondi")