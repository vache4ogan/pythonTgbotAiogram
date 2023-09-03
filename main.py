from aiogram import Bot, Dispatcher, types
import logging
import asyncio
import random
import config
import players_info_base

objects = ["Камень", "Ножницы", "Бумага"]

players_id_list = []
# Подготовка-

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)

dp = Dispatcher(bot)

score_player = 0
score_bot = 0

btn_1 = types.KeyboardButton(text="Играть")

keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.add(btn_1)

keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)

kamen_btn = types.KeyboardButton(text="Камень")
nozhni_btn = types.KeyboardButton(text="Ножницы")
bumag_btn = types.KeyboardButton(text="Бумага")

StopGame_Btn = types.KeyboardButton(text="Стоп")
score_null_btn = types.KeyboardButton(text="Обнулить счет")

keyboard2.add(kamen_btn)
keyboard2.add(nozhni_btn)
keyboard2.add(bumag_btn)
keyboard2.add(StopGame_Btn)
keyboard2.add(score_null_btn)


# Хендлеры, обработчики

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    players_info_base.save(str(message.from_user.id), message.from_user.first_name)

    btn_1 = types.KeyboardButton(text="Играть")

    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(btn_1)

    await message.answer("Привет, это игра Камень, Ножницы, Бумага", reply_markup=keyboard1)


@dp.message_handler(commands=["prank"])
async def konmamik(message: types.Message):
    await message.answer('Это секретная функция, отправка спам сообщения по id,'
                         ' но перед этим человек, которому я напишу, должен хоть один раз нажать старт на своем устройстве.'
                         ' Как только это будет сделано, отправь мне сообщение "/prankich (id человека) (Текст, который ему нужно отправить)"'
                         ' потом отдельным сообщением текст, который хотите отправить')


@dp.message_handler(commands=["prankich"])
async def prankich(message: types.Message):
    id1 = ""
    try:

        id = str(message.text.lower())

        for i in id:
            if i in config.nums:
                id1 = id1 + i

        print(id1)

        await message.answer('id = ' + id1)
        await message.answer('Теперь, можешь отправить текст сообщения')
        maintext = ""
        text = message.text.lower()

        text1 = text.replace('/prankich ', '')
        for i in text1:
            if i in config.symbols:
                maintext = maintext + i

        print(maintext)
        await message.answer('Все готово, по id: ' + id1 + "Будет отправлено сообщение с текстом: " + maintext)

        config.Spam(id1, maintext)
    except:
        await message.answer('Ошибка')


@dp.message_handler()
async def message(message: types.Message):
    if message.text.lower() == "играть":
        if str(message.from_user.id) not in players_info_base.info:
            players_info_base.add_to_base(str(message.from_user.id), message.from_user.first_name, 0, 0)
            print(players_info_base.info)
            print(players_info_base.Player_scores)
            print(players_info_base.bot_scores)

        await message.answer('Выбирай', reply_markup=keyboard2)

    Player_Choice = message.text.lower()
    if message.text.lower() == "камень" or message.text.lower() == "бумага" or message.text.lower() == "ножницы":
        bot_choice = random.choice(objects)
        await message.answer(bot_choice)
    try:
        if Player_Choice == bot_choice.lower():
            await message.answer(
                "Ничья)\nСчет: \n" + message.from_user.first_name + ': ' + str(
                    players_info_base.Player_scores[str(message.from_user.id)]) + '\nБот: ' + str(
                    players_info_base.bot_scores[str(message.from_user.id)]))
    except:
        pass
    if Player_Choice == "камень" and bot_choice == "Бумага":
        players_info_base.bot_scores[str(message.from_user.id)] += 1
        await message.answer(
            'Ха-ха\nТы проиграл\nСчет: \n' + message.from_user.first_name + ': ' + str(
                players_info_base.Player_scores[str(message.from_user.id)]) + '\nБот: ' + str(
                players_info_base.bot_scores[str(message.from_user.id)]))
    if Player_Choice == "камень" and bot_choice == "Ножницы":
        players_info_base.Player_scores[str(message.from_user.id)] += 1
        await message.answer(
            'Ты выиграл\nСчет: \n' + message.from_user.first_name + ': ' + str(
                players_info_base.Player_scores[str(message.from_user.id)]) + '\nБот: ' + str(
                players_info_base.bot_scores[str(message.from_user.id)]))
    if Player_Choice == "бумага" and bot_choice == "Ножницы":
        players_info_base.bot_scores[str(message.from_user.id)] += 1
        await message.answer(
            'Ха-Ха\nТы проиграл\nСчет: \n' + message.from_user.first_name + ': ' + str(
                players_info_base.Player_scores[str(message.from_user.id)]) + '\nБот: ' + str(
                players_info_base.bot_scores[str(message.from_user.id)]))
    if Player_Choice == "бумага" and bot_choice == "Камень":
        players_info_base.Player_scores[str(message.from_user.id)] += 1
        await message.answer(
            'Ты выиграл\nСчет: \n' + message.from_user.first_name + ': ' + str(
                players_info_base.Player_scores[str(message.from_user.id)]) + '\nБот: ' + str(
                players_info_base.bot_scores[str(message.from_user.id)]))

    if Player_Choice == "ножницы" and bot_choice == "Камень":
        players_info_base.bot_scores[str(message.from_user.id)] += 1
        await message.answer(
            'Ха-Ха\nТы проиграл\nСчет: \n' + message.from_user.first_name + ': ' + str(
                players_info_base.Player_scores[str(message.from_user.id)]) + '\nБот: ' + str(
                players_info_base.bot_scores[str(message.from_user.id)]))
    if Player_Choice == "ножницы" and bot_choice == "Бумага":
        players_info_base.Player_scores[str(message.from_user.id)] += 1
        await message.answer(
            'Ты выиграл \nСчет: \n' + message.from_user.first_name + ': ' + str(
                players_info_base.Player_scores[str(message.from_user.id)]) + '\nБот: ' + str(
                players_info_base.bot_scores[str(message.from_user.id)]))
    if message.text.lower() == 'стоп':
        await message.answer('Игра остновлена', reply_markup=keyboard1)
    if message.text.lower() == "обнулить счет":
        players_info_base.bot_scores[str(message.from_user.id)] = 0
        players_info_base.Player_scores[str(message.from_user.id)] = 0
        await message.answer('Счет обнулён')
        print(players_info_base.info)
        print(players_info_base.Player_scores)
        print(players_info_base.bot_scores)

        # Запуск


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
