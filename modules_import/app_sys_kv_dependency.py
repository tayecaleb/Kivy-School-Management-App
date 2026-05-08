from .KV_Files.Main_KV import Main_KV
from .KV_Files.Home_Screen_KV import Home_Screen


KV_Routes = [
    Main_KV,
    Home_Screen
]

kv_holder = ''' '''

for routes in KV_Routes:
    kv_holder += routes

kv = kv_holder



