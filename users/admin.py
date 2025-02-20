from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from buttons.butons import admin_btn,tasqidlash,user_btn
# from aiogram.utils.keyboard import  

from aiogram import Router ,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router, F,Bot
from database.databas  import * 
from data.config import token,admin_id
from buttons import *
from state.state import *
from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton,InlineKeyboardMarkup
bot = Bot(token=token)
# from crud import SQLiteBaza
# admin_router = Router()
# from buttons import 
# admis =[5148276461]
admin_router = Router()



@admin_router.message(CommandStart())
async def start_command(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    read_admins = readadminstable()
    
    # Admin ekanligini tekshirish
    if any(admin[2] == user_id for admin in read_admins):
        await message.answer("Assalomu alaykum! Admin.", reply_markup=admin_btn)
    else:
        # User ma'lumotlar bazasida borligini tekshirish
        if not any(user[2] == username for user in readusertable()):
            insertusertable(username=username, user_id=user_id)
        
        await message.answer(
            f"Assalomu alaykum! {message.from_user.full_name}, Quyidagilardan birini tanlang!", 
            reply_markup=user_btn
        )


@admin_router.message(F.text == "💬 Izohlarni ko'rish 💬")
async def izohkorish(message: Message, state: FSMContext):
    user_id = message.from_user.id

    if user_id == admin_id: 
        for i in readizobtable():
            user = await bot.get_chat(i[1])
            izoh_text = f"Telegram ismi: {user.full_name} | Izoh: {i[2]}"
            await message.answer(
                text=izoh_text,
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text="Javob yozish", callback_data=f"send::{i[1]}::{i[0]}"),
                         InlineKeyboardButton(text="O'chirish", callback_data=f"delete::{i[0]}")]
                    ]
                )
            )
    else:
        await message.answer("Siz bu funksiyadan foydalanish uchun admin bo'lishingiz kerak.")
