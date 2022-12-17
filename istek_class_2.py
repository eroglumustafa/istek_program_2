class istek:

    def __init__(self,a={},deger={}):
        self.a = a
        self.deger = deger
    
    def ekle(self):
        properties = {}
        property_list = []
        while True:
            x = input("\nHangi ozelliği eklemek istersiniz: (İptal için 0)  ")
            if x == "0":
                break
            else:
                self.deger = input(f"{x} Miktarını ya da Değerini giriniz: ")
                properties[x] = self.deger
                
        return properties    

    def menu(self):
        while True:
            choice = input("\nProgramdan çıkmak için 0, Ürün eklemek için 1 giriniz: ")
            if choice == "0":
                print("\nÇıkış yaptınız.\n")
                return False
            elif choice == "1":
                product = input("\nÜrün Adı ? ")
                return product
            else:
                print("\nHatalı giriş yaptınız. 0 ya da 1 arasında seçim yapnız.")

i = istek()
all_products = {}

while True:
    product = i.menu()
    if product == False:
        break
    all_products[product] = i.ekle()

print("\nÜrünler ve Özellikleri:"+"\n"+"*"*23)

for i, j in all_products.items():
    print("\nÜrün adı: ", i)
    for key in j:
        print(key,":\t",j[key])
