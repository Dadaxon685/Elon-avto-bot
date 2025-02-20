from aiogram.fsm.state import State, StatesGroup

# E'lon uchun State-lar
class CarAd(StatesGroup):
    model = State()
    year = State()
    mileage = State()
    color = State()
    fuel = State()
    location = State()
    price = State()
    phone = State()
    photos = State()
    finish = State()
    tasqidlash = State()
class botelon(StatesGroup):
    elon = State()
    finish = State()
    finish2 = State()
class takliforshikoyat(StatesGroup):
    matn = State()
class send_izoh(StatesGroup):
    text = State()

class adminadd(StatesGroup):
    add = State()
    name = State()
    finish = State()
    
class admindelete(StatesGroup):
    delete = State()
    confirm = State()