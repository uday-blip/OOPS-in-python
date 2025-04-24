class Laptops:
    instance_count=0
    def __init__(this,name,brand,processor,ram,storage,screen):
        Laptops.instance_count+=1
        if Laptops.instance_count==1:
         print('laptop specifications')
        this.model=name
        this.company=brand
        this.processor=processor
        this.ram=ram
        this.capacity=storage
        this.size=screen
    def description(this):
        return f'this laptops name is {this.model} it is from a brand named  {this.company} the processor is {this.processor} it is variant of ram {this.ram} and rom {this.capacity} and screen size is {this.size}'
uday=Laptops('galaxybook360','samsung','i7','16gb','512gb','14inches')
nani=Laptops('mihorizon','xomi','i7','16gb','512gb','13inches')
vinay=Laptops('edgeultra','infinix','i5','8gb','216gb','13inches')
aditya=Laptops('book7','acer','i5','8gb','216gb','16inches')
arvind=Laptops('asustufgaming','Asus','raizen5','16gb','512gb','15inches')
Sai=Laptops('macbook4','apple','m4','32gb','1tb','13inches')
Sanny=Laptops('macbook3','apple','m3','32gb','1tb','13inches')
paul=Laptops('911rs','porche','i9','64gb','2tb','13inchesfulidltpo display')
Han=Laptops('rx-7','mazda','i9','64gb','2tb','13inches qualcom oled display')
Mcqueen=Laptops('v8','americanmuscle','supercharged','32gb','1tb','13inches qualcom display')
Hodson=Laptops('v6','vintagesedan','turbocharged','32gb','1tb','14inches ltop oled')
print(uday.description())
print(nani.description())
print(vinay.description())
print(aditya.description())
print(Sai.description())
print(arvind.description())
print(paul.description())
print(Mcqueen.description())
print(Hodson.description())
print(Sanny.description())
print(Han.description())

