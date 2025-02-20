# from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

# user_btn = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text='📢 Elon berish'),KeyboardButton(text="🤗 Taklif yoki shikoyat yuborish")],
#         [KeyboardButton(text="Adminlar Bilan Bog'lanish"),KeyboardButton(text="Mening Elonlarim")]
#         ],resize_keyboard=True
    
# )
# admin_btn = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Izohlarni ko'rish")],
#         [KeyboardButton(text="Elon yuborish")],
#         [KeyboardButton(text="Admin qo'shish")],
#         [KeyboardButton(text="Admin O'chirish")]
#     ],resize_keyboard=True
# )
# elon = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Kanalga elon yuborish")],
#         [KeyboardButton(text="Botga elon yuborish")]
#     ],resize_keyboard=True
# )
# tasqidlash = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Ha"),KeyboardButton(text="Yo'q")]
#     ],resize_keyboard=True
# )



# # send_contact_button = ReplyKeyboardMarkup(
# #     keyboard=[
# #         [KeyboardButton(text="Contactni ulashish")]
# #     ],resize_keyboard=True
# # )
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📢 Elon berish 📢'), KeyboardButton(text="🤗 Taklif yoki shikoyat yuborish 🤗")],
        [KeyboardButton(text="📞 Adminlar Bilan Bog'lanish 📞"), KeyboardButton(text="📂 Mening Elonlarim 📂")]
    ], resize_keyboard=True
)

admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💬 Izohlarni ko'rish 💬")],
        [KeyboardButton(text="📨 Elon yuborish 📨")],
        [KeyboardButton(text="➕ Admin qo'shish ➕")],
        [KeyboardButton(text="❌ Admin O'chirish ❌")]
    ], resize_keyboard=True
)

elon = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📢 Kanalga elon yuborish 📢")],
        [KeyboardButton(text="🤖 Botga elon yuborish 🤖")]
    ], resize_keyboard=True
)

tasqidlash = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ], resize_keyboard=True
)
