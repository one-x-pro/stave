import time
from datetime import datetime, timedelta, timezone, UTC
from pocketoptionapi.stable_api import PocketOption
import pocketoptionapi.global_value as global_value
import pocketoptionapi.razred_Masaniello_v3 as MC
import pocketoptionapi.razred_super_trend as ST

#from ssl import SSL_ERROR_INVALID_ERROR_CODE
#import math, asyncio, json, threading, random
#from types import prepare_class
#from zipfile import BadZipfile

# from pocketoptionapi.stable_api import PocketOption
# import Trejd_RL_sistem_v1
#from pocketoptionapi.api import PocketOptionAPI
#import logging
# import time
# import json


""" TUKAJ JE TESTIRANJE:
    TESTIRANJE Z 1 EUROM
    """
# Configure logging (optional)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


# Session configuration
# ssid = """42["auth",{"session":"sua_sessao_aqui","isDemo":1,"uid":seu_uid_aqui,"platform":2}]"""
ssid = """42["auth",{"sessionToken":"241641b6886bb2afa68a1c3487ec0d37","uid":"22580961","lang":"en","currentUrl":"cabinet/demo-quick-high-low"}]"""

# real
# ssid = """42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"c152f17bb882b8b7afdf134f982f6bc1\";s:10:\"ip_address\";s:13:\"178.79.67.174\";s:10:\"user_agent\";s:101:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1756551420;}3861b539c3310e0842e1ee7924326032","isDemo":0,"uid":22580961,"platform":3,"isFastHistory":true,"isOptimized":true}]"""
# demo
# ssid = """42["auth",{"session":"33f9269kh2c1ghtjflktr7umdc","isDemo":1,"uid":22580961,"platform":3,"isFastHistory":true,"isOptimized":true}]"""
# ssid = """42["auth",{"sessionToken":"241641b6886bb2afa68a1c3487ec0d37","uid":"22580961","lang":"en","currentUrl":"cabinet/demo-quick-high-low","isChart":1}]"""
demo = True  # True for demo account, False for real account
# demo = False

'''
if not demo:
    # print("\n PRIJAVA V REALNI RACUN")
    # ssid = """42["auth",{"session": "a:4:{s:10:\"session_id\";s:32:\"c152f17bb882b8b7afdf134f982f6bc1\";s:10:\"ip_address\";s:13:\"178.79.67.174\";s:10:\"user_agent\";s:101:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1756551420;}3861b539c3310e0842e1ee7924326032", "isDemo": 0,"uid": 22580961,"platform": 3,"isFastHistory": true, "isOptimized": true }]"""
    # ssid = """42["auth",{"sessionToken":"241641b6886bb2afa68a1c3487ec0d37","uid":"22580961","lang":"en","currentUrl":"cabinet/quick-high-low/USD","isChart":1}]"""
    ssid = """42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"c152f17bb882b8b7afdf134f982f6bc1\";s:10:\"ip_address\";s:13:\"178.79.67.174\";s:10:\"user_agent\";s:101:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1756551420;}3861b539c3310e0842e1ee7924326032","isDemo":0,"uid":22580961,"platform":3,"isFastHistory":true,"isOptimized":true}]"""
    ssid = """42["auth",{"sessionToken":"241641b6886bb2afa68a1c3487ec0d37","uid":"22580961","lang":"en","currentUrl":"cabinet/quick-high-low/USD","isChart":1}]"""
    ssid = r'42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"e4f71e46a84bb35bb4953b909f1bda36\";s:10:\"ip_address\";s:13:\"178.79.67.174\";s:10:\"user_agent\";s:101:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1757160624;}1fcecbaa9b35ab3f0448c6092b870e6c","isDemo":0,"uid":22580961,"platform":3,"isFastHistory":true,"isOptimized":true}]'


else:
    # print("\nPRIJAVA V DEMO RACUN")
    # ssid = """42["auth",{"sessionToken":"241641b6886bb2afa68a1c3487ec0d37","uid":"22580961","lang":"en","currentUrl":"cabinet/demo-quick-high-low","isChart":1}]"""
    ssid = """42["auth",{"session":"33f9269kh2c1ghtjflktr7umdc","isDemo":1,"uid":22580961,"platform":3,"isFastHistory":true,"isOptimized":true}]"""
'''


#if '"isDemo":1' in ssid:
if demo:
    # demo
    ssid = """42["auth",{"session":"33f9269kh2c1ghtjflktr7umdc","isDemo":1,"uid":22580961,"platform":3,"isFastHistory":true,"isOptimized":true}]"""
    #print("Najdem DEMO")
    #demo
    #print("sid je za demo")
    print("\n**************************************************\n")
    print("********************* D E M O ********************")
    print("\n**************************************************\n")
    demo = True
else:
    # ta dela
    ssid = r'42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"1136a16d8d024d099d028122545d03b3\";s:10:\"ip_address\";s:11:\"86.58.10.12\";s:10:\"user_agent\";s:101:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1769199057;}312dd79092977a125a5a9e4a4130ed23","isDemo":0,"uid":22580961,"platform":3,"isFastHistory":true,"isOptimized":true}]'
    #real
    #print("ne najdem Demo!")
    #print("sid je za real")
    print("\n**************************************************\n")
    print("********************* R E A L ********************")
    print("\n**************************************************\n")
    demo = False
    
    
# print("\n 21 global_value.websocket_is_connected = ",global_value.websocket_is_connected)

# Initialize API
api = PocketOption(ssid, demo)

# Connect
# print(api.connect())
connect = api.connect()
print("povezano: ", connect)
while global_value.websocket_is_connected is False:
    time.sleep(0.1)
time.sleep(2)


def preveri_rezultat(trejd):
    if api.check_win(trejd) == None:
        return api.check_win(trejd)
    else:
        return api.check_win(trejd)


def akcija(znesek, Aktivni_par, smer, iztek_casa=59):
    print("===== FUNKCIJA HITRIH 5 ======")
    print(f"{znesek}, {Aktivni_par}, {smer}, {iztek_casa}\n")
    rezultat = api.buy(
        amount=znesek,  # Value in $
        active=Aktivni_par,  # Currency pair (note the _otc suffix)
        action=smer,  # "call" (High) or "put" (Low)
        expirations=iztek_casa,  # Expiration in seconds
        #expirations=58,  # Expiration in seconds
    )
    if rezultat:
        return rezultat


def najdi_vzorec_vhod_izhod(komplet):
    pass


# def ma(komplet: dict{Any,Any})->None:
def kluci(komplet):
    
    #print(komplet)
    exit("\nUSTAVLJENO V FUNKCIJI KLUCI")
    """
    kluci = list(komplet.keys())
    sveca_0 = komplet[kluci[-1]]  # to sedaj je list
    close_sveca_0 = sveca_0[-1]
   
    list_open = []
    list_high = []
    list_low = []
    list_close = []
    #if len(komplet) > ma + 3:
        
    for i in komplet.keys():
        # print("list close: ",list_close)
        # print("\n IME KLJUCA JE: i =", i, " \nin JE LIST KLUCA z -1 je zadnja cena v listu: komplet[i][-1] = ",komplet[i][-1])
        # list_close.append([i][-1]) # napaka ZAPISUJEM IMENA KLJUCEV
        list_close.append(komplet[i][-1])
        list_open.append(komplet[i][0])
        list_high.append(max(komplet[i]))
        list_low.append(min(komplet[i]))
        
    return {"open":list_open,"high":list_high,"low":list_low,"close":list_close}
    """

# def ma(komplet: dict{Any,Any})->None:
def ma_nova_verzija(komplet, ma) -> None:
    kluci = list(komplet.keys())
    sveca_0 = komplet[kluci[-1]]  # to sedaj je list
    list_close = []
    if len(komplet) > ma + 3:
        for i in komplet:
            # print("list close: ",list_close)
            # print("\n IME KLJUCA JE: i =", i, " \nin JE LIST KLUCA z -1 je zadnja cena v listu: komplet[i][-1] = ",komplet[i][-1])
            # list_close.append([i][-1]) # napaka ZAPISUJEM IMENA KLJUCEV
            list_close.append(komplet[i][-1])
    try:
        return moving_average(list_close,ma)
    except:
        #UnboundLocalError: cannot access local variable 'ma_2' where it is not associated with a value
        return []


# def ma(komplet: dict{Any,Any})->None:
def ma(komplet, ma) -> None:
    """vzorec vhod izhod 3 svec plus offset"""

    kluci = list(komplet.keys())
    sveca_0 = komplet[kluci[-1]]  # to sedaj je list
    close_sveca_0 = sveca_0[-1]
    """
    print(f"funkcija:: ma = {ma}")
    print(f"\nfunkcija:: dolzina dict = {len(komplet)} \n")
    print(f"\nfunkcija:: cena sveca_0 close = {close_sveca_0} \n")
    """
    list_close = []
    if len(komplet) > ma + 3:
        for i in komplet:
            # print("list close: ",list_close)
            # print("\n IME KLJUCA JE: i =", i, " \nin JE LIST KLUCA z -1 je zadnja cena v listu: komplet[i][-1] = ",komplet[i][-1])
            # list_close.append([i][-1]) # napaka ZAPISUJEM IMENA KLJUCEV
            list_close.append(komplet[i][-1])
    # print("podatki lista list_close = ",list_close)
    #print("funkcja(",ma,"):: len(list_close) = ", len(list_close))
    
    
    #print("\nma>> moving_average IZPIS = ",moving_average(list_close,ma) )
    print("")
    if len(list_close) > ma + 3:
        ma_0 = sum(list_close[-ma:])
        ma_1 = sum(list_close[-(ma + 1) : -1])
        ma_2 = sum(list_close[-(ma + 2) : -2])
        ma_3 = sum(list_close[-(ma + 3) : -3])
        
        """
        print(f" list -{ma}: = {list_close[-ma:]}")
        print(f" list [-{ma + 1}:-1] = {list_close[-(ma + 1) : -1]}")
        print(f" list [-{ma + 2}:-2]: = {list_close[-(ma + 2) : -2]}")
        print(
            f"ma 0: 0/{ma} = {ma_0 / ma:.5f} < ma{ma} 1 = {ma_1 / ma:.5f}  smer je: {'dol' if ma_0 / ma < ma_1 / ma else 'gor'} "
        )
        print(
            f"ma  1: 1/{ma} = {ma_1 / ma:.5f} < ma 2/{ma} = {ma_2 / ma:.5f}  smer je: {'dol' if ma_1 / ma < ma_2 / ma else 'gor'} "
        )
        print(
            f"ma  0/{ma} = {ma_0/ ma:.5f} < ma 2/{ma} = {ma_2 / ma:.5f}  smer je: {'dol' if ma_0 / ma < ma_2 / ma else 'gor'} "
        )
        """
    try:
        return [round(ma_3 / ma,6),round(ma_2 / ma,6), round(ma_1 / ma,6), round(ma_0 / ma,6)]
        #return moving_average(list_close,ma)
        
    except:
        #UnboundLocalError: cannot access local variable 'ma_2' where it is not associated with a value
        return []

def moving_average(data, window_size):
    averages = []
    #print("moving_average:: date = ",data.keys())
    kluci = list(data.keys())
    #print("moving_average:: kluci = ",kluci)
    list_close = []
    #print(f"len(kljuci){len(kluci)} > window_size {window_size}")
    if len(kluci) > window_size:
        for i in kluci:
            # print("list close: ",list_close)
            # print("\n IME KLJUCA JE: i =", i, " \nin JE LIST KLUCA z -1 je zadnja cena v listu: komplet[i][-1] = ",komplet[i][-1])
            # list_close.append([i][-1]) # napaka ZAPISUJEM IMENA KLJUCEV
            list_close.append(data[i][-1])
    for i in range(len(list_close) - window_size + 1):
        window = list_close[i:i + window_size]
        #print("MOVING_AVERAGE:: okno = ",window)
        window_average = sum(window) / window_size
        averages.append(round(window_average,6))
    return averages # prva sveca je zadnja stevilka v listu

def moving_average_original(data, window_size):
    averages = []
    print("moving_average:: date = ",data)
    
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        #print("MOVING_AVERAGE:: okno = ",window)
        window_average = sum(window) / window_size
        averages.append(round(window_average,6))
    return averages # prva sveca je zadnja stevilka v listu

def ma_bar(arr):
    #print("len = ",len(arr))
    okno = int(len(arr)/2)
    window_size = okno

    i = 0
    # Initialize an empty list to store moving averages
    moving_averages = []

    # Loop through the array to consider
    # every window of size 3
    while i < len(arr) - window_size + 1:
    
        # Store elements from i to i+window_size
        # in list to get the current window
        window = arr[i : i + window_size]

        # Calculate the average of current window
        window_average = round(sum(window) / window_size, 5)
        
        # Store the average of current
        # window in moving average list
        moving_averages.append(window_average)
        
        # Shift window to right by one position
        i += 1

    return moving_averages
    
    
# def moving_average(window = 10,podatki):
# podatki bi bili dict po minuto
def ohlc_izpis(sveca):
    # print("v ohlc je sveca tip = ",type(sveca))
    """dobim list vrnem dict!
    parameter: list (sveca)
    return: dict ohlc
    """
    s = {}
    s["o"] = sveca[0]
    s["h"] = max(sveca)
    s["l"] = min(sveca)
    s["c"] = sveca[-1]
    #print("funkcija: ohlc_izpis:: ",s)
    return s

def ohlc(svece,zaporedje):
    # print("v ohlc je sveca tip = ",type(sveca))
    """dobim dict vrnem dict!
    parameter: dict (svece)
    parameter: zaporedje
    return: dict ohlc 
    """
    #if zaporedje == 0:
    
    #>print("funkcija:: pred izracunom zaporedje = ",zaporedje)
    zaporedje = -1*(zaporedje+1)
    #>print("funkcija::  zaporedje = ",zaporedje)
    kluci = list(svece.keys())
    """
    print("funkcija:: kluci= ",kluci)
    print("funkcija:: kluci[-1]= ",kluci[-1])
    print("funkcija:: kluci[zaporedje]= ",kluci[zaporedje])
    """
    bar = svece[kluci[zaporedje]]
    s = {}
    s["o"] = bar[0]
    s["h"] = max(bar)
    s["l"] = min(bar)
    s["c"] = bar[-1]
    s["s"] = "BULL" if s["o"] < s["c"] else "BEAR"
    #print("dict iz ohlc = ",s)
    return s
    
min_payout = 92

def bars(par):
    bar = {}
    minuta = 100
    zadnja_minuta = 100
    for i in global_value.zgodovina_3[par]["zgodovina"]:
        zadnja_minuta = datetime.fromtimestamp(i[0]).minute
        # zadnja_minuta = datetime.fromtimestamp(i[0]).minute
        # # zadnja_minuta = datetime.fromtimestamp(i[0]).minute
        ura = datetime.now().hour
        if zadnja_minuta != minuta:
            minuta = zadnja_minuta
            bar[f"{ura}_minuta_{minuta}"] = []
            ## print(f"v FOR >> IZDELAN KLJUC: minuta_{minuta}")
            # minute[f"minuta_{minuta}"].append(i[1])
    
        # print(f"for:: V TA KLJUC: minuta_{minuta} PRPENJAM CENO: {i[1]}")
        bar[f"{ura}_minuta_{minuta}"].append(i[1])
    #print("bars:: zadnja_minuta = ",zadnja_minuta)
    return bar
    
def sveza_cena(par):
    return global_value.zgodovina_3[par]["zgodovina"][-1][1]

def funkcija_odlocitev(par):
    print(f"\n\n SEKUND = 58 ({datetime.now().second}) ZADNJA OHLC IZ BARS\n")
    print("bar_2 = ",ohlc(bars(par),2))
    print("")
    print("bar_1 = ",ohlc(bars(par),1))
    print("")
    print("bar_0 = ",ohlc(bars(par),0))
    print("")
    print(f"\n\n(def)funkcija_odlocitev:: *** KONEC *** SEKUND = 58? = ({datetime.now().second}) ZADNJA OHLC IZ BARS\n\n")
    
    
