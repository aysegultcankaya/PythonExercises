'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.

player={
   "1":{
        "id":1,
        "name":"Cristiano Ronaldo",
        "yearOfBirth":1985,
        "nationality":"Portugal",
        "current_team":"Portugal",
        "history":["Juventus,Real Madrid,Portugal"]},
   "2":{
        "id":2,
        "name":"Lionel Messi",
        "yearOfBirth":1987,
        "nationality":"Argentina",
        "current_team":"Barcelona",
        "history":["Barcelona,Argentina,Portugal"]}
}

# player=[
#     {
#         "id":1,
#         "name":"Cristiano Ronaldo",
#         "yearOfBirth":1985,
#         "nationality":"Portugal",
#         "current_team":"Portugal",
#         "history":["Juventus,Real Madrid,Portugal"]
#     },
#     {
#          "id":2,
#         "name":"Lionel Messi",
#         "yearOfBirth":1987,
#         "nationality":"Argentina",
#         "current_team":"Barcelona",
#         "history":["Barcelona,Argentina,Portugal"]
#     }
# ]


# print(player)

# 2- id' e göre arama yapınız.
x=input("id no giriniz:")

players=player[x]["name"]

print(players)


# 3- id' e göre bilgi kayıt siliniz.

id=input("Silmek istediğiniz id numarasını giriniz=")
player.pop(id)
print(player)

