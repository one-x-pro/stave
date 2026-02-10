from datetime import datetime
import os
import json

rp = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + '/../')
dp = os.path.join(rp, 'history')
if not os.path.exists(dp):
    os.makedirs(dp)
    print("\nDATOTEKA JE IZDELANA ((dp) = ",dp,")")

# Global variables
websocket_is_connected = False
# try fix ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2361)
ssl_Mutual_exclusion = False  # mutex read write
# if false websocket can sent self.websocket.send(data)
# else can not sent self.websocket.send(data)
ssl_Mutual_exclusion_write = False  # if thread write

SSID = None
DEMO = None

check_websocket_if_error = False
websocket_error_reason = None

napake = None
"""
(except Exception) preverjam!!
 in ws > ZACETEK SPOROCILA(prvih 150 znakov):  <websockets.asyncio.client.ClientConnection object at 0x7530872d80b0>  (konec ws (150 znakov))

2025-11-04 11:09:53.208955 :[INFO]: vrstica 95 *WRNING* Error occurred: sent 1011 (internal error) keepalive ping timeout; no close frame received
Exception:: POSILJAM SPOROCILO:  b'[["AEDCNY_otc",1762256068.092,1.87143]]'
poglej >> 97 client.py Exception Sporocilo: Neka notranja napaka!!!
Zakljucil bom povezavo in jo na novo vspostavil!! 

HUDA NAPAKA!! error =  sent 1011 (internal error) keepalive ping timeout; no close frame received
2025-11-04 11:09:53.209203 :[ERROR]: Quitter.__call__() takes from 1 to 2 positional arguments but 3 were given
2025-11-04 11:09:53.209232 :[INFO]: 583 on_error:: [ERROR] imam info = Quitter.__call__() takes from 1 to 2 positional arguments but 3 were given

    exit("\n(exit) USTAVLJAM IZVAJANJE PROGRAMA KER JE PRISLO DO NAPAKE ",error)
TypeError: Quitter.__call__() takes from 1 to 2 positional arguments but 3 were given
"""

obe_bear = False
obe_bull = False
tri_bear = False
tri_bull = False

aktivni_par = None
balance_id = 0
balance_pred_vplacilom = 0
balance_po_vplacilu = 0
balance = None
balance_type = None
balance_updated = None
result = None
napaka = None
order_data = {}
order_open = []
order_closed = []
closed_deals = []
open_orders = []
closed_orders = []
trejd_je_odprt =  False
# successcloseOrder
failopenOrder = []
napaka =[]
trades = {}
stat = []
pairs = {}
assets = []
zgodovina = {}
zgodovina_2 = []
zgodovina_3 = {}
minute = {}
svecke = []
vloga = []
data = []

successdrawing = {}

masaniello_vloge =[]
laubuchere_vloge = []

""" OSCAR GRIND"""
oscar_zakljuceno = True
oscar_negativno = False
oscar_pozitivno = False
oscar_procent = 0 #0.02 # 0.02 == 2%
oscar_vloga = 0 # = banka * procent # unit
oscar_osnovna_vloga = 0 # oscar_vloga
oscar_vplacilo = 0
oscar_banka = 0
oscar_profit = 0 # oscar_banka + oscar_osnovna_vloga
oscar_profit_dosezen = False
oscar_skupaj_vplacano = 0
oscar_skupaj_potrebno_vplacati = 0
oscar_aktivni_trejd = []

stiri_bari_data = {}
stiri_bari_history = {}
stiri_bari_candles = {}

trejd = 0
izzid_trejda = None
updateStream  = None
krog=0
seja =0
seja_stara = None
zadnja_smer_trejda = None
aktivni_fraktal = "ne"
aktivni_fraktal_hiter = "ne"

dolzina_kljucev = 0

trikotnik_akcija = None
trikotnik_akcija_m5 = None
ma2_ma7_smer = None
sredina_cen = None

# logika
smer_ma10_ma1 = "ne"
trejd_napoved = "ne"
prehod_ma10_ma7_12 = "ne"
prehod_ma10_ma7_23 = "ne"
fraktal_cena_call = -1
fraktal_cena_put = -1
fraktal_cena = -1
fraktal_dict = {"cena":-1,"call":-1,"put":-1}

prehod_pristop = "ne"
prehod_pristop_kombo = "ne"
prehod_pristop_kombo_hiter = "ne"
prehod_pristop_trikotnik = "ne"
ma3_vrh_dno = 0
kombi_ma = 0

odprti_trejd = ""
bar_pogoj = 0

podatki_hitri =[0,0]
negativni_hitri =0


loglevel = 'INFO'

# To get the payment details for the different pairs
PayoutData = None

def zapis_rezultata(zapis):
    with open("info_log.txt","a") as f:
        f.write(f"\n{zapis}")
            #print(f"> {i}  {zapis[i]} ")
        #f.write(f"\n*** {datetime.now()} ***\n")

def logger(message, lvl):
    if loglevel == 'DEBUG':
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print('%s :[DEBUG]: %s' %(str(dt), str(message)))
    elif loglevel == lvl:
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print('%s :[%s]: %s' %(str(dt), str(lvl), str(message)))
        zapis_rezultata(f"{dt}: {lvl}: {message}")
    elif lvl == 'ERROR':
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print('%s :[ERROR]: %s' %(str(dt), str(message)))
    return


def set_cache(key, value, path=None):
    #data={"timestamp": int(time.time()), "value": value}
    print("\n60 global_value.py KLICEM SET_CACHE ZA ZAPIS PARA ki je key = ",key)
    data={"value": value}
    #print("data = ",data)
    print("data[value] = len = ",len(data["value"]))
    #print("data[value] = ",data["value"])
    
    print("\n62 global_value.py DATA delni izpis  =  str(data[value])[:50] = ",str(data["value"])[:50])
    #print("\n62 global_value.py DATA delni izpis  =  str(data[value]) = ",str(data["value"]))
    file = os.path.join(rp, str(key))
    if os.path.exists(file+".json"):
        os.remove(file+".json")
    with open(file+".json", "w") as k:
        json.dump(data, k, indent=4)
    


def check_cache(key, path=None):
    print("check_cache key= ",key," path= ",path)
    try:
        if path: file = os.path.join(dp, path, str(key))
        else: file = os.path.join(rp, str(key))
        print("datoteka je = ",file)
        if os.path.exists(file+".json"):
            return True
        """
        else:
            print("\nIZDELAJ DATOTEKO ",file,".json")
            print("in vpisi podatke")
        
            """
        return False
    except:
        return None


def get_cache(key, path=None):
    try:
        if path: file = os.path.join(dp, path, str(key))
        else: file = os.path.join(rp, str(key))
        with open(file+".json") as k:
            r = json.load(k)
        value = r.get('value')
        print("\nglobal_value:: get_cache > file = ",file)
        return value
    except:
        return None