def funkcija_ma(par,printaj=1):

    print(f"\n ========= tukaj klicem funkcijo za ma... ========= {par}\n")
    ma_3 = ma(bars(par), 3)
    ma_5 = ma(bars(par), 5)
    """
    ma_8 = ma(minute, 8)
    if len(ma_8) == 0:
        print("\n\n>> ma_8 ima premalo polj len = ",len(ma_8))
        continue
    """
    razlika = 0
    if ma_3[-1] > ma_5[-1]:
        razlika = ma_3[-1] - ma_5[-1]
    elif ma_3[-1] > ma_5[-1]:
        razlika = ma_5[-1] - ma_3[-1]
    
    povprecek = (ma_3[-1] + ma_5[-1]) / 2
    procentna_razlika = (razlika / povprecek ) * 100
    ma_3_32 = 'gor' if ma_3[-2] > ma_3[-3] else 'dol'
    ma_3_12 ='gor' if ma_3[-1] > ma_3[-2] else 'dol'
    ma_3_5_11 ='m3 zgoraj' if ma_3[-1] > ma_5[-1] else 'm3 spodaj'
    ma_5_12 ='gor' if ma_5[-1] > ma_5[-2] else 'dol'
    if printaj:
        print(f"\nma 3 -3 = {ma_3[-3]:.5f} -2 = {ma_3[-2]:.5f} smer= {ma_3_32} ")
        print(f"ma 3 -1 = {ma_3[-1]:.5f} -2 = {ma_3[-2]:.5f} smer= {ma_3_12} ")
        print(f"ma 3 -1 = {ma_3[-1]:.5f} m5 -1 = {ma_5[-2]:.5f} smer= {ma_3_5_11} ({ma_3[-1] - ma_5[-1]:.5f})\n")
        print(f"ma 5 -1 = {ma_5[-1]:.5f} -2 = {ma_5[-2]:.5f} smer= {ma_5_12} \n")
        print(f"med ma_3[-1] in ma_5[-1] RAZLIKA = {razlika:.5f} POVPRECEK = {povprecek:.2f} PROCENTNA_RAZLIKA = {procentna_razlika:.2f} ")
    """
    #ma_smer = "cakaj"
    if ma_3[-1] > ma_5[-1]:
        print("\n ma_3[-1] > ma_5[-1] gor kupi")
        #ma_smer = "call"
    elif ma_3[-1] < ma_5[-1]:
        print("\n ma_3[-1] < ma_5[-1] dol prodaj")
        #ma_smer = "put"
    else:
        print("\n ma else cakaj")
        #ma_smer = "cakaj"
    """
    
    return [ma_3_32, ma_3_12, ma_3_5_11, ma_5_12,razlika,povprecek,procentna_razlika]
                
Aktivni_par = None
global_value.seja =0
povzeto={}
zapis={}
dovolim = False
with open("spremljanje.txt","w") as f:
    f.write("\n**** NA NOVO **** \n")
    
with open("rezultati.txt","w") as f:
    f.write(f"\n**** NA NOVO **** \n")
    

    
def funkcija_z_ma7(par):
    # pripravi funkcijo ki bo enako delovala kot je spodnji if stavek z ma_7 = ma(bars(Aktivni_par), 7) in vrne smer!!!!
    ma_7 = ma(bars(par), 7)
    smer = "ne"
    print(f"\n*****************\nCENE:\n  ma_7[-3] = {ma_7[-3]}  \n ma_7[-2]  = {ma_7[-2]} \n ma_7[-1]  = {ma_7[-1]} \n**************\n")
    if  ma_7[-2] > ma_7[-3] and ma_7[-1] > ma_7[-2]:
        print("\n7 je obrnjena GOR smer je call")
        print(f"\n*****************\nAKCIJA CENE:\n  ma_7[-3] = {ma_7[-3]}  \n ma_7[-2]  = {ma_7[-2]} \n ma_7[-1]  = {ma_7[-1]} \n**************\n")
        
        smer = "call"
        #akcija(1, Aktivni_par, smer, 58)
    elif ma_7[-2] < ma_7[-3] and ma_7[-1] < ma_7[-2]:
        print("\n7 je obrnjena DOL smer je put")
        print(f"\n*****************\nAKCIJA CENE:\n  ma_7[-3] = {ma_7[-3]}  \n ma_7[-2]  = {ma_7[-2]} \n ma_7[-1]  = {ma_7[-1]} \n**************\n")
        
        smer = "put"
        #akcija(1, Aktivni_par, smer, 58)    
        
    print("\n>>>>>>>>>>>>>> RETURN FUKCIJE funkcija_z_ma7 je smer = ",smer," <<<<<<<<<<<<< \n")
    return smer

def funkcija_oznacba_prehod(tekst:str = "") -> None:
    print("\n************************************************* ")
    if tekst:
        print(f" ************ >>>>>>>>>>>>> {tekst} <<<<<<<<<<<<<<<< *****************")
    print(f" >>>>>>>>> {datetime.now()} <<<<<<<<<<<<\n***********************************************\n ")
    
    
def vloga_masaniello(ms_pozitivnih,ms_trejdov,ms_procent,ms_vloga):
    vm =MC.Masaniello_MM(ms_pozitivnih,ms_trejdov,ms_procent,ms_vloga)
    #zacetna_banka = ms_vloga
    vse_vloge=[]
    #print("vloga_masaniello:: popravek zacnem z bilanco = ", zacetna_banka)
    #print(f"\nvloga_masaniello:: Znesek prve investicije = {vm.investicija:0.2f}")
    vse_vloge.append(vm.investicija)
    #print(f"\nvloga_masaniello:: Znesek seje = {vm.cena_seje:0.2f}")
    for i in range(ms_trejdov):
        #print(i)
        #print("ponovitev ",vm.ponovitev)
        vm.Rezultat(0)
        dosezeno = vm.NoviKrog()
        print(f"vloga_masaniello:: dosezeno (i={i}) {dosezeno}")
        if dosezeno[1] == 0:
            break
        vse_vloge.append(dosezeno[1])
        if i >= ms_trejdov-2 :
            break
    #print("to je namenjeno za return = vse_vloge = ",vse_vloge)
    return vse_vloge
    
def Laubuchere_sistem(polog,maksimalen_polog = 1):
    i=1
    polog_list =[]
    polog = polog/maksimalen_polog
    while i<polog:
        #print(i)
        polog_list.append(1)
        i+=1
    #print("48 test_1.py > Laubuchere_sistem => polog = ",polog_list)
    return polog_list
   
def L_trejd(vloga):
    if len(vloga) <2:
        print("konec")
        return 0
    print(" ")
    print(vloga[0]+vloga[-1])
    vloga.pop()
    print(vloga)
    vloga.pop(0)
    print(vloga)
    
    
def zapis_rezultata(zapis):
    with open("rezultati.txt","a") as f:
        for i in zapis:
            f.write(f"\n{i}  {zapis[i]}")
            #print(f"> {i}  {zapis[i]} ")
        f.write(f"\n*** {datetime.now()} ***\n")

def funkcija_izbora_trejda(krog):
    krog = krog + int(datetime.now().minute)
    #krog = krog % 2
    izbor = "call" if krog % 2 else "put"
    print(f"funkcija_izbora_trejda:: {krog} izbor: {izbor}")
    return izbor # "call" if krog % 2 else "put"

def izracun_procentov(a,b):
    print(f"a= {a}")
    print(f"b= {b}")
    procent = (a-b)/((a+b)/2)
    print("return procent= ",round(procent, 5))
    print("return % procent= ",round(procent*100,2))
    return round(procent*100,2)

def izracun_procentov_FIBO(a,b):
    print(f"a= {a}")
    print(f"b= {b}")
    procent = (a-b)/((a+b)/2)
    print("return procent= ",round(procent, 5))
    print("return % procent= ",round(procent*100,2))
    print("return razlika= ",round(a-b,5))
    print("return sredina= EQULIBRIUM= ",(a+b)/2)
    print("return razlika tocke= ",round((a-b)/0.0001,2))
    print("RETURN FIBO PROCENTE!!")
    
def izracun_nagiba_priprava(cena_a,cena_b):
    #from datetime import datetime,timedelta
    # Using current time
    cas_sedaj = datetime.now()
    
    # printing initial_date
    print ("initial_date", str(cas_sedaj))
    
    # Izracun zamik casa
    # tri minute nazaj 
    minute_nazaj = cas_sedaj - \
                            timedelta(minutes = 3)
    
    future_date_after_2days = cas_sedaj + \
                            timedelta(minutes = 120)
                            
    #cas_aktivni = 
    
    # printing calculated future_dates
    print('minute_nazaj(3):', str(minute_nazaj))
    print('future_date_after_2days:', str(future_date_after_2days))
    print('future_date_after_2days:', future_date_after_2days.timestamp())
    print('future_date_after_2days:', float(future_date_after_2days.timestamp()))
    stevilo = float(cas_sedaj.timestamp()) -float(minute_nazaj.timestamp())
    print("stevilo = ",stevilo)
    
    cena_a = 1.95967 
    cena_b = 1.95781
    cena = cena_a - cena_b
    #cena = 1.95781 - 1.95967
    print("cena = ",cena)
    
    print(f"rezultat = {cena/stevilo:.6f}")


def izracun_nagiba(cena_a,cena_b,minut_nazaj = 4):
    #from datetime import datetime,timedelta
    # Using current time
    cas_sedaj = datetime.now()
    
    # printing initial_date
    #print ("initial_date", str(cas_sedaj))
    
    # Izracun zamik casa
    # tri minute nazaj 
    minute_nazaj = cas_sedaj - \
                            timedelta(minutes = minut_nazaj)
    
    #future_date_after_2days = cas_sedaj + timedelta(minutes = 120)
                            
    #cas_aktivni = 
    
    # printing calculated future_dates
    print('cas_sedaj:', str(cas_sedaj))
    print('minute_nazaj(3):', str(minute_nazaj))
    #print('future_date_after_2days:', str(future_date_after_2days))
    #print('future_date_after_2days:', future_date_after_2days.timestamp())
    #print('future_date_after_2days:', float(future_date_after_2days.timestamp()))
    stevilo = float(cas_sedaj.timestamp()) -float(minute_nazaj.timestamp())
    print("stevilo = ",stevilo)
    print(f"cena a = {cena_a} \ncena b = {cena_b}")
    
    #cena_a = 1.95967 
    #cena_b = 1.95781
    cena = cena_a - cena_b
    sredina = (cena_a + cena_b)/2
    #cena = 1.95781 - 1.95967
    print("cena = ",cena)
    
    print(f"naklon rezultat * 1000 = {cena/stevilo*1000:.6f}")
    print(f"naklon rezultat  = {cena/stevilo:.6f}")
    #return [cena/stevilo,cena/stevilo*1000]
    return [sredina,cena/stevilo*1000]
    #return cena/stevilo*1000
    
    
def fib(n):
    a,b=0,1
    #print(">>> n: ",n)
    for i in range(n):
        #print("i ==> ",i)
        a,b=b,a+b   
        #print("i >",i," ",a," ",b)
    return a 
    
def ternery(stevilo:int = 0)->str:
    #return lambda stevilo : " call" if stevilo > 0 else " put" if stevilo < 0 else " ne"
    if stevilo > 0:
        return "call"
    elif stevilo < 0:
        return "put"
    else:
        return "ne"
    
def zgodovina_svec(aktivni_par:str, cas:int = 60)->bool:
    
    api.get_candles(aktivni_par, cas)
    time.sleep(1)
    print(
        f"aktivni par: {aktivni_par} zapisan:  ",
        "JE" if aktivni_par in global_value.zgodovina_3 else "NI",
    )
    
    if aktivni_par not in global_value.zgodovina_3:
        exit(f"\n============= IZHOD ==============\n NI ZAPISA V ZGODOVINI ZA PAR: {aktivni_par} ")
        return False
        #quit("IZHOD QUIT!!")
            
    print("kluci v zgodovini ", global_value.zgodovina_3.keys())
    if aktivni_par in global_value.zgodovina_3:
        if "zgodovina" in global_value.zgodovina_3[aktivni_par]:
            print("\n\n ***************** POGOJI SO IZPOLNJENI  ****************** \n")
            print(" par je v zgodovini 3 in zgodovina je zapisana!!!!\n")
            return True
            
    return False
            


def labuchere(rezultat_ma3,povzeto):
    print("\n\n ******************************************* \
        \n :: PREVERJANJE REZULTATA TREJDA V NACUNU LABUSHERE ::\
        \n ***********************************************\n\n")
    print("GV.laubuchere_vloge = ",global_value.laubuchere_vloge)
    print("rezultat_ma3 = ",rezultat_ma3)
    #print("vloga_ma3 = ",vloga_ma3)
    print("... preverjam api.check_win...")
    api_check_win = api.check_win(rezultat_ma3[1]) if rezultat_ma3 else None
    print("api.check_win(rezultat_ma3[1]) = ",api_check_win)
    print("\n")
    if len(rezultat_ma3)> 0 and rezultat_ma3[0]:
        povzeto["LABU:: api check_win = (LIST) = ", ] = api_check_win # TUKAJ DOBIM:  (-1.11, 'loose')
        povzeto["LABU:: api check_win[0] = ", ] = api_check_win[0]
        povzeto["LABU:: api check_win[1] = ", ] = api_check_win[1]
        global_value.izzid_trejda = api_check_win[1]
        povzeto["LABU:: rezultat_ma3 = "] = rezultat_ma3 # TUKAJ DOBIM: (True, 'cc4d19f6-543c-4ae5-90f6-bbedd9213989')
        #povzeto["LABU:: list vlog = "] = vplacilo_vloge
        povzeto["LABU:: list vlog = "] = global_value.laubuchere_vloge
        print("rezultat_ma3 = ",rezultat_ma3)
        if api_check_win[0] == None:
            quit("\n\n KONCANJE SKRIPTA IN PROGRAMA \n\n")
        #if (api.check_win(rezultat_ma3[1]))[0] > 0: #pozitiven
        if api_check_win[0] > 0: # pozitiven
            print("\n >>> api.check_win(rezultat_ma3[1]) = ",api_check_win)
            povzeto["LABU::POZITIVNO rezultat_ma3 = "] = rezultat_ma3
            print("\nAPI::: POZITIVEN TREJD\n")
            global_value.trejd = 0
            
            #if labu:
            #[0] = 1 + api_check_win = 1.01 = 2.01
            #nov_znesek = vplacilo_vloge[0] + api_check_win[0]<
            nov_znesek = global_value.laubuchere_vloge[0] + api_check_win[0]
            print("TO JE ZNESEK KI SE DODAJA LISTU VLOG: ",round(nov_znesek,2) )
            #vplacilo_vloge.append(round(nov_znesek,2))
            global_value.laubuchere_vloge.append(round(nov_znesek,2))
            print("LABU::list:: obnovljeno vplacilo_vloge = ",global_value.laubuchere_vloge)
            povzeto["LABU:: obnovljen list vlog = "] = global_value.laubuchere_vloge
            #vloga_ma3 = vplacilo_vloge[-1]
            #print("LABU:: nova vloga iz labushere: ", vloga_ma3)
            #vplacilo_vloge.pop(0)
            #vplacilo_vloge.pop()
            #krog_obrat=0
            povzeto["LABU::trejd je = "] = "POZITIVEN TREJD"
            povzeto["LABU::stanje racuna = "] = f"{api.get_balance()}\n"
            zapis_rezultata(povzeto)
            povzeto={}
            #negativni_trejdi = 0
            #time.sleep(15)
            """
            with open("spremljanje.txt","a") as f:
                for i in zapis:
                    f.write(f"\n{i}  {zapis[i]}")
                    print(f"> {i}  {zapis[i]} ")
                f.write(f"\n***\n")
                """
            zapis_rezultata(povzeto)
            povzeto={}
        #elif (api.check_win(rezultat_ma3[1]))[0] < 0:
        elif api_check_win[0] < 0: # negativen
            print("\n >->-> api.check_win(rezultat_ma3[1]) = ",api_check_win)
            povzeto["LABU::NEGATIVNO rezultat_ma3 = "] = rezultat_ma3
            print("\nAPI::: NEGATIVEN TREJD\n")
            
            
            global_value.trejd +=1
            povzeto["LABU::trejd je = "] = "NEGATIVEN TREJD"
            povzeto["LABU::stanje racuna = "] = f"{api.get_balance()}\n"
            #if labu:
            #print("TO JE ZNESEK KI SE DODAJA LISTU VLOG: ",round(api_check_win[0],2) )
            #vplacilo_vloge.append(round(api_check_win[0],2))
            #print("LABU::list:: vplacilo_vloge = ",vplacilo_vloge)
            print("LABU::list:: vplacilo_vloge = ",global_value.laubuchere_vloge)
            #TUKAJ MORAM ODSTRANITI PRVO IN ZADNJO
            n = 1
            #vplacilo_vloge = vplacilo_vloge[n:-n]
            # TUKAJ ODVZAMEM PRVO IN ZADNJO POZICIJO
            global_value.laubuchere_vloge = global_value.laubuchere_vloge[n:-n]
            povzeto["LABU:: obnovljen list vlog = "] = global_value.laubuchere_vloge
            #vloga_ma3 = vplacilo_vloge[-1]
            #print("LABU:: nova vloga iz labushere: ", vloga_ma3)
            #vplacilo_vloge.pop(0)
            #vplacilo_vloge.pop()
            zapis_rezultata(povzeto)
            povzeto={}
        #elif (api.check_win(rezultat_ma3[1]))[0] == 0:
        elif api_check_win[0] == 0: # *nec*
            povzeto["LABU::*NEC* rezultat_ma3 = "] = rezultat_ma3
            print("\nAPI::: ***NEC*** TREJD\n")
            #print("tukaj bi morala ostati ista vloga ki je = ", vloga_ma3)
            povzeto["LABU::trejd je = "] = "***NEC*** TREJD"
            povzeto["LABU::stanje racuna = "] = f"{api.get_balance()}\n"
            zapis_rezultata(povzeto)
            povzeto={}
            
    print("\n\n********************************************************\
        \n***** PREVERJANJE REZULTATA TREJDA V NACUNU LABUSHERE ****\
        \n************************ K O N E C ***********************\n\n")
            
            

