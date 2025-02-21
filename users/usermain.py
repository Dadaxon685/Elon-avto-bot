# from aiogram.types import Message,CallbackQuery
# from aiogram.fsm.context import FSMContext
# from aiogram import Router, F,Bot
# from aiogram.filters import CommandStart
# from buttons.butons import admin_btn,user_btn ,tasqidlash
# from database.databas import *
# from state.state import *
# from data.config import token,admin_id
# from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardMarkup,InlineKeyboardButton
# bot = Bot(token=token)


# user_router = Router()
# @user_router.message(CommandStart())
# async def start_command(message: Message):
#     user_id = message.from_user.id
#     username = message.from_user.username
#     read_admins = readadminstable()
    
#     # Admin ekanligini tekshirish
#     if any(admin[2] == user_id for admin in read_admins):
#         await message.answer("Assalomu alaykum! Admin.", reply_markup=admin_btn)
#     else:
#         # User ma'lumotlar bazasida borligini tekshirish
#         if not any(user[2] == username for user in readusertable()):
#             insertusertable(username=username, user_id=user_id)
        
#         await message.answer(
#             f"Assalomu alaykum! {message.from_user.full_name}, Quyidagilardan birini tanlang!", 
#             reply_markup=user_btn
#         )
    


# @user_router.message(F.text == '📢 Elon berish 📢')
# async def start_ad(message: Message, state: FSMContext):
#     await message.answer("Avtomobil modelini kiriting (masalan, Nexia 2):")
#     await state.set_state(CarAd.model)

# @user_router.message(CarAd.model)
# async def enter_model(message: Message, state: FSMContext):
#     await state.update_data(model=message.text)
#     await message.answer("Yilini kiriting (masalan, 2009):")
#     await state.set_state(CarAd.year)

# @user_router.message(CarAd.year)
# async def enter_year(message: Message, state: FSMContext):
#     if not message.text.isdigit() or not (1900 <= int(message.text) <= 2024):
#         await message.answer("Yil noto'g'ri kiritildi. Iltimos, to'g'ri yilni kiriting (masalan, 2009):")
#         return
#     await state.update_data(year=message.text)
#     await message.answer("Yurilgan masofani kiriting (masalan, 43,000 км):")
#     await state.set_state(CarAd.mileage)

# @user_router.message(CarAd.mileage)
# async def enter_mileage(message: Message, state: FSMContext):
#     if not message.text.replace(',', '').isdigit():
#         await message.answer("Yurilgan masofa noto'g'ri kiritildi. Iltimos, raqam shaklida kiriting (masalan, 43000):")
#         return
#     await state.update_data(mileage=message.text)
#     await message.answer("Bo'yoq holatini kiriting (masalan, asligicha qilingan):")
#     await state.set_state(CarAd.color)

# @user_router.message(CarAd.color)
# async def enter_color(message: Message, state: FSMContext):
#     await state.update_data(color=message.text)
#     await message.answer("Yo'qilg'i turini kiriting (masalan, benzin/metan):")
#     await state.set_state(CarAd.fuel)

# @user_router.message(CarAd.fuel)
# async def enter_fuel(message: Message, state: FSMContext):
#     await state.update_data(fuel=message.text)
#     await message.answer("Manzilni kiriting (masalan, Samarqand):")
#     await state.set_state(CarAd.location)

# @user_router.message(CarAd.location)
# async def enter_location(message: Message, state: FSMContext):
#     await state.update_data(location=message.text)
#     await message.answer("Narxni kiriting (masalan, $4,500):")
#     await state.set_state(CarAd.price)


# @user_router.message(CarAd.price)
# async def enter_price(message: Message, state: FSMContext):
#     try:
#         price = message.text.replace(',', '').replace('$', '')
#         if not price.isdigit() or int(price) <= 0:
#             raise ValueError
#         await state.update_data(price=message.text)
#         await message.answer("Telefon raqamingizni kiritishingiz mumkin:")
#         await state.set_state(CarAd.phone)
#     except ValueError:
#         await message.answer("Narx noto'g'ri formatda kiritilgan. Iltimos, to'g'ri narxni kiriting (masalan, $4500):")

