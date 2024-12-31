# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('Ваня', color="#1aa61e")
define dad = Character('Папа', color="#f50c0c")
define friend = Character('Друг', color="#03a9ff")
define teacher = Character('Преподаватель', color="#a4afb4")
define storyteller = Character('Закадровый голос', color="#e7d713")
define newFriend = Character('Вася', color="#e78513")
define parents = Character('Родители', color="#871ec5")
define mom = Character('Мама', color="#da1cf7")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    #scene 1
    $ renpy.music.play(bg_music, loop=True)  # Включаем музыку с циклическим воспроизведением
    scene bg display

    $ renpy.sound.play(gp_sound)
    "Звуки геймплея."
    
    window hide
    $ renpy.pause()

    # scene 2
    scene bg room with dissolve

    
    $ renpy.pause() 

    scene bg dad and son with dissolve 
    window show
    storyteller "К главному герою, играющему в компьютерные игры, подходит Папа и хлопает его по плечу."

    ##scene 2.1-2.3
    scene bg room with fade
    scene bg room blured with dissolve 

    show dad normal
    $ renpy.pause()
    show dad talk 2 with dissolve 

    dad "Ваня, я понимаю, что у тебя каникулы, что ты успешно закончил школу, но пора задуматься о выборе института."
    show dad normal small at Position(xalign=0.82) 
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Пап, я помню, скоро этим займусь." 

    show dad talk 2 small at Position(xalign=0.82)
    dad "Надеюсь на это, сына."  

    hide dad gg

    ##scene 3-3.1
    scene bg room with dissolve 
    $ renpy.sound.play(unmute_sound)

    friend "#Слушай, ну реально у тебя папа прав, ты всё время сидишь за компом, займись уже чем-нибудь действительно полезным.#"
    gg "Может ещё катку сыграем?"
    friend "#Я не могу, у меня завтра тренировка рано утром. Лучше прислушайся к словам отца!#"
    gg "Слушай, я сам разберусь что для меня лучше, иди давай уже, школьник!"
    friend "#Мдааа, так друзей и теряют!#"
    gg "Пока."

    $ renpy.sound.play(disconnect_sound)
    $ renpy.pause()

    ##scene 4
    scene bg room tw with dissolve 
    $ renpy.pause()
    storyteller "Ваня всё-таки садится смотреть специальности, на которые ведёт институт набор."
    window hide
    scene bg house tw with fade
    $ renpy.pause()
    scene bg house sun with fade
    $ renpy.pause()
    ##scene 5-5.4
    scene bg room with fade
    $ renpy.pause()
    scene bg room blured with dissolve 

    show dad angry talk 2 small at Position(xalign=0.82)

    dad "Ваня, опять ты весь день играл как ты мне уже надоел со своими играми!"

    show dad angry small at Position(xalign=0.82)

    show gg bruh small lt at Position(xalign=0.18)

    gg "Ум..."

    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Нет папа, ты не прав, я всю ночь изучал специальности, на которые буду подавать документы!"

    show gg normal small lt at Position(xalign=0.18)
    show dad talk 2 small at Position(xalign=0.82)

    dad "Решил на что будешь подавать!?"

    show dad normal small at Position(xalign=0.82)
    show gg talk 2 small lt at Position(xalign=0.18)
    
    gg "Да, на “Прикладную информатику” в УрФУ."

    show gg normal small lt at Position(xalign=0.18)
    show dad talk 2 small at Position(xalign=0.82)

    dad "Ну ладно, молодец, это серьёзный и тяжёлый выбор!"

    hide gg dad

    ##Scene 6
    scene bg bus with fade

    storyteller "Ваня поехал подавать документы в институт."

    ##Scene 7-7.1
    scene bg_urfu with fade

    storyteller "Ваня стоял ошеломленный красотой и масштабностью здания, именно в этот момент он точно понял, что будет учится здесь!"
    $ renpy.pause()

    scene bg bus mirror with fade
    storyteller "Подав документы, он отправился обратно в свой родной город, поскольку до начала учёбы был еще целый месяц."

    ##Scene 8
    scene black with fade

    storyteller "Настало время учёбы."
    storyteller "Слегка промозглое сентябрьское утро, под моросязий дождь, Ваня спешит на свою первую пару, как и тысячи студентов сегодня."
    $ renpy.sound.play(crowd_sound)
    storyteller "Ваня рад началу учёбы. Да и при заселении в общежитие успел завести друзей."
    
    scene bg class happy with fade
    $ renpy.pause()
    scene bg class happy blured with dissolve
    show teacher talk
    teacher "Дорогие ученики поздравляю вас всех с началом учёбы! Первые 2 недели у вас будут вводные, а под конец этих 2-х недель у вас будет выбор индивидуальной образовательной траектории."

    ##Scene 9-9.1
    teacher "Вы выберете профессию, на которую будете обучаться весь семестр. По окончании семестра, если она вам не понравится, вы сможете её поменять."
    show teacher talk with dissolve
    gg "*Ого звучит интересно и одновременно страшно!*"
    hide teacher

    ##Scene 10-10.1
    scene bg hostel with dissolve
    storyteller "Сегодня, все студенты одновременно будут выбирать профессию, на которую они будут учиться!"
    gg "*Надо успеть всё сделать быстро пока не заняли профессии, которые я для себя присмотрел!*"

    ##Scene 11
    call screen choice_menu

    $ resultChoice = _return

    # Обработка результата.
    if resultChoice == "modeling":
        $ path = "modeling"
    elif resultChoice == "python":
        $ path = "python"
    elif resultChoice == "sysadmin":
        $ path = "sysadmin"
    elif resultChoice == "design":
        $ path = "design"

    ##Scene 12
    scene bg hostel with dissolve
    gg "*Фух, ну вроде выбрал что хотел, посмотрим что будет дальше!*"

    ##Scene 13-13.4
    scene bg class happy with fade
    storyteller "Прошло 2 месяца. Ваня успел сдружиться с Васей."

    scene bg class happy blured with dissolve

    show gg normal small lt at Position(xalign=0.18)
    show nfriend talk 2 small at Position(xalign=0.82)

    newFriend "Ваня, ну как тебе учёба?"

    show gg talk 2 small lt at Position(xalign=0.18)
    show nfriend normal small at Position(xalign=0.82)

    gg "Слушай, так много разных и интересных предметов. У меня удобное расписание получилось составить. Очень много различных курсов надо проходить на дому. Как-то тяжело всё даётся."

    show gg normal small lt at Position(xalign=0.18)
    show nfriend talk 2 small at Position(xalign=0.82)

    newFriend "Тебе тоже по началу тяжело было разобраться во всех этик курсах?"

    show gg talk 2 small lt at Position(xalign=0.18)
    show nfriend normal small at Position(xalign=0.82)

    gg "Да! Не особо понятно было, но тьютор помог во всём разобраться."

    hide gg nfriend
    ##Scene 14-15
    scene bg class sad with dissolve

    storyteller "Прошёл еще месяц."

    scene bg class sad blured with dissolve

    show gg normal small lt at Position(xalign=0.18)
    show nfriend talk 2 small at Position(xalign=0.82)

    newFriend "Кстати, давно хотел поинтересоваться, какие у тебя профильные предметы?"

    show gg talk 2 small lt at Position(xalign=0.18)
    show nfriend normal small at Position(xalign=0.82)

    $ profession_data = {
        "modeling": "Ну поскольку я учусь на 3-D моделирование, то у меня: компьютерная графика, игровая разработка, введение в индустрию VR. На следующих курсах, будут добавляться всё новые и новые предметы.",
        "python": "Ну поскольку я учусь на Python разработчика, то у меня: программирование на этом языке, мобильная разработка, тестирования ПО, основы игровых механик. На следующих курсах, будут добавляться всё новые и новые предметы.",
        "sysadmin": "Ну поскольку я учусь на Сисадмина, то у меня: аналитик качества системы, системный анализ, администрирование. На следующих курсах, будут добавляться всё новые и новые предметы.",
        "design": "Ну поскольку я учусь на UX/UI дизайнера, то у меня: естественно основы дизайна, трёхмерная визуализация, проектирование интерфейсов. На следующих курсах, будут добавляться всё новые и новые предметы."
    }

    if path in profession_data:
        gg "[profession_data[path]]"

        show gg normal small lt at Position(xalign=0.18)
        show nfriend talk 2 small at Position(xalign=0.82)

        hide gg 
        hide nfriend

        newFriend "Ты какой-то задумчивый, что случилось?"

        menu:
            "Мне не нравится учиться на мою профессию":
                jump notLike
            "Не спал всю ночь, делал уроки.":
                newFriend "Хах, знакомо."
                jump expression path

