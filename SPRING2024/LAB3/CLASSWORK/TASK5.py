#5
class CellPackage:
  def __init__(self,dam,poriman,somoy,sms,discount,validity):
    poriman=poriman.split()
    self.data=int(poriman[0])*1024
    self.price=dam
    self.talktime=somoy
    self.sms=sms
    offer=discount.split('%')
    self.discount=self.price*(int(offer[0])//100)
    self.validity=validity

pkg = CellPackage(150, '6 GB', 99, 20,'7%', 7)
print('===========Package1=============')
if pkg.data !=0 :
      print(f'Data = {pkg.data} MB')
if pkg.talktime !=0 :
      print(f'Talktime = {pkg.talktime} Minutes')
if pkg.sms !=0 :
      print(f'SMS/MMS = {pkg.sms} ')
if pkg.validity != 0:
      print(f'Validity = {pkg.validity} Days')
if pkg.price !=0 :
      print(f'--> Price {pkg.price} tk')
if pkg.discount !=0 :
      print(f'Buy now to get {pkg.discount} tk cashback.')
pkg2 = CellPackage(700, '35 GB', 700, 0,'10%', 30)
print('===========Package2=============')
# Subtask 3: Check each attribute and print
if pkg2.data !=0 :
      print(f'Data = {pkg2.data} MB')
if pkg2.talktime !=0 :
      print(f'Talktime = {pkg2.talktime} Minutes')
if pkg2.sms !=0 :
      print(f'SMS/MMS = {pkg2.sms} ')
if pkg2.validity != 0:
      print(f'Validity = {pkg2.validity} Days')
if pkg2.price !=0 :
      print(f'--> Price {pkg2.price} tk')
if pkg2.discount !=0 :
      print(f'Buy now to get {pkg2.discount} tk cashback.')
pkg4 = CellPackage(120, '0 GB', 190, 0,'0%', 10)
print('============Package3============')
if pkg4.data !=0 :
      print(f'Data = {pkg4.data} MB')
if pkg4.talktime !=0 :
      print(f'Talktime = {pkg4.talktime} Minutes')
if pkg4.sms !=0 :
      print(f'SMS/MMS = {pkg4.sms} ')
if pkg4.validity != 0:
      print(f'Validity = {pkg4.validity} Days')
if pkg4.price !=0 :
      print(f'--> Price {pkg4.price} tk')
if pkg4.discount !=0 :
      print(f'Buy now to get {pkg4.discount} tk cashback.')
# Subtask 4: Check each attribute and print