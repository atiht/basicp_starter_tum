#def show_movies(movie_list):
def show_movies(movie_list,ticket_price):
    for s in main :
        print(main)

        #print(s)

def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    menu = int(input("เลือกเมนู: (1)แสดงหนัง (2)ซื้อตั๋วหนัง "))
    if menu == 1:
        for s in movies:
            print({s["movie_name"]})
    elif menu == 2 :
            for s in movies:
                print(f"ชื่อหนัง{s["movie_name"]} | ราคาหนัง : {s["ticket_price"]}")
main()


