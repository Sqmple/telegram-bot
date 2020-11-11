from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, ContentType
import sqlite3
from loader import *
from states.test import Test
import keyboard as kb

# БД
db = sqlite3.connect('ajj.db', check_same_thread=False)
sql = db.cursor()

# Create table
sql.execute('''CREATE TABLE IF NOT EXISTS name(
    id TEXT,
    call_data TEXT,
    messag_text TEXT
) ''')
db.commit()

i = [('AgACAgIAAxkBAAMoX52AILubJTBkHIWQDBZNRbu9PRoAAnOuMRslGPBIqyRYTDLP-zP8r2yWLgADAQADAgADeQAD7lMDAAEbBA', 'biology1',
      '1'),
     # 2
     ('AgACAgIAAxkBAAMTX51vtvhTqKaKrMoQe0r7l93jKdgAAi-uMRslGPBIzdcC4cmshh64HMqXLgADAQADAgADeQAD9kwCAAEbBA', 'biology2',
      '2'),
     # 3
     ('AgACAgIAAxkBAAMUX51v5aoa9qRAx8o8Ub1devWWlFsAAjCuMRslGPBIzCn_lCvoFQABdfbVli4AAwEAAwIAA3kAA-MWAwABGwQ',
      'biology3', '3'),
     # 4
     ('AgACAgIAAxkBAAMVX51wAfEiXLTsO1lb_JlD15nIbF8AAjGuMRslGPBIksT_5qzkdh9TvtGXLgADAQADAgADeQADA0kCAAEbBA',
      'biology4', '4'),
     # 5
     ('AgACAgIAAxkBAAMWX51wKPwPL6BtFk2d90-UfM2liQADM64xGyUY8Ejvts84eaMBI1UHbZcuAAMBAAMCAAN5AAPBhwIAARsE', 'biology5',
      '5'),
     # 6
     ('AgACAgIAAxkBAAMXX51wRT5hl_i5izo1xkiJezgdELkAAjSuMRslGPBIZZ9G0nGii0VUidqWLgADAQADAgADeQADbhYDAAEbBA', 'biology6',
      '6'),
     # 7
     ('AgACAgIAAxkBAAMYX51wZv_o26Ohj8ia7mfhGARFtTwAAjWuMRslGPBIIuQNlERX9q77QfCXLgADAQADAgADeQAD-F8CAAEbBA', 'biology7',
      '7'),
     # 8
     ('AgACAgIAAxkBAAMZX51weLPHXSMNVEc1JJZmepYRCroAAjauMRslGPBI1lggOS2VoWYzThKVLgADAQADAgADeQADbPwFAAEbBA', 'biology8',
      '8'),
     # 9
     ('AgACAgIAAxkBAAMaX51wrTasDFXGR_U3SG8X_uhIXZsAAjiuMRslGPBIII74ck-HyhldQfCXLgADAQADAgADeQADeF4CAAEbBA', 'biology9',
      '9'),
     # 10
     ('AgACAgIAAxkBAAMbX51w1pVNOPuGQXXZdf1_KRkIs_oAAjmuMRslGPBIHNpb2rJgdCPicGaaLgADAQADAgADeQAD3jwAAhsE', 'biology10',
      '10'),
     # 11
     ('AgACAgIAAxkBAAMcX51w9ZbT62kpsxxfbLF2V_cadmMAAjquMRslGPBICyax5fqh6QmIyNSXLgADAQADAgADeQAD2kUCAAEbBA',
      'biology11', '11'),
     # 12
     ('AgACAgIAAxkBAAMdX51yk_DOGnce-q8BMQ9p8QMisrsAAj2uMRslGPBIh5e5PZKTBFrsidqWLgADAQADAgADeQAD7BwDAAEbBA',
      'biology12', '12'),
     # 13
     ('AgACAgIAAxkBAAMfX51yuXJ3RiEpNcjw9jWYKmBiBRgAAj-uMRslGPBI1mkAAfyT81nOW_fVli4AAwEAAwIAA3kAA3oTAwABGwQ',
      'biology13', '13'),
     # 14
     ('AgACAgIAAxkBAAMeX51ypQUIyrj8dOnnoR1Bsi-7o18AAj6uMRslGPBI5BxfiHfa7bomy9SXLgADAQADAgADeQAESgIAARsE', 'biology14',
      '14'),
     # 15
     ('AgACAgIAAxkBAAMgX51y3GZNrQOq8zvc3_EOVgjMYlMAAkCuMRslGPBI3viUpRuceGITYmOaLgADAQADAgADeQADbjwAAhsE', 'biology15',
      '15'),
     # 16
     (
         'AgACAgIAAxkBAAMhX51y9Kn5RcheSLLZRkqqPUmqWrwAAkGuMRslGPBI_6RgySb6r0iwTRKVLgADAQADAgADeQADOQEGAAEbBA',
         'biology16', '16'),
     # 17
     (
         'AgACAgIAAxkBAAMiX51zBqSw6KE9149bZfWOT-l3uDsAAkKuMRslGPBIUd6qdzTMtwiJRAWXLgADAQADAgADeQAD5GYCAAEbBA',
         'biology17', '17'),
     # 18
     (
         'AgACAgIAAxkBAAMjX51zFtQQg0PX5Q34fZkM-HyCaiMAAkOuMRslGPBIcRFhXI7x6jG6FKKWLgADAQADAgADeQADVVQDAAEbBA',
         'biology18', '18'),
     # 19
     (
         'AgACAgIAAxkBAAMkX51zJHHtkFwyC2Ikd59BXKxib0kAAkSuMRslGPBIgAGrOO9maN5KZRaYLgADAQADAgADeQADpHYCAAEbBA',
         'biology19', '19'),
     # 20
     (
         'AgACAgIAAxkBAAMlX51zN1UpWOVa6GyJS1Fz-rDhm-AAAkWuMRslGPBI4s5xGhHJNIVH4haVLgADAQADAgADeQADhvwFAAEbBA',
         'biology20', '20'),
     # 21
     (
         'AgACAgIAAxkBAAMmX51zQ8zG3istpVZ7tiwswoeqSjQAAkauMRslGPBI5O2JGT8lYKZPcmiXLgADAQADAgADeQADroYCAAEbBA',
         'biology21', '21'),
     # 22
     ('AgACAgIAAxkBAAMnX51zU4-vxT3GFklSZaKkdr8S8jIAAkeuMRslGPBIjfZu55KrEViR5T6WLgADAQADAgADeQADTbwDAAEbBA', 'biology22',
      '22')
     ]