@admin_router.callback_query(F.data.startswith("send::"))
async def SendUser(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split("::")
    user_id = int(data[1])
    message_id = int(data[2])
    await callback.message.delete()
    await callback.message.answer(text="Izohga javobingini kiriting.")
    await state.set_state(send_izoh.text)
    await state.update_data(user_id=user_id, message_id=message_id)

@admin_router.message(F.text, send_izoh.text)
async def SendIzoh(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = data["user_id"]
    message_id = data["message_id"]
    izoh = message.text
    await bot.send_message(
        chat_id=user_id,
        text=f"Admindan izohingizga javob keldi.\n\n<i>{izoh}</i>"
    )
    await message.answer(text="Xabar yuborildi")
    await state.clear()
@admin_router.callback_query(F.data.startswith("delete::"))
async def delete_comment(callback: CallbackQuery):
    data = callback.data.split("::")
    comment_id = int(data[1])  # Izohning ID'si

    # Izohni o'chirish
    delete_comment_from_db(comment_id)

    await callback.message.edit_text("Izoh muvaffaqiyatli o'chirildi.")
    await callback.answer()

@admin_router.message(F.text, send_izoh.text)
async def SendIzoh(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = data["user_id"]
    message_id = data["message_id"]
    izoh = message.text
    

    await bot.send_message(
        chat_id=user_id,
        text=f"Admindan izohingizga javob keldi.\n\n<i>{izoh}</i>"
    )
    await message.answer(text="Xabar yuborildi")
    await state.clear()

@admin_router.message(F.text ==("➕ Admin qo'shish ➕"))
async def addadmin(message: Message ,state: FSMContext):
    user_id = message.from_user.id

    if user_id == admin_id:
        # await message.answer("Admin qo'shish uchun Telegram ID yuboring:")
        await message.answer("Admin qo'shish uchun admin ismini  yuboring:")
        await state.set_state(adminadd.add)
    else:
        await message.answer("Siz admin emassiz.")
@admin_router.message(adminadd.add)
async def user_id(message: Message, state: FSMContext):
    # user_id = message.from_user.id
    xabar = message.text
    print(xabar)
    for i in readadminstable():
        if xabar != i[1] :
            await message.answer("Admin telegram idsini yuboring")
            await state.set_state(adminadd.name)
            await state.update_data(ism=xabar)
        elif xabar:
            await message.answer("Sizda bu user admin!!")
@admin_router.message(adminadd.name)
async def name(message :Message,state : FSMContext):
    xabar = message.text
    print(xabar)
    if xabar.isdigit():
        await message.reply("Admin qo'shishni Tasqidlaysizmi?",reply_markup=tasqidlash)
        await state.set_state(adminadd.finish)
        await state.update_data(user_id=int(xabar))
    else:
        await message.answer("Qo'shish bekor qilindi")
    # print(xabar)
    # if xabar == "Ha":
    #     data = await state.get_data()
    #     user_id = data["user_id"]
    #     add_admin(USER_ID=user_id)
    #     await message.answer("Admin qo'shildi")
    # else:
    #     await message.answer("Admin qo'shishni bekor qilishni qoldiring")
    # await state.clear()   
@admin_router.message(adminadd.finish)
async def finshadmin(message: Message,state:FSMContext):
    xabar = message.text
    if xabar == "Ha":
        data = await state.get_data()
        user_id = data["user_id"]
        ism = data["ism"]
        add_admin(admin_name=user_id,USER_ID=ism)
        await message.answer("Admin qo'shildi",reply_markup=admin_btn)
    else:
        await message.answer("Admin qo'shishni bekor qilishni qoldiring",reply_markup=admin_btn)
    await state.clear()
@admin_router.message(F.text == '📨 Elon yuborish 📨')
async def send_elon(message: Message,state: FSMContext):
    await message.answer("Elon Rasmini yuboring: ")
    await state.set_state(botelon.elon)
@admin_router.message(botelon.elon)
async def send_elon2(message: Message,state: FSMContext):
    rasm = message.photo[-1].file_id
    print(rasm)
    await message.answer("Elon captionni yuboring: ")
    await state.update_data(rasm=rasm)
    await state.set_state(botelon.finish)
@admin_router.message(botelon.finish)
async def send_elon3(message: Message,state: FSMContext):
    xabar = message.text
    print(xabar)
    await state.update_data(caption=xabar)
    await message.answer("elomn yuborishni tasqidlaysiizmi?",reply_markup=tasqidlash)
    await state.set_state(botelon.finish2)
@admin_router.message(botelon.finish2)
async def send_elon4(message: Message,state: FSMContext):
    xabar =     message.text
    print(xabar)
    if xabar == 'Ha':
        data = await state.get_data()
        rasm = data['rasm']
        caption = data['caption']
        for i in readusertable():
            await message.answer("Elon yuborildi.",reply_markup=admin_btn)
            await bot.send_photo(chat_id=i[2],photo=rasm,caption=caption)
    else:
        await message.answer("Elon yuborish bekor qilindi.",reply_markup=admin_btn)

# Adminni o'chirish uchun funksiya
@admin_router.message(F.text == "❌ Admin O'chirish ❌")
async def delete_admin1(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # Faqat asosiy admin (admin_id) adminlarni o'chirishi mumkin
    if user_id == admin_id:
        await message.answer("O‘chiriladigan admin ID'sini yuboring:")
        await state.set_state(admindelete.delete)
    else:
        await message.answer("Siz adminlarni o‘chirish huquqiga ega emassiz.")

@admin_router.message(admindelete.delete)
async def confirm_delete_admin(message: Message, state: FSMContext):
    try:
        admin_id_to_delete = int(message.text)
    except ValueError:
        await message.answer("Iltimos, to'g'ri ID yuboring.")
        return

    user_id = message.from_user.id

    # O‘zini o‘zi o‘chirishga yo‘l qo‘yilmaydi
    if admin_id_to_delete == user_id:
        await message.answer("Siz o'zingizni o'chira olmaysiz.")
        await state.clear()
        return

    # Admin mavjudligini tekshirish
    admin_list = readadminstable()
    for admin in admin_list:
        if admin[2] == admin_id_to_delete:
            await message.answer(
                f"Admin ID {admin_id_to_delete} o'chiriladi. Tasdiqlaysizmi?",
                reply_markup=tasqidlash  # Tasdiqlash tugmalari
            )
            await state.update_data(admin_id=admin_id_to_delete)
            await state.set_state(admindelete.confirm)
            return

    await message.answer("Bunday admin topilmadi.")
    await state.clear()

@admin_router.message(admindelete.confirm)
async def finalize_delete_admin(message: Message, state: FSMContext):
    response = message.text
    if response == "Ha":
        data = await state.get_data()
        admin_id = data["admin_id"]

        # Adminni ma'lumotlar bazasidan o'chirish
        delete_admin(admin_id=admin_id)

        await message.answer(f"Admin ID {admin_id} muvaffaqiyatli o'chirildi.", reply_markup=admin_btn)
    else:
        await message.answer("Adminni o'chirish bekor qilindi.", reply_markup=admin_btn)

    await state.clear()
