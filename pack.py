ghostitem = ['700','50']
ghoststat = {1:'3' , 2:'5' , 3:'2'}
hero = {1:'30' , 2:'50' , 3:'99'}
print("pack man game start")
print("유령이 나타 났다")
print("1.run away 2.look 3.kill")
number = int(input("숫자를 입력하세요:"))
#만약에 유저가 입력한 글자가 1 도망.
#만약에 유저가 입력한 글자가 2 관찰한다.
#만약에 유져가 입력한 글자가 3 싸운다.
if number == 1:
    print("도망갔지만 잡혀버렸다.")
elif number == 2:
        print("유령의 공격력은 : " + ghoststat[1] + " 방어력은 : " + ghoststat[2])
elif number == 3:
            print("승리했다. 전리품을 얻었다. " + ghostitem[0] + " 골드 ," + ghostitem[1] + " 경험치" )