label notLike:
    ##scene 15.1-15.6
    
    show gg normal small lt at Position(xalign=0.18)
    show nfriend talk 2 small at Position(xalign=0.82)

    newFriend "Ого, это серьёзно, ну ты главное не опускай руки, по окончании семестра ты сможешь поменять свою профессию на другую."

    show gg talk 2 small lt at Position(xalign=0.18)
    show nfriend normal small at Position(xalign=0.82)

    gg "Да надеюсь на это." 

    show gg normal small lt at Position(xalign=0.18)
    show nfriend talk 2 small at Position(xalign=0.82)

    newFriend "У меня пока всё нормально, хоть и много заданий. Особенно по математике."

    show gg talk 2 small lt at Position(xalign=0.18)
    show nfriend normal small at Position(xalign=0.82)

    gg "О, математика – это боль! Я недавно чуть не завалил контрольную."

    show gg normal small lt at Position(xalign=0.18)
    show nfriend talk 2 small at Position(xalign=0.82)

    newFriend "Кошмар! Мне кажется, преподаватели объясняют доступно. Важно не пропускать занятия."

    show gg talk 2 small lt at Position(xalign=0.18)
    show nfriend normal small at Position(xalign=0.82)

    gg "Согласен. Надо держаться и не сдаваться!"
    
    hide gg nfriend
    ##scene 16
    scene bg hostel
    storyteller "заканчивается 1-й семестр."
    gg "Надо подумать о смене направления своего обучения на другую профессию!"

    ##Scene 17
    if path == "modeling":
        menu:
            "Python разработчик":
                gg "Точно, выберу это!"
                jump python
            "Сисадмин":
                gg "Точно, выберу это!"
                jump sysadmin
            "UX/UI дизайн":
                gg "Точно, выберу это!"
                jump design

    elif path == "python":
        menu:
            "3-D моделирование для игровой или смежной сферы":
                gg "Точно, выберу это!"
                jump modeling
            "Сисадмин":
                gg "Точно, выберу это!"
                jump sysadmin
            "UX/UI дизайн":
                gg "Точно, выберу это!"
                jump design

    elif path == "sysadmin":
        menu:
            "3-D моделирование для игровой или смежной сферы":
                gg "Точно, выберу это!"
                jump modeling
            "Python разработчик":
                gg "Точно, выберу это!"
                jump python
            "UX/UI дизайн":
                gg "Точно, выберу это!"
                jump design

    elif path == "design":
        menu:
            "3-D моделирование для игровой или смежной сферы":
                gg "Точно, выберу это!"
                jump modeling
            "Python разработчик":
                gg "Точно, выберу это!"
                jump python
            "Сисадмин":
                gg "Точно, выберу это!"
                jump sysadmin
        

