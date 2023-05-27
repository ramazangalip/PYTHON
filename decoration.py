def selamlama(fn):
    def wrapper():
        print("hoş geldiniz.")
        fn()
        print("gorusmek uzere")
    return wrapper

def gunaydin():
    print("günaydın benim adım ramo")
    


def iyigunler():
   print("iyi gunler benim adım ramo")

g =selamlama(gunaydin)

g()