# @user_router.message(CarAd.phone)
# async def enter_phone(message: Message, state: FSMContext):
#     phone_number = message.text
#     if not phone_number.startswith('+') or not phone_number[1:].isdigit():
#         await message.answer("Telefon raqam noto'g'ri kiritildi. Iltimos, +998901234567 shaklida kiriting.")
#         return
#     await state.update_data(phone=phone_number)
#     # await message.answer("2 dan 4 tagacha rasm yuboring. Barcha rasmlarni yuboring.")
#     # await state.set_state(CarAd.photos)

#     # print(phone_number)
#     # else:
#     #     await message.answer("Telefon raqam noto'g'ri kiritildi. Iltimos, to'g'ri telefon raqamini kiriting (masalan, +9989809090):")
        

#     await message.answer("2 dan 4 tagacha rasm yuboring. Barcha rasmlarni yuboring")
#     await state.set_state(CarAd.photos)

    
# @user_router.message(F.photo, CarAd.photos)
# async def add_photo(message: Message, state: FSMContext):
#     data = await state.get_data()
#     photos = data.get('photos', [])
#     if len(photos) < 4:
#         photos.append(message.photo[-1].file_id)
#         await state.update_data(photos=photos)
#         if len(photos) < 4:
#             await message.answer(f"Rasm saqlandi. Yana {4 - len(photos)} ta rasm yuborishingiz mumkin.")
#         else:
#             await message.answer("Barcha rasmlar saqlandi. Tasdiqlash uchun /done buyrug'ini bosing.")
#     else:
#         await message.answer("Siz maksimal 4 ta rasm yuborishingiz mumkin. /done buyrug'ini bosing.")

# @user_router.message(F.text == '/done', CarAd.photos)
# async def finish_photos(message: Message, state: FSMContext):
#     data = await state.get_data()
#     photos = data.get('photos', [])
#     if not photos:
#         await message.answer("Siz birorta ham rasm yubormadingiz. Iltimos, kamida 1 ta rasm yuboring.")
#         return

#     ad_text = (f"💸 {data['model']} САТИЛАДИ 💸\n\n"
#                f"📆 Ишлаб чиқарилган йили: {data['year']}\n"
#                f"🛣 Юрган йўли: {data['mileage']}\n"
#                f"🎨 Бодиси: {data['color']}\n"
#                f"⛽️ Ёқилғи тури: {data['fuel']}\n"
#                f"🚩 Манзил: {data['location']}\n"
#                f"💰 Нархи: {data['price']}\n"
#                f"☎️ Телефон: {data['phone']}\n")
#     await message.answer(f"{ad_text}\n\n\nShularni tasdiqlaysizmi?", reply_markup=tasqidlash)
#     await state.set_state(CarAd.tasqidlash)

# @user_router.message(CarAd.tasqidlash)
# async def tasqidlashsh(message: Message, state: FSMContext):
#     if message.text == "Ha":
#         data = await state.get_data()
#         ad_text = (f"💸 {data['model']} САТИЛАДИ 💸\n\n"
#                    f"📆 Ишлаб чиқарилган йили: {data['year']}\n"
#                    f"🛣 Юрган йўли: {data['mileage']}\n"
#                    f"🎨 Бодиси: {data['color']}\n"
#                    f"⛽️ Ёқилғи тури: {data['fuel']}\n"
#                    f"🚩 Манзил: {data['location']}\n"
#                    f"💰 Нархи: {data['price']}\n"
#                    f"☎️ Телефон: {data['phone']}\n"
#                    f" #{data['location']} #{data['model']}"  )
#         inserttableelonlar(
#             user_id=message.from_user.id,
#             mashina_model=data['model'],
#             mashina_yili=data['year'],
#             mashina_proberg=data['mileage'],
#             mashina_ranggi=data['color'],
#             mashina_yoqilgisi=data['fuel'],
#             manzil=data['location'],
#             mashina_narxi=data['price'],
#             egasi_tel_raqami=data['phone']
#         )

#         await state.update_data(photos=data.get('photos', []))
#         await message.answer("E'loningiz admin tasdiqlashiga yuborildi.")

#         photos = data.get('photos', [])
#         for photo in photos:
#             await bot.send_photo(admin_id, photo)