label modeling:
    ##Scene 18
    scene bg hostel winter with fade
    $ renpy.music.play(bg_music_2, loop=True)
    storyteller "Прошло больше года с момента выбора профессии. Теперь Ваня полностью увлечён своей учёбой, сейчас у него предметы такие как: трёхмерное моделирование, трёхмерная визуализация, работа в KOMPAS – 3D."
    $ renpy.pause()

    ##Scene 19-19.2
    scene bg hi yandex with fade
    storyteller "Ваня проходит практики в самых престижных копаниях страны (Яндекс, Росатом, Газпром)."
    storyteller "На практиках Ваня углублённо изучает свою профессию, общается со специалистами в этой сфере, на практических примерах закрепляет пройденный материал."
    storyteller "И вот, постепенно подходит время выпускных экзаменов и защиты диплома."

    ##Scene 20-20.1
    scene bg senior student with fade
    $ renpy.pause()
    scene bg senior student  blured with dissolve
    show teacher talk 
    
    teacher "Ну что, ученики, я надеюсь вы подготовились к экзамену, желаю вам удачи!"
    
    hide teacher

    gg "*Я справлюсь!*"

    ##Scene 21-21.6
    $ rightAnswer = 0
    label questionModeling1:
        call screen modeling_question1()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Молодец, да действительно, трёхмерная графика применяется повсюду!"
            jump questionModeling2
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionModeling2

    label questionModeling2:
        call screen modeling_question2()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Да правильно, в трёхмерной графике применяется множество программ и это одна из них!"
            jump questionModeling3
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionModeling3
        

        label questionModeling3:
        call screen modeling_question3()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump resultModeling
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher "Неправильный ответ."
            jump resultModeling

    label resultModeling:
        if rightAnswer < 2:
            teacher "Очень плохо!"
            teacher "Приходи на пересдачу."
            $ renpy.pause()
            jump questionModeling1
        else:
            teacher "Прекрасно! Вы сдали экзамен!"
            jump diplom