# География
j = [('AgACAgIAAxkBAAICWF-jGUMv7QF4xs0ocUT3ak0FfepwAAJPsjEblQQZSVriN_A65cwkHk0SlS4AAwEAAwIAA3kAA2UoBgABHgQ',
      'geography1', 'geo1'),
     ('AgACAgIAAxkBAAICWV-jGVmsMKguWFsB1hcfCCeBjajAAALkrzEbTSghSd_Fey4eo7-RE7V3ly4AAwEAAwIAA3kAA9KwAgABHgQ',
      'geography2', 'geo2'),
     ('AgACAgIAAxkBAAICWl-jGWnTctRcxz9FDdxRgsoD_NM5AAJQsjEblQQZSSV3jLiF8E7bBvRBli4AAwEAAwIAA3kAA1TvAwABHgQ',
      'geography3', 'geo3'),
     ('AgACAgIAAxkBAAICW1-jGZl3im62AdtcUHzsgtK4n1tbAAJRsjEblQQZSW4-Hho4ohmzdwzkly4AAwEAAwIAA3kAAxObAgABHgQ',
      'geography4', 'geo4'),
     ('AgACAgIAAxkBAAICXF-jGx3egR0xKiavAs7pWpPfYoDeAAJQrzEbeOsZSfFUqQeh88DrFmcYlS4AAwEAAwIAA3kAA6gvBgABHgQ',
      'geography5', 'geo5'),
     ('AgACAgIAAxkBAAICXV-jGz4RxVYFvkeTmvxZROU1FWNjAAJQrzEbeOsZSfFUqQeh88DrFmcYlS4AAwEAAwIAA3kAA6gvBgABHgQ',
      'geography6', 'geo6'),
     ('AgACAgIAAxkBAAICX1-jG5A_QiROGO8h7bh0E-keSrkhAAJVsjEblQQZSbADyFLretjaIPjVli4AAwEAAwIAA3kAA74_AwABHgQ',
      'geography7', 'geo7'),
     ('AgACAgIAAxkBAAICXl-jG1DYf7IT86OfRhgSLA0O5DghAAJUsjEblQQZSXBmdgxHKUS9LQ5Ili4AAwEAAwIAA3kAA6XqAwABHgQ',
      'geography8', 'geo8'),
     ('AgACAgIAAxkBAAICYF-jG7Fkphimg-_ONjmYWa1uRt0RAAJWsjEblQQZSWaFzpiBQnSvUBNwly4AAwEAAwIAA3kAA6msAgABHgQ',
      'geography9', 'geo9'),
     ('AgACAgIAAxkBAAICYV-jG8Nej85yRlgLYcnp56dZL6-4AAJXsjEblQQZSWgIO6kYDlgbAAGco5YuAAMBAAMCAAN5AAM1eQMAAR4E',
      'geography10', 'geo10')]

