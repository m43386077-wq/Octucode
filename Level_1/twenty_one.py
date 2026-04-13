import os
from random import choice
from time import sleep
from pyfiglet import figlet_format

LOGO = figlet_format("TWENTYONE")
CARDS = {
    # Spades - البستوني ♠
    "🂡": 1, "🂢": 2, "🂣": 3, "🂤": 4, "🂥": 5, "🂦": 6, "🂧": 7, "🂨": 8, "🂩": 9, "🂪": 10, "🂫": 10, "🂭": 10, "🂮": 10,

    # Hearts - القلوب ♥
    "🂱": 1, "🂲": 2, "🂳": 3, "🂴": 4, "🂵": 5, "🂶": 6, "🂷": 7, "🂸": 8, "🂹": 9, "🂺": 10, "🂻": 10, "🂽": 10, "🂾": 10,

    # Diamonds - الديناري ♦
    "🃁": 1, "🃂": 2, "🃃": 3, "🃄": 4, "🃅": 5, "🃆": 6, "🃇": 7, "🃈": 8, "🃉": 9, "🃊": 10, "🃋": 10, "🃍": 10, "🃎": 10,

    # Clubs - السباتي ♣
    "🃑": 1, "🃒": 2, "🃓": 3, "🃔": 4, "🃕": 5, "🃖": 6, "🃗": 7, "🃘": 8, "🃙": 9, "🃚": 10, "🃛": 10, "🃝": 10, "🃞": 10
}
    
deck = list(CARDS.keys())

def clear_screen():
    """مسح الشاشة وطباعة الشعار"""
    os.system("cls" if os.name == "nt" else "clear")
    print(LOGO)

def get_card():
    """الحصول على كارت عشوائي وحذفه من قائمة الكروت"""
    card = choice(deck)
    deck.remove(card) 
    return card

def calc_score(player_cards):
    """حساب قيمة الكروت"""
    scores = [CARDS[card] for card in player_cards]
    
    #إستبدال قيمة الكارت 1 في حال كان استبداله في مصلحة اللاعب 
    if 1 in scores and sum(scores) + 10 <= 21:
        scores.remove(1)
        scores.append(11)

    return sum(scores)
        
def print_cards(player_cards, computer_cards, one=True):
    """طباعة الكروت التي مع اللاعب وأول كارت أو كل الكروت التي مع الموزع"""
    
    print(f"\n===== Your Cards (Score: {calc_score(player_cards)}) =====")
    print(" ".join(player_cards))

    if one:
        print("\n===== Computer's First Card (Score: ?)=====")
        print(computer_cards[0] + " 🂠")
        return
    
    print(f"\n===== Computer's Cards (Score: {calc_score(computer_cards)}) =====")
    print(" ".join(computer_cards))

def print_final_result(player_cards, computer_cards):
    """التحقق من الفائز وطباعة النتيجة النهائية"""
    
    clear_screen()
    print_cards(player_cards, computer_cards, False)

    # التحقق في حالة كانت قيمتا كروت اللاعب وكروت الموزع أقل من 21 
    if calc_score(computer_cards) < 21 and calc_score(player_cards) < 21:
        
        # حالة الفوز 
        if (21 - calc_score(player_cards)) < (21 - calc_score(computer_cards)):
            print("Cogratulations\nYou win 🏆🏆🏆")
            
        # حالة التعادل 
        elif calc_score(player_cards) == calc_score(computer_cards):
            print("Draw 😐😐")

        # حالة الخسارة 
        elif (21 - calc_score(player_cards)) > (21 - calc_score(computer_cards)):
            print("You lost 😥😥")   
    
    #حالة الفوز 
    elif (calc_score(player_cards) == 21 and calc_score(computer_cards) != 21) or (calc_score(computer_cards) > 21 and calc_score(player_cards) <= 21):
        print("Congratulations\nYou win 🏆🏆🏆")

    #حالة التعادل 
    elif (calc_score(player_cards) > 21 and calc_score(computer_cards) > 21) or (calc_score(player_cards) == 21 and calc_score(computer_cards) == 21):
        print("Draw 😑😑") 

    #حالة الخسارة 
    elif (calc_score(player_cards) > 21 and calc_score(computer_cards) <= 21) or (calc_score(computer_cards) == 21 and calc_score(player_cards)!= 21):
        print("You lost 😥😥")
        
def main():

    global deck
    deck = list(CARDS.keys())

    # توزيع أول كرتين على الموزع واللاعب 
    computer_cards = [get_card() for _ in range(2)]
    player_cards = [get_card() for _ in range(2)]
    
    # رسالة الترحيب والبدء في اللعبة 
    clear_screen()
    print("Welcome to twenty one game")
    input("\nPress Enter to start...")
    clear_screen()
    print("Starting......")
    sleep(2)
    clear_screen()
    
    #طباعة القيم للمستخدم 
    print_cards(player_cards, computer_cards)
    
    # سؤال اللاعب هل يريد كروت أخرى في حالة عدم فوزه ببلاك جاك 
    if calc_score(player_cards) < 21:
        
        while calc_score(player_cards) < 21:
            
            if input("Get another card? (y/n): ").lower() == "y":
                player_cards.append(get_card())
                clear_screen()
                print_cards(player_cards, computer_cards)
                continue
            
            sleep(2)
            break
    
    #إعطاء كروت الموزع للكمبيوتر 
    clear_screen()
    print_cards(player_cards, computer_cards, False)
    sleep(2)
    while calc_score(computer_cards) <= 17 and calc_score(player_cards) < 21:
        computer_cards.append(get_card())
        print("Computer taked a card.")
        print_cards(player_cards, computer_cards, False)
        sleep(3)

    #طباعة النتيجة النهائية 
    print_final_result(player_cards, computer_cards)
    
    #سؤال اللاعب إذا كان يرغب في اللعب مرة أخرى 
    if input("\nPlay again? (y/n): ").lower() == "y":
        clear_screen()
        main()

# تشغيل اللعبة 
main()
