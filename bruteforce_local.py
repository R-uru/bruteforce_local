import os
import sys
import webbrowser

os.system('clear')
banner = '''                     ...:=-                   
                  .@@@@@@@@@@:                
                 #@@@@@@@@@@@@-               
                -=#%@@@@@@@@@@@               
                =-+#***@=%@@@@@:              
               :-=+-+:=**%#%@%*=              
               :-:=-=%%%%+=*@++.              
                ::.=*%%%#=+-+*=               
                 =#****%**+=##                
                ..+%%#%%%%%%@+:               
            ..--::.*%%%#*%%@*+++*+-.          
        :==----::-. :#%###+-.-++*******-      
      :=------:---:...-*=---:--:--=++****-    
      -:------:---.-==-=====:----------+=*    
     .-:-------:--:========---::-------:-*.   
     :-:----------:========------------:-*.   
     ..:----------:========-----------..=*    
     .:.:----------:=======----------- -.+    
     .-.:----------:======:--=-------:::.=    
     :-::------------====-.-==-------:- -=    
     -:::-----:--:-=:====.:-=:-==-----.:-=:   
     --.:-----:--:-=====-.:=-:-==----..--+:   
     --. ------.-:-=====:.--.:====---.--=*.   
'''
bye = '''
.----..-.  .-..----..----.
| {}  }\ \/ / | {_  | {_  
| {}  } }  {  | {__ | {__ 
`----'  `--'  `----'`----'

'''
menu = ('''
[1] Pass Guess
[2] Ruru Facebook
[0] Exit
''')

def recall():
    url = "https://www.facebook.com/ruruonfb"
    print(banner, menu)
    while True:
        try:
            ask = int(input('Input : '))
            if ask in (0,1,2):
                if ask == 1:
                    loop = True
                    user = input('\ninput combination: ')
                    with open('rockyou.txt','r', encoding='latin-1') as ruru:
                        for i, rurus in enumerate(ruru, start=1):
                            rurus = rurus.strip()
                            print(f"{i} • Trying | {rurus}")
                            if rurus == user:
                                print(f"\n[{i}] Pass: {rurus}\n")
                                recall()
                                break
                    if not loop:
                        print(banner)
                        print('no match :(')
                elif ask == 2:
                    os.system(f'xdg-open {url}')
                    webbrowser.open(url)
                elif ask == 0:
                    os.system('clear')
                    print(bye)
                    sys.exit()    
            else:
                print('\nAvailable: [0] [1] [2]') 
        except ValueError:
            print('\n— Input \'int\' only!]')
recall()        
    