#         await bot.send_message(
#             admin_id,
#             text=f"Sizga @{message.from_user.username} dan xabar keldi:\n\n{ad_text}",
#             reply_markup=InlineKeyboardMarkup(
#                 inline_keyboard=[
#                     [
#                         InlineKeyboardButton(text="Yuborish", callback_data="yubor"),
#                         InlineKeyboardButton(text="Bekor qilish", callback_data="otmen")
#                     ]
#                 ]
#             )
#         )
#     else:
#         await message.answer("Eloningiz bekor qilindi.")
        


# @user_router.callback_query(F.data.startswith("yubor"))
# async def yubor_to_group(callback_query: CallbackQuery, state: FSMContext):
#     GROUP_ID = -1002368244871
#     data = await state.get_data()

#     if not data or 'model' not in data:
#         await callback_query.message.answer("E'lon ma'lumotlari topilmadi. Iltimos, qayta urinib ko'ring.")
#         return

#     ad_text = (f"💸 {data['model']} САТИЛАДИ 💸\n\n"
#                f"📆 Ишлаб чиқарилган йили: {data['year']}\n"
#                f"🛣 Юрган йўли: {data['mileage']}\n"
#                f"🎨 Бодиси: {data['color']}\n"
#                f"⛽️ Ёқилғи тури: {data['fuel']}\n"
#                f"🚩 Манзил: {data['location']}\n"
#                f"💰 Нархи: {data['price']}\n"
#                f"☎️ Телефон: {data['phone']}\n"
#                f" #{data['location']} #{data['model']}"  
#                )
#     photos = data.get('photos', [])
#     for photo in photos:
#         await bot.send_photo(chat_id=GROUP_ID, photo=photo)
#     await bot.send_message(chat_id=GROUP_ID, text=ad_text)
#     await callback_query.message.answer("E'lon muvaffaqiyatli guruhga yuborildi!",reply_markup=user_btn)
#     await state.clear()


# @user_router.callback_query(F.data.startswith("otmen"))
# async def cancel_ad(callback_query: CallbackQuery,state: FSMContext):
#     await callback_query.message.edit_reply_markup() 
#     await callback_query.message.answer("Xabar bekor qilindi.",reply_markup=user_btn)
#     await state.clear()
    

# @user_router.message(F.text == "🤗 Taklif yoki shikoyat yuborish 🤗")
# async def ask_feedback(message: Message, state: FSMContext):
#     await message.answer("Taklif yoki shikoyatingizni yozib yuboring. ✅")
#     await state.set_state(takliforshikoyat.matn)

# @user_router.message(takliforshikoyat.matn)
# async def answer(message: Message, state: FSMContext):
#     izoh = message.text
#     user_id = message.from_user.id
#     await state.update_data(taklif =user_id)
#     insertizohlar(user_id=user_id,izohi=izoh)  
#     await message.answer("Taklif/shikoyat yuborildi. Tez orada javob keladi.. ", reply_markup=user_btn)
#     await state.clear()

# @user_router.message(F.text == "📂 Mening Elonlarim 📂")
# async def elonkorish(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     elonlar = readtableelonlar()  # Bu sizning DB'dan o'qish funksiyangiz

#     if not elonlar:
#         await message.answer("Sizda e'lonlar mavjud emas.")
#         return

#     for i in elonlar:
#         if user_id == i[1]:  # Foydalanuvchining e'lonlari
#             ad = i[2]
#             yili = i[3]
#             yuli = i[4]
#             rangi = i[5]
#             yoqilgisi = i[6]
#             manzil = i[7]
#             narxi = i[8]
#             telefon = i[9]
#             elon_id = i[0]  # E'lonning unikal ID'si

#             a = (
#                 f"Mashina nomi: {ad}\n"
#                 f"Yili: {yili}\n"
#                 f"Yurgani: {yuli}\n"
#                 f"Rangi: {rangi}\n"
#                 f"Yoqilgisi: {yoqilgisi}\n"
#                 f"Manzil: {manzil}\n"
#                 f"Narxi: {narxi}\n"
#                 f"Telefon: {telefon}"
#             )

#             await message.answer(
#                 a,
#                 reply_markup=InlineKeyboardMarkup(
#                     inline_keyboard=[
#                         [
#                             InlineKeyboardButton(
#                                 text="E'lonni o'chirish",
#                                 callback_data=f"delete_elon:{elon_id}"  # E'lon ID'sini yuboramiz
#                             )
#                         ]
#                     ]
#                 )
#             )
#     await state.clear()

