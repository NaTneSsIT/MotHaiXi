from pickle import FALSE
import random
def computer():
    Computer_Choice=["D","L","K"]
    random_choice=random.randint(0,2)
    result=Computer_Choice[random_choice]
    return result
def main():
    print("Chao mung ban den voi game MOT HAI XI!!!!!")
    print('Chon "D"=Đấm "L"=Lá "K"=Kéo "T"=Thoat.')
    dang_choi=True
    tran=1
    
    while dang_choi:
        
        player_choice=input(f"#Tran {tran}.Nhap vao lua chon cua ban:").upper()
        while player_choice!="K" and player_choice!="D" and player_choice!="L" and player_choice!="Q":
            print('Ban phai nhap "D" "K" "L"!!!!!' )
            player_choice=input(f"#Tran {tran}.Nhap vao lua chon cua ban:").upper()
        computer_play=computer()
        
        
        if(player_choice=="Q"):
            print("Ban da chon thoat game!!")
            dang_choi=False
        else:
            if player_choice=="D" and computer_play=="L":
                print('Bạn ra "Đấm" VS Máy ra "Lá" ')
                print("============YOU LOSE============")
            elif player_choice=="D" and computer_play=="D":
                print('Bạn ra "Đấm" VS Máy ra "Đấm" ')
                print("============TIE============")
            elif player_choice=="D" and computer_play=="K":
                print('Bạn ra "Đấm" VS Máy ra "Kéo" ')
                print("============YOU WIN============")
            elif player_choice=="K" and computer_play=="D":
                print('Bạn ra "Kéo" VS Máy ra "Đấm" ')
                print("============YOU LOSE============")
            elif player_choice=="K" and computer_play=="K":
                print('Bạn ra "Kéo" VS Máy ra "Kéo" ')
                print("============TIE============")
            elif player_choice=="K" and computer_play=="L":
                print('Bạn ra "Kéo" VS Máy ra "Lá" ')
                print("============YOU WIN============")
            elif player_choice=="L" and computer_play=="D":
                print('Bạn ra "Lá" VS Máy ra "Đấm" ')
                print("============YOU WIN============")
            elif player_choice=="K" and computer_play=="K":
                print('Bạn ra "Lá" VS Máy ra "Kéo" ')
                print("============YOU LOSE============")
            elif player_choice=="K" and computer_play=="L":
                print('Bạn ra "Lá" VS Máy ra "Lá" ')
                print("============TIE============")
             

        tran+=1
if __name__=="__main__":
    main()