label python:
    ##Scene 18
    scene bg hostel winter with fade
    $ renpy.music.play(bg_music_2, loop=True)
    storyteller "Прошло больше года с момента выбора профессии. Теперь Ваня полностью увлечён своей учёбой, сейчас у него предметы такие как: WEB- программирование, многопоточное программирование, разработка игр. "

    ##Scene 19-19.2
    scene bg hi yandex with fade
    storyteller "Ваня проходит практики в самых престижных копаниях страны (Яндекс, Росатом, Газпром)."
    storyteller "На практиках Ваня углублённо изучает свою профессию, общается со специалистами в этой сфере, на практических примерах закрепляет пройденный материал."
    storyteller "И вот, постепенно подходит время выпускных экзаменов и защиты диплома."

    ##Scene 20-20.1
    scene bg senior student with fade
    $ renpy.pause()
    scene bg senior student  blured with dissolve
    show teacher talk 
    
    teacher "Ну что, ученики, я надеюсь вы подготовились к экзамену, желаю вам удачи!"
    
    hide teacher

    gg "*Я справлюсь!*"

    ##Scene 21-21.6
    $ rightAnswer = 0
    label questionPython1:
        call screen python_question1()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Да правильно!"
            jump questionPython2
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionPython2

    label questionPython2:
        call screen python_question2()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Молодец, да действительно, все выше перечисленные варианты верны!"
            jump questionPython3
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionPython3
        

        label questionPython3:
        call screen python_question3()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump resultPython
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher "Неправильный ответ."
            jump resultPython

    label resultPython:
        if rightAnswer < 2:
            teacher "Очень плохо!"
            teacher "Приходи на пересдачу."
            $ renpy.pause()
            jump questionPython1
        else:
            teacher "Прекрасно! Вы сдали экзамен!"
            jump diplom