def rezultat_test(rezultat_ma3,povzeto):
    print("\n\n*************************************************** \
        \n PREVERJANJE REZULTATA TREJDA V NACUNU >> TESTIRANJA << \
        \n***************************************************\n")
    if len(rezultat_ma3)> 0 and rezultat_ma3[0]:
        #print(".. preverjam api.check_win...")
        print("... preverjam api.check_win ZA M1... rezultat_ma3 = ",rezultat_ma3)
        #print("... preverjam api.check_win ZA S30... rezultat_ma3_s30 = ",rezultat_ma3_s30)
        api_check_win = api.check_win(rezultat_ma3[1])
        #api_check_win_s30 = api.check_win(rezultat_ma3_s30[1])
        print("\napi.check_win(rezultat_ma3[1]) = ",api_check_win)
        #print("api_check_win_s30 = api.check_win(rezultat_ma3_s30[1]) = ",api_check_win_s30)
        povzeto["\napi check_win = "] = api_check_win
        #povzeto["api check_win_s30 = ", ] = api_check_win_s30
        global_value.izzid_trejda = api_check_win[1]
        #print("rezultat_ma3 = ",rezultat_ma3)
        if api_check_win[0] == None:
            quit("\n\n KONCANJE SKRIPTA IN PROGRAMA \n\n")
        povzeto["rezultat_ma3 = "] = rezultat_ma3
        #povzeto["rezultat_ma3_s30 = "] = rezultat_ma3_s30
        if (api.check_win(rezultat_ma3[1]))[0] > 0: #pozitiven
            print("\n :::API::: POZITIVEN TREJD \n URA: ",datetime.now())
            global_value.trejd = 0
            global_value.seja += 1

            povzeto["trejd je = "] = f"POZITIVEN TREJD\n URA: {datetime.now()}"
            global_value.balance = api.get_balance()
            povzeto["stanje racuna = "] = f"{api.get_balance()}\n"
            zapis_rezultata(povzeto)
            povzeto={}
            #negativni_trejdi = 0
            """
            with open("spremljanje.txt","a") as f:
                for i in zapis:
                    f.write(f"\n{i}  {zapis[i]}")
                    print(f"> {i}  {zapis[i]} ")
                f.write(f"\n***\n")
                """
        elif (api.check_win(rezultat_ma3[1]))[0] < 0:
            print("\n :::API::: NEGATIVEN TREJD \n URA: ",datetime.now())
            global_value.trejd +=1
            
            global_value.balance = api.get_balance()
            povzeto["stanje racuna = "] = f"{api.get_balance()}\n"
            povzeto["trejd je = "] = f"NEGATIVEN TREJD ({global_value.trejd}) (novi obrat = {global_value.trejd} )\n URA: {datetime.now()}\n"
            zapis_rezultata(povzeto)
            povzeto={}
            
        elif (api.check_win(rezultat_ma3[1]))[0] == 0:
            print("\n :::API::: ***NEC*** TREJD\n URA: ",datetime.now())
            povzeto["trejd je = "] = f"***NEC*** TREJD\nURA: {datetime.now()}"
            global_value.balance = api.get_balance()
            povzeto["stanje racuna = "] = f"{api.get_balance()}\n"
            zapis_rezultata(povzeto)
            povzeto={}
    print("...PRAZNJENJE:: preverjam api.check_win ZA M1... rezultat_ma3 = ",rezultat_ma3)
    rezultat_ma3=[]
    print("\n*************************************************** \
        \n PREVERJANJE REZULTATA TREJDA V NACUNU >> TESTIRANJA << \
        \n***************** K O N E C ****************************\n\n")
    #print("...PRAZNJENJE:: preverjam api.check_win ZA S30... rezultat_ma3_s30 = ",rezultat_ma3_s30)     
    #rezultat_ma3_s30=[]  


labu = False
testiranje_skripta = True