# # E'lonni o'chirish uchun callback
# @user_router.callback_query(lambda c: c.data and c.data.startswith("delete_elon:"))
# async def delete_elon(callback_query: CallbackQuery):
#     elon_id = int(callback_query.data.split(":")[1])  # E'lon ID'sini ajratib olish
#     user_id = callback_query.from_user.id

#     # DB'dan o'chirish funksiyasi
#     if delete_elon_from_db(elon_id, user_id):  # Foydalanuvchi ID tekshiriladi
#         await callback_query.message.edit_text("E'lon muvaffaqiyatli o'chirildi.")
#     else:
#         await callback_query.message.answer("E'lonni o'chirishda xatolik yuz berdi yoki sizga tegishli emas.")






# ## admin nb aloqa
# @user_router.message(F.text == "📞 Adminlar Bilan Bog'lanish 📞")
# async def adminlaraloqa(message: Message):
#     await message.answer(
#         text="Adminlar bilan bog'lanish uchun quyidagi tugmalardan birini tanlang:",
#         reply_markup=InlineKeyboardMarkup(
#             inline_keyboard=[
#                 [InlineKeyboardButton(text="Telegram", url="https://t.me/dadaxonmasharibov")],
#                 [InlineKeyboardButton(text="Instagram", url="https://instagram.com/dadaxon_685")],
#                 [InlineKeyboardButton(text="Telefon orqali bog'lanish", callback_data="call_admin")]
#             ]
#         )
#     )

# @user_router.callback_query(F.data == "call_admin")
# async def call_admin(callback_query: CallbackQuery):
#     await callback_query.message.answer("Adminning telefon raqami: +998977902332")  
#     await callback_query.answer()


from aiogram import Router, F,Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from buttons.butons import admin_btn , user_btn
from state.state import *
from buttons.butons import tasqidlash 
from data.config import admin_id
# **Ma'lumotlar bazasi bilan ishlovchi funksiya**
from database.databas import readadminstable, readusertable, insertusertable, readtableelonlar,delete_elon_from_db,inserttableelonlar,insertizohlar

user_router = Router()  # Foydalanuvchilar uchun router

# # **Tugmalar**
# admin_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="📢 Elon berish 📢", callback_data="elon_berish")],
#     [InlineKeyboardButton(text="📂 Mening Elonlarim 📂", callback_data="mening_elonlarim")],
#     [InlineKeyboardButton(text="📞 Adminlar Bilan Bog'lanish 📞", callback_data="admin_aloqa")]
# ])

# user_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="📢 Elon berish 📢", callback_data="elon_berish")],
#     [InlineKeyboardButton(text="📂 Mening Elonlarim 📂", callback_data="mening_elonlarim")],
#     [InlineKeyboardButton(text="🤗 Taklif yoki shikoyat yuborish 🤗", callback_data="taklif_shikoyat")],
#     [InlineKeyboardButton(text="📞 Adminlar Bilan Bog'lanish 📞", callback_data="admin_aloqa")]
# ])

# # **E'lon berish uchun state-lar**
# class CarAd(StatesGroup):
#     model = State()
#     year = State()
#     mileage = State()
#     color = State()
#     fuel_type = State()
#     location = State()
#     price = State()
#     phone = State()

# **Taklif yoki shikoyat uchun state**
# class TaklifShikoyat(StatesGroup):
#     matn = State()

# **/start komandasi**
@user_router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.clear()  # Har doim holatni tozalash

    user_id = message.from_user.id
    username = message.from_user.username
    read_admins = readadminstable()
    
    if any(admin[2] == user_id for admin in read_admins):
        await message.answer("Assalomu alaykum! Admin.", reply_markup=admin_btn)
    else:
        if not any(user[2] == username for user in readusertable()):
            insertusertable(username=username, user_id=user_id)
        
        await message.answer(
            f"Assalomu alaykum! {message.from_user.full_name}, Quyidagilardan birini tanlang!", 
            reply_markup=user_btn
        )