label sysadmin:
    ##Scene 18
    scene bg hostel winter with fade
    $ renpy.music.play(bg_music_2, loop=True)
    storyteller "Прошло больше года с момента выбора профессии. Теперь Ваня полностью увлечён своей учёбой, сейчас у него предметы такие как: теория автоматического управления, системное администрирование, курсы по использованию Git."

    ##Scene 19-19.2
    scene bg hi yandex with fade
    storyteller "Ваня проходит практики в самых престижных копаниях страны (Яндекс, Росатом, Газпром)."
    storyteller "На практиках Ваня углублённо изучает свою профессию, общается со специалистами в этой сфере, на практических примерах закрепляет пройденный материал."
    storyteller "И вот, постепенно подходит время выпускных экзаменов и защиты диплома."

    ##Scene 20-20.1
    scene bg senior student with fade
    $ renpy.pause()
    scene bg senior student  blured with dissolve
    show teacher talk 
    
    teacher "Ну что, ученики, я надеюсь вы подготовились к экзамену, желаю вам удачи!"
    
    hide teacher

    gg "*Я справлюсь!*"

    ##Scene 21-21.6
    $ rightAnswer = 0
    label questionSysadmin1:
        call screen sysadmin_question1()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump questionSysadmin2
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionSysadmin2

    label questionSysadmin2:
        call screen sysadmin_question2()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump questionSysadmin3
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionSysadmin3
        

        label questionSysadmin3:
        call screen sysadmin_question3()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump resultSysadmin
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher "Неправильный ответ."
            jump resultSysadmin


    label resultSysadmin:
        if rightAnswer < 2:
            teacher "Очень плохо!"
            teacher "Приходи на пересдачу."
            $ renpy.pause()
            jump questionSysadmin1
        else:
            teacher "Прекрасно! Вы сдали экзамен!"
            jump diplom

label design:
    ##Scene 18
    scene bg hostel winter with fade
    $ renpy.music.play(bg_music_2, loop=True)
    storyteller "Прошло больше года с момента выбора профессии. Теперь Ваня полностью увлечён своей учёбой, сейчас у него предметы такие как: дизайн-мышление, исследование пользователей, UX-дизайн, UI-дизайн."

    ##Scene 19-19.2
    scene bg hi yandex with fade
    storyteller "Ваня проходит практики в самых престижных копаниях страны (Яндекс, Росатом, Газпром)."
    storyteller "На практиках Ваня углублённо изучает свою профессию, общается со специалистами в этой сфере, на практических примерах закрепляет пройденный материал."
    storyteller "И вот, постепенно подходит время выпускных экзаменов и защиты диплома."

    ##Scene 20-20.1
    scene bg senior student with fade
    $ renpy.pause()
    scene bg senior student  blured with dissolve
    show teacher talk 
    
    teacher "Ну что, ученики, я надеюсь вы подготовились к экзамену, желаю вам удачи!"
    
    hide teacher

    gg "*Я справлюсь!*"

    ##Scene 21-21.6
    $ rightAnswer = 0
    label questionDesign1:
        call screen design_question1()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump questionDesign2
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionDesign2

    label questionDesign2:
        call screen design_question2()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump questionDesign3
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher " Неправильный ответ."
            jump questionDesign3
        

        label questionDesign3:
        call screen design_question3()

        $ resultQuestion = _return

        if resultQuestion == "right":
            scene bg senior student
            $ rightAnswer +=1
            $ renpy.sound.play(right_answer_sound)
            teacher "Правильный ответ!"
            jump resultDesign
        else:
            scene bg senior student sad
            $ renpy.sound.play(wrong_answer_sound)
            teacher "Неправильный ответ."
            jump resultDesign

    label resultDesign:
        if rightAnswer < 2:
            teacher "Очень плохо!"
            teacher "Приходи на пересдачу."
            $ renpy.pause()
            jump questionDesign1
        else:
            teacher "Прекрасно! Вы сдали экзамен!"
            jump diplom


