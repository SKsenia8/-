import telebot
from telebot import types

bot = telebot.TeleBot('6751604416:AAExyftiQBSwiU3WTPEVJDVq-nPpmT14GQM')


@bot.message_handler(commands=['start'])
def main(message):
    file = open('./first2.jpg', 'rb')
    bot.send_photo(message.chat.id, file, f'Добро пожаловать, {message.from_user.first_name}, в телеграмм-боте "Молодёжный Нижний".' )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Выбрать район', callback_data='neighborhood'))
    markup.add(types.InlineKeyboardButton('Выбрать мероприятие', callback_data='events'))
    file = open('./r.png', 'rb')
    bot.send_photo(message.chat.id, file, 'Ты можешь выбрать район в котором хочешь прогуляться или выбрать просмотр'
                                      ' актуальных мероприятий в городе', reply_markup=markup)


@bot.message_handler(commands=['neighborhood'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Канавинский район', callback_data='kr')
    btn2 = types.InlineKeyboardButton('Нижегородский район', callback_data='nr')
    btn3 = types.InlineKeyboardButton('Московский район', callback_data='mr')
    btn4 = types.InlineKeyboardButton('Советский район', callback_data='sr')
    btn5 = types.InlineKeyboardButton('Ленинский район', callback_data='lr')
    btn6 = types.InlineKeyboardButton('Приокский район', callback_data='pr')
    btn7 = types.InlineKeyboardButton('Сормовский район', callback_data='sorr')
    btn8 = types.InlineKeyboardButton('Автозаводский район', callback_data='ar')
    markup.row(btn2)
    markup.row(btn4)
    markup.row(btn6, btn1)
    markup.row(btn3, btn5)
    markup.row(btn7, btn8)
    bot.send_message(message.chat.id, 'Выбери район в котором хочешь хорошо провести время', reply_markup=markup)


@bot.message_handler(commands=['events'])
def main(message):
    file = open('./liniy.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, '<b>Линия движется по бумаге и исчезает в лесу</b>\n\n'
                                                'Более 60 графических листов, выполненных в экспериментальных, авторских техниках.'
                                                '\nВыставочный проект представляет раннее творчество Сергея Проворова — '
                                                'участника арт-группы «Провмыза», основанной в 1998 году вместе с Галиной Мызниковой.'
                                                '\n\n<em>Место: Арсенал, Кремль, 6</em>', parse_mode='html')
    file = open('./starij.jfif', 'rb')
    bot.send_photo(message.chat.id, file, '<b>Гуляя по старому Нижнему</b>\n\n'
                                                'Прогулка по Нижнему Новгороду, каким он был на рубеже XIX - XX веков.'
                                                '\nВ экспозиции зрители совершают прогулку по Нижнему Новгороду, '
                                                'каким он был на рубеже XIX - XX веков. Сопровождать посетителей '
                                                'музея в этом путешествии будет Татьяна Павловна Виноградова — '
                                                'известный педагог, краевед, профессор кафедры ЮНЕСКО ННГАСУ, '
                                                'почетный гражданин Нижнего Новгорода, автор более двухсот '
                                                'публикаций, посвященных городу и его культурному наследию.'
                                                '\n\n<em>Место: НГХМ | Манеж, Кремль 1А</em>', parse_mode='html')
    file = open('./eo.jfif', 'rb')
    bot.send_photo(message.chat.id, file, '<b>С.С. Прокофьев «Евгений Онегин»</b>\n\n'
                                                'Музыка к неосуществленному спектаклю Московского камерного театра по роману Пушкина.'
                                                '\nВ «Евгении Онегине» Прокофьева соблюдены все законы '
                                                'драматического театра. Музыка, сопровождающая актерские мизансцены,'
                                                ' деликатно поддерживает произносимый ими текст. Вместе с тем, в '
                                                'готовящемся спектакле должны были звучать и сольные оркестровые '
                                                'фрагменты — лейтмотивы главных героев, танцевальные номера, '
                                                'драматические музыкальные эпизоды, усиливающие напряжение событий '
                                                'спектакля, вокализы и даже канцонетта Онегина на французском.'
                                                '\n\n<em>Место: Концертный зал Пакгаузы, ул. Стрелка, д. 21Ж</em>', parse_mode='html')
    file = open('./NON SEMANTIC.jfif', 'rb')
    bot.send_photo(message.chat.id, file, '<b>NON SEMANTIC</b>\n\n'
                                                'Погружение в альтернативное пространство в отрыве от повседневной реальности.'
                                                '\nХудожники media.tribe — экспериментаторы, постоянно ищущие '
                                                'нетипичные способы применения технологий в искусстве. В своих '
                                                'проектах коллектив исследует коммуникацию со зрителем на уровне '
                                                'эмоций и ощущений. Этот диалог выстраивается с помощью света, '
                                                'звука и организации пространства.'
                                                '\n\n<em>Место: Мультимедиа‑арт‑пространство ЦЕХ*, Варварская ул., 32</em>', parse_mode='html')
    file = open('./eb.jfif', 'rb')
    bot.send_photo(message.chat.id, file, '<b>ГОРИЗОНТ. К 90-летию Эрика Булатова</b>\n\n'
                                                'Около 20 крупномасштабных произведений художника.'
                                                '\nЭрик Булатов — один из ведущих представителей неофициального '
                                                'искусства СССР. В Экспозиции представлено около 20 крупномасштабных '
                                                'произведений художника, созданных с 1966 по 2010 год. Эксперимент '
                                                'с пространством, перспективой, взаимодействием шрифта и живописи '
                                                'сочетается в творчестве Булатова с высоким живописным мастерством. '
                                                'Основу экспозиции составят произведения из частных российских '
                                                'коллекций, которые редко показываются широкому кругу зрителей.'
                                                '\n\n<em>Место: Выставочный центр Пакгаузы, мыс Стрелка</em>', parse_mode='html')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'neighborhood':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Канавинский район', callback_data='kr')
        btn2 = types.InlineKeyboardButton('Нижегородский район', callback_data='nr')
        btn3 = types.InlineKeyboardButton('Московский район', callback_data='mr')
        btn4 = types.InlineKeyboardButton('Советский район', callback_data='sr')
        btn5 = types.InlineKeyboardButton('Ленинский район', callback_data='lr')
        btn6 = types.InlineKeyboardButton('Приокский район', callback_data='pr')
        btn7 = types.InlineKeyboardButton('Сормовский район', callback_data='sorr')
        btn8 = types.InlineKeyboardButton('Автозаводский район', callback_data='ar')
        markup.row(btn2)
        markup.row(btn4)
        markup.row(btn6, btn1)
        markup.row(btn2, btn5)
        markup.row(btn7, btn8)
        bot.send_message(callback.message.chat.id, 'Выбери район в котором хочешь хорошо провести время', reply_markup=markup)
    elif callback.data == 'events':
        bot.send_message(callback.message.chat.id, 'Вот список мероприятий, которые проходят сейчас в Нижнем')
    if callback.data == 'kr':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./kr3.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Канавинский район</b>\n\n'
                                                  'Канавинский район расположен в Заречной части Нижнего Новгорода, на '
                                                    'левом берегу реки Оки и правом берегу реки Волги. С 1918 по 1928 '
                                                    'год Канавино являлся городом. Канавинский район — один из старейших'
                                                    ' районов Нижнего Новгорода.\n\nС какой стороны ты бы хотел узнать '
                                                    '<u>Канавинский район</u>?', parse_mode='html', reply_markup=markup)
    elif callback.data == 'nr':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='hnr')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gnr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='onr')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./nr.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Нижегородский район</b>\n\n'
                                                    'Нижегородский район — центральный городской район Нижнего '
                                                    'Новгорода. Район располагается в Нагорной части города и граничит '
                                                    'с Советским, Канавинским и Приокским районами города, а также с '
                                                    'Кстовским районом Нижегородской области.\n\nС какой стороны ты бы хотел узнать '
                                                    '<u>Нижегородский район</u>?', parse_mode='html', reply_markup=markup)
    elif callback.data == 'mr':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='omr')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./mr.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Московский район</b>\n\n'
                                                    'Московский район - один из восьми внутригородских районов в '
                                                    'составе Нижнего Новгорода. Расположен в Заречной части города.'
                                                    ' Данная территория расположена в низинном междуречье Волги и Оки, '
                                                    'по-другому называемом «балахонской стрелицей», поскольку напоминает'
                                                    ' по форме стрелу. Указом Президиума Верховного Совета РСФСР от 9 '
                                                    'декабря 1970 года из частей Сормовского и Канавинского районов '
                                                    'был создан Московский район.\n\nС какой стороны ты бы хотел узнать.'
                                                    '<u>Московский район</u>?', parse_mode='html', reply_markup=markup)
    elif callback.data == 'sr':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='hsr')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gsr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='osr')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./sr.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Советский район</b>\n\n'
                                                    'Советский район - один из восьми внутригородских районов в составе'
                                                    ' Нижнего Новгорода. Расположен на крутом правом берегу Оки. Район '
                                                    'большой, наполнен различными местами для проведения досуга.\n\nС '
                                                    'какой стороны ты бы хотел узнать.<u>Советский район</u>?',
                                                    parse_mode='html', reply_markup=markup)
    elif callback.data == 'lr':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='hlr')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='glr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='olr')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./lrjpg.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Ленинский район</b>\n\n'
                                                    'Ленинский район расположен в заречной части Нижнего Новгорода '
                                                    'вдоль реки Оки, между Канавином и Автозаводом (площадь района – '
                                                    '10% территории города, т.е. 32 квадратных километра).\n\nС '
                                                    'какой стороны ты бы хотел узнать.<u>Ленинский район</u>?', parse_mode='html', reply_markup=markup)
    elif callback.data == 'pr':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='hpr')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gpr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='opr')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./pr.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Приокский район</b>\n\n'
                                                    'Приокский район занимает юго-восточную часть города. '
                                                    'Он расположен на крутом правом берегу реки Оки. В этом районе'
                                                    ' много промышленных и научных предприятий.\n\nС '
                                                    'какой стороны ты бы хотел узнать.'
                                                    '<u>Приокский район</u>?', parse_mode='html', reply_markup=markup)
    elif callback.data == 'sorr':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='hsorr')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gsorr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='osorr')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./sorr.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сормовский район</b>\n\n'
                                                    'Сормовский район - один из крупнейших районов Нижнего Новгорода, '
                                                    'в состав которого Сормово вошло в 1929 году.Это ромышленный район,'
                                                    ' занимающий северо-западный сектор Заречной части города.\n\nС '
                                                    'какой стороны ты бы хотел узнать.'
                                                    '<u>Сормовский район</u>?', parse_mode='html', reply_markup=markup)
    elif callback.data == 'ar':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('История и искусство', callback_data='har')
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gar')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='oar')
        markup.row(btn1)
        markup.row(btn2, btn4)
        file = open('./ar.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Автозаводский район</b>\n\n'
                                                    'Автозаводский район - расположен в заречной части города вдоль '
                                                    'реки Оки. По площади (около 90 квадратных километров, т.е. 27% '
                                                    'территории города), населению и своему промышленному значению это '
                                                    'своего рода «город в городе», хотя всё здесь, по существу, связано '
                                                    'с ключевым предприятием - Автозаводом, который был заложен в 1930 '
                                                    'году и менее чем за два года введен в действие\n\nС '
                                                    'какой стороны ты бы хотел узнать.'
                                                    '<u>Автозаводский район</u>?', parse_mode='html', reply_markup=markup)
    if callback.data == 'hkr':
        file = open('./can1.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Главный ярморочный дом</b>\n\n'
                                                    'Исторический район, где располагалась крупнейшая ярмарка '
                                                    'Российской империи. Центральный выставочный центр Нижнего '
                                                    'Новгорода. В Главном ярмарочном доме находится выставка «Россия - моя история».'
                                                    '\n\n<em>Адрес: ул. Совнаркомская, д. 13 (площадь Ленина)</em>', parse_mode='html')
        file = open('./museum7.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей истории и развития Горьковской железной дороги</b>\n\n'
                                                    'Музей находится возле железной дороги Нижний Новгород - Москва.  В коллекции музея '
                                                   'имеется 15 экземпляров паровозов, выпущенных в России, СССР, Швеции '
                                                   'и Германии в первой половине XX века.\n\n<em>Адрес: ул. Гороховецкая, д. 12</em>', parse_mode='html')
        file = open('./museum8.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей «История Канавина»</b>\n\n'
                                                    'Музей «История Канавина» находится при библиотеке им. А. Гайдара,'
                                                    ' в двадцати минутах ходьбы от станции метро «Московская». Цель '
                                                    'создания музея ‒ рассказать о более чем 400-летней истории Канавинской слободы.'
                                                    '\n\n<em>Адрес: ул. Мануфактурная, д. 9</em>', parse_mode='html')
        file = open('./can2.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Дом И.Я. Чеснокова</b>\n\n'
                                                    'Дом внесён в список охраняемых объектов. Здесь 4 года проживал'
                                                    ' Алеша Пешков, известный как Максим Горький.'
                                                    '\n\n<em>Адрес: ул. Алёши Пешкова, д. 44А</em>', parse_mode='html')
        file = open('./can3.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Мемориал "Бронепоезд «Козьма Минин»</b>\n\n'
                                                    'Бронепоезд построе горьковчанами во время ВОВ рабочими депо. 6 мая'
                                                    ' 1946 года Горьковский дивизион бронепоездов был расформирован,'
                                                    ' а бронепоезд «Козьма Минин» поставлен на вечную стоянку неподалеку'
                                                    ' от Дворца культуры «Железнодорожник».'
                                                    '\n\n<em>Адрес: ул. Июльских Дней, у ДК Железнодорожников</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id,'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                  'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'okr':
        file = open('./vyisota-molodezhnyii-czentr.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Молодежный Центр «Высота»</b>\n\n'
                                                    'Площадка, которая объединяет тысячи молодых людей региона. Здесь '
                                                    'можно забронировать помещение под встречу или мероприятие любой '
                                                    'молодежной командой, поработать в бесплатном коворкинге, а также '
                                                    'здесь проводятся мероприятия от команды МолодёжНО.'
                                                    '\n\n<em>Адрес: Совнаркомовская ул., 4</em>', parse_mode='html')
        file = open('./img.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Пакгаузы на Стрелке</b>\n\n'
                                                    'Пакгаузы — это два масштабных культурных павильона: выставочный и '
                                                    'концертный, с постоянной программой. Стильные зеркальные построены '
                                                    'в контуре исторического сооружения — ажурных металлических '
                                                    'конструкций, оставшихся в Нижнем Новгороде после XVI Всероссийской '
                                                    'промышленно-художественной ярмарки с конца XIX века.'
                                                    '\n\n<em>Адрес: ул. Стрелка, 21В</em>', parse_mode='html')
        file = open('./planetarij2.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Планетарий им. Гречко</b>\n\n'
                                                    'Этот высококлассный планетарий носит имя летчика-космонавта Георгия '
                                                    'Гречко, здесь обширная культурная программа и достаточно плотное '
                                                    'расписание, так что прийти можно в любой день.  В большом звездном '
                                                    'зале под 16-ти метровым куполом-экраном можно отправиться в '
                                                    'виртуальное путешествие по Вселенной, а в открытой астрономической '
                                                    'обсерватории — воспользоваться телескопом и прогуляться по лунным кратерам.'
                                                    '\n\n<em>Адрес: ул. Революционная, 20</em>', parse_mode='html')
        file = open('./park.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Зона отдыха "Берёзовая роща"</b>\n\n'
                                                    'Рекреационно-природная территория Берёзовая роща - прекрасная зона,'
                                                    ' где можно отдохнуть и провести время с друзьями'
                                                    ' от Дворца культуры «Железнодорожник».'
                                                    '\n\n<em>Адрес: ул. Движенцев</em>', parse_mode='html')
        file = open('./park8.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк культуры и отдыха имени 1 мая</b>\n\n'
                                                    'Один из старейших парков в городе, заложен в 1894 году. Создание'
                                                    ' парка было приурочено к началу строительства в Нижнем Новгороде '
                                                    'Всероссийской торгово-промышленной и художественной выставки. '
                                                    'В парке работают аттракционы, кафе, есть несколько детских площадок, устроен пруд.'
                                                    '\n\n<em>Адрес: ул. Октябрьской Революции, д. 31</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)

    elif callback.data == 'gkr':
        file = open('./cafe10.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Кафе "Бульвар"</b>\n\n'
                                                    'Ресторан с приятной атмосферой, вкусными шашлыками и напитками.'
                                                    '\n\n<em>Адрес: Мещерский бульвар, 10Б</em>', parse_mode='html')
        file = open('./cafe9.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Кафе "Печь"</b>\n\n'
                                                    'Это пиццерия с русским акцентом на популярные блюда. '
                                                    'Все готовится в дровяной печи на огне. Вам точно всё понравится.'
                                                    '\n\n<em>Адрес: ул. Мануфактурная, д. 18</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'hmr':
        file = open('./museum3.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей истории и культуры Московского района</b>\n\n'
                                                    'Музей был основан в 1976 г. как музей боевой и трудовой славы.'
                                                    ' С этого времени началась активная выставочная и культурно-просветительская '
                                                    'деятельность музея, и он становится одним из значительных '
                                                    'культурных центров Нижнего Новгорода. Здесь открыты четыре постоянные экспозиции.'
                                                    '\n\n<em>Адрес: ул. 50-летия Победы, д. 25</em>', parse_mode='html')
        file = open('./museum4.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей истории и трудовой славы авиастроительного завода «Сокол»</b>\n\n'
                                                    'Музей находится прям на территории завода. Интересен он может быть '
                                                    'не только специалистам в отрасли авиастроения, но и просто '
                                                    'любителям истории. Много оригинальных документов и исторических фотографий.'
                                                    '\n\n<em>Адрес: ул. Чаадаева, д. 1</em>', parse_mode='html')
        file = open('./mos1.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Памятник Г.К. Орджоникидзе</b>\n\nПамятник Г.К. Орджоникидзе - '
                                                    'памятник грузинскому революционеру, руководителю ВКП(б).'
                                                    '\n\n<em>Адрес: ул. Чаадаева, д. 1</em>', parse_mode='html')
        file = open('./mos3.png', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк Славы</b>\n\n'
                                                    'Мемориал Славы в честь Героя Советского Союза В. К. Клюева и работников эвакогоспиталя № 2808'
                                                    '\n\n<em>Адрес: ул. Просвещенская около МОУ СОШ №115</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'omr':
        file = open('./park3.jpeg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сквер им. Люкина</b>\n\n'
                                                    'Сквер им. Люкина - прекрасный парк Московского района. Здесь '
                                                    'чувствуется особая атмосфера пространства благодаря его главной'
                                                    ' концепции – сохранению памяти нашего земляка, поэта-фронтовика '
                                                    'Александра Ивановича Люкина. Можно найти и скамейки, и детские '
                                                    'площадки, и поляны с клумбами. Всё это в память поэта.'
                                                    '\n\n<em>Адрес: Московское шоссе, д. 177</em>', parse_mode='html')
        file = open('./sssr.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей «Назад в СССР»</b>\n\n'
                                                    'Музей «Назад в СССР» — это масштабная экспозиция уникальных '
                                                    'артефактов, предметов, техники, документов, символики и даже '
                                                    'личных вещей людей той эпохи. Экспозиция включает в себя более '
                                                    '10 тысяч самых различных экспонатов.'
                                                    '\n\n<em>Адрес: ул. Ярошенко, 7б, к4</em>', parse_mode='html')
        file = open('./icon.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сквер Целинников</b>\n\n'
                                                    'Сквер в часть горьковчан, осваивавших целину в Казахстане, был '
                                                    'заложен в 50-е годы. Здесь вы сможете познакомиться с историей,'
                                                    ' погулять и приятно провести время.'
                                                    '\n\n<em>Адрес: ул. Чаадаева, 20А</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'gmr':
        file = open('./cafe4.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Кофетайм</b>\n\n'
                                                    'Кофетайм - кофейня с прекрасными дессертами и напитками.'
                                                    '\n\n<em>Адрес: Московское ш., 11Б</em>', parse_mode='html')
        file = open('./cafe5.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сальвадор Дали</b>\n\n'
                                                    'Сальвадор Дали - кафе с прекрасной мзыкой и атмосферой, блюда вкусные и приятные.'
                                                    '\n\n<em>Адрес: ул. Коминтерна, д. 10</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'hpr':
        file = open('./museum5.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей-квартира А. Д. Сахарова</b>\n\n'
                                                    'Музей открыт в квартире, в которой Сахаров 7 лет отбывал в '
                                                    'политической ссылке. Музей состоит из двух композиций. Также там'
                                                    ' проходят различные интересные лекции.'
                                                    '\n\n<em>Адрес: пр-кт Гагарина, д. 214</em>', parse_mode='html')
        file = open('./museum6.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей Ф.И. Шаляпина</b>\n\n'
                                                    'Музей чтит память известного певца, который тесто связан с '
                                                    'городом и М. Горьким. Большая часть экспонатов представлена его'
                                                    ' дочерью. Всем почитателям творчества однозначно стоит познакомиться с музеем.'
                                                    '\n\n<em>Адрес: ул. Ветлужская, д. 2</em>', parse_mode='html')
        file = open('./pri1.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Мемориальный комплекс «Победа»</b>\n\n'
                                                    'Мемориальный комплекс «Победа» на площади маршала Г.К.Жукова - '
                                                    'композиция из нескольких обелисков памяти, посвящённых павшим '
                                                    'во время Великой Отечественной войны.'
                                                    '\n\n<em>Адрес: площадь Маршала Жукова</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'opr':
        file = open('./park5.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк Щёлковский хутор</b>\n\n'
                                                    '"Щёлковский хутор" - памятник природы регионального областного '
                                                    'значения Нижнего Новгорода. Парк больше напоминает лес с зелёными '
                                                    'и уютными полянками, на которых отдыхающие часто разводят костры и'
                                                    ' готовят шашлыки. На территории лесопарка можно увидеть специально '
                                                    'высаженные деревья необычных для здешних мест пород. Гости парка '
                                                    'могут побывать в настоящих крестьянских избах, внутреннее убранство'
                                                    ' которых полностью воспроизводит старинный быт.'
                                                    '\n\n<em>Адрес: ул. Горбатовская, 41</em>', parse_mode='html')
        ile = open('./planetarij.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Планетарий 1</b>\n\n'
                                                    'Новая современная мультимедийная площадка в парке «Швейцария» с '
                                                    'диаметром купола 18 метров. Здесь проходят показы полнокупольных '
                                                    'фильмов, перформансы, аудиовизуальные шоу, иммерсивные театральные '
                                                    'постановки и презентации. Кроме того, в планетарии действует '
                                                    'свободный коворкинг, лекторий и библиотека с научпоп-литературой.'
                                                    '\n\n<em>Адрес: пр. Гагарина, 35</em>', parse_mode='html')
        file = open('./Botanical_Garden_Tropic.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Ботанический сад ННГУ им. Н. И. Лобачевского</b>\n\n'
                                                    'Дубрава Ботанического сада университета - ландшафтный памятник'
                                                    ' природы. Был основа в 1934 г. Это настоящий музей растений, здесь'
                                                    ' можно увидеть множество представителей флоры.'
                                                    '\n\n<em>Адрес: ул. Ботанический Сад, д. 1</em>', parse_mode='html')
        file = open('./okeanis.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Аквапарк «Океанис»</b>\n\n'
                                                    'Первый аквапарк в Нижнем Новгороде занимает 40 000 квадратных '
                                                    'метров. Здесь есть 17 горок, 7 джакузи, семейный водный игровой '
                                                    'комплекс, волновой бассейн и «ленивая река». Этот аквапарк не '
                                                    'только для экстремалов и любителей острых ощущений, но и для тех, '
                                                    'кто хочет по-настоящему расслабиться — огромная зона спа к '
                                                    'этому располагает.'
                                                    '\n\n<em>Адрес: пр. Гагарина 35/3, ТРЦ Океанис, 2 этаж</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'gpr':
        file = open('./cafe6.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>"Самурай"</b>\n\n'
                                                    '"Самурай" - семейное кафе европейской и азиатской кухни. Здесь '
                                                    'вы сможете приятно пообедать или поужинать интересными блюдами.'
                                                    '\n\n<em>Адрес: пр-кт Гагарина, д. 192</em>', parse_mode='html')
        file = open('./cafe7.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>"Сладкий Горький"</b>\n\n'
                                                    '"Сладкий Горький" - кофейня с интересными авторскими напитками и десертами.'
                                                    '\n\n<em>Адрес: пр-кт Гагарина, д. 101/4</em>', parse_mode='html')
        file = open('./cafe8.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>"Хачапури и вино"</b>\n\n'
                                                    '"Хачапури и вино" - прекрасный ресторан грузинской кухни. Здесь '
                                                    'вы сможете попробовать ии хачапури, и хинкали, и другие вкусности грузинской кухни.'
                                                    '\n\n<em>Адрес: ул. Большая Покровская, д. 82</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'hsr':
        file = open('./museum1.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей истории ННГУ им. Лобачевского</b>\n\n'
                                                    'Экспозиция по истории университета отражает многолетний путь '
                                                    'университетского коллектива от учебного заведения просветительского'
                                                    ' типа (Нижегородский Народный университет 1916 г.) до крупнейшего'
                                                    ' в регионе научно-образовательного учреждения — Университета Лобачевского.'
                                                    '\n\n<em>Адрес: Зоологогический музей ННГУ им. Лобачевского</em>', parse_mode='html')
        file = open('./sov1.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>"Тобольские казармы"</b>\n\n'
                                                    'История Тобольских казарм начинается с Тобольского полка, '
                                                    'созданного бояриным Стрешневым в 1703 году. Сейчас же это здание'
                                                    ' из красного кирпича с многовековой историей, где живут люди.'
                                                    '\n\n<em>Адрес: просп. Гагарина, 60 к1</em>', parse_mode='html')
        file = open('./sov2.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Домик Каширина</b>\n\n'
                                                    'Домик Каширина - музей детства А.М. Горького. В музее хранится '
                                                    'ценное собрание изданий повести «Детство» на языках народов мира '
                                                    '(с 1914). Дом представляет собой 1-этажный сруб, обшитый и неокрашенный, с 5 комнатами.'
                                                    '\n\n<em>Адрес: ул. Почтовый Съезд, 21</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'osr':
        file = open('./park1.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк "Швейцария"</b>\n\n'
                                                    'Парк "Швейцария" - самый большой и популярный парк в Нижнем '
                                                    'Новгороде. Это место с прекрасной инфраструктурой, подойдёт для '
                                                    'прогулок, большая территория, на которой располагается аквапарк, '
                                                    'планетарий, смотровая площадка с видом на Оку.'
                                                    '\n\n<em>Адрес: пр-кт.Гагарина, д.35</em>', parse_mode='html')
        file = open('./park2.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк культуры им. А.С. Пушкина</b>\n\n'
                                                    'Городской ландшафтный парк культуры и отдыха имени А.С. Пушкина. '
                                                    'Часть парка является объектом культурного наследия (памятником '
                                                    'истории) регионального значения, её граница проходит по '
                                                    'диагональной дорожке, идущей от телецентра, и параллельно улице '
                                                    'Белинского на уровне здания в центре парка. В парке есть много '
                                                    'скамеек, фонтан, деревья, которые растут там уже много столетий, кафе.'
                                                    '\n\n<em>Адрес: ул. Белинского, д. 40</em>', parse_mode='html')
        file = open('./teatr.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Театр оперы и балета</b>\n\n'
                                                    'С 1935 года в здании бывшего Народного дома существует театр оперы '
                                                    'и балета имени А.С. Пушкина. Сейчас театр переживает настоящий '
                                                    'ренессанс! В 2022 году главным дирижером стал Дмитрий Синьковский '
                                                    '— всемирно известный музыкант, знаток барочной музыки, талантливый '
                                                    'скрипач и контратенор. На премьеры опер «Кармен» и «Пиковая дама» '
                                                    '(последняя, кстати, «переехала» на нижегородскую сцену из Большого '
                                                    'театра) ценители едут и из столицы, на «Щелкунчика» в новогодние '
                                                    'праздники в Нижнем попасть легче, а радости не меньше.'
                                                    '\n\n<em>Адрес: ул. Белинского, 59</em>', parse_mode='html')
        file = open('./sport.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>КРК "Нагорный"</b>\n\n'
                                                    'КРК "Нагорный" - культурно-развлекательный комплекс. Если ты фанат '
                                                    'хоккея, то это место точно для  тебя. Матчи нижегородского клуба '
                                                    '"Торпедо" проходят регулярно.'
                                                    '\n\n<em>Адрес: пр-кт. Гагарина, д. 29</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'gsr':
        file = open('./cafe1.jpeg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>"Хачапурия"</b>\n\n'
                                                    '"Хачапурия" - кафе с грузинской кухней. При посещении этого места '
                                                    'вы насладитесь прекрасными блюдами и колоритом этой страны.'
                                                    '\n\n<em>Адрес: ул. Совесткая площадь, д. 5</em>', parse_mode='html')
        file = open('./cafe2.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>"Сова"</b>\n\n'
                                                    '"Сова" - ресторан с русской и европейской кухней. Ресторан '
                                                    'находится при отеле, здесь вы сможете приятно провести время и '
                                                    'попробовать интересные блюда.'
                                                    '\n\n<em>Адрес: ул. Ванеева, д 121</em>', parse_mode='html')
        file = open('./cafe3.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>"Домашняя Италия"</b>\n\n'
                                                    '"Домашняя Италия" - ресторан итальянской кухни. Здесь вы сможете '
                                                    'попробовать все интересные и вкусные блюда итальянской кухни.'
                                                    '\n\n<em>Адрес: ул Советская площадь, д. 5</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'har':
        file = open('./muzei-gaz.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей истории ГАЗ</b>\n\n'
                                                    'Экспозиция обновленного музея истории ГАЗа рассказывает историю '
                                                    'автомобильного завода с самого основания в 1929 году и до '
                                                    'современности. В основе музея — коллекция автомобилей, выпущенных '
                                                    'в разные годы, например, легендарные «Чайки» и «Волги», но наряду '
                                                    'с ними здесь множество интерактивных зон с сенсорными экранами и VR-технологиями.'
                                                    '\n\n<em>Адрес: просп. Ленина, 95</em>', parse_mode='html')
        file = open('./avtozavod2.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Серо-бусыгинский квартал</b>\n\n'
                                                    'Уникальное место в Автозаводском районе — Серо-бусыгинский '
                                                    'квартал. Назван он в честь легендарного кузнеца Горьковского '
                                                    'автомобильного завода Александра Бусыгина. Уникальное место в '
                                                    'Автозаводском районе — Серо-бусыгинский квартал. Назван он в честь '
                                                    'легендарного кузнеца Горьковского автомобильного завода Александра '
                                                    'Бусыгина. Здания разделяются красивыми римскими арками, всего их семь, и они разной высоты.'
                                                    '\n\n<em>Адрес: пр. Октября, 21</em>', parse_mode='html')
        file = open('./22.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей Нижегородского метрополитена</b>\n\n'
                                                    'Музей Нижегородского метрополитена предлагает окунуться в историю '
                                                    'возникновения и становления метро, собрав в себя все знаковые '
                                                    'экспонаты за более чем 30 лет существования нижегородской подземки.'
                                                    '\n\n<em>Адрес: Автозаводская линия, метро Комсомольская (2 вестибюль)</em>', parse_mode='html')
        file = open('./23.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Паровозы России</b>\n\n'
                                                    'Открытая экспозиционная площадка «Паровозы России» Подразделения '
                                                    'по сохранению исторического наследия Горьковской железной дороги.'
                                                    '\n\n<em>Адрес: мкр. Сортировочный, Гороховецкая ул., 1Г</em>', parse_mode='html')
        file = open('./24.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Монумент боевой и трудовой славы автозаводцев</b>\n\n'
                                                    'Монумент боевой и трудовой славы автозаводцев - памятник, '
                                                    'посвящённый трудовому и ратному подвигу автозаводцев в годы '
                                                    'Великой Отечественной войны.'
                                                    '\n\n<em>Адрес: парк Славы</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'oar':
        file = open('./avtozavod.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Автозаводский парк</b>\n\n'
                                                    'Центральный парк культуры и отдыха Автозаводского района — '
                                                    'типичный и, в то же время, уникальный объект, рожденный эпохой '
                                                    'советской архитектуры 30-50-х годов прошлого века. Здесь можно и '
                                                    'просто гулять в тени вековых деревьев и активно проводить время в '
                                                    'зоне с детскими площадками и каруселями.'
                                                    '\n\n<em>Адрес: ул. Прыгунова, 2</em>', parse_mode='html')
        file = open('./20.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк имени 777-летия Нижнего Новгорода</b>\n\n'
                                                    'Парк имени 777-летия Нижнего Новгорода - Парк 777-летия Нижнего '
                                                    'Новгорода был заложен администрацией города в 1998 году в '
                                                    'Автозаводском районе в границах улиц Львовской, Строкина, '
                                                    'Дьяконова и Дворовой. В народе название этого парка сокращают просто до «777».'
                                                    '\n\n<em>Адрес: мкр. Северный</em>', parse_mode='html')
        file = open('./20.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк Славы</b>\n\n'
                                                    'Парк Славы - это мемориальный парк.'
                                                    '\n\n<em>Адрес: Парк Славы</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'gar':
        file = open('./25.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Italica</b>\n\n<em>Адрес: Молодёжный просп., 2А</em>', parse_mode='html')
        file = open('./26.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Маруся</b>\n\n<em>Адрес: просп. Кирова, 6</em>', parse_mode='html')
        file = open('./27.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Барбамбия</b>\n\n<em>Адрес: ул. Янки Купалы, 30А</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'hsorr':
        file = open('./35.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Метеор</b>\n\n'
                                                    'Метеор - судно на подводных крыльях, установленное в Сормовском районе Нижнего Новгорода.'
                                                    '\n\n<em>Адрес: площадь Буревестника</em>', parse_mode='html')
        file = open('./rostislavalekseev.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Памятник Ростиславу Алексееву</b>\n\n'
                                                    'Памятник всемирно известному конструктору судов на подводных '
                                                    'крыльях, экранопланов и экранолетов находится в Центре Сормова, и '
                                                    'расположение это не случайно — именно на заводе «Красное Сормово» '
                                                    'прошло становление выдающегося конструктора.'
                                                    '\n\n<em>Адрес: Юбилейный бульвар</em>', parse_mode='html')
        file = open('./sadimeni.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сад имени</b>\n\n'
                                                    '«Сад имени» — это общественный мемориальный комплекс, созданный '
                                                    'во внутреннем дворе частного крематория на окраине города. Проект '
                                                    'задуман как функционирующий ботанический сад, а звуковая '
                                                    'инсталляция основывается на современных ритуальных формах, '
                                                    'представлениях о телесности и виртуальности памяти.'
                                                    '\n\n<em>Адрес: ул. Зайцева, 27</em>', parse_mode='html')
        file = open('./sssr.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Музей «Назад в СССР»</b>\n\n'
                                                    'Музей «Назад в СССР» — это масштабная экспозиция уникальных '
                                                    'артефактов, предметов, техники, документов, символики и даже '
                                                    'личных вещей людей той эпохи. Экспозиция включает в себя более '
                                                    '10 тысяч самых различных экспонатов.'
                                                    '\n\n<em>Адрес: ул. Ярошенко, 7б, к4</em>', parse_mode='html')
        file = open('./39.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Шуховская башня</b>\n\n'
                                                    'Шуховская башня - Единственная в мире гиперболоидная '
                                                    'многосекционная опора линии электропередачи, выполненная в виде '
                                                    'несущей сетчатой оболочки.'
                                                    '\n\n<em>Адрес: примерно в 12 км от города Дзержинск на левом берегу'
                                                    ' Оки, за посёлком Дачный</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'osorr':
        file = open('./limpopo.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Зоопарк «Лимпопо»</b>\n\n'
                                                    'Первый частный зоопарк России и одно из любимых мест для прогулок '
                                                    'детей и взрослых в Нижнем Новгороде. Сегодня здесь обитает около '
                                                    '270 видов животных, многие из которых занесены в Красную Книгу '
                                                    'России и не встречаются более ни в одном зоопарке России.'
                                                    '\n\n<em>Адрес: ул. Ярошенко, 7Б</em>', parse_mode='html')
        file = open('./wake52.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Вейк-парк WAKE52</b>\n\n'
                                                    'Самый популярный вейк-парк города, команда которого профессионально ставит на вейк вот уже 10 лет.'
                                                    '\n\n<em>Адрес: Сормовский парк культуры и отдыха</em>', parse_mode='html')
        file = open('./34.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сормовский парк</b>\n\n'
                                                    'Сормовский парк - Парк культуры и отдыха им. А.А. Жданова был '
                                                    'задуман в 1920-х годах одновременно со строительством дворца культуры завода «Красное Сормово».'
                                                    '\n\n<em>Адрес: Сормовский парк культуры и отдыха</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'gsorr':
        file = open('./42.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Киш Миш</b>\n\n<em>Адрес: ул. Коминтерна, 105</em>', parse_mode='html')
        file = open('./43.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Киш Миш</b>\n\n<em>Адрес: ул. Коминтерна, 105</em>', parse_mode='html')
        file = open('./44.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Киш Миш</b>\n\n<em>Адрес: ул. Коминтерна, 105</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'hlr':
        file = open('./28.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк им.1 Мая</b>\n\n'
                                                    'Парк им.1 Мая — один из старейших в городе. Он был заложен в '
                                                    '1894 году и расположен на территории Всероссийской торгово-промышленной '
                                                    'и художественной выставки 1896 г. Нынешний Парк им. 1 Мая занимает '
                                                    '15,25 % территории выставки. В настоящее время инфраструктура '
                                                    'парка удовлетворяет потребности всех категорий населения, каждый '
                                                    'найдет в парке занятия по своему интересу.'
                                                    '\n\n<em>Адрес: Парк им.1 Мая</em>', parse_mode='html')
        file = open('./29.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Дубки</b>\n\n'
                                                    'Парк находится на месте исторического произрастания дубов возрастом более 100 лет.'
                                                    '\n\n<em>Адрес: парк Дубки</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'olr':
        file = open('./28.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Парк им.1 Мая</b>\n\n'
                                                    'Парк им.1 Мая — один из старейших в городе. Он был заложен в '
                                                    '1894 году и расположен на территории Всероссийской торгово-промышленной '
                                                    'и художественной выставки 1896 г. Нынешний Парк им. 1 Мая занимает '
                                                    '15,25 % территории выставки. В настоящее время инфраструктура '
                                                    'парка удовлетворяет потребности всех категорий населения, каждый '
                                                    'найдет в парке занятия по своему интересу.'
                                                    '\n\n<em>Адрес: Парк им.1 Мая</em>', parse_mode='html')
        file = open('./29.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Дубки</b>\n\n'
                                                    'Парк находится на месте исторического произрастания дубов возрастом более 100 лет.'
                                                    '\n\n<em>Адрес: парк Дубки</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'glr':
        file = open('./30.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Самурай</b>\n\n<em>Адрес: просп. Ленина, 36</em>', parse_mode='html')
        file = open('./31.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сова</b>\n\n<em>Адрес: просп. Ленина, 36</em>', parse_mode='html')
        file = open('./32.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Колизей</b>\n\n<em>Адрес: Минская ул., 16А</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'hnr':
        file = open('./15.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Нижегородский кремль</b>\n\n'
                                                    'Нижегородский кремль - Крепость в историческом центре Нижнего '
                                                    'Новгорода и его древнейшая часть, главный общественно-политический '
                                                    'и историко-художественный комплекс города. Официальная резиденция '
                                                    'полномочного представителя президента России в Приволжском '
                                                    'федеральном округе, губернатора Нижегородской области и мэра Нижнего Новгорода.'
                                                    '\n\n<em>Адрес: Кремль 6А</em>', parse_mode='html')
        file = open('./8.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Памятник Валерию Чкалову</b>\n\n'
                                                    'Памятник Валерию Чкалову - одна из достопримечательностей Нижнего '
                                                    'Новгорода, установлен вблизи Георгиевской башни Нижегородского '
                                                    'кремля в честь знаменитого советского лётчика, совершившего первый '
                                                    'беспосадочный перелёт из СССР в США через Северный полюс. От памятника '
                                                    'к Волге спускается Волжская лестница, которую также называют «Чкаловской».'
                                                    '\n\n<em>Адрес: улица Пожарского</em>', parse_mode='html')
        file = open('./9.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Памятник Максиму Горькому</b>\n\n'
                                                    'Памятник Максиму Горькому - находится в сквере на площади '
                                                    'Горького, был открыт 2 ноября 1952 года.'
                                                    '\n\n<em>Адрес: площадь Максима Горького</em>', parse_mode='html')
        file = open('./10.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Памятник Минину и Пожарскому</b>\n\n'
                                                    'Памятник Минину и Пожарскому - скульптурный монумент, посвящённый '
                                                    'предводителям Второго народного ополчения 1612 года, а также '
                                                    'окончанию Смутного времени и изгнанию польских интервентов из России.'
                                                    '\n\n<em>Адрес: Рождественская улица</em>', parse_mode='html')
        file = open('./1.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Площадь Минина и Пожарского</b>\n\n'
                                                    'Площадь Минина и Пожарского - главная площадь Нижнего Новгорода. '
                                                    'Является общественно-культурным центром города, местом проведения '
                                                    'всех наиболее значимых торжеств и праздников. Расположена в '
                                                    'исторической части города, с юго-восточной стороны от нагорной части Кремля.'
                                                    '\n\n<em>Адрес: площадь Минина и Пожарского</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('Гастрономия', callback_data='gkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'onr':
        file = open('./2.jpeg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Верхне-волжская набережная</b>\n\n'
                                                    'Верхне-волжская набережная (до революции — Георгиевская набережная, '
                                                    'в советское время — Верхне-Волжская набережная имени Жданова) — '
                                                    'набережная в историческом центре Нижнего Новгорода. Простирается '
                                                    'вдоль откоса к Волге от площади Минина и Пожарского до Сенной площади.'
                                                    '\n\n<em>Адрес: Верхне-волжская набережная</em>', parse_mode='html')
        file = open('./verxnevolzhskaya.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Дом Архитектора</b>\n\n'
                                                    'Дом Архитектора - одно из самых стильных зданий города Дом '
                                                    'Архитектора, здесь можно застать одну из регулярных прогрессивных '
                                                    'выставок, связанных с дизайном и архитектурой, сделать пару фото в '
                                                    'интерьере и посидеть в коворкинге на третьем этаже прямо у '
                                                    'панорамного окна с видом на Волгу и Чкаловскую лестницу.'
                                                    '\n\n<em>Адрес: Верхне-Волжская наб., 2</em>', parse_mode='html')
        file = open('./krasnaysloboda.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>«Красная Слобода»</b>\n\n'
                                                    '«Красная Слобода» - новообразованный кластер, находящийся в начало '
                                                    'Нижне-Волжской набережной. Здесь вы найдёте на выбор самую разную '
                                                    'кухню фудкорта «ПОРТ», попадёте на выставки актуальных художников '
                                                    'и вечеринки с крутыми хедлайнерами.'
                                                    '\n\n<em>Адрес: ул. Красная Слобода</em>', parse_mode='html')
        file = open('./XXXL.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Терминал А</b>\n\n'
                                                    '«Терминал А» – это выставочный центр, расположенный на территории '
                                                    'бывшей судоверфи, где проводятся выставки современного искусства и мастер-классы.'
                                                    '\n\n<em>Адрес: ул. Красная Слобода, 9</em>', parse_mode='html')
        file = open('./3.jpeg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Чкаловская лестница</b>\n\n'
                                                    'Чкаловская лестница - монументальная лестница в историческом центре '
                                                    'Нижнего Новгорода, соединяющая Верхне-Волжскую и Нижне-Волжскую '
                                                    'набережные. Построена по проекту архитекторов Александра Яковлева,'
                                                    ' Льва Руднева и Владимира Мунца. Являлась самой длинной лестницей '
                                                    'в России до аннексии Крыма.'
                                                    '\n\n<em>Адрес: Александровский сад</em>', parse_mode='html')
        file = open('./rakushka.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Александровский сад. Ракушка</b>\n\n'
                                                    'В верхней части сада можно найти необычное уличное кафе «Парк '
                                                    'Бистро» с кофе, лимонадами и сытными ланчами, там можно отдохнуть '
                                                    'на лежаках с видом на сад. Летним вечером вы можете тут не только '
                                                    'с удовольствием погулять и насладиться видами, но и попасть на '
                                                    'концерт программы «Столицы Закатов». Здесь на реконструированной к '
                                                    '800-летию города сцене «Ракушка» каждые выходные(летом) '
                                                    'организуются концерты как академической музыки, так и популярных '
                                                    'исполнителей со всей страны.'
                                                    '\n\n<em>Адрес: Александровский сад</em>', parse_mode='html')
        file = open('./4.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Улица Большая Покровская</b>\n\n'
                                                    'Улица Большая Покровская - главная улица Нижнего Новгорода. '
                                                    'Расположена в историческом центре города. Связывает 4 площади: '
                                                    'Минина и Пожарского, Театральную, Горького и Лядова. Одна из самых '
                                                    'старинных улиц. До 1917 года считалась дворянской. Оформилась как '
                                                    'главная улица города к концу XVIII века.'
                                                    '\n\n<em>Адрес: Улица Большая Покровская</em>', parse_mode='html')
        file = open('./5.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Набережная Федоровского</b>\n\n'
                                                    'Набережная Федоровского  — набережная в историческом районе '
                                                    'Започаинье Нижнего Новгорода. Современное название получила в честь '
                                                    'выдающегося учёного, доктора геолого-минералогических наук Николая '
                                                    'Михайловича Федоровского.'
                                                    '\n\n<em>Адрес: Набережная Федоровского</em>', parse_mode='html')
        file = open('./7.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Площадь Горького</b>\n\n'
                                                    'Площадь Горького — одна из центральных площадей Нижнего Новгорода. '
                                                    'Находится на пересечении улиц Большая Покровская и Максима Горького. '
                                                    'Площадь названа в честь писателя Максима Горького. В центре площади устроен сквер.'
                                                    '\n\n<em>Адрес: площадь Максима Горького</em>', parse_mode='html')
        file = open('./knizhnyii-novgorod.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Книжный на пл. Минина</b>\n\n'
                                                    '«Книжный Новгород» - большой новый книжный магазин. Название для '
                                                    'местных спорное (нижегородцы очень не любят, когда город путают с '
                                                    'Новгородом), зато место очень красивое, а подборка издательств и '
                                                    'авторов достойная. Место уже нарекли «нижегородскими Подписными» '
                                                    'за высокие панорамные окна, книжные полки под потолок и схожую '
                                                    'атмосферу.'
                                                    '\n\n<em>Адрес: ул. Алексеевская, 2</em>', parse_mode='html')
        file = open('./xoll-of-feim_0x0_061.jpeg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>«Холл-оф-фейм»</b>\n\n'
                                                    '«Холл-оф-фейм» популярное у молодежи и туристов место, недавно '
                                                    'ставшее предметом внимания. Это переулок, где стихийно на протяжении '
                                                    'последних пяти лет регулярно появляются работы самых разных '
                                                    'художников из Нижнего и других городов, настоящее «лоскутное '
                                                    'одеяло» стрит-арта, на фоне которого классно фотографироваться.'
                                                    '\n\n<em>Адрес: ул. Алексеевская, между домами 13Б и 13Д</em>', parse_mode='html')
        file = open('./molodost.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>«Молодость»</b>\n\n'
                                                    '«Молодость» - лавка рукотворных аксессуаров и сувениров. Помимо '
                                                    'прочих уникальных вещиц здесь можно найти и милые тематические '
                                                    'сувениры, посвященные Нижнему и его достопримечательностям.'
                                                    '\n\n<em>Адрес: ул. Октябрьская, 6</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hmr')
        btn4 = types.InlineKeyboardButton('Гастрономия', callback_data='gmr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    elif callback.data == 'gnr':
        file = open('./11.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Сoffee cake</b>\n\n<em>Адрес: Большая Покровская улица, 2</em>', parse_mode='html')
        file = open('./12.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Мoloko</b>\n\n<em>Адрес: Алексеевская ул., 15, лит.Б</em>', parse_mode='html')
        file = open('./13.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Хачапурия</b>\n\n<em>Адрес: Большая Покровская ул., 6</em>', parse_mode='html')
        file = open('./14.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Вспышка</b>\n\n'
                                                    '«Вспышка» - стильная пышечная, куда можно '
                                                    'заглянуть за кофе и парой горячих пышек (всего по 20 рублей!). '
                                                    'Помимо фотогеничного интерьера и недорогого перекуса здесь регулярно '
                                                    'можно застать небольшие выставки локальных художников, которые '
                                                    'команда пышечной организует по собственной инициативе.'
                                                    '\n\n<em>Адрес: Алексеевская ул., 11</em>', parse_mode='html')
        file = open('./bar.jpg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>«Селедка и кофе»</b>'
                                                    '\n\nПопулярное небольшое заведение в начале '
                                                    'гастрономической улицы — Рождественской. Летом здесь проходят '
                                                    'шумные вечеринки, а толпа у входа в заведение не расходится до самого утра.'
                                                    '\n\n<em>Адрес: ул. Рождественская, 19</em>', parse_mode='html')
        file = open('./port.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Фудкорт «ПОРТ»</b>\n\n<em>Адрес: ул. Красная Слобода</em>', parse_mode='html')
        file = open('./sovok.webp', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Совок</b>\n\n'
                                                    '«Совок» - самый молодежный местный стрит-фуд, '
                                                    'где можно насладиться хенд-мейд лапшой.'
                                                    '\n\n<em>Адрес: Большая Покровская ул., 2</em>', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('История и искусство', callback_data='hkr')
        btn4 = types.InlineKeyboardButton('Отдых и прогулка', callback_data='okr')
        markup.row(btn2, btn4)
        bot.send_message(callback.message.chat.id, 'Вот что ещё можно узнать об этом районе.\nВыбери с какой ещё '
                                                   'стороны ты бы хотел узнать этот район', reply_markup=markup)
    if callback.data == 'events':
        file = open('./liniy.jpeg', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Линия движется по бумаге и исчезает в лесу</b>\n\n'
                                                    'Более 60 графических листов, выполненных в экспериментальных, авторских техниках.'
                                                    '\nВыставочный проект представляет раннее творчество Сергея Проворова — '
                                                    'участника арт-группы «Провмыза», основанной в 1998 году вместе с Галиной Мызниковой.'
                                                    '\n\n<em>Место: Арсенал, Кремль, 6</em>', parse_mode='html')
        file = open('./starij.jfif', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>Гуляя по старому Нижнему</b>\n\n'
                                                    'Прогулка по Нижнему Новгороду, каким он был на рубеже XIX - XX веков.'
                                                    '\nВ экспозиции зрители совершают прогулку по Нижнему Новгороду, '
                                                    'каким он был на рубеже XIX - XX веков. Сопровождать посетителей '
                                                    'музея в этом путешествии будет Татьяна Павловна Виноградова — '
                                                    'известный педагог, краевед, профессор кафедры ЮНЕСКО ННГАСУ, '
                                                    'почетный гражданин Нижнего Новгорода, автор более двухсот '
                                                    'публикаций, посвященных городу и его культурному наследию.'
                                                    '\n\n<em>Место: НГХМ | Манеж, Кремль 1А</em>', parse_mode='html')
        file = open('./eo.jfif', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>С.С. Прокофьев «Евгений Онегин»</b>\n\n'
                                                    'Музыка к неосуществленному спектаклю Московского камерного театра по роману Пушкина.'
                                                    '\nВ «Евгении Онегине» Прокофьева соблюдены все законы '
                                                    'драматического театра. Музыка, сопровождающая актерские мизансцены,'
                                                    ' деликатно поддерживает произносимый ими текст. Вместе с тем, в '
                                                    'готовящемся спектакле должны были звучать и сольные оркестровые '
                                                    'фрагменты — лейтмотивы главных героев, танцевальные номера, '
                                                    'драматические музыкальные эпизоды, усиливающие напряжение событий '
                                                    'спектакля, вокализы и даже канцонетта Онегина на французском.'
                                                    '\n\n<em>Место: Концертный зал Пакгаузы, ул. Стрелка, д. 21Ж</em>', parse_mode='html')
        file = open('./NON SEMANTIC.jfif', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>NON SEMANTIC</b>\n\n'
                                                    'Погружение в альтернативное пространство в отрыве от повседневной реальности.'
                                                    '\nХудожники media.tribe — экспериментаторы, постоянно ищущие '
                                                    'нетипичные способы применения технологий в искусстве. В своих '
                                                    'проектах коллектив исследует коммуникацию со зрителем на уровне '
                                                    'эмоций и ощущений. Этот диалог выстраивается с помощью света, '
                                                    'звука и организации пространства.'
                                                    '\n\n<em>Место: Мультимедиа‑арт‑пространство ЦЕХ*, Варварская ул., 32</em>', parse_mode='html')
        file = open('./eb.jfif', 'rb')
        bot.send_photo(callback.from_user.id, file, '<b>ГОРИЗОНТ. К 90-летию Эрика Булатова</b>\n\n'
                                                    'Около 20 крупномасштабных произведений художника.'
                                                    '\nЭрик Булатов — один из ведущих представителей неофициального '
                                                    'искусства СССР. В Экспозиции представлено около 20 крупномасштабных '
                                                    'произведений художника, созданных с 1966 по 2010 год. Эксперимент '
                                                    'с пространством, перспективой, взаимодействием шрифта и живописи '
                                                    'сочетается в творчестве Булатова с высоким живописным мастерством. '
                                                    'Основу экспозиции составят произведения из частных российских '
                                                    'коллекций, которые редко показываются широкому кругу зрителей.'
                                                    '\n\n<em>Место: Выставочный центр Пакгаузы, мыс Стрелка</em>', parse_mode='html')
bot.polling(none_stop=True)