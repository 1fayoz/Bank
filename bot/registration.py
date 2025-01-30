from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.inline_keyboards import INLINE_KEYBOARDS
from bot.utils import get_employee, update_or_create_employee

router = Router()


class Registration(StatesGroup):
    mfo = State()
    tab_number = State()
    crm_id = State()


@router.message(CommandStart())
async def welcome(message: types.Message, state: FSMContext):
    await message.reply('Xush kelibsiz')
    employee = await get_employee(message.from_user.id)
    if employee and not employee.status:
        await message.answer('MFO kiriting')
        await state.set_state(Registration.mfo)
    elif employee and employee.status:
        keyboard = INLINE_KEYBOARDS.get_message_buttons()
        await message.answer('Botdan foydalanishingiz mumkin', reply_markup=keyboard)
    else:
        await message.answer('MFO kiriting')
        await state.set_state(Registration.mfo)


@router.message(StateFilter(Registration.mfo))
async def mfo(message: types.Message, state: FSMContext):
    global mfo
    try:
        mfo = message.text
    except:
        await message.answer("Text ko'rinishida bo'lsin")
    await state.update_data(mfo=mfo)
    await state.set_state(Registration.tab_number)
    await message.answer('Nomer kirting')


@router.message(StateFilter(Registration.tab_number))
async def tab_number(message: types.Message, state: FSMContext):
    get_data = await state.get_data()
    mfo = get_data.get('mfo')
    global tab_number
    try:
        tab_number = message.text
    except:
        await message.answer("Text ko'rinishida bo'lsin")
    await state.update_data(tab_number=tab_number, mfo=mfo)
    await state.set_state(Registration.crm_id)
    await message.answer('ID kirting')


@router.message(StateFilter(Registration.crm_id))
async def crm(message: types.Message, state: FSMContext):
    get_data = await state.get_data()
    global crm_id
    try:
        crm_id = message.text
    except:
        await message.answer("Text ko'rinishida bo'lsin")
    tab_number = get_data.get('tab_number')
    mfo = get_data.get('mfo')

    await update_or_create_employee(message.from_user.id, mfo, tab_number, crm_id)

    keyboard = INLINE_KEYBOARDS.get_message_buttons()
    await message.answer('Botdan foydalanishingiz mumkin', reply_markup=keyboard)
    await state.clear()