label diplom:
    ##Scene 22
    scene bg  defence of dissertations with fade

    storyteller "Ваня уверенно защищает диплом, поскольку приложил большое количество услий в его подготовке!"
    $ renpy.pause()

    ##Scene 23
    scene bg graduation ceremony with fade

    storyteller "Ваня получает диплом с отличием, он безумно этому рад!"
    $ renpy.pause()

    ##Scene 24-24.3
    scene bg hugs parents with fade
    $ renpy.pause()
    scene bg hugs parents blured with dissolve

    show dad talk 2 small at Position(xalign=0.65)
    show mom talk small at Position(xalign=0.82)  
    show gg smile small lt at Position(xalign=0.18)

    parents "Сынок, молодец, мы в тебя всегда верили! Ты будешь отличным специалистом!"

    show dad normal small at Position(xalign=0.65)
    show mom normal small at Position(xalign=0.82)  
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Спасибо за вашу поддержку, без вас я бы не справился!"

    show mom talk small at Position(xalign=0.82)  
    show gg smile small lt at Position(xalign=0.18)

    mom "Что будешь делать дальше?"

    show mom normal small at Position(xalign=0.82)  
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Пойдёмте в кафе там и расскажу!"

    show gg talk 2 small lt at Position(xalign=0.18)

    ##Scene 25-25.3
    scene bg cafe wt parents with dissolve
    $ renpy.pause()
    scene bg cafe wt parents blured with dissolve

    show dad normal small at Position(xalign=0.65)
    show mom talk small at Position(xalign=0.82)  
    show gg smile small lt at Position(xalign=0.18)

    mom  "Ну что ты решил где будешь жить?"

    show mom normal small at Position(xalign=0.82)  
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Да, останусь жить в Екатеринбурге!"
    gg "В этом городе столько возможностей, друзей тут у меня много, да и..."
    gg "я уже привык к нему."

    show dad talk 2 small at Position(xalign=0.65)
    show gg smile small lt at Position(xalign=0.18)
    dad "А работать ты где будешь?"

    hide gg 
    hide mom 
    hide dad

    menu:
        "Мне пришло приглашение на собеседование в очень неплохую IT компанию, схожу туда и посмотрю, что мне смогут там предложить.":
            jump office
        "Я решил работать на фрилансе.":
            jump freelans

label office:
    $ officialWork = 1
    ##Scene 25.4-25.5
    show dad normal small at Position(xalign=0.65)
    show mom talk small at Position(xalign=0.82)  
    show gg smile small lt at Position(xalign=0.18)

    mom "Ого, круто, поздравляю! Будет у тебя стабильный заработок и хорошая зарплата!"

    show mom normal small at Position(xalign=0.82)  
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Спасибо, через 2 недели иду на собеседование!"
    jump cafeAndEpilogue

label freelans:
    ##Scene 25.4-25.8
    show dad normal small at Position(xalign=0.65)
    show mom talk small at Position(xalign=0.82)  
    show gg smile small lt at Position(xalign=0.18)

    mom "Это как?"

    show mom normal small at Position(xalign=0.82)  
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Это когда я выполняю работу по просьбе разных компаний без долгосрочных контрактов."

    show mom talk small at Position(xalign=0.82)  
    show gg smile small lt at Position(xalign=0.18)

    mom "Ого, сынок ты понимаешь, что это не стабильная работа, что ты целый месяц или больше можешь сидеть без работы!"

    show mom normal small at Position(xalign=0.82)  
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Да мам, я это понимаю, но я не хочу работать в сжатых рамках, я хочу свободы, выполнять разные задачи, по своему желанию!"

    show mom talk small at Position(xalign=0.82)  
    show gg smile small lt at Position(xalign=0.18)

    mom "Ладно, сынок, надеюсьты сделал правильный выбор. Я тебе доверяю."
    jump cafeAndEpilogue

