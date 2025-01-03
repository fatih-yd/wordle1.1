import random

from colorama import Fore, init
#Back, Style

init(autoreset=True)

with open("words5722.txt","r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    clear_words_list = icerik.split()
    #print(clear_words_list)


    #my_radom_word = choice(my_words_list)
        #daha kolay yapma yöntemi
    rnd = random.randint(0, len(clear_words_list) - 1)
    my_random_word = clear_words_list[rnd]
    my_random_word = my_random_word.lower()
    green_list = [" "] * 5
    yellow_list = [" "] * 5
    yellow_lists_list = list()
    my_random_word_piece_list = []
    print(my_random_word) #rastgele olan kelime


    #burada rastgele seçilmiş olan kelimeyi listeye parçalı şekilde ekliyoruz
    for i in my_random_word:
        my_random_word_piece_list.append(i)
    #print(my_random_word_piece_list)
    print(Fore.BLUE+">>>Wordle Oyununa Hoşgeldin<<<")

    guess_word_list = [" "] * 5
    tryy = 8
    while True:
        if tryy>0:
            control_1 = False
            guess_word = input(Fore.BLUE+">>>")

            for i in clear_words_list:
                if i.lower() == guess_word.lower():
                    control_1 = True
                else:
                    pass

            if len(guess_word) == 5:
                if control_1:  #"if control_1 == True" ile aynı şey
                    tryy -= 1

                    guess_word = guess_word.lower()
                    count_a = 0
                    for i in guess_word:
                        guess_word_list[count_a] = i
                        count_a += 1
                    print(guess_word_list)
                    count_g = 0
                    count_y =0
                    for a,b,c in zip(guess_word_list, my_random_word_piece_list,green_list): #burası yeşil olan(yeri doğru olan kelimeler) kısımı
                        if c == " " and  a==b:
                            green_list[count_g] = a

                        else:
                            pass
                        count_g += 1
                    print(Fore.GREEN+str(green_list))

                    for a in guess_word_list:   #burada sarı liste yapıldı
                        for b in my_random_word_piece_list:
                            if a == b :
                                yellow_list[count_y] = a
                        count_y +=1
                    yellow_lists_list.append(yellow_list.copy())
                    #print(Fore.YELLOW+str(yellow_list))

                    for i in yellow_lists_list:
                        print(Fore.YELLOW+str(i))

                    for i in range(0,len(yellow_list)):
                        yellow_list[i] = " "

                    control_1 = False
                    if my_random_word.lower() == guess_word:
                        print(Fore.GREEN+">>>Doğru Bildin Tebrikler<<<")
                        break
                    else:
                        pass
                    print(Fore.BLUE+f"******************{tryy} hakkınız kaldı******************")
                else:
                    print(Fore.RED +"UYARI!!!>>>",end="")
                    print(">>>Bu kelime listede yok,tekrar dene")
                    control_1 =False
            else:
                print(Fore.RED+"UYARI!!!>>>",end="")
                print("5 harfli bir kelime denemelisin")

        else:
            print(Fore.RED+"UYARI!!!>>>",end="")
            print("Giriş hakkın doldu")
            print(Fore.CYAN+f"Doğru Kelime: {my_random_word} ")
            break