g = [('AgACAgIAAxkBAAIChV-jJ2RaF6EezSDhse9TeVdSOb5zAAJwsjEblQQZSc1_U0GwBGrs4gafli4AAwEAAwIAA3kAA355AwABHgQ', 'engl_wd1',
      'eng_words1'),
     ('AgACAgIAAxkBAAIC4V-jwrWJ4MQpw_UoO4V0g29In0zSAAJ2sjEblQQZSchtzWuZ4odDowPZli4AAwEAAwIAA3kAA7NEAwABHgQ', 'engl_wd2',
      'eng_words2'),
     (
         'AgACAgIAAxkBAAICh1-jJ6EkzLyaHihKC75hZTHhbasQAAJ3sjEblQQZSfT0AAFgFbjb32GBa5cuAAMBAAMCAAN5AAP5rgIAAR4E',
         'engl_wd3',
         'eng_words3')]
a = [('AgACAgIAAxkBAAIDKF-kYxmweGMLYVLYyQuON9QDodgXAALAszEblQQhSZ_vNQ9gg58RSR5Lli4AAwEAAwIAA3kAAxb3AwABHgQ',
      'engl_konsp1', 'english_1'),
     ('AgACAgIAAxkBAAIDKV-kY19qCPb4QFvniScbo6c5fBZwAALBszEblQQhSfwgICNAtkBNClBVmS4AAwEAAwIAA3kAA_tuAAIeBA',
      'engl_konsp2', 'english_2'),
     ('AgACAgIAAxkBAAIDK1-kY53nrdp22TBZEVL6W4pwYJ3BAALDszEblQQhSRSMnIOwSYejrtFemi4AAwEAAwIAA3kAA0puAAIeBA',
      'engl_konsp3', 'english_3'),
     ('AgACAgIAAxkBAAIDKl-kY2rambRL-i8naWjKxbvlQOtnAALCszEblQQhSapyQoI2obwMhMnUly4AAwEAAwIAA3kAAzV8AgABHgQ',
      'engl_konsp4', 'english_4'),
     ('AgACAgIAAxkBAAIDLF-kY75EoHo-tuDzeDrG0Cscs7G8AALEszEblQQhSeJN4U9RU9NhaG5Ali4AAwEAAwIAA3kAA0f9AwABHgQ',
      'engl_konsp5', 'english_5'),
     ('AgACAgIAAxkBAAIDLl-kY-IVzAkyvnpiINeFYtI4IQJiAALGszEblQQhSb8bG1YHQWJ2OVhgmi4AAwEAAwIAA3kAAzBxAAIeBA',
      'engl_konsp6', 'english_6'),
     ('AgACAgIAAxkBAAIDLV-kY8wgQvI5Qffan_rfgdFKTUvtAALFszEblQQhSesT0A5nYGLE1YdGli4AAwEAAwIAA3kAA4P2AwABHgQ',
      'engl_konsp7', 'english_7'),
     ('AgACAgIAAxkBAAIDL1-kZAQMB8PMOJaNWNPMW7kRzDTVAALHszEblQQhSQXxa7kcSDxw2-pRmC4AAwEAAwIAA3kAA3mTAgABHgQ',
      'engl_konsp8', 'english_8'),
     ('AgACAgIAAxkBAAIDMF-kZBUiaVk80k5R9lKF0H84vl79AALIszEblQQhSdndKSHiXKLOYxRwly4AAwEAAwIAA3kAA167AgABHgQ',
      'engl_konsp9', 'english_9'),
     ('AgACAgIAAxkBAAIDMV-kZCS94DfZ5OAMRCpyypnq77elAALJszEblQQhSVn3b5f7Q3XoiGVjmi4AAwEAAwIAA3kAAy9wAAIeBA',
      'engl_konsp10', 'english_10'),
     ('AgACAgIAAxkBAAIDMl-kZDZsgmBmphOhlezVppJoUn9-AALKszEblQQhSWhFHVGgPILwBKNMli4AAwEAAwIAA3kAA_nzAwABHgQ',
      'engl_konsp11', 'english_11'),
     ('AgACAgIAAxkBAAIDM1-kZEVZh0iNdFx93y_Yw9FLwtchAALLszEblQQhSebxao9_e9pOem5Ali4AAwEAAwIAA3kAA2n1AwABHgQ',
      'engl_konsp12', 'english_12'),
     ('AgACAgIAAxkBAAIDNF-kZF8tNfBNGNRnL_BfzEtxNYd8AALMszEblQQhSZekjWeT1tTSvAoglS4AAwEAAwIAA3kAA8w5BgABHgQ',
      'engl_konsp13', 'english_13'),
     ('AgACAgIAAxkBAAIDNV-kZGt8v4VnLnpeqKdVMEthZ4z3AALNszEblQQhSYYVGT-V1XnL7fRBli4AAwEAAwIAA3kAAw_5AwABHgQ',
      'engl_konsp14', 'english_14'),
     ('AgACAgIAAxkBAAIDNl-kZILmIR78XMqpE3dTDWulWzwdAALOszEblQQhSaERer7zvv1FsRvKly4AAwEAAwIAA3kAA8h_AgABHgQ',
      'engl_konsp15', 'english_15'),
     ('AgACAgIAAxkBAAIDN1-kZJDaM0LXzMqixdgar0UN2q15AALPszEblQQhSds7VQ3CAAEHqMoZ55cuAAMBAAMCAAN5AAOipAIAAR4E',
      'engl_konsp16', 'english_16'),
     ('AgACAgIAAxkBAAIDOF-kZJ8542Dcx40RnAABumDBykSpRgAC0LMxG5UEIUk3a20nuYMrldkIn5YuAAMBAAMCAAN5AAPoiQMAAR4E',
      'engl_konsp17', 'english_17'),
     ('AgACAgIAAxkBAAIDOV-kZKsgNBTVN4nFPn-N6arK01x3AALRszEblQQhScXhBLvu5ANqWwFFli4AAwEAAwIAA3kAA_f4AwABHgQ',
      'engl_konsp18', 'english_18')
     ]