# **E'lon berish**
@user_router.message(F.text == "📢 Elon berish 📢")
async def start_ad(message: Message, state: FSMContext):
    await state.clear()  # Barcha oldingi state-larni tozalash
    await message.answer("Avtomobil modelini kiriting (masalan, Nexia 2):")
    await state.set_state(CarAd.model)

# **Mening e'lonlarim**
@user_router.message(F.text == "📂 Mening Elonlarim 📂")
async def elonkorish(message: Message, state: FSMContext):
    
    await state.clear()  # Holatlarni tozalash
    # @user_router.callback_query(lambda c: c.data and c.data.startswith("delete_elon:"))
# async def delete_elon(callback_query: CallbackQuery):
#     elon_id = int(callback_query.data.split(":")[1])  # E'lon ID'sini ajratib olish
#     user_id = callback_query.from_user.id

#     # DB'dan o'chirish funksiyasi
#     if delete_elon_from_db(elon_id, user_id):  # Foydalanuvchi ID tekshiriladi
#         await callback_query.message.edit_text("E'lon muvaffaqiyatli o'chirildi.")
#     else:
#         await callback_query.message.answer("E'lonni o'chirishda xatolik yuz berdi yoki sizga tegishli emas.")


    user_id = message.from_user.id
    elonlar = readtableelonlar()

    if not elonlar:
        await message.answer("Sizda e'lonlar mavjud emas.")
        return

    for i in elonlar:
        if user_id == i[1]:  # Foydalanuvchining e'lonlari
            ad = i[2]
            yili = i[3]
            yuli = i[4]
            rangi = i[5]
            yoqilgisi = i[6]
            manzil = i[7]
            narxi = i[8]
            telefon = i[9]
            elon_id = i[0]  # E'lonning unikal ID'si

            a = (
                f"Mashina nomi: {ad}\n"
                f"Yili: {yili}\n"
                f"Yurgani: {yuli}\n"
                f"Rangi: {rangi}\n"
                f"Yoqilgisi: {yoqilgisi}\n"
                f"Manzil: {manzil}\n"
                f"Narxi: {narxi}\n"
                f"Telefon: {telefon}"
            )

            await message.answer(
                a,
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="E'lonni o'chirish",
                                callback_data=f"delete_elon:{elon_id}"
                            )
                        ]
                    ]
                )
            )

@user_router.callback_query(lambda c: c.data and c.data.startswith("delete_elon:"))
async def delete_elon(callback_query: CallbackQuery):
    elon_id = int(callback_query.data.split(":")[1])  # E'lon ID'sini ajratib olish
    user_id = callback_query.from_user.id

    # DB'dan o'chirish funksiyasi
    if delete_elon_from_db(elon_id, user_id):  # Foydalanuvchi ID tekshiriladi
        await callback_query.message.edit_text("E'lon muvaffaqiyatli o'chirildi.")
    else:
        await callback_query.message.answer("E'lonni o'chirishda xatolik yuz berdi yoki sizga tegishli emas.")


# **Taklif yoki shikoyat yuborish**
@user_router.message(F.text == "🤗 Taklif yoki shikoyat yuborish 🤗")
async def ask_feedback(message: Message, state: FSMContext):
    await state.clear()  # Holatni tozalash
    await message.answer("Taklif yoki shikoyatingizni yozib yuboring. ✅")
    await state.set_state(takliforshikoyat.matn)
@user_router.message(takliforshikoyat.matn)
async def answer(message: Message, state: FSMContext):
    izoh = message.text
    user_id = message.from_user.id
    await state.update_data(taklif =user_id)
    insertizohlar(user_id=user_id,izohi=izoh)  
    await message.answer("Taklif/shikoyat yuborildi. Tez orada javob keladi.. ", reply_markup=user_btn)
    await state.clear()

# **Adminlar bilan bog'lanish**
@user_router.message(F.text == "📞 Adminlar Bilan Bog'lanish 📞")
async def adminlaraloqa(message: Message, state: FSMContext):
    await state.clear()  # Holatni tozalash
    await message.answer(
        text="Adminlar bilan bog'lanish uchun quyidagi tugmalardan birini tanlang:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Telegram", url="https://t.me/dadaxonmasharibov")],
                [InlineKeyboardButton(text="Instagram", url="https://instagram.com/dadaxon_685")],
                [InlineKeyboardButton(text="Telefon orqali bog'lanish", callback_data="call_admin")]
            ]
        )
    )



