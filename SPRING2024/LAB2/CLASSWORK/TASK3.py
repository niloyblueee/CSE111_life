#task3
def replace_domain(main,new='sheba.xyz',old=''):
   email=main.split('@')
   if email[1]==new:
     new_email=main
   else:
    new_email=email[0]+"@"+new
   if new_email==main:
    print(f'Unchanged: {new_email}')
   else:
    print(f'Changed: {new_email}')

replace_domain("alice@kaaj.com","sheba.xyz","kaaj.com")
replace_domain('bob@sheba.xyz','sheba.xyz')