def masaniello():
    funkcija_oznacba_prehod("======= M A S A N I E L L O =======")
    print("\n\n*******************************======= M A S A N I E L L O =======************************************\n\n")
    povzeto={}
    krog_obrat =0
    gv_negativni_hitri = 9
    deals_id = ""
    vplacano=()
    osvezena_cena = 0
    global_value.seja +=1
    global_value.dolzina_kljucev = 0
    rezultat_ma3 =[]
    rezultat_ma3_s30 =[]
    podatki_za_masaniello=[]
    vloga_ma3 = 2
    """
    izpis napake ker ni bilo povezave!!
    2025-08-13 20:05:26.629891 :[ERROR]: timed out during opening handshake
    2025-08-13 20:05:35.608071 :[ERROR]: [Errno -3] Temporary failure in name resolution
    """
        
    # TRENUTNO NE POTREBUJEM PODATKOV ZADNJIH KONCANIH TREJDOV
    
    
    min_payout = 92
    
    racun_zacetna_banka = api.get_balance()

    if racun_zacetna_banka < 1:
        quit(f"\n\nQUIT ****** QUIT ******* ZNESEK NA RACUNU JE PREMAJHEN ({racun_zacetna_banka}) ********** QUIT **************** QUIT\n\n")
        #exit(f"\n\nEXIT ****** EXIT ******* ZNESEK NA RACUNU JE PREMAJHEN ({racun_zacetna_banka}) ********** EXIT **************** EXIT\n\n")
        #print(f"\n\nRETURN ****** RETURN ******* ZNESEK NA RACUNU JE PREMAJHEN ({racun_zacetna_banka}) ********** RETURN ********** RETURN\n\n")
        #return
    
    print("\nKLIC FUNKCIJE za nastavitev parov >  api.set_payout_pairs()\n")
    if not api.set_payout_pairs():
        quit("QUIT! Ni aktivnih parov")
    time.sleep(1)
    print("\nglobal_value.pairs.keys()\n")
    print(global_value.pairs.keys())
    print("\nkeys len = ",len(global_value.pairs.keys()))
    
    Aktivni_par = list(global_value.pairs.keys())[0]
    print("Aktivni_par = ", Aktivni_par)
    print(
        "podatki aktivnega para: ", global_value.pairs[Aktivni_par],
        "podatek za payout: ",global_value.pairs[Aktivni_par]["payout"]
    )  # dobim dict >>  {'id': 67, 'payout': 92, 'type': 'currency'}
    aktivni_payout = global_value.pairs[Aktivni_par]["payout"]
    """
    print("\n\n==============>>>>> Aktinvni par assets = ",global_value.assets[0])
    print("\n")
    """
    primerjevalni_payout = 0
    for i in global_value.assets:
        #print(i)
        if i[1] == Aktivni_par:
            """
            print(f"\nIZPIS IZ SEZNAMA ASSETS:\n PAR: {Aktivni_par}\n PODATKI: {i}")
            print(f"\nPRIMERJAVA pairs in assets: \npairs-payout: {global_value.pairs[Aktivni_par]["payout"]} \nassets-payout: {i[5]} \n")
            """
            primerjevalni_payout = i[5]
            
    print("\n")
    print(f"\nIZID PRIMERJAVE = (pairs) {aktivni_payout} VS (assets) {primerjevalni_payout} \nSTA ENAKA {aktivni_payout == primerjevalni_payout} \n")
    if aktivni_payout != primerjevalni_payout:
        print(" ker nista enaka klicem ponovno >> masaniello <<")
        #novi_par=None
        for i in global_value.assets:
            if  i[14] == True and "_otc" in i[1] and i[5] == 92 and i[3] == "currency":
                print(i)
                Aktivni_par = i[1]
                break
            """
            PRIMER IZPISA:
            [68, 'AUDCHF_otc', 'AUD/CHF OTC', 'currency', 5, 92, 60, 30, 3, 1, 0, 37, [], 1763251200, True, [{'time': 60}, {'time': 120}, {'time': 180}, {'time': 300}, {'time': 600}, {'time': 900}, {'time': 1800}, {'time': 2700}, {'time': 3600}, {'time': 7200}, {'time': 10800}, {'time': 14400}], 0, 3, -1]
            [38, 'AUDJPY', 'AUD/JPY', 'currency', 3, 50, 60, 30, 3, 0, 69, 0, [], 1763251200, False, [{'time': 60}, {'time': 120}, {'time': 180}, {'time': 300}, {'time': 600}, {'time': 900}, {'time': 1800}, {'time': 2700}, {'time': 3600}, {'time': 7200}, {'time': 10800}, {'time': 14400}], -1, 60, 1763344800]
            [69, 'AUDJPY_otc', 'AUD/JPY OTC', 'currency', 3, 80, 60, 30, 3, 1, 0, 38, [], 1763251200, True, [{'time': 60}, {'time': 120}, {'time': 180}, {'time': 300}, {'time': 600}, {'time': 900}, {'time': 1800}, {'time': 2700}, {'time': 3600}, {'time': 7200}, {'time': 10800}, {'time': 14400}], 0, 3, -1]
            """
        """
        api.change_symbol(novi_par,60)
        time.sleep(1)
        print("\n\nKONCAN IZPISA ASSETS! KLICEM MASANIELLO!!\n\n")
        quit("ZAENKRAT USTAVLJENO \n\n")
        masaniello()
        """
        
    # par = Aktivni_par
    # menjava =api.change_symbol(Aktivni_par,60)
    # menjava =api.change_symbol(Aktivni_par,30)
    #svece = api.get_candles(Aktivni_par, 60)
    """ zacetek funkcije"""
    #zgodovina_svec(Aktivni_par,60)
    if not zgodovina_svec(Aktivni_par,60):
        quit("(1)IZHOD zgodovina_svec (quit())")
    """
    api.get_candles(Aktivni_par, 60)
    time.sleep(1)
    print(
        f"aktivni par: {Aktivni_par} zapisan:  ",
        "JE" if Aktivni_par in global_value.zgodovina_3 else "NI",
    )
    
    if Aktivni_par not in global_value.zgodovina_3:
        exit(f"\n============= IZHOD ==============\n NI ZAPISA V ZGODOVINI ZA PAR: {Aktivni_par} ")
        quit("IZHOD QUIT!!")
        
        
    print("kluci v zgodovini ", global_value.zgodovina_3.keys())
    if Aktivni_par in global_value.zgodovina_3:
        if "zgodovina" in global_value.zgodovina_3[Aktivni_par]:
            print("\n\n ***************** POGOJI SO IZPOLNJENI  ****************** \n")
            print(" par je v zgodovini 3 in zgodovina je zapisana!!!!\n")
    """
    """ konec funkcije """        
    zgodovina = global_value.zgodovina_3[Aktivni_par]["zgodovina"]
    
    zgodovina_3_zadni = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][0]
    zgodovina_3_pred_zadni = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-2][0]
    print(f" URA: pred zadni {zgodovina_3_pred_zadni} || zadni {zgodovina_3_zadni} ")
    
    minute = {}
    
    
    """
    # DEL UCNEGA PROCESA
    print("zgodovina prvi izpis = ",global_value.zgodovina_3[Aktivni_par]["zgodovina"][0])
    print("zgodovina prvi izpis cas= ",datetime.fromtimestamp(global_value.zgodovina_3[Aktivni_par]["zgodovina"][0][0]))
    print("zgodovina prvi izpis UTC cas= ",datetime.fromtimestamp(global_value.zgodovina_3[Aktivni_par]["zgodovina"][0][0],tz=timezone.utc))
    print("zgodovina prvi izpis cena= ",global_value.zgodovina_3[Aktivni_par]["zgodovina"][0][-1])
    print("zgodovina ZADNI izpis = ",global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1])
    print("zgodovina ZADNI izpis cas= ",datetime.fromtimestamp(global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][0]))
    print("zgodovina ZADNI izpis UTC cas= ",datetime.fromtimestamp(global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][0],tz=timezone.utc))
    print("zgodovina ZADNI izpis cena= ",global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][-1])
    """
    
    # primer za izdelavo dict
    # global_value.zgodovina_3[message["asset"]]={"zgodovina": message["history"]}
    global_value.minute[Aktivni_par]=bars(Aktivni_par)
    minute = bars(Aktivni_par)
    kluci = list(minute.keys())
    
    """
    #za debug odkomentiraj
    print("\nvsi kljuci >> prvic\n")
    print(minute.keys())
    print("\n:::::::::::::::::::::::::::::::\nvsi kljuci >> drugic\n")
    print(kluci)
    print("\nvsi kljuci konec\n\n")
    """
    
    print("ZADNJA OHLC IZ BARS")
    bar_1 = ohlc(bars(Aktivni_par),1)
    bar_0 = ohlc(bars(Aktivni_par),0)
    
    """
    print("SVECA 1 (to je misljena predzadnja sveca MINUTNA)")
    print(" z prvo ceno ", minute[kluci[-2]][0])
    print(" z max ceno (high) ", max(minute[kluci[-2]]))
    print(" z min ceno (low) ", min(minute[kluci[-2]]))
    print(" z zadnjo ceno ", minute[kluci[-2]][-1])
    print("\nsveca je 1 ohlc: (PREDZADNJA *MINUTNA* SVECA)")
    ohlc_izpis(minute[kluci[-2]])
    print("\npredzadnji BAR")
    ohlc(minute,1)
    
    print("SVECA 0 (to je aktivna sveca MINUTNA!!")
    print(" zadnji kljuc z prvo ceno ", minute[kluci[-1]][0])
    print(" zadnji kljuc z max ceno (high) ", max(minute[kluci[-1]]))
    print(" zadnji kljuc z min ceno (low) ", min(minute[kluci[-1]]))
    print(" zadnji kljuc z zadnjo ceno ", minute[kluci[-1]][-1])
    print("\nsveca je 0 ohlc: (AKTIVNA *MINUTNA* SVECA)")
    ohlc_izpis(minute[kluci[-1]])
    """
    
    """
    print("\nzadnji BAR")
    #bar_1 = ohlc(minute,1)
    print("bar_1 o = ",bar_1["o"])
    print("bar_1 h = ",bar_1["h"])
    print("bar_1 l = ",bar_1["l"])
    print("bar_1 c = ",bar_1["c"])
    print("bar_1 s = ",bar_1["s"])
    print("BULL" if bar_1["o"] < bar_1["c"] else "BEAR")
    print("\naktivni BAR")
    #bar_0 = ohlc(minute,0)
    print("bar_0 o = ",bar_0["o"])
    print("bar_0 h = ",bar_0["h"])
    print("bar_0 l = ",bar_0["l"])
    print("bar_0 c = ",bar_0["c"])
    print("bar_0 s = ",bar_0["s"])
    print("BULL" if bar_0["o"] < bar_0["c"] else "BEAR")
    
    """
    
    #bar_0 = ohlc(minute,0)
    #print("bar_0[o] = ",bar_0["o"])
    
    # DOBIM PREAVILNI IZPIS print("ohlc(minute_0)[o] = ",ohlc(minute,0)["o"])
    

    zadnja_minuta = datetime.now().minute
    
    zadnji_izdelan_kluc_minute = list(minute.keys())[-1]
    # while True:
        # 
        # 
        # 
    print("\n", "=" * 50, "\nPRED WHILE >> PRVIC\n", "=" * 50)
    print("bar 1 = ",bar_1["s"])
    print("aktivni bar = ","BULL" if bar_0["o"] < bar_0["c"] else "BEAR")
    print("!aktivni! bar 0 = ",bar_0["s"])
    print("zadnji_izdelan_kluc_minute = ",zadnji_izdelan_kluc_minute)
    krogov = 0
    
    # while zadnja_minuta == datetime.now().minute:
        # 
        # 
        # 
    rezultat = []
    koncan_trejd = [0, "cakam"]
    zacetni_trejd = 0
    uspesni_trejdi = 0
    neuspesni_trejdi = 0
    ma_skupina_pozitivni=[]
    ma_skkupina_negativni=[]
    
    # zacetna_banka =0
    #racun_zacetna_banka = api.get_balance()
    print("\n\n Aktivna bilanca racuna = ", racun_zacetna_banka)

    print("""\n   ===================  MASANIELLO PODATKI ==============  \n""")
    
    zacetna_banka = 83

    
    """ od 25 do 50 zacetna vloga: 1.03
    ms_pozitivnih = 1
    ms_trejdov = 4
    ms_procent = 1.92
    #ms_vloga = 17# popravek na 20 ker imama zacetni trejd 1,21<
    ms_vloga = 20# popravek na 20 ker imama zacetni trejd 1,21
    """
    """ EXTREMNI TEST """
    ms_pozitivnih = 1
    ms_trejdov = 9
    ms_procent = 1.92
    ms_vloga = 700# popravek na 20 ker imama zacetni trejd 1,21
    
    
    
    """ od 50 do 100 
    prvi poskus neuspesen
    ms_pozitivnih = 1
    ms_trejdov = 6
    ms_procent = 1.92
    ms_vloga = 80
    """
    
    """
    ms_pozitivnih = 1
    ms_trejdov = 5
    ms_procent = 1.92
    ms_vloga = 40
    
    ms_pozitivnih = 2
    ms_trejdov = 7
    ms_procent = 1.92
    ms_vloga = 40
    
    ms_pozitivnih = 2
    ms_trejdov = 8
    ms_procent = 1.92
    ms_vloga = 100
    """
    
    
    # to je namenjeno z enim pravilnim
    if ms_pozitivnih == 1:
        vplacilo_vloge = vloga_masaniello(ms_pozitivnih,ms_trejdov,ms_procent,ms_vloga)
        global_value.masaniello_vloge = vplacilo_vloge
    if labu:
        vplacilo_vloge = Laubuchere_sistem(15)
        global_value.laubuchere_vloge = vplacilo_vloge
    print("\n PRIPRAVA ZA vplacilo_vloge ZACETEK")
    print("list vplacilnih vlog = ",vplacilo_vloge)
    print(" PRIPRAVA ZA vplacilo_vloge KONEC \n")
    #quit(f"IZHOD QUIT!! preverjam funkcijo masaniello")
    
    Mmm =MC.Masaniello_MM(ms_pozitivnih,ms_trejdov,ms_procent,ms_vloga)
    zacetna_banka = ms_vloga
    print("\nTREJDANJE NI PO PRINCIPU COMPAUNDINGA!!")
    print("\n\npopravek zacnem z bilanco = ", zacetna_banka)
    prva_investicija = Mmm.investicija
    print(f"\nZnesek prve investicije = {prva_investicija:0.2f}")
    print(f"\nTEST NOVEGA PRISTOPA UPORABE Masaniello vlog >> Znesek prve investicije = {global_value.masaniello_vloge[0]:0.2f}")
    print(f"\nZnesek seje = {Mmm.cena_seje:0.2f}")
    #print(f"potrebnih tock je : {Mmm.investicija * 10:0.2f}")
    dosezeno = None
    inp = None
    
    negativni_trejdi = 0
    pozitivni_trejdi = 0
    stetje_trejdov = 0
    uspesnost_trejdov = []
    zaporedje_trejdov = []
    shranjen_izbor = []
    ma_skupna=[]
    mas_vloga=[]
    aktivacija_akcije = False
    vloga_ma3 = Mmm.investicija
    if len(global_value.masaniello_vloge) > 0:
        vloga_ma3 = global_value.masaniello_vloge[0]
    
    global_value.vloga.append(vloga_ma3)
    if labu:
        global_value.vloga=[]
        global_value.vloga.append(vplacilo_vloge[0] + vplacilo_vloge[-1])
        vplacilo_vloge.pop(0)
        vplacilo_vloge.pop()
        
        
    """ za slepi krog"""
    #odprt_nadaljevalni_znesek = 0
    # zacetni_trejd=0
    slepi_krog = 0
    # exit()
    # while krogov < 4:
    #
    start = time.perf_counter()
    polje = []
    preverjanje_izbora = []
    ma_izbor=[]
    izbrana_smer=[]
    izbor_tri=[]
    kombinacija_izbor=[]
    prehod_while = 0
    trikratnik_smer = "+X+"
    aktivni_bar = []
    prejsni_bar =[]
    minuta =100
    #zapis={}
    smer = "ne"
    
    
    """
    print("dolzina len zgodovine = ",len(global_value.zgodovina_3[Aktivni_par]["zgodovina"]))
    for i in range(10):
        stevec = -1*(i+1)
        print("for:: stevec ",stevec)
        gv_cas = global_value.zgodovina_3[Aktivni_par]["zgodovina"][stevec][0]
        gv_cas = datetime.fromtimestamp(gv_cas)
        print("cas: ",gv_cas)
        print("minute: ",gv_cas.minute)
    """
    #exit("USTAVLJAM TESTIRAM")
    obracanje_smeri = False # pri vsakem drugem negativnem trejdu zamenja smer
    preskok = 0 # stevilo pri preskoku pomeni koliko minut se zamakne nov trejd
    minuta_preskok = 0
    zaklenjena_smer = 0 # zaklepanje smeri pri tretjem negativnem trejdu
    
    
    print("\n\n\n************************************************* ZAGON WHILE ***********************************************\n ",datetime.now())
    print("\n")
    
    
    trejd_aktiven = True
    
    
    while True:
        #print("\n************************************************* NOVI KROG ***********************************************\n ",datetime.now())
        gv_cas = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][0]
        gv_cas_utc = datetime.fromtimestamp(gv_cas,tz=timezone.utc)
        gv_cas = datetime.fromtimestamp(gv_cas)
        gv_cena = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
        #zadnja_aktivna_cena = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
        zadnja_aktivna_cena = gv_cena
    
        # print(">>##>> TO CENO PRIPENJAM >>zadnja_aktivna_cena = ",zadnja_aktivna_cena," kluc: ",zadnji_izdelan_kluc_minute)
    
        zadnja_minuta = datetime.now().minute
        zadnja_sekunda = datetime.now().second
        # zadnja_minuta = datetime.fromtimestamp(i[0]).minute
        # # zadnja_minuta = datetime.fromtimestamp(i[0]).minute
        if zadnja_minuta != minuta:
            funkcija_oznacba_prehod()
            global_value.balance_po_vplacilu = global_value.balance
            minuta = zadnja_minuta
            ura = datetime.now().hour
            zadnji_izdelan_kluc_minute = f"{ura}_minuta_{minuta}"
            #minute[f"minuta_{minuta}"] = []
            minute[zadnji_izdelan_kluc_minute] = []
            # izdelava novega kluca
            #global_value.minute[f"minuta_{minuta}"] = []
            global_value.minute[zadnji_izdelan_kluc_minute] = []
            global_value.minute[Aktivni_par].update({zadnji_izdelan_kluc_minute:[]})
            global_value.zadnji_izdelan_kljuc = zadnji_izdelan_kluc_minute
            
            print(f"\n\n ************************************************************************************************ \
                \n> >IF  v WHILE >> IZDELAN KLJUC: {ura}_minuta_{minuta} || seja: {global_value.seja} || Par: {Aktivni_par} \
                \n ***************************************************************************************************\n\n")
            
            print("\nGV.balance:: STANJE BANKE: ",global_value.balance)
            print("\nGV.pred_vplacilom::  STANJE BANKE: ",global_value.balance_pred_vplacilom)
            print("\nGV.po_vplacilu:: STANJE BANKE: ",global_value.balance_po_vplacilu)
            print("\n\npreverjam TRIKRATNIK_SMER = ",trikratnik_smer)
            print("preverjam SMER = ",smer)
            print("zadnji_izdelan_kluc_minute = ",zadnji_izdelan_kluc_minute)
            
            
            print("\n PREDOGLED>> PODATKI ZA MASANIELO: podatki_za_masaniello = ",podatki_za_masaniello)
            print("\n PREDOGLED>> TUKAJ BOM NAPISAL  PODATKE rezultat_ma3 = ",rezultat_ma3)
            #print("\nTUKAJ BOM NAPISAL  PODATKE rezultat_ma3 = len = ",len(rezultat_ma3)) # LEN JE TUKAJ ZMERAJ 2
            print("\nPREVERJANJE global_value.vloga = ",global_value.vloga)
            print(f"\n\n (STEVEC: {krog_obrat} ) seja: {global_value.seja}")
            
            
            
            if labu:
                print("\n\n ******************************************* \
                    \n PREVERJANJE REZULTATA TREJDA V NACUNU LABUSHERE \
                    \n ***********************************************\n\n")
                print("GV.laubuchere_vloge = ",global_value.laubuchere_vloge)
                print("rezultat_ma3 = ",rezultat_ma3)
                print("vloga_ma3 = ",vloga_ma3)
                print("... preverjam api.check_win...")
                api_check_win = api.check_win(rezultat_ma3[1]) if rezultat_ma3 else None
                print("api.check_win(rezultat_ma3[1]) = ",api_check_win)
                print("\n")
                if len(rezultat_ma3)> 0 and rezultat_ma3[0]:
                    povzeto["LABU:: api check_win = (LIST) = ", ] = api_check_win # TUKAJ DOBIM:  (-1.11, 'loose')
                    povzeto["LABU:: api check_win[0] = ", ] = api_check_win[0]
                    povzeto["LABU:: api check_win[1] = ", ] = api_check_win[1]
                    global_value.izzid_trejda = api_check_win[1]
                    povzeto["LABU:: rezultat_ma3 = "] = rezultat_ma3 # TUKAJ DOBIM: (True, 'cc4d19f6-543c-4ae5-90f6-bbedd9213989')
                    povzeto["LABU:: list vlog = "] = vplacilo_vloge
                    print("rezultat_ma3 = ",rezultat_ma3)
                    if api_check_win[0] == None:
                        quit("\n\n KONCANJE SKRIPTA IN PROGRAMA \n\n")
                    #if (api.check_win(rezultat_ma3[1]))[0] > 0: #pozitiven
                    if api_check_win[0] > 0: # pozitiven
                        povzeto["LABU::POZITIVNO rezultat_ma3 = "] = rezultat_ma3
                        print("\nAPI::: POZITIVEN TREJD\n")
                        
                        if labu:
                            #[0] = 1 + api_check_win = 1.01 = 2.01
                            nov_znesek = vplacilo_vloge[0] + api_check_win[0]
                            print("TO JE ZNESEK KI SE DODAJA LISTU VLOG: ",round(nov_znesek,2) )
                            vplacilo_vloge.append(round(nov_znesek,2))
                            print("LABU::list:: vplacilo_vloge = ",vplacilo_vloge)
                            vloga_ma3 = vplacilo_vloge[-1]
                            print("LABU:: nova vloga iz labushere: ", vloga_ma3)
                            #vplacilo_vloge.pop(0)
                            #vplacilo_vloge.pop()
                        krog_obrat=0
                        povzeto["LABU::trejd je = "] = "POZITIVEN TREJD"
                        povzeto["LABU::stanje racuna = "] = api.get_balance()
                        zapis_rezultata(povzeto)
                        povzeto={}
                        negativni_trejdi = 0
                        time.sleep(15)
                        """
                        with open("spremljanje.txt","a") as f:
                            for i in zapis:
                                f.write(f"\n{i}  {zapis[i]}")
                                print(f"> {i}  {zapis[i]} ")
                            f.write(f"\n***\n")
                            """
                    #elif (api.check_win(rezultat_ma3[1]))[0] < 0:
                    elif api_check_win[0] < 0: # negativen
                        povzeto["LABU::NEGATIVNO rezultat_ma3 = "] = rezultat_ma3
                        print("\nAPI::: NEGATIVEN TREJD\n")
                        negativni_trejdi += 1
                        povzeto["LABU::stanje racuna = "] = api.get_balance()
                        krog_obrat += 1
                        povzeto["LABU::trejd je = "] = "NEGATIVEN TREJD"
                        if labu:
                            #print("TO JE ZNESEK KI SE DODAJA LISTU VLOG: ",round(api_check_win[0],2) )
                            #vplacilo_vloge.append(round(api_check_win[0],2))
                            print("LABU::list:: vplacilo_vloge = ",vplacilo_vloge)
                            #TUKAJ MORAM ODSTRANITI PRVO IN ZADNJO
                            n = 1
                            vplacilo_vloge = vplacilo_vloge[n:-n]
                            vloga_ma3 = vplacilo_vloge[-1]
                            print("LABU:: nova vloga iz labushere: ", vloga_ma3)
                            #vplacilo_vloge.pop(0)
                            #vplacilo_vloge.pop()
                        zapis_rezultata(povzeto)
                        povzeto={}
                    #elif (api.check_win(rezultat_ma3[1]))[0] == 0:
                    elif api_check_win[0] == 0: # *nec*
                        povzeto["LABU::*NEC* rezultat_ma3 = "] = rezultat_ma3
                        print("\nAPI::: ***NEC*** TREJD\n")
                        print("tukaj bi morala ostati ista vloga ki je = ", vloga_ma3)
                        povzeto["LABU::trejd je = "] = "***NEC*** TREJD"
                        povzeto["LABU::stanje racuna = "] = api.get_balance()
                        zapis_rezultata(povzeto)
                        povzeto={}
                        
                print("\n\n**************** KONEC ******************\n*************** PREVERJANJE REZULTATA TREJDA V NACUNU LABUSHERE *********\n\n")
                        
            '''
            #### zakomentiraj
            if testiranje_skripta:
                print("\n\n ******************************************* \
                    \n PREVERJANJE REZULTATA TREJDA V NACUNU >> TESTIRANJA << \
                    \n ***********************************************\n\n")
                if len(rezultat_ma3)> 0 and rezultat_ma3[0]:
                    print("\n\n... preverjam api.check_win...")
                    print("... preverjam api.check_win ZA M1... rezultat_ma3 = ",rezultat_ma3)
                    print("... preverjam api.check_win ZA S30... rezultat_ma3_s30 = ",rezultat_ma3_s30)
                    api_check_win = api.check_win(rezultat_ma3[1])
                    #api_check_win_s30 = api.check_win(rezultat_ma3_s30[1])
                    print("\napi.check_win(rezultat_ma3[1]) = ",api_check_win)
                    #print("api_check_win_s30 = api.check_win(rezultat_ma3_s30[1]) = ",api_check_win_s30)
                    povzeto["\napi check_win = ", ] = api_check_win
                    #povzeto["api check_win_s30 = ", ] = api_check_win_s30
                    global_value.izzid_trejda = api_check_win[1]
                    print("rezultat_ma3 = ",rezultat_ma3)
                    if api_check_win[0] == None:
                        quit("\n\n KONCANJE SKRIPTA IN PROGRAMA \n\n")
                    povzeto["rezultat_ma3 = "] = rezultat_ma3
                    #povzeto["rezultat_ma3_s30 = "] = rezultat_ma3_s30
                    if (api.check_win(rezultat_ma3[1]))[0] > 0: #pozitiven
                        print("\nAPI::: POZITIVEN TREJD ", Aktivni_par,"\n")
                        
                        if labu:
                            vplacilo_vloge.append(round(api_check_win[0],2))
                            #vplacilo_vloge.pop(0)
                            #vplacilo_vloge.pop()
                        krog_obrat=0
                        povzeto["trejd je = "] = "POZITIVEN TREJD"
                        povzeto["stanje racuna = "] = api.get_balance()
                        zapis_rezultata(povzeto)
                        povzeto={}
                        negativni_trejdi = 0
                        """
                    """
                        with open("spremljanje.txt","a") as f:
                            for i in zapis:
                                f.write(f"\n{i}  {zapis[i]}")
                                print(f"> {i}  {zapis[i]} ")
                            f.write(f"\n***\n")
                            """
                    """
                    elif (api.check_win(rezultat_ma3[1]))[0] < 0:
                        print("\nAPI::: NEGATIVEN TREJD ",Aktivni_par,"\n")
                        negativni_trejdi += 1
                        povzeto["stanje racuna = "] = api.get_balance()
                        krog_obrat += 1
                        povzeto["trejd je = "] = f"NEGATIVEN TREJD ({negativni_trejdi}) (novi obrat = {krog_obrat})"
                        bar1 = ohlc(bars(Aktivni_par),1)
                        print("================================================ bar1 =====================================")
                        print(bar1)
                        povzeto[f"{bar1} = "] = f"{bar1}"
                        print("================================================ bar1 =====================================\n")
                        zapis_rezultata(povzeto)
                        povzeto={}
                        
                    elif (api.check_win(rezultat_ma3[1]))[0] == 0:
                        print("\nAPI::: ***NEC*** TREJD\n")
                        povzeto["trejd je = "] = "***NEC*** TREJD"
                        povzeto["stanje racuna = "] = api.get_balance()
                        zapis_rezultata(povzeto)
                        povzeto={}
                print(Aktivni_par,"...PRAZNJENJE:: preverjam api.check_win ZA M1... rezultat_ma3 = ",rezultat_ma3)
                rezultat_ma3=[]
                print("...PRAZNJENJE:: preverjam api.check_win ZA S30... rezultat_ma3_s30 = ",rezultat_ma3_s30)     
                rezultat_ma3_s30=[]
            #### zakomentiraj
            '''
    
                 
            if negativni_trejdi >=3:
                povzeto["klicem masanielo ="] =f"\n({Aktivni_par})  mesaniello() !!! STEVEC negativnih trejdov: {negativni_trejdi} \nURA: {datetime.now()}\n"
                #print(f"\n\n\n({Aktivni_par})  mesaniello() !!! STEVEC negativnih trejdov: {negativni_trejdi} \nURA: {datetime.now()} \n\n\n")
                print(f"\n\n\n({Aktivni_par})  RESET TRIKOTNIK!!! STEVEC negativnih trejdov: {negativni_trejdi} \nURA: {datetime.now()} \n\n\n")
                global_value.trikotnik_akcija = None
                global_value.trikotnik_akcija_m5 = None
                #masaniello()       
  
            
            
            #if not smer  in "ne" and not labu:
            if not labu and not testiranje_skripta:
                print("\n\n ******************************************* \
                    \n PREVERJANJE REZULTATA TREJDA V NACUNU  !! MASANIELLO !! \
                    \n ***********************************************\n\n")
                
                if len(rezultat_ma3) > 0:# tukaj je len vedno 2 ali je prav ali je narobe!!!!
                    print("\nZACETEK PREVERJANJA ==== AKTIVNE VLOGE ====  || ZNESEK: vloga_ma3 = ",vloga_ma3," Vplacano: ",rezultat_ma3[0])
                    print("\nZADNJI POSTAVLJEN TREJD: podatki_za_masaniello = ",podatki_za_masaniello)
                    print("pred if >> rezultat_ma3 = ",rezultat_ma3)
                    if not rezultat_ma3[0]: # TO POMENI DA JE FALSE
                        print("\n====================================================== \
                            \nPREVERI ZADNJI TREJD, CE SE UJEMA Z CENO AKTIVNE VLOGE\n IN PRIDOBI PODATKE ZA NADALJNE ODLOCANJE!!\
                            \n==========================================================\n")
                        time.sleep(1)
                        trejd_je_odprt = api.get_async_order()
                        print("\nIZPIS PODATKOV ZADNJEGA TREJDA:\n")
                        print(trejd_je_odprt)
                        #print("\nglobal_value.order_closed: ",global_value.order_closed) # to je prazen list
                        #print("\n")
                        #print("\napi.get_deals => ",api.get_deals()) # tu je ogromno trejdov ampak za celo uro kasneje
                        print("zadnji trejd id: ",trejd_je_odprt["deals"][0]["id"])
                        print("zadnji trejd profit: ",trejd_je_odprt["deals"][0]["profit"])
                        print("zadnji trejd amount: ",trejd_je_odprt["deals"][0]["amount"])
                        print("zadnji trejd asset: ",trejd_je_odprt["deals"][0]["asset"])
                        #print("PRED >>> zadnji trejd id: ",trejd_je_odprt["deals"][1]["id"])
                        
                        """ SE ENO PREVERJANJE !!"""
                        print(f"global_value.balance_pred_vplacilom != global_value.balance_po_vplacilu  >> {global_value.balance_pred_vplacilom != global_value.balance_po_vplacilu}")
                        if global_value.balance_pred_vplacilom != global_value.balance_po_vplacilu:
                            print("zneska balance se ne ujemata!!!")
                            print("\n\n KAR POMENI DA JE BILO VPLACANO AMPAK JE NEKJE NAPAKA MORDA V POVEZAVI \
                                \n ZATO JE POTREBNO ROCNO VNESTI PODATKE ZA MASANIELLO!!!\n\n")
                            # podatki_za_masaniello =  (1.0212, 'win')
                            podatki_za_masaniello[0] = trejd_je_odprt["deals"][0]["profit"]
                            podatki_za_masaniello[1] = "win" if trejd_je_odprt["deals"][0]["profit"] > 0 else "loose"
                            print("zadnji zakljucen trejd podatki_za_masaniello : ",podatki_za_masaniello)
                            print("zadnji zakljucen trejd podatki_za_masaniello[0] profit: ",podatki_za_masaniello[0])
                        
                        try:
                            print("zadnji zakljucen trejd podatki_za_masaniello profit: ",podatki_za_masaniello[0])
                        except Exception as e:
                            print("Exception as e = ",e)
                            print("except:: zadnji zakljucen trejd podatki_za_masaniello profit: ",podatki_za_masaniello)
                            print("pred if >> rezultat_ma3 = ",rezultat_ma3)
                            if not rezultat_ma3[0]:
                                quit("\n\nIZHOD KER NI BILO VPLACANO\n\n")
                            
                        print("\n\n************************************ \
                            \nKONEC PREVERJANJA ZAKLJUCENIH TREJDOV \
                            \n**************************************\n\n")
                        
                    if rezultat_ma3[0]:
                        podatki_za_masaniello = api.check_win(rezultat_ma3[1])
                        print("\n*** AKTIVNI *** PODATKI ZA MASANIELO: podatki_za_masaniello = ",podatki_za_masaniello)
                        if podatki_za_masaniello[1] == "unknown":
                            print("\n\n*************** ZAKLJUCI IN KONCAJ SKRIPT ZARADI NEVELJAVNIH PODATKOV!!!****api_Stop() namesto quit()***\n\n")
                            api.Stop()
                            quit("**** quit *****\n\n")
                        """ *****************  MASANIELLO ZA ma3 *************************"""
                        if podatki_za_masaniello[0] > 0:
                            #zmaga
                            print("\nZMAGA ",datetime.now())
                            print(f"\ntest izpisa za smer {smer} ki jo dodam k globalni!!\n")
                            global_value.izzid_trejda = "ZMAGA"
                            global_value.zadnja_smer_trejda = smer
                            
                            print("\n\n************************** PREVERJANJE ****************************\n")
                            print("ZMAGAL JE ZNESEK = ",podatki_za_masaniello[0])
                            print(f"Vplacan znesek: {vloga_ma3+0.1:.2f}")
                            print("nov znesek za trejdanje = ", podatki_za_masaniello[0] + vloga_ma3 +0.1)
                            investicija = (vloga_ma3 + 0.1) * 1.92
                            print(f"ALI znesek * 1,92 = {(vloga_ma3 + 0.1) * 1.92:.2f}")
                            print("\n\n************* K O N E C ************* PREVERJANJE IZRACUNA ****************************\n\n")
                            print("\n============ Z M A G A ================== >>  >>> Priprava za novi krog: ")
                            print("Mmm.ponovitev = ",Mmm.ponovitev)
                            print("\n>>>>> krog_obrat = ",krog_obrat)
                            # inp = 1 if odgovor[1]== "win" else 0
                            # ce je rezultat pozitiven bom sesteval profit do dolocene vsote
                            # nova investicija je znesek ki se je vplacal in znesek ki je bil dobitni
                            print("VPLACANI ZNESEK: ",vloga_ma3)
                            print("dodano k vplacenemu znesku = 0.1")
                            print("zato je vplacani znesek skupaj ",vloga_ma3 + 0.1)
                            print(f"prva investicija = {prva_investicija} vloga = {vloga_ma3} vplacani znesek skupaj {vloga_ma3 + 0.1}\n\n")
                            
                            Mmm.Rezultat(1)
                            dosezeno = Mmm.NoviKrog()
                            print("================================= kaj pa investicija je ",dosezeno[1])
                            print("================================= nova  investicija je ",investicija)
                            print("\nDOSEZENO izpis = ",dosezeno)
                            
                            
                            povzeto["trejd je = "] = "POZITIVEN TREJD"
                            povzeto["stanje racuna GV= "] = global_value.balance
                            povzeto["stanje racuna api= "] = api.get_balance()
                            print("\n************************** *** K O N E C *** PREVERJANJE ****************************\n\n")
                            zapis_rezultata(povzeto)
                            povzeto={}
                            negativni_trejdi = 0
                            if dosezeno[0] == 2:
                                print("\n\n**************==============*********************\n")
                                print("DOSEZEN USPEH!! RESET ZA PONOVNI KROG!! cas=",datetime.now())
                                print("\n\n**************==============*********************\n")
                                #time.sleep(120)
                                print(("PRED PRAZNJENJEM >> izpis vlog = ",global_value.vloga))
                                global_value.vloga=[]
                                global_value.prehod_pristop = "ne"
                                global_value.prehod_pristop_kombo = "ne"
                                global_value.prehod_pristop_kombo_hiter = "ne"
                                
                                print(("PO PRAZNJENJU >> izpis vlog = ",global_value.vloga))
                                krog_obrat=0
                                
                                print("\n KLICEM FUNKCIJO MASANIELLO!! \n\n")
                                masaniello()
                                
                            vloga_ma3 = dosezeno[1]
                            if vloga_ma3 < 1:
                                print("\n\nvloga je manjsa kot 1 ********** klicem masaniello() !! ")
                                print(("PRED PRAZNJENJEM >> izpis vlog = ",global_value.vloga))
                                global_value.vloga=[]
                                print(("PO PRAZNJENJU >> izpis vlog = ",global_value.vloga))
                                print("\n KLICEM FUNKCIJO MASANIELLO!! \n\n")
                                krog_obrat=0
                                masaniello()
                                
                        elif podatki_za_masaniello[0] < 0:
                            #izguba
                            print("\nporaz ",datetime.now())
                            print(f"\ntest izpisa za smer {smer} ki jo dodam k globalni!!\n")
                            global_value.izzid_trejda = "PORAZ"
                            global_value.zadnja_smer_trejda = smer
                            negativni_trejdi += 1
                            print(
                                "\n========= P O R A Z =====================>>>> Priprava za novi krog: ",
                                Mmm.ponovitev,
                            )
                            # inp = 1 if odgovor[1]== "win" else 0
                            Mmm.Rezultat(0)
                            dosezeno = Mmm.NoviKrog()
                            print(
                                "\n=================================kaj pa investicija je ",
                                dosezeno[1],
                            )
                            print("DOSEZENO izpis = ",dosezeno)
                            print("DOSEZENO test dosezeno[0] == 3 = ",dosezeno[0] == 3)
                            povzeto["stanje racuna = "] = api.get_balance()
                            print("Stanje racuna: ",povzeto["stanje racuna = "])
                            print("\nPREVERJANJE ZA NOVO VLOGO IZ GV.masanillo lista = ",global_value.masaniello_vloge[negativni_trejdi])
                            if povzeto["stanje racuna = "] < dosezeno[1]:
                                print("TUKAJ USTAVLJAM SKRIPT KER JE STANJE RACUNA MANJSE KOT JE NASLEDNJA VLOGA!!!")
                                dosezeno[0]=3
                            krog_obrat += 1
                            povzeto["trejd je = "] = "NEGATIVEN TREJD"
                            zapis_rezultata(povzeto)
                            povzeto={}
                            if dosezeno[0] == 3:
                                print("\nZAKLJUCUJEM MASANIELLO!! vloga JE NA NULI!!! \n cas = ",datetime.now())
                                print("\nZA IZHOD JE UPORABLJEN >> quit <<\n\n")
                                #break
                                #print("\nZA IZHOD JE UPORABLJEN >> RETURN <<\n\n")
                                #return
                                quit()
                                
                            vloga_ma3 = dosezeno[1]
                            
                            #krog_obrat += 1
                            #print("v izgubi POVECAM krog_obrat ZA 1")
                            
                            """
                            print(vloga_ma3," *PRED ** PRESKOK ZA 2 MINUTI CAS: ",datetime.now())
                            time.sleep(120)
                            print(vloga_ma3," PRESKOK ZA 2 MINUTI CAS: ",datetime.now())
                            """
                        elif podatki_za_masaniello[0] == 0:
                            # NEC
                            print("\nNEC ",datetime.now())
                            #vloga_ma3 
                            povzeto["trejd je = "] = "***NEC*** TREJD"
                            povzeto["stanje racuna = "] = api.get_balance()
                            zapis_rezultata(povzeto)
                            povzeto={}
                            
                        """ ***************** KONEC MASANIELLO ZA ma3 *************************"""
                        
                        
                        print("\n\n*************************************************** \n")
                        print(f"(STEVEC: {krog_obrat} ) VLOGA ZA MA_3 JE NASTAVLJENA NA ZNESEK: {vloga_ma3:.2f} cas: {datetime.now()} ")
                        print("\n*************************************************** \n")
                        
                        """ ZAPIS ZNESKA V GLAOBAL """
                        global_value.vloga.append(vloga_ma3)
                        print(">>>>>>>> vse zapisane vloge : ",global_value.vloga)
                        
                        if global_value.vloga[-1] == 0:
                            print("\n\n\nKONCUJEM Z quit KER JE VLOGA NA NULI!!! !!!\n\n\n")
                            #break
                            #print("\n\n\nKONCUJEM Z RETURN KER JE VLOGA NA NULI!!! DA GREM IZ FUNKCIJE TRENUTNO JE RETURN PRAZEN!!!\n\n\n")
                            #return
                            quit()
                            
                        
                    else:
                        print("\n\n\nKONCUJEM  KER JE VLOGA NA NULI!!! DA GREM IZ while loop!!!\n\n\n")
                        ##break
                        #print("\n\n\nKONCUJEM Z RETURN KER JE VLOGA NA NULI!!! DA GREM IZ FUNKCIJE TRENUTNO JE RETURN PRAZEN!!!\n\n\n")
                        #print(f"\n::RETURN:: ZAKLJUCUJEM PODATKI MA_3 SO >FALSE< ({rezultat_ma3})!!! \n cas = {datetime.now()} ")
                        #return
                        print(f"\n::quit:: ZAKLJUCUJEM PODATKI MA_3 SO >FALSE< ({rezultat_ma3})!!! \n cas = {datetime.now()} \n\n")
                        quit()
            else:
                if testiranje_skripta:
                    print("\n TESTIRANJE SKRIPTA ********* NACIN MASANIELLO JE IZKLOPLJEN!!!\n\n")
                if labu:
                    print("\nNACIN LABUSHERE *************** NACIN MASANIELLO JE IZKLOPLJEN!!\n\n")
                    print("LABUSHE VLOGE: ",global_value.laubuchere_vloge)
         
                    
            if api.get_balance() < 1:
                #print("\n\nif api.get_balance() < 1:\nKONCUJEM Z RETURN KER JE VLOGA NA NULI!!! DA GREM IZ FUNKCIJE TRENUTNO JE RETURN PRAZEN!!!\n\n\n")
                #print("\n::RETURN:: ZAKLJUCUJEM BANKA JE NA NULI!!! \n cas = ",datetime.now())
                #return
                print("\nZAKLJUCUJEM BANKA JE NA NULI!!! \n cas = ",datetime.now(),"\n\n")
                quit()
                
                
            
            """****************VAZNO VAZNO VAZNO VAZNO VAZNO****************************************************"""
            """****************VAZNO VAZNO VAZNO VAZNO VAZNO****************************************************"""
            
            """ PREVERJANJE IN PRIMERJAVA V PROCETIH IN NJIHOVA OBNOVA """
            
            #aktivni_payout = global_value.pairs[Aktivni_par]["payout"]
            #print("\n\n==============>>>>> global_value.assets[0] = ",global_value.assets[0])
            #print("\n")
            primerjevalni_payout = 0
            for i in global_value.assets:
                #print(i)
                if i[1] == Aktivni_par:
                    #print(f"\nIZPIS IZ SEZNAMA ASSETS:\n PAR: {Aktivni_par}\n PODATKI: {i}")
                    #print(f"\nPRIMERJAVA pairs in assets: \npairs-payout: {global_value.pairs[Aktivni_par]["payout"]} \nassets-payout: {i[5]} \n")
                    primerjevalni_payout = i[5]
                    
            print("\n")
            print("VAZNO "*5)
            print(f"\n >>>>>>> PAR: {Aktivni_par} <<<<<<<<")
            print(f"\n >>>>>>> banka: {global_value.balance} <<<<<<<<")
            print(f"\nIZID PRIMERJAVE pairs= {aktivni_payout} VS assets= {primerjevalni_payout} STA ENAKA {aktivni_payout == primerjevalni_payout} \ncas = {datetime.now()}")
            print("\n","VAZNO "*5,"\n")
            
            """ PREVERJANJE IN PRIMERJAVA V PROCENTIH IN NJIHOVA OBNOVA === KONEC ==="""
            
            """
            # ce je false preveri kaksen je bil zadnji trejd:
                # - ce je bil negativen
                # - ce je bil pozitiven
                # zacni novo z boljsimi procenti!!!
            """
            if aktivni_payout != primerjevalni_payout:
                print(Aktivni_par," ker nista enaka klicem ponovno >> masaniello <<")
                #novi_par=None
                for i in global_value.assets:
                    if  i[14] == True and "_otc" in i[1] and i[5] == 92 and i[3] == "currency":
                        print(i)
                        Aktivni_par = i[1]
                        break
                    """
                    PRIMER IZPISA:
                    [68, 'AUDCHF_otc', 'AUD/CHF OTC', 'currency', 5, 92, 60, 30, 3, 1, 0, 37, [], 1763251200, True, [{'time': 60}, {'time': 120}, {'time': 180}, {'time': 300}, {'time': 600}, {'time': 900}, {'time': 1800}, {'time': 2700}, {'time': 3600}, {'time': 7200}, {'time': 10800}, {'time': 14400}], 0, 3, -1]
                    [38, 'AUDJPY', 'AUD/JPY', 'currency', 3, 50, 60, 30, 3, 0, 69, 0, [], 1763251200, False, [{'time': 60}, {'time': 120}, {'time': 180}, {'time': 300}, {'time': 600}, {'time': 900}, {'time': 1800}, {'time': 2700}, {'time': 3600}, {'time': 7200}, {'time': 10800}, {'time': 14400}], -1, 60, 1763344800]
                    [69, 'AUDJPY_otc', 'AUD/JPY OTC', 'currency', 3, 80, 60, 30, 3, 1, 0, 38, [], 1763251200, True, [{'time': 60}, {'time': 120}, {'time': 180}, {'time': 300}, {'time': 600}, {'time': 900}, {'time': 1800}, {'time': 2700}, {'time': 3600}, {'time': 7200}, {'time': 10800}, {'time': 14400}], 0, 3, -1]
                    """
                """
                api.change_symbol(novi_par,60)
                time.sleep(1)
                print("\n\nKONCAN IZPISA ASSETS! KLICEM MASANIELLO!!\n\n")
                quit("ZAENKRAT USTAVLJENO \n\n")
                masaniello()
                """
                    
                # par = Aktivni_par
                # menjava =api.change_symbol(Aktivni_par,60)
                # menjava =api.change_symbol(Aktivni_par,30)
                #svece = api.get_candles(Aktivni_par, 60)
                if not zgodovina_svec(Aktivni_par,60):
                    quit("IZHOD zgodovina_svec (quit())")
                """        
                api.get_candles(Aktivni_par, 60)
                time.sleep(1)
                print(
                    f"aktivni par: {Aktivni_par} zapisan:  ",
                    "JE" if Aktivni_par in global_value.zgodovina_3 else "NI",
                )
                global_value.dolzina_kljucev =0
                if Aktivni_par not in global_value.zgodovina_3:
                    exit(f"\n============= IZHOD ==============\n NI ZAPISA V ZGODOVINI ZA PAR: {Aktivni_par} ")
                    quit("IZHOD QUIT!!")
                    
                    
                print("kluci v zgodovini ", global_value.zgodovina_3.keys())
                if Aktivni_par in global_value.zgodovina_3:
                    if "zgodovina" in global_value.zgodovina_3[Aktivni_par]:
                        print("\n\n *******drugic********** POGOJI SO IZPOLNJENI  *********drugic********* \n")
                        print(" par je v zgodovini 3 in zgodovina je zapisana!!!!\n")
                """
                """ RESETIRANJE DOLOCENIH PODATKOV ZARADI ZAMENJAVE PARA !!! """
                global_value.minute[Aktivni_par]=bars(Aktivni_par)
                global_value.trikotnik_akcija = None
                global_value.trikotnik_akcija_m5 = None
            
            """****************VAZNO VAZNO VAZNO VAZNO VAZNO****************************************************"""
            
        minute[zadnji_izdelan_kluc_minute].append(zadnja_aktivna_cena)
        try:
            global_value.minute[Aktivni_par][zadnji_izdelan_kluc_minute].append(zadnja_aktivna_cena)
        except Exception as e:
            print(f"\ntry blok::: napaka: {e} pri global_value.minute[Aktivni_par]\n")
    
        time.sleep(1)
        
        
        # TUKAJ MORAM POSKUSITI Z MA_3
        
        """
        # tukaj se dogajajo aktivne stvari 
        print("TO JE AKTIVNI DEL PROCESA IN LAHKO IZPISUJEM TUDI CAS IN CENO")
        print(f"cas {gv_cas} cena = {gv_cena}")
        #> primer izpisa
        #> cas 2025-10-16 11:47:11.568000 cena = 0.9432
        #> TO JE AKTIVNI DEL PROCESA IN LAHKO IZPISUJEM TUDI CAS IN CENO
        #> cas 2025-10-16 11:47:12.553000 cena = 0.94313
        
        """
        """ AKTIVNO SPREMLJANJE """
        if trejd_aktiven:
            
            MA10 = moving_average(bars(Aktivni_par), 10)
            MA5 = moving_average(bars(Aktivni_par), 5)
            MA3 = moving_average(bars(Aktivni_par), 3)
            MA2 = moving_average(bars(Aktivni_par), 2)
            #print(MA10)
            if len(MA10) >=4:
                bar0 = ohlc(bars(Aktivni_par),0)
                bar1 = ohlc(bars(Aktivni_par),1)
                #bar2 = ohlc(bars(Aktivni_par),2)
                C,T,D,P = MA10[-4:]
                C5,T5,D5,P5 = MA5[-4:]
                C3,T3,D3,P3 = MA3[-4:]
                C2,T2,D2,P2 = MA2[-4:]
                
                #>print("negativni trejdi = ",negativni_trejdi)
                # IMA PRVA SVECA ZGORNJI IN SPODNJI VIK
                """
                zgoraj = max(bar0["o"] , bar0["c"])
                spodaj = min(bar0["o"] , bar0["c"])
                vik_z = False
                vik_s = False
                if zgoraj < bar0["h"]:
                    print("\n zgornji vik je narejen ura ",datetime.now())
                    print("razlika = ",bar0["h"]-zgoraj)
                if spodaj > bar0["l"]:
                    print("\n spodnji vik je narejen ura ",datetime.now())
                    print("razlika = ",spodaj - bar0["l"])
                if vik_z and vik_s:
                    print(f"\nNAREJENA STA OBA VIKA SEDAJ PREVERI CENO VIK ZGORAJ = {bar0['h']} VIK SPODAJ = {bar0['l']}")
                    """
                #zadnja_cena_15 =global_value.zgodovina_3[Aktivni_par]["zgodovina"][-15][1]
                #zadnja_cena_5 =global_value.zgodovina_3[Aktivni_par]["zgodovina"][-5][1]
                zadnja_cena_1 = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                
                if bar0["o"] > bar1["o"]:
                    #>print("\n\n***************++ 1 +++++++++++++***********\n")
                    trejd_je_odprt = api.get_async_order()
                    #>print(trejd_je_odprt)
                    if trejd_je_odprt is not None:
                        # {'profit': 2.11, 'deals': [{'id': '12caa98c-5390-4dfd-9ee9-074000f8aea7', 
                        #print("profit = ",trejd_je_odprt["profit"])
                        #print("id = ",trejd_je_odprt["deals"][0]["id"])
                        if deals_id is not  trejd_je_odprt["deals"][0]["id"]:
                            try:
                                print("profit = ",trejd_je_odprt["profit"] )
                                print("deals[0][profit] = ",trejd_je_odprt["deals"][0]["profit"] )
                                print("deals[0][id] = ",trejd_je_odprt["deals"][0]["id"])
                                deals_id = trejd_je_odprt["deals"][0]["id"]
                                global_value.trejd_je_odprt = False
                            except Exception as e:
                                print("except e: ",e)
                        
                            #print("preverjam profit == 0: ",trejd_je_odprt["profit"] == 0)
                            #print("preverjam profit != 0: ",trejd_je_odprt["profit"] != 0)
                            if trejd_je_odprt["profit"] == 0:
                                global_value.trejd_je_odprt = False
                                print("negativni trejdi v negativnem pred = ",negativni_trejdi)
                                negativni_trejdi += 1
                                pozitivni_trejdi = 0
                                print("negativni trejdi v negativnem PO = ",negativni_trejdi)
                            
                            if trejd_je_odprt["profit"] != 0 :
                                global_value.trejd_je_odprt = False
                                print("negativni trejdi v negativnem pred = ",negativni_trejdi)
                                negativni_trejdi =0
                                pozitivni_trejdi += 1
                                print("negativni trejdi v negativnem PO = ",negativni_trejdi)
                            print("\n CISCENJE VARIABLE >vplacano<  KI IMA VREDNOST = ",vplacano)
                            print("vplacano len = ",len(vplacano))
                            print("vplacano type = ",type(vplacano))
                            vplacano = ()
                            print("PO CISCENJU JE vplacano = ",vplacano)
                    #>print("\n***************+++++++++++++++***********\n\n")
                    
                    #if bar1["h"] < zadnja_cena_1 :<
                    if bar1["c"] < zadnja_cena_1 :
                        # ko gre preko kupi za ali do konca
                        # to naredi samo enkrat na sveco
                        sekunde = int(datetime.now().second)
                        razlika_do_konce_minute = 60 - sekunde
                        print("TRENUTNO JE SEKUND: ",sekunde ," razlika do 60 = ",razlika_do_konce_minute)
                        print("URA: ",datetime.now())
                        trejd_aktiven = False
                        if razlika_do_konce_minute > 6:
                            #preveri kaksen je bil prejsen trejd
                            #print("preveri ce je odprti trejd ce je pocakaj vplacano = ",vplacano)
                            print("***BAR BAR ** SPROZI NAKUP ")
                            """
                            cena_pred = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena pred = ",cena_pred)
                            time.sleep(1)
                            cena_po = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena PO = ",cena_po)
                            za_smer = "call" if cena_pred < cena_po else "put"
                            """
                            
                            vplacilo = negativni_trejdi
                            print("call vplacilo za masanielo = ",vplacilo)
                            print("put masaniello_vloge = ",global_value.masaniello_vloge)
                            vplacilo = global_value.masaniello_vloge[vplacilo]
                            
                            print("\nput POTREBNO JE VPLACATI ",vplacilo)
                            if negativni_trejdi >= 3:
                                print("\nGV.balance:: STANJE BANKE: ",global_value.balance)
                                print("1 >> preveri banko in ce je potrebno zmanjsaj znesek na minimalno")
                                print(">> prva pozicija masanielo je = ",global_value.masaniello_vloge[0])
                            
                            # 10 X 1.1 = 11
                            if global_value.balance < global_value.masaniello_vloge[0] * 10:
                                vplacilo = global_value.masaniello_vloge[0]
                            
                                if pozitivni_trejdi == 2:
                                    vplacilo = global_value.masaniello_vloge[2]
                                
                            #za_smer = "call" if P < P5 else "put"
                            #vplacano = akcija(1.1, Aktivni_par, za_smer, 5)# 1.2
                            
                            if bar1["c"] < D3 < P5 <P:
                                print("\ntu je prodaja")
                            if bar1["c"] > D3 > P5 >P:
                                print("\ntu je nakup")
                                
                            izracun_procentov(P,P5)
                            print("\nza ma2 in ma3 stanje je: ", "P2 JE ZGORAJ " if P2 > P3 else "P3 je zgoraj")
                            print("za ma2 in ma3 stanje je: ", "D2 JE ZGORAJ " if D2 > D3 else "D3 je zgoraj")
                            print("za ma2 in ma5 stanje je: ", "*D2* JE ZGORAJ " if D2 > D5 else "*D5* je zgoraj")
                            print("za MA5 SMER P5 in D5 je: ", "SMER JE GOR " if P5 > D5 else "SMER JE DOL ")
                            print("za MA10 SMER P in D je: ", "SMER JE GOR " if P > D else "SMER JE DOL ")
                            print("za MA10  P in zadnja_cena_1 je: ", "SMER JE DOL " if P > zadnja_cena_1 else "SMER JE GOR ")
                            za_smer = "put" if P > D5 and P5 > D2 else "call"
                            print("(1)> za smer je = ",za_smer)
                            print("vplacano len = ",len(vplacano))
                            print("preverjanje pred vplacilom ali je trejd odprt ",global_value.trejd_je_odprt)
                            vplacano = akcija(vplacilo, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<<
                            #vplacano = akcija(1.1, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<
                            #vplacano = akcija(1.1, Aktivni_par, "call", razlika_do_konce_minute)# 1.2<
                            print("call vplacano = ",vplacano)
                            
                    if bar1["o"] > zadnja_cena_1:
                        # ko gre spodaj prodaj za 5 ali do konca 
                        # to naredi samo enkrat na sveco
                        sekunde = int(datetime.now().second)
                        razlika_do_konce_minute = 60 - sekunde
                        print("TRENUTNO JE SEKUND: ",sekunde ," razlika do 60 = ",razlika_do_konce_minute)
                        print("URA: ",datetime.now())
                        trejd_aktiven = False
                        if razlika_do_konce_minute > 6:
                            #preveri kaksen je bil prejsen trejd
                            #print("preveri ce je odprti trejd ce je pocakaj vplacano = ",vplacano)
                            print("***BAR BAR ** SPROZI PRODAJO ")
                            """
                            cena_pred = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena pred = ",cena_pred)
                            time.sleep(1)
                            cena_po = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena PO = ",cena_po)
                            za_smer = "put" if cena_pred > cena_po else "call"
                            """
                            
                            
                            vplacilo = negativni_trejdi
                            print("call vplacilo za masanielo = ",vplacilo)
                            print("put masaniello_vloge = ",global_value.masaniello_vloge)
                            vplacilo = global_value.masaniello_vloge[vplacilo]
                            
                            print("\nput POTREBNO JE VPLACATI ",vplacilo)
                            if negativni_trejdi >= 3:
                                print("\nGV.balance:: STANJE BANKE: ",global_value.balance)
                                print("2 >> preveri banko in ce je potrebno zmanjsaj znesek na minimalno")
                                print(">> prva pozicija masanielo je = ",global_value.masaniello_vloge[0])
                            
                            # 10 X 1.1 = 11
                            if global_value.balance < global_value.masaniello_vloge[0] * 10:
                                vplacilo = global_value.masaniello_vloge[0]
                                
                            
                                if pozitivni_trejdi == 2:
                                    vplacilo = global_value.masaniello_vloge[2]
                                
                            #za_smer = "put" if P > P5 else "call"
                            #vplacano = akcija(1.1, Aktivni_par, za_smer, 5)# 1.2
                            #za_smer = "put" if P > D5 else "call"
                            
                            if bar1["c"] < D3 < P5 <P:
                                print("\ntu je prodaja")
                            if bar1["c"] > D3 > P5 >P:
                                print("\ntu je nakup")
                                
                            izracun_procentov(P,P5)
                            print("\nza ma2 in ma3 stanje je: ", "P2 JE ZGORAJ " if P2 > P3 else "P3 je zgoraj")
                            print("za ma2 in ma3 stanje je: ", "D2 JE ZGORAJ " if D2 > D3 else "D3 je zgoraj<")
                            print("za ma2 in ma5 stanje je: ", "*D2* JE ZGORAJ " if D2 > D5 else "*D5* je zgoraj")
                            print("za MA5 SMER P5 in D5 je: ", "SMER JE GOR " if P5 > D5 else "SMER JE DOL ")
                            print("za MA10 SMER P in D je: ", "SMER JE GOR " if P > D else "SMER JE DOL ")
                            print("za MA10  P in zadnja_cena_1 je: ", "SMER JE DOL " if P > zadnja_cena_1 else "SMER JE GOR ")
                            za_smer = "put" if P > D5 and P5 > D2 else "call"
                            print("(2)> za smer je = ",za_smer)
                            print("vplacano len = ",len(vplacano))
                            print("vplacano (to bi  moralo biti prazno)  = ",vplacano)
                            print("preverjanje pred vplacilom ali je trejd odprt ",global_value.trejd_je_odprt)
                            print(f"(2) Vplacilo: {vplacilo} za smer: {za_smer}")
                            vplacano = akcija(vplacilo, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<<
                            #vplacano = akcija(1.1, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<
                            #vplacano = akcija(1.1, Aktivni_par, "put", razlika_do_konce_minute)# 1.2<
                            print("put vplacano = ",vplacano)
                        
                if bar0["o"] < bar1["o"]: # to poneni da je bar ena bear
                    #>print("\n\n***************++ 2 +++++++++++++***********\n")
                    trejd_je_odprt = api.get_async_order()
                    #>print(trejd_je_odprt)
                    if trejd_je_odprt is not None:
                        #print("profit = ",trejd_je_odprt["profit"])
                        #print("id = ",trejd_je_odprt["deals"][0]["id"])
                        if deals_id is not trejd_je_odprt["deals"][0]["id"]:
                            try:
                                print("profit = ",trejd_je_odprt["profit"] )
                                print("deals[0][profit] = ",trejd_je_odprt["deals"][0]["profit"] )
                                print("deals[0][id] = ",trejd_je_odprt["deals"][0]["id"])
                                deals_id = trejd_je_odprt["deals"][0]["id"]
                                global_value.trejd_je_odprt = False
                            except Exception as e:
                                print("except e: ",e)
                        
                            if trejd_je_odprt["profit"] == 0 :
                                global_value.trejd_je_odprt = False
                                print("negativni trejdi v negativnem pred = ",negativni_trejdi)
                                negativni_trejdi += 1
                                pozitivni_trejdi = 0
                                print("negativni trejdi v negativnem PO = ",negativni_trejdi)
                            if trejd_je_odprt["profit"] != 0 :
                                global_value.trejd_je_odprt = False
                                print("negativni trejdi v negativnem pred = ",negativni_trejdi)
                                negativni_trejdi =0
                                pozitivni_trejdi += 1
                                print("negativni trejdi v negativnem PO = ",negativni_trejdi)
                            print("\n CISCENJE VARIABLE >vplacano<  KI IMA VREDNOST = ",vplacano)
                            print("vplacano len = ",len(vplacano))
                            print("vplacano type = ",type(vplacano))
                            vplacano = ()
                            print("PO CISCENJU JE vplacano = ",vplacano)
                            
                    #>print("\n***************+++++++++++++++***********\n\n")
                    #if bar1["l"] > zadnja_cena_1 :<
                    if bar1["c"] > zadnja_cena_1 :
                        # ko gre spodaj prodaj za ali do konca
                        # to naredi samo enkrat na sveco
                        sekunde = int(datetime.now().second)
                        razlika_do_konce_minute = 60 - sekunde
                        print("TRENUTNO JE SEKUND: ",sekunde ," razlika do 60 = ",razlika_do_konce_minute)
                        print("URA: ",datetime.now())
                        trejd_aktiven = False
                        if razlika_do_konce_minute > 6:
                            #preveri kaksen je bil prejsen trejd
                            #print("preveri ce je odprti trejd ce je pocakaj vplacano = ",vplacano)
                            # 
                            # 
                            print("***BAR BAR ** SPROZI PRODAJO ")
                            """
                            cena_pred = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena pred = ",cena_pred)
                            time.sleep(1)
                            cena_po = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena PO = ",cena_po)
                            za_smer = "put" if cena_pred > cena_po else "call"
                            """
                            
                            
                            vplacilo = negativni_trejdi
                            print("call vplacilo za masanielo = ",vplacilo)
                            print("put masaniello_vloge = ",global_value.masaniello_vloge)
                            vplacilo = global_value.masaniello_vloge[vplacilo]
                            
                            print("\nput POTREBNO JE VPLACATI ",vplacilo)
                            if negativni_trejdi >= 3:
                                print("\nGV.balance:: STANJE BANKE: ",global_value.balance)
                                print("3 >> preveri banko in ce je potrebno zmanjsaj znesek na minimalno")
                                print(">> prva pozicija masanielo je = ",global_value.masaniello_vloge[0])
                            # 10 X 1.1 = 11
                            if global_value.balance < global_value.masaniello_vloge[0] * 10:
                                vplacilo = global_value.masaniello_vloge[0]
                                
                            
                                if pozitivni_trejdi == 2:
                                    vplacilo = global_value.masaniello_vloge[2]
                            
                            #za_smer = "put" if P > P5 else "call"
                            #vplacano = akcija(1.1, Aktivni_par, za_smer, 5)# 1.2
                            #za_smer = "put" if P > D5 else "call"
                            
                            if bar1["c"] < D3 < P5 <P:
                                print("\ntu je prodaja")
                            if bar1["c"] > D3 > P5 >P:
                                print("\ntu je nakup")
                                
                            izracun_procentov(P,P5)
                            print("\nza ma2 in ma3 stanje je: ", "P2 JE ZGORAJ " if P2 > P3 else "P3 je zgoraj")
                            print("za ma2 in ma3 stanje je: ", "D2 JE ZGORAJ " if D2 > D3 else "D3 je zgoraj<")
                            print("za ma2 in ma5 stanje je: ", "*D2* JE ZGORAJ " if D2 > D5 else "*D5* je zgoraj")
                            print("za MA5 SMER P5 in D5 je: ", "SMER JE GOR " if P5 > D5 else "SMER JE DOL ")
                            print("za MA10 SMER P in D je: ", "SMER JE GOR " if P > D else "SMER JE DOL ")
                            print("za MA10  P in zadnja_cena_1 je: ", "SMER JE DOL " if P > zadnja_cena_1 else "SMER JE GOR ")
                            za_smer = "put" if P > D5 and P5 > D2 else "call" if P < D5 and P5 < D2 else "ne"
                            print("(3)> za smer je = ",za_smer)
                            """
                            if P3 > P2:
                                print("preverjam za obrat bar1 je ?BEAR? ",bar1["s"])
                            if za_smer == "call" and P3 > D2 :#and bar1["s"] == "BEAR":
                                print("obrat smeri iz *call* v -put- SVECA JE: ?BEAR? ", bar1["s"])
                                za_smer = "put"
                                """
                            print("PREVERJANJE PRED IF: za_smer = ",za_smer)
                            if za_smer != "ne":
                                print("vplacano len = ",len(vplacano))
                                print("preverjanje pred vplacilom ali je trejd odprt ",global_value.trejd_je_odprt)
                                vplacano = akcija(vplacilo, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<<
                                #vplacano = akcija(1.1, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<
                                #vplacano = akcija(1.1, Aktivni_par, "put", razlika_do_konce_minute)# 1.2<
                                print("put vplacano = ",vplacano)
                            
                    if bar1["o"] < zadnja_cena_1:
                        # ko gre zgoraj kupi za 5 ali do konca 
                        # to naredi samo enkrat na sveco
                        sekunde = int(datetime.now().second)
                        razlika_do_konce_minute = 60 - sekunde
                        print("TRENUTNO JE SEKUND: ",sekunde ," razlika do 60 = ",razlika_do_konce_minute)
                        print("URA: ",datetime.now())
                        trejd_aktiven = False
                        if razlika_do_konce_minute > 6:
                            #preveri kaksen je bil prejsen trejd
                            #print("preveri ce je odprti trejd ce je pocakaj vplacano = ",vplacano)
                            print("***BAR BAR ** SPROZI NAKUP ")
                            """
                            cena_pred = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena pred = ",cena_pred)
                            time.sleep(1)
                            cena_po = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                            print("cena PO = ",cena_po)
                            za_smer = "call" if cena_pred < cena_po else "put"
                            """
                            vplacilo = negativni_trejdi
                            print("call vplacilo za masanielo = ",vplacilo)
                            print("put masaniello_vloge = ",global_value.masaniello_vloge)
                            vplacilo = global_value.masaniello_vloge[vplacilo]
                            
                            print("\nput POTREBNO JE VPLACATI ",vplacilo)
                            if negativni_trejdi >= 3:
                                print("\nGV.balance:: STANJE BANKE: ",global_value.balance)
                                print("4 >> preveri banko in ce je potrebno zmanjsaj znesek na minimalno")
                                print(">> prva pozicija masanielo je = ",global_value.masaniello_vloge[0])
                                
                            # 10 X 1.1 = 11
                            if global_value.balance < global_value.masaniello_vloge[0] * 10:
                                vplacilo = global_value.masaniello_vloge[0]
                                
                            
                                if pozitivni_trejdi == 2:
                                    vplacilo = global_value.masaniello_vloge[2]
                            
                            #za_smer = "call" if P < P5 else "put"
                            #vplacano = akcija(1.1, Aktivni_par, za_smer, 5)# 1.2
                            #za_smer = "put" if P > D5 else "call"
                            # 
                            
                            if bar1["c"] < D3 < P5 <P:
                                print("\ntu je prodaja")
                            if bar1["c"] > D3 > P5 >P:
                                print("\ntu je nakup")
                            izracun_procentov(P,P5)
                            print("\nza ma2 in ma3 stanje je: ", "P2 JE ZGORAJ " if P2 > P3 else "P3 je zgoraj")
                            print("za ma2 in ma3 stanje je: ", "D2 JE ZGORAJ " if D2 > D3 else "D3 je zgoraj<")
                            print("za ma2 in ma5 stanje je: ", "*D2* JE ZGORAJ " if D2 > D5 else "*D5* je zgoraj")
                            print("za MA5 SMER P5 in D5 je: ", "SMER JE GOR " if P5 > D5 else "SMER JE DOL ")
                            print("za MA10 SMER P in D je: ", "SMER JE GOR " if P > D else "SMER JE DOL ")
                            print("za MA10  P in zadnja_cena_1 je: ", "SMER JE DOL " if P > zadnja_cena_1 else "SMER JE GOR ")
                            za_smer = "put" if P > D5 and P5 > D2 else "call"
                            print("(4)> za smer je = ",za_smer)
                            print("vplacano len = ",len(vplacano))
                            print("preverjanje pred vplacilom ali je trejd odprt ",global_value.trejd_je_odprt)
                            vplacano = akcija(vplacilo, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<<
                            #vplacano = akcija(1.1, Aktivni_par, za_smer, razlika_do_konce_minute)# 1.2<
                            #vplacano = akcija(1.1, Aktivni_par, "call", razlika_do_konce_minute)# 1.2<
                            print("call vplacano = ",vplacano)
                    
                """
                # za dol
                if P > zadnja_cena_1:
                    print("\n\n***************+++++++++++++++***********\n")
                    trejd_je_odprt = api.get_async_order()
                    print(trejd_je_odprt)
                    print("\n***************+++++++++++++++***********\n\n")
                    if bar0["o"] > bar1["l"]:
                        if bar1["l"] > zadnja_cena_1 :
                            print(f"\n***********************************============== A K T I V N O ** SPREMLJANJNE ===== PAR: {Aktivni_par} ==============**********************\n\n")
                            print(f"bar0['O'] = {bar0['o']} > bar1 l = {bar1['l']} > zadnja_cena = {zadnja_cena_1} < P = {P}")
                            print("\ntukaj prodas in cas je do zakljucka svece!\n")
                            sekunde = int(datetime.now().second)
                            razlika_do_konce_minute = 60 - sekunde
                            print("TRENUTNO JE SEKUND: ",sekunde ," razlika do 60 = ",razlika_do_konce_minute)
                            print("URA: ",datetime.now())
                            trejd_aktiven = False
                            if razlika_do_konce_minute > 6:
                                #preveri kaksen je bil prejsen trejd
                                #print("preveri ce je odprti trejd ce je pocakaj vplacano = ",vplacano)
                                print("SPROZI PRODAJO ")
                                time.sleep(1)
                                vplacano = akcija(1.1, Aktivni_par, "put", razlika_do_konce_minute-2)# 1.2
                                print("put vplacano = ",vplacano)
                                
                                
                            print("\n------------------------>>> ***********************************============== A K T I V N O (prodaja) SPREMLJANJNE ===================**********************\n\n")
                # za gor
                if P < zadnja_cena_1:
                    print("\n\n***************+++++++++++++++***********\n")
                    trejd_je_odprt = api.get_async_order()
                    print(trejd_je_odprt)
                    print("\n***************+++++++++++++++***********\n\n")
                    if bar0["o"] < bar1["h"]:
                        if bar1["h"] < zadnja_cena_1:
                            print(f"bar1 h = {bar1['h']} < zadnja_cena = {zadnja_cena_1} > P = {P}  ")
                            print(f"\n***********************************============== A K T I V N O ** SPREMLJANJNE ====== PAR: {Aktivni_par} =============**********************\n\n")
                            print("tukaj KUPIS in cas je do zakljucka svece!\n")
                            sekunde = int(datetime.now().second)
                            razlika_do_konce_minute = 60 - sekunde
                            print("TRENUTNO JE SEKUND: ",sekunde ," razlika do 60 = ",razlika_do_konce_minute)
                            print("URA: ",datetime.now())
                            trejd_aktiven = False
                            if razlika_do_konce_minute > 6:
                                # preveri kaksen je bil prejsen trejd
                                # 
                                #print("preveri ce je odprti trejd ce je pocakaj vplacano = ",vplacano)
                                print("SPROZI NAKUP ")
                                time.sleep(1)
                                vplacano = akcija(1.1, Aktivni_par, "call", razlika_do_konce_minute-2)# 1.2
                                print("call vplacano = ",vplacano)
                                
                            
                            
                            
                            print("\n++++++++++++++++++++++>>> *************************************============= A K T I V N O (nakup) SPREMLJANJNE ================**********************\n\n")
                            """
                            
        #if not int(datetime.now().second)%10:
        if datetime.now().second > 0 and datetime.now().second < 2:
            trejd_aktiven = True
            print("\nRESET  RESET RESET<\n")
            print("\nRESET  RESET RESET<\n")
            print("\nRESET  RESET RESET\n")
            continue
            print(f"\n\n*******************************************************\
                    \n *** VSAKIH 10 SEKUND ({datetime.now().second}) ***\
                    \n*********************************************************\n\n")
            MA10 = moving_average(bars(Aktivni_par), 10)
            MA7 = moving_average(bars(Aktivni_par), 7)
            MA5 = moving_average(bars(Aktivni_par), 5)
            MA3 = moving_average(bars(Aktivni_par), 3)
            MA2 = moving_average(bars(Aktivni_par), 2)
            print(MA10)
            if len(MA10) >=4:
                bar0 = ohlc(bars(Aktivni_par),0)
                bar2 = ohlc(bars(Aktivni_par),2)
                C,T,D,P = MA10[-4:]
                C7,T7,D7,P7 = MA5[-4:]
                C5,T5,D5,P5 = MA5[-4:]
                C3,T3,D3,P3 = MA3[-4:]
                C2,T2,D2,P2 = MA2[-4:]
                zadnja_cena_15 =global_value.zgodovina_3[Aktivni_par]["zgodovina"][-15][1]
                zadnja_cena_5 =global_value.zgodovina_3[Aktivni_par]["zgodovina"][-5][1]
                zadnja_cena_1 = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1]
                print("\n15 ZADNJA CENA ",zadnja_cena_15)
                print("\n5 ZADNJA CENA ",zadnja_cena_5)
                print("\nZADNJA CENA ",zadnja_cena_1)
                
                """
                if P > T and P5 < T5:
                    print(f"\n\nmodra dva = {D} || rumena dva = {D5} PAR: {Aktivni_par}")
                    print(f"MODRA GRE GOR +++++ RUMENA GRE DOL +++++ NI TREJDA *** CONTINUE *** \nURA: {datetime.now()}\n\n")
                    continue
                if P < T and P5 > T5:
                    print(f"\n\nmodra dva = {D} || rumena dva = {D5}  PAR: {Aktivni_par}")
                    print(f"MODRA GRE DOL +++++ RUMENA GRE GOR +++++  NI TREJDA *** CONTINUE ***  PAR: {Aktivni_par} \nURA: {datetime.now()}\n\n")
                    continue
                if  P < bar0['o'] < P5 or P > bar0['o'] > P5 :
                    print(f" \n\n>> ODPIRANJE << MED MODRO IN RUMENO ***** NI TREJDA *** CONTINUE *** PAR: {Aktivni_par} \nURA: {datetime.now()} \n\n")
                    continue
                    
                    """
                    
                    
                #C = zadnja_cena_5
                P = zadnja_cena_1
                vsakih_10_sekund = "DOL" if C > P else "GOR" if C < P else "CAKAJ"
                print("\n izpis smeri = ",vsakih_10_sekund)
                #if C > P and P5 > P2:# smer je dol<
                if C > P and P5 > P:# smer je dol
                    print(f"\n v if gre dol izbor po bar = {'PRODAJ' if bar0['o'] < bar2['l'] else 'CAKAJ'}\n")
                    print(f"\n v if gre dol izbor po MA7 = {'PRODAJ' if P < P7 else 'CAKAJ'}\n")
                    print(f"\n v if gre dol izbor po MA3 = {'PRODAJ' if P < P3 else 'CAKAJ'}\n")
                    print(f"\n v if gre dol izbor po MA2 = {'PRODAJ' if P < P2 else 'CAKAJ'}\n")
                    print("\n***** smer je dol ************")
                    print("put za vplacilo podatki = ",global_value.podatki_hitri)
                    print("\nput za vplacilo podatki =  type = ",type(global_value.podatki_hitri))
                    print("*****************\n")
                    #print("\nput za vplacilo podatki[0] = ",global_value.podatki_hitri[0])
                    print("\nput global_value.negativni_hitri = ",global_value.negativni_hitri)
                    print("put gv_negativni_hitri = ",gv_negativni_hitri)
                    #negativni_hitri =global_value.negativni_hitri
                    print(f"\npred IF so podatki_hitri[0] = {global_value.podatki_hitri[0]} in podatki_hitri[1] = {global_value.podatki_hitri[1]}")
                    if global_value.podatki_hitri[0] >0 :
                        vplacilo = global_value.negativni_hitri =0
                        print("PRIMERJAVA put POZ gv_negativni_hitri = ",gv_negativni_hitri)
                        #print(">>> PUT ce je POZITIVEN trejd ga deli z 8 in dobis = ",global_value.balance/8)
                        print(f">>> PUT ce je POZITIVEN trejd ga deli z {gv_negativni_hitri} in dobis = {global_value.balance/gv_negativni_hitri}")
                        #vplacilo = global_value.balance/gv_negativni_hitri
                        gv_negativni_hitri =9
                    elif global_value.podatki_hitri[0] <0 :
                        global_value.negativni_hitri +=1
                        vplacilo = global_value.negativni_hitri 
                        #vplacilo = vplacilo += 1
                        #global_value.negativni_hitri = vplacilo
                        print("povecevanje v put ",global_value.negativni_hitri)
                        if gv_negativni_hitri > 2:
                            gv_negativni_hitri -=1
                        #vplacilo = gv_negativni_hitri
                        print("PRIMERJAVA put NEG gv_negativni_hitri = ",gv_negativni_hitri)
                        print(f">>> PUT ce je negativen trejd ga deli z {gv_negativni_hitri} in dobis = {global_value.balance/gv_negativni_hitri}")
                        print(">>> PUT ce je negativen trejd ga deli z 8 in dobis = ",global_value.balance/8)
                        #vplacilo = global_value.balance/gv_negativni_hitri
                    else :
                        vplacilo = global_value.negativni_hitri 
                        #vplacilo = global_value.balance/gv_negativni_hitri
                    """
                    """
                    print("call vplacilo za masanielo = ",vplacilo)
                    print("put masaniello_vloge = ",global_value.masaniello_vloge)
                    vplacilo = global_value.masaniello_vloge[vplacilo]
                    
                    print("\nput POTREBNO JE VPLACATI ",vplacilo)
                    
                    vplacano = akcija(vplacilo, Aktivni_par, "put", 55)# 1.2
                    print("put vplacano = ",vplacano)
                    api_check_win = api.check_win(vplacano[1])
                    print("\nput PREVERJANJE api.check_win = type = ",type(api_check_win))
                    print("\nput PREVERJANJE api.check_win = CEL IZPIS =  ",api_check_win)
                    global_value.podatki_hitri = api_check_win
                    print("\nput podatki od preverjanja so = ",global_value.podatki_hitri)
                    
                    
                #if C < P and P5 < P2: #  TUKAJ GRE GOR<
                if C < P and P5 < P: #  TUKAJ GRE GOR
                    print(f"\n v if gre gor izbor po bar = {'KUPI' if bar0['o'] > bar2['l'] else 'CAKAJ'}\n")
                    #print(f"\n v if gre gor izbor po ma7 = {'KUPI' if bar0['o'] > bar2['l'] else 'CAKAJ'}\n")
                    print(f"\n v if gre GOR izbor po MA7 = {'KUPI' if P > P7 else 'CAKAJ'}\n")
                    print(f"\n v if gre GOR izbor po MA3 = {'KUPI' if P > P3 else 'CAKAJ'}\n")
                    print(f"\n v if gre GOR izbor po MA2 = {'KUPI' if P > P2 else 'CAKAJ'}\n")
                    print("\n****** TUKAJ GRE GOR ***********")
                    print("\ncall za vplacilo podatki = ",global_value.podatki_hitri)
                    print("\ncall za vplacilo podatki = tip = ",type(global_value.podatki_hitri))
                    print("*****************\n")
                    #print("\ncall za vplacilo podatki[0] = ",global_value.podatki_hitri[0])
                    print("\ncall global_value.negativni_hitri = ",global_value.negativni_hitri)
                    print(f"\npred IF so podatki_hitri[0] = {global_value.podatki_hitri[0]} in podatki_hitri[1] = {global_value.podatki_hitri[1]}")
                    if global_value.podatki_hitri[0] >0 :
                        vplacilo = global_value.negativni_hitri =0
                        print("PRIMERJAVA call POZ gv_negativni_hitri = ",gv_negativni_hitri)
                        print(f">>> CALL ce je POZITIVEN< trejd ga deli z {gv_negativni_hitri} in dobis = {global_value.balance/gv_negativni_hitri}")
                        #vplacilo = global_value.balance/gv_negativni_hitri
                        gv_negativni_hitri =9
                    elif global_value.podatki_hitri[0] <0 :
                        global_value.negativni_hitri += 1
                        vplacilo = global_value.negativni_hitri
                        print("povecevanje v call ",global_value.negativni_hitri)
                        
                        if gv_negativni_hitri >2:
                            gv_negativni_hitri -=1
                        #vplacilo = gv_negativni_hitri
                        print("PRIMERJAVA call NEG gv_negativni_hitri = ",gv_negativni_hitri)
                        print(f">>> CALL ce je negativen trejd ga deli z {gv_negativni_hitri} in dobis = {global_value.balance/gv_negativni_hitri}")
                        print(">>>> CALL ce je negativen trejd ga deli z 8 in dobis = ",global_value.balance/8)
                        #vplacilo = global_value.balance/gv_negativni_hitri
                    else :
                        vplacilo = global_value.negativni_hitri 
                        #vplacilo = global_value.balance/gv_negativni_hitri
                        """
                        """
                    print("call vplacilo za masanielo = ",vplacilo)
                    print("call masaniello_vloge = ",global_value.masaniello_vloge)
                    vplacilo = global_value.masaniello_vloge[vplacilo]
                    print("\ncall POTREBNO JE VPLACATI ",vplacilo)
                    vplacano = akcija(vplacilo, Aktivni_par, "call", 55)#1.2
                    print("call vplacano = ",vplacano)
                    api_check_win = api.check_win(vplacano[1])
                    print("\n call PREVERJANJE api.check_win = type = ",type(api_check_win))
                    print("\n call PREVERJANJE api.check_win = CEL IZPIS =  ",api_check_win)
                    global_value.podatki_hitri = api_check_win
                    print("\ncall podatki od preverjanja so = ",global_value.podatki_hitri)
                    
                    
                print( vsakih_10_sekund)
                povzeto[f"vsakih_10_sekund ({datetime.now().second})= "] = f"modra je obrnjena: {vsakih_10_sekund}"
                print(f"\n modra je obrnjena: {vsakih_10_sekund}")
            print(f"\nTESTIRAM ---->>> sekunde = {datetime.now().second}  <<<<------------ \n\n")
        
            
            
            
        if datetime.now().second > 57 and datetime.now().second < 59:
            print(f"\n\n*******************************************************\
                    \n *** ZADNJA SEKUNDA ({datetime.now().second}) ***\
                    \n*********************************************************\n\n")
            MA3 = moving_average(bars(Aktivni_par), 3)
            print(MA3)
            
            T3,D3,P3 = MA3[-3:]
            if osvezena_cena == P3:
                print("\nNEKAJ NI VREDU cena je se zmeraj enaka\n")
                print("***************************************************************************************************************<")
                print("***************************************************************************************************************<")
                print("***************************************************************************************************************\n\n")
                if not zgodovina_svec(Aktivni_par,60):
                    quit("IZHOD zgodovina_svec (quit())")
                print("\nNEKAJ NI VREDU cena je se zmeraj enaka\n")
                print("***************************************************************************************************************<")
                print("***************************************************************************************************************<")
                print("***************************************************************************************************************\n\n")
            if osvezena_cena != P3:
                osvezena_cena = P3
                print("\nCENA JE OSVEZENA\n")
                
            ma3_vrh = P3 < D3 and D3 > T3 and T3 > P3
            ma3_dno = P3 > D3 and D3 < T3 and T3 < P3
            #global_value.ma3_vrh_dno = "ne"
            #global_value.ma3_vrh_dno = 0
            if ma3_vrh:
                #global_value.ma3_vrh_dno = "put"
                global_value.ma3_vrh_dno = -1
            if ma3_dno:
                #global_value.ma3_vrh_dno = "call"
                global_value.ma3_vrh_dno = 1
                
            print(f"\n ******************* STARA MINUTA ***************\nGV.ma3_vrh_dno = {global_value.ma3_vrh_dno}\n\n")
            bar0 = ohlc(bars(Aktivni_par),0)
            print("CENA T3 = ",T3)
            print("CENA bar0[c] = ",bar0["c"])
            gv_cas = global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][0]
            gv_cas_utc = datetime.fromtimestamp(gv_cas,tz=timezone.utc)
            gv_cas = datetime.fromtimestamp(gv_cas)
            print(f"ZADNJA URA = {gv_cas} UTC = {gv_cas_utc}")
            print("ZADNJA CENA = ",global_value.zgodovina_3[Aktivni_par]["zgodovina"][-1][1])
            print(f"\n MED MA3 IN PRVO SVECO(close) je ODLOCITEV = {'KUPI' if T3 < bar0['c'] else 'PRODAJ'} \n")
            povzeto["\nSTARA MINUTA GV.ma3_vrh_dno = "] = f"GV.ma3_vrh_dno = {global_value.ma3_vrh_dno} ODLOCITEV: {'KUPI' if T3 < bar0['c'] else 'PRODAJ'} "
            print(f"\n ****** K O N E C ************* STARA MINUTA ***************\nGV.ma3_vrh_dno = {global_value.ma3_vrh_dno}\n\n")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            '''
        if datetime.now().second > 100 and datetime.now().second < 102:
        #if datetime.now().second > 1 and datetime.now().second < 3:
        #if datetime.now().second > 1 and datetime.now().second < 3:
        #if datetime.now().second > 4 and datetime.now().second < 6:
            #krog_obrat =1
            print("\n\n================================================================")
            print(f"\n\n KONEC KROGA WHILE \n\n NADALJENVANJE NOVEGA KROGA \n\n Aktivni par: {Aktivni_par}\n\n")
            print(f"::> Stanje racuna {global_value.balance} Vplacano: {rezultat_ma3[0]} Vplacan znesek: {vloga_ma3+0.1:.2f} \n\n")
            print(f"STEVILKA {krog_obrat} KROGA \n\n")
            print(f"STEVILKA SEJE: {global_value.seja}  \n\n")
            print("================================================================\n\n")
            
            povzeto["krog in seja = "] = f"{krog_obrat} || {global_value.seja} || {datetime.now()}"
            povzeto["bilanca vplacano in znesek = "] = f"{global_value.balance} || {rezultat_ma3} || {vloga_ma3+0.1:.2f}"
            
            print(":::v pripravi::: ce ni vplacano prekini proces!!! :::v pripravi:::\n")
            
            '''
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    """ KONCAN WHILE LOOP """
    kluci = list(minute.keys())
    
    print("minutni kluci:")
    print(kluci)
    
    """
    print("")
    test_dict = {"besedilo 1":"vsebina","b 2":22}
    
    test_dict["\nb 3"] = "dodatek"
    
    print(test_dict)
    with open("besedilo.txt","a") as f:
        for i in test_dict:
            f.write(f"{i} = {test_dict[i]}")
            print(f" {i}  = {test_dict[i]} ")
    
    
    print("\nIZPIS\n")
    with open("besedilo.txt") as r:
        print(r.read())
    """
    
    zapis["Masaniello = "]=[ms_pozitivnih, ms_trejdov, ms_procent, ms_vloga]
    zapis["Zakljuceno_ob_uri = "]= datetime.now()
    
    print("* open ", minute[kluci[-1]][0])
    print("M1 HIGH ", max(minute[kluci[-1]]))
    print("M1 LOW ", min(minute[kluci[-1]]))
    print("M1 CLOSE ", minute[kluci[-1]][-1])
    odprta = minute[zadnji_izdelan_kluc_minute][0]
    zaprta = minute[zadnji_izdelan_kluc_minute][-1]
    print("\nAktivni_par = ", Aktivni_par)
    zapis["Aktivni_par = "]=Aktivni_par
    print("podatki aktivnega para: ", global_value.pairs[Aktivni_par])
    zapis["\npodatki_aktivnega_para: "] = global_value.pairs[Aktivni_par]
    print("\nzadnja minutna >> sveca je ", "BULL" if odprta < zaprta else "BEAR")
    print("  KONCANO ")
    
    # racun_koncna_banka =0
    racun_koncna_banka = api.get_balance()
    # cas_isteka = 5
    # print("KONCANO krog= ",krogov," cas isteka svece= ",cas_isteka," sekund")
    print("Zakljuceno ob uri: ", datetime.now())
    print("KONCANO krog= ", krogov)
    zapis["KONCANO_krog: "] = krogov
    print("bilo je vseh trejdov= ", stetje_trejdov)
    print("pozitivni= ", pozitivni_trejdi)
    print("negativnih= ", stetje_trejdov - pozitivni_trejdi)
    try:
        print("razmerje= ", (stetje_trejdov - pozitivni_trejdi) / pozitivni_trejdi)
    except ZeroDivisionError as e:
        print("ne gre izracunat razmerja zaradi napake: ", e)
    except:
        print(" ne morem izracunati RAZMERJA!! (ZeroDivisionError: division by zero)")
    print("zaporedje trejdov= ", zaporedje_trejdov)
    zapis["zaporedje_trejdov= "]=zaporedje_trejdov
    # print("rezultati trejdov ",rezultati_trejdov)
    print("Uspesnost trejdov = ", uspesnost_trejdov)
    zapis["uspesnost_trejdov: "] = uspesnost_trejdov
    print("shranjen izbor = ", shranjen_izbor)
    zapis["shranjen_izbor: "] = shranjen_izbor
    print("polja = ", polje)
    print("preverjanje_izbora = ", preverjanje_izbora)
    zapis["preveerjanje_izbora "] = preverjanje_izbora
    print("MA IZBOR: ",ma_izbor)
    print("ma_skupna= ", ma_skupna)
    zapis["ma_skupna "] = ma_skupna
    print("ma_skupna pozitivna= ", ma_skupina_pozitivni)
    zapis["ma_skupna_pozitivni"] = ma_skupina_pozitivni
    print("ma_skupna negativna= ", ma_skkupina_negativni)
    zapis["ma_skupna_negativni "] = ma_skkupina_negativni
    print("!!>> kombinacija_izbor IZBOR: ",kombinacija_izbor)
    print("IZBRANA SMER: ",izbrana_smer)
    zapis["IZBRANA_SMER: "]=izbrana_smer
    print("izbor tri je: ",izbor_tri)
    zapis["izbor tri je: "] = izbor_tri
    print("aktivni_bar je: ",aktivni_bar)
    zapis["aktivni_bar je: "] =aktivni_bar
    print("prejsni_bar je: ",prejsni_bar)
    zapis["prejsni_bar je: "] =prejsni_bar
    print("TEST:: zapis[prejsni_bar je: ] => ",zapis["prejsni_bar je: "])
    print("aktivne vloge: ",mas_vloga)
    zapis["aktivne_vloge: "] = mas_vloga
    
    
    
    print(f"Banka zacetek: {zacetna_banka} ")  # banka konec: {koncna_banka} ")
    print(f"Znesek banke = {Mmm.mbanka:0.2f}")
    print(f"Rezultat razlika: {(Mmm.mbanka - zacetna_banka):0.2f}")
    
    print(f"> racun_zacetna_banka = {racun_zacetna_banka}")
    print(f"> PROFIT = {(racun_koncna_banka - racun_zacetna_banka):0.2f} ")
    print(f"> racun_koncna_banka = {racun_koncna_banka} ")
    zapis["racun_zacetna_banka ="]=f"{racun_zacetna_banka}"
    zapis["PROFIT ="]=f"{(racun_koncna_banka - racun_zacetna_banka):0.2f}"
    zapis["racun_koncna_banka ="]=f"{racun_koncna_banka:0.2f}"
    konec = time.perf_counter()
    # print("start = ",start)
    # print("konec = ",konec)
    print("trajanje skupaj: sekun=  ", int(konec - start))
    print("trajanje skupaj:   ", (int(konec - start)) / 60)
    zapis["trajanje_skupaj ="]=(int(konec - start)) / 60
    
    with open("spremljanje.txt","a") as f:
        for i in zapis:
            f.write(f"\n{i}  {zapis[i]}")
            print(f"> {i}  {zapis[i]} ")
        f.write(f"\n***\n")
    
    
    return racun_koncna_banka - racun_zacetna_banka
    
    
#to_je_za_prenos_za_modul = f"\nkoncano mmbanka = {(Mmm.mbanka - zacetna_banka):0.2f} PROFIT = {(racun_koncna_banka - racun_zacetna_banka):0.2f} NOVO STANJE = {racun_koncna_banka} "

"""  WILE DELA TRENUTNO PREVERJAM SE ZMERAJ NAPAKE ZATO RABIM SAMO POSAMEZNO SEJO """
koncan_krog = "\nkoncano ___________ !!! ZACNEM !!! Z WHILE 10X____________\n"

krogov = 0
rezultat = 0
while krogov < 5:
    #if mas.koncan_krog == "koncano":
    #print("\nzakljucen krog ")
    #print("\nrezultat = ",rezultat)
    if krogov == 0:
        print("\n\n============================ KLICEM masaniello() ================== SPODAJ ============\n\n")
    else:
        print(f"\n\n({krogov})======================= PONOVNO KLICEM masaniello() ========= SPODAJ ================\n\n")
    #mas.koncan_krog=""
    rezultat = masaniello()
    print("\nzakljucen krog ")
    print("\nWHILE rezultat = ",rezultat)
    print("while krogov = ",krogov)
    
    zapis["while_krogov = "]= krogov
    with open("spremljanje.txt","a") as f:
        f.write(f"\nWHILE krogov = {krogov}")
        f.write(f"\n=========================\n")
    
    krogov +=1
    
    
print("\nKONCANO while krogov = ",krogov)
    
"""
print("\n\n=======================  KLICEM masaniello() =========================\n\n")
rezultat = masaniello()
print("\nrezultat: ",rezultat)

"""


print("\n\n=======================  !!! KONCNI IZPIS !!! =========================\n\n")
for i in zapis:
    print(f"{i} = {zapis[i]}")
    


"""
with open("spremljanje.txt","a") as f:
    for i in zapis:
        f.write(f"\n{i}  {zapis[i]}")
        print(f"> {i}  {zapis[i]} ")
    f.write(f"\n")
"""
print("\nIZPIS datoteke spremljanje.txt\n")
with open("spremljanje.txt") as r:
    print(r.read())