@user_router.message(CarAd.model)
async def enter_model(message: Message, state: FSMContext):
    await state.update_data(model=message.text)
    await message.answer("Yilini kiriting (masalan, 2009):")
    await state.set_state(CarAd.year)

@user_router.message(CarAd.year)
async def enter_year(message: Message, state: FSMContext):
    if not message.text.isdigit() or not (1900 <= int(message.text) <= 2024):
        await message.answer("Yil noto'g'ri kiritildi. Iltimos, to'g'ri yilni kiriting (masalan, 2009):")
        return
    await state.update_data(year=message.text)
    await message.answer("Yurilgan masofani kiriting (masalan, 43,000 км):")
    await state.set_state(CarAd.mileage)

@user_router.message(CarAd.mileage)
async def enter_mileage(message: Message, state: FSMContext):
    if not message.text.replace(',', '').isdigit():
        await message.answer("Yurilgan masofa noto'g'ri kiritildi. Iltimos, raqam shaklida kiriting (masalan, 43000):")
        return
    await state.update_data(mileage=message.text)
    await message.answer("Bo'yoq holatini kiriting (masalan, asligicha qilingan):")
    await state.set_state(CarAd.color)

@user_router.message(CarAd.color)
async def enter_color(message: Message, state: FSMContext):
    await state.update_data(color=message.text)
    await message.answer("Yo'qilg'i turini kiriting (masalan, benzin/metan):")
    await state.set_state(CarAd.fuel)

@user_router.message(CarAd.fuel)
async def enter_fuel(message: Message, state: FSMContext):
    await state.update_data(fuel=message.text)
    await message.answer("Manzilni kiriting (masalan, Samarqand):")
    await state.set_state(CarAd.location)

@user_router.message(CarAd.location)
async def enter_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await message.answer("Narxni kiriting (masalan, $4,500):")
    await state.set_state(CarAd.price)


@user_router.message(CarAd.price)
async def enter_price(message: Message, state: FSMContext):
    try:
        price = message.text.replace(',', '').replace('$', '')
        if not price.isdigit() or int(price) <= 0:
            raise ValueError
        await state.update_data(price=message.text)
        await message.answer("Telefon raqamingizni kiritishingiz mumkin:")
        await state.set_state(CarAd.phone)
    except ValueError:
        await message.answer("Narx noto'g'ri formatda kiritilgan. Iltimos, to'g'ri narxni kiriting (masalan, $4500):")