label cafeAndEpilogue:
    ##Scene 26-26.1
    storyteller "Прошло 4 месяца."
    if officialWork > 0:
        scene bg office with fade
        storyteller "Ваня сидел и спокойно работал в компании, и тут ему пишет Вася."
    else:
        scene bg freelans with fade
        storyteller "Ваня сидел и спокойно работал у себя дома, и тут ему пишет Вася."

    newFriend "Привет!"
    gg "Алоха!"
    newFriend "Не хочешь пересечься? Посидим где-нибудь."
    gg "Да, конечно! Буду рад."

    ##Scene 27-27.5
    $ profession_dialog1 = {
        "modeling": "Я решил удариться в работу и в карьеру. Сейчас работаю в IT компании, на перспективной должности, занимаюсь 3-D моделированием для одной игры. ",
        "python": "Я решил удариться в работу и в карьеру. Сейчас работаю в IT компании, на перспективной должности, занимаюсь написанием одного приложения для пользователей.",
        "sysadmin": "Я решил удариться в работу и в карьеру. Сейчас работаю в IT компании, на перспективной должности, занимаюсь устранением проблем для работников этой компании.",
        "design": "Я решил удариться в работу и в карьеру. Сейчас работаю в IT компании, на перспективной должности, занимаюсь обновлением интерфейса для приложения."
    }
    
    $ profession_dialog2 = {
        "modeling": "Ну смотри, мне поставили задачу, смоделировать определённые предметы для игры. Как завершу эту задачу, мне дадут следующую.",
        "python": "Ну смотри, мне поставили задачу, разработать определённый блок кода, который будет выполнять определённую задачу. Как завершу эту задачу, мне дадут следующую.",
        "sysadmin": "Ну смотри, мне каждый день дают список проблем, которые я должен устранить. Как закончу с этими ошибками, мне дадут следующие, помимо есть проекты по внедрению.",
        "design": "Ну смотри, мне поставили задачу, привести в порядок некую часть интерфейса и добавить несколько новых функций. Как завершу эту задачу, мне дадут следующую."
    }

    $ profession_dialog3 = {
        "modeling": "Я решил удариться в работу. Работаю фрилансером, беру заказы от разных людей на разных площадках. Составляю своё портфолио, для большего доверия от клиентов, сейчас у меня в работе несколько моделей для одного из клиентов.",
        "python": "Я решил удариться в работу. Работаю фрилансером, беру заказы от разных людей на разных площадках. Составляю своё портфолио, для большего доверия от клиентов, сейчас у меня в разработке код для одного клиента.",
        "sysadmin": "Я решил удариться в работу. Работаю фрилансером, беру заказы от разных людей на разных площадках. Составляю своё портфолио, для большего доверия от клиентов, сейчас я работаю с несколькими компаниями по администрированию их сайтов.",
        "design": "Я решил удариться в работу. Работаю фрилансером, беру заказы от разных людей на разных площадках. Составляю своё портфолио, для большего доверия от клиентов, сейчас у меня в работе оформление сайта для клиента."
    }
    
    $ profession_dialog4 = {
        "modeling": "Ну смотри, мне дали зарисовки и размеры предметов, которые мне надо смоделировать в 3-D.",
        "python": "Ну смотри, мне дали список того, что должен делать мой код и где он будеи применятся.",
        "sysadmin": "Ну смотри, есть много маленьких компаний которые не могу себе позволить постоянного сисадмина, а я решаю их проблемы. Так сказать снимаю их головную боль.",
        "design": "Ну смотри, у меня задача полность нарисовать сайт, все вкладки, кнопки, что будет открываться наживая на них."
    }
    
    scene bg cafe wt vasya with fade
    "..."
    gg "Поздравляю тебя! Надеюсь, у тебя всё получится в новом городе!"
    newFriend "Спасибо! Ну расскажи, как у тебя дела, чем занимаешься?" 


    if officialWork > 0:
        if path in profession_dialog1:
            gg "[profession_dialog1[path]]"
            newFriend "Звучит интересно, расскажи поподробнее!"
            gg "[profession_dialog2[path]]"
            gg "Надеюсь она будет ещё интереснее."
            gg "С начальником мне повезло, он хоть и требовательный, но и юмор в нём проскакивает. В целом, мне нравится там работать!"
    elif path in profession_dialog3:
            gg "[profession_dialog3[path]]"
            newFriend "Звучит интересно, расскажи поподробнее!"
            gg "[profession_dialog4[path]]"
            gg "Работаю сколько захочу и сколько надо, максимально гибкий график, работаю то дома, то на улице за ноутбуком. Не работа, а мечта!"


    newFriend "Рад был видеть!"
    gg "Я тоже! Надо будет как-нибудь ещё посидеть."
    newFriend "Это точно"

    ##Scene Epilogue
    scene black with fade
    storyteller "И вот вы увидели историю обычного студента из провинциального городка."
    storyteller "Который прошёл долгий путь обучения. Который заёл друзей. "
    storyteller "Который нашёл своё место в жизни и получил плоды от своих стараний."
    window hide
    play movie the_end
    $ renpy.pause()


    return
