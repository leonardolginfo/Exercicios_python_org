
def month_name(number):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    if number in months:
        return months[number]
month = int(input())

name = month_name(month)
print(name)




'''
# Declarar uma variável do tipo inteiro
MAX_LEN = 140
eh140 = False

T = "Amor, confiança,fe"

if(len(T)<=MAX_LEN):
  eh140 = True

if(eh140):
  print("TWEET")
else:
  print("MUTE")
  '''