@user_router.message(CarAd.phone)
async def enter_phone(message: Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.startswith('+') or not phone_number[1:].isdigit():
        await message.answer("Telefon raqam noto'g'ri kiritildi. Iltimos, +998901234567 shaklida kiriting.")
        return
    await state.update_data(phone=phone_number)
    # await message.answer("2 dan 4 tagacha rasm yuboring. Barcha rasmlarni yuboring.")
    # await state.set_state(CarAd.photos)

    # print(phone_number)
    # else:
    #     await message.answer("Telefon raqam noto'g'ri kiritildi. Iltimos, to'g'ri telefon raqamini kiriting (masalan, +9989809090):")
        

    await message.answer("2 dan 4 tagacha rasm yuboring. Barcha rasmlarni yuboring")
    await state.set_state(CarAd.photos)

    
@user_router.message(F.photo, CarAd.photos)
async def add_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    photos = data.get('photos', [])
    if len(photos) < 4:
        photos.append(message.photo[-1].file_id)
        await state.update_data(photos=photos)
        if len(photos) < 4:
            await message.answer(f"Rasm saqlandi. Yana {4 - len(photos)} ta rasm yuborishingiz mumkin.")
        else:
            await message.answer("Barcha rasmlar saqlandi. Tasdiqlash uchun /done buyrug'ini bosing.")
    else:
        await message.answer("Siz maksimal 4 ta rasm yuborishingiz mumkin. /done buyrug'ini bosing.")

@user_router.message(F.text == '/done', CarAd.photos)
async def finish_photos(message: Message, state: FSMContext):
    data = await state.get_data()
    photos = data.get('photos', [])
    if not photos:
        await message.answer("Siz birorta ham rasm yubormadingiz. Iltimos, kamida 1 ta rasm yuboring.")
        return

    ad_text = (f"💸 {data['model']} САТИЛАДИ 💸\n\n"
               f"📆 Ишлаб чиқарилган йили: {data['year']}\n"
               f"🛣 Юрган йўли: {data['mileage']}\n"
               f"🎨 Бодиси: {data['color']}\n"
               f"⛽️ Ёқилғи тури: {data['fuel']}\n"
               f"🚩 Манзил: {data['location']}\n"
               f"💰 Нархи: {data['price']}\n"
               f"☎️ Телефон: {data['phone']}\n")
    await message.answer(f"{ad_text}\n\n\nShularni tasdiqlaysizmi?", reply_markup=tasqidlash)
    await state.set_state(CarAd.tasqidlash)

@user_router.message(CarAd.tasqidlash)
async def tasqidlashsh(message: Message, state: FSMContext):
    if message.text == "Ha":
        data = await state.get_data()
        ad_text = (f"💸 {data['model']} САТИЛАДИ 💸\n\n"
                   f"📆 Ишлаб чиқарилган йили: {data['year']}\n"
                   f"🛣 Юрган йўли: {data['mileage']}\n"
                   f"🎨 Бодиси: {data['color']}\n"
                   f"⛽️ Ёқилғи тури: {data['fuel']}\n"
                   f"🚩 Манзил: {data['location']}\n"
                   f"💰 Нархи: {data['price']}\n"
                   f"☎️ Телефон: {data['phone']}\n"
                   f" #{data['location']} #{data['model']}"  )
        inserttableelonlar(
            user_id=message.from_user.id,
            mashina_model=data['model'],
            mashina_yili=data['year'],
            mashina_proberg=data['mileage'],
            mashina_ranggi=data['color'],
            mashina_yoqilgisi=data['fuel'],
            manzil=data['location'],
            mashina_narxi=data['price'],
            egasi_tel_raqami=data['phone']
        )

        await state.update_data(photos=data.get('photos', []))
        await message.answer("E'loningiz admin tasdiqlashiga yuborildi.")
        from data.config import token
        bot= Bot(token=token)
        photos = data.get('photos', [])
        for photo in photos:
            await bot.send_photo(admin_id, photo)

        await bot.send_message(
            admin_id,
            text=f"Sizga @{message.from_user.username} dan xabar keldi:\n\n{ad_text}",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Yuborish", callback_data="yubor"),
                        InlineKeyboardButton(text="Bekor qilish", callback_data="otmen")
                    ]
                ]
            )
        )
    else:
        await message.answer("Eloningiz bekor qilindi.")
        


@user_router.callback_query(F.data.startswith("yubor"))
async def yubor_to_group(callback_query: CallbackQuery, state: FSMContext):
    GROUP_ID = -1002368244871
    data = await state.get_data()

    if not data or 'model' not in data:
        await callback_query.message.answer("E'lon ma'lumotlari topilmadi. Iltimos, qayta urinib ko'ring.")
        return

    ad_text = (f"💸 {data['model']} САТИЛАДИ 💸\n\n"
               f"📆 Ишлаб чиқарилган йили: {data['year']}\n"
               f"🛣 Юрган йўли: {data['mileage']}\n"
               f"🎨 Бодиси: {data['color']}\n"
               f"⛽️ Ёқилғи тури: {data['fuel']}\n"
               f"🚩 Манзил: {data['location']}\n"
               f"💰 Нархи: {data['price']}\n"
               f"☎️ Телефон: {data['phone']}\n"
               f" #{data['location']} #{data['model']}"  
               )
    photos = data.get('photos', [])
    for photo in photos:
        from data.config import token
        bot= Bot(token=token)
        await bot.send_photo(chat_id=GROUP_ID, photo=photo)
    await bot.send_message(chat_id=GROUP_ID, text=ad_text)
    await callback_query.message.answer("E'lon muvaffaqiyatli guruhga yuborildi!",reply_markup=user_btn)
    await state.clear()


@user_router.callback_query(F.data.startswith("otmen"))
async def cancel_ad(callback_query: CallbackQuery,state: FSMContext):
    await callback_query.message.edit_reply_markup() 
    await callback_query.message.answer("Xabar bekor qilindi.",reply_markup=user_btn)
    await state.clear()
 