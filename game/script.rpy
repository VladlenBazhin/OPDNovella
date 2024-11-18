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

    "Звуки геймплея."
    $ renpy.sound.play(gp_sound)
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

    dad "Ваня, я понимаю, что у тебя каникулы, что ты успешно закончил школу, но пора задуматься об институте."
    show dad normal small at Position(xalign=0.82) 
    show gg talk 2 small lt at Position(xalign=0.18)

    gg "Пап, я помню скоро этим займусь."   

    dad "Надеюсь на это, сына."  

    hide dad gg
    ##scene 3-3.1
    scene bg room with dissolve 
    $ renpy.sound.play(unmute_sound)
    friend "#Слушай, ну реально у тебя папа прав, ты всё время сидишь за компом, займись уже чем-нибудь действительно полезным.#"
    
    gg "Угу."
    
    friend "#Ладно давай спокойной ночи.#"

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

    show dad angry talk 2 small at Position(xalign=0.82)

    dad "Ваня, опять ты весь день играл как ты мне уже надоел со своими играми!"

    show gg bruh small lt at Position(xalign=0.18)
    gg "Ум..."
    show gg talk 2 small lt at Position(xalign=0.18)
    gg "Нет папа, ты не прав, я всю ночь изучал специальности, на которые буду подавать документы!"

    show dad talk 2 small at Position(xalign=0.82)

    dad "Решил на что будешь подавать!?"

    gg "Да, на “Прикладную информатику” в УрФУ."

    dad "Ну ладно, молодец, это серьёзный и тяжёлый выбор!"

    hide gg dad

    ##Scene 6
    scene purple

    storyteller "Ваня поехал подавать документы в институт."

    ##Scene 7-7.1
    scene purple

    storyteller "Ваня стоял ошеломленный красотой и масштабностью здания, именно в этот момент он точно понял, что будет учится здесь!"
    storyteller "Подав документы, он отправился обратно в свой родной город, поскольку до начала учёбы был еще целый месяц."

    ##Scene 8
    teacher "Дорогие ученики поздравляю вас всех с началом учёбы! Первые 2 недели у вас будут вводные, а под конец этих 2-х недель у вас будет выбор индивидуальной образовательной траектории."

    ##Scene 9-9.1
    teacher "Вы выберете профессию, на которую будете обучаться весь семестр. По окончании семестра, если она вам не понравится, вы сможете её поменять."
    gg "*Ого звучит интересно и одновременно страшно!*"

    ##Scene 10-10.1
    storyteller "Сегодня, все студенты одновременно будут выбирать профессию, на которую они будут учиться!"
    gg "*Надо успеть всё сделать быстро пока не заняли профессии, которые я для себя присмотрел!*"

    ##Scene 11
    menu:
        "3-D моделирование для игровой или смежной сферы":
            # Действия, если игрок выбрал первый вариант
            "1"
        
        "Python разработчик":
            # Действия, если игрок выбрал второй вариант
            "2"

        "Сисадмин":
            "3"

        "UX/UI дизайн":
            "4"

    return