for ii in i:
    sql.execute('SELECT id FROM name WHERE call_data  = (?)', (ii[1],))
    sql.execute('SELECT id FROM name WHERE messag_text = (?)', (ii[2],))
    if sql.fetchone() is None:
        sql.execute('INSERT INTO name VALUES (?, ?, ?)', (ii[0], ii[1], ii[2]))
        db.commit()
    else:
        pass
for jj in j:
    sql.execute("SELECT id FROM name WHERE call_data = (?)", (jj[1],))
    sql.execute("SELECT id FROM name WHERE messag_text = (?)", (jj[2],))
    if sql.fetchone() is None:
        sql.execute('INSERT INTO name VALUES(?,?,?)', (jj[0], jj[1], jj[2]))
        db.commit()
    else:
        pass
for gg in g:
    sql.execute("SELECT id FROM name WHERE call_data = (?)", (gg[1],))
    sql.execute("SELECT id FROM name WHERE messag_text = (?)", (gg[2],))
    if sql.fetchone() is None:
        sql.execute("INSERT INTO name VALUES(?,?,?)", (gg[0], gg[1], gg[2]))
        db.commit()
    else:
        pass
for kk in a:
    sql.execute("SELECT id FROM name WHERE call_data = (?)", (kk[1],))
    sql.execute("SELECT id FROM name WHERE messag_text = (?)", (kk[2],))
    if sql.fetchone() is None:
        sql.execute("INSERT INTO name VALUES(?,?,?)", (kk[0], kk[1], kk[2]))
        db.commit()
    else:
        pass


# Старт команды
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Выберите какие нужны предметы", reply_markup=kb.button)


# Получение file_id
@dp.message_handler(content_types=ContentType.PHOTO)
async def photo(message):
    fileID = message.photo[-1].file_id
    print(fileID)


# Биология
@dp.callback_query_handler(lambda call: True, state=None)
async def biology(call: CallbackQuery):
    if call.data == 'biology' or 'geography' or 'math' or 'physics' or 'english' or 'ukraine_language':
        await bot.send_message(call.message.chat.id, "Выберите страницу")
    await Test.next()


@dp.message_handler(content_types=['text'], state=Test.Q1)
async def grt(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    try:
        if message.text == '1':
            sql.execute("SELECT id FROM name WHERE messag_text = (?)", ('1',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '2':
            sql.execute("SELECT id FROM name WHERE messag_text = (?)", ('2',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '3':
            sql.execute("SELECT id FROM name WHERE messag_text = (?)", ('3',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '4':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('4',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '5':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('5',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '6':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('6',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '7':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('7',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '8':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('8',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '9':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('9',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '10':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('10',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '11':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('11',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '12':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('12',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '13':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('13',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '14':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('14',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '15':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('15',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '16':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('16',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '17':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('17',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '18':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('18',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '19':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('19',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '20':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('20',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '21':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('21',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        elif message.text == '22':
            sql.execute(f"SELECT id FROM name WHERE messag_text = (?)", ('22',))
            rows = sql.fetchone()
            await bot.send_photo(message.chat.id, photo=rows[0])
            await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
    except Exception:
        await bot.send_message(message.chat.id, "Если вы хотите выйти пропишите /q")
        await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def gg(message: types.Message, state: FSMContext):
    answer1 = message.text
    await state.update_data(answer2=answer1)
    await bot.send_message(message.chat.id, "Вы в главном меню",reply_markup=kb.button)
    await Test.next()
