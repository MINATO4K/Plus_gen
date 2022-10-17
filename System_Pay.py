import os

cor1 = "\033[1;31m"
cor2 = "\033[1;32m"
cor3 = "\033[1;33m"
cor4 = "\033[1;34m"
cor5 = "\033[1;35m"
cor6 = "\033[1;36m"
cor7 = "\033[1;37m"
fch = "\033[m"

op1 = f"{cor2}[{cor1}1{fch}{cor2}]{cor6}"
op2 = f"{cor2}[{cor1}2{fch}{cor2}]{cor6}"
op3 = f"{cor2}[{cor1}3{fch}{cor2}]{cor6}"
op4 = f"{cor2}[{cor1}4{fch}{cor2}]{cor6}"
op5 = f"{cor2}[{cor1}5{fch}{cor2}]{cor6}"
op6 = f"{cor2}[{cor1}6{fch}{cor2}]{cor6}"
op7 = f"{cor2}[{cor1}7{fch}{cor2}]{cor6}"
op8 = f"{cor2}[{cor1}8{fch}{cor2}]{cor6}"
op9 = f"{cor2}[{cor1}9{fch}{cor2}]{cor6}"
os.system("clear")
print(f""" 
{cor5}        ℙ𝔸𝕐 𝕊𝕐𝕊𝕋𝔼𝕄{fch}

{op1}~~> {cor3}Gerar Arquivo conecta4G 

{op2}~~> {cor3}Gerar Payload 

{op3}~~> {cor3}Sair
""")
menu = input(f">>> {cor2}")

if int(menu) == 1:
  os.system("clear")
  print("endesenvolvimento")
elif int(menu) == 2:
  os.system("clear")
  print(f"""
{op1}~~> {cor3}Direct

{op2}~~> {cor3}Ssl + Pay

{op3}~~> {cor3}Custom 
  """)
  menu_pay = int(input(f">>> {cor2}"))
  if menu_pay == 1:
    domínio = input(f"{cor3}Domínio 🌐 >>> {cor2}")
    gg = f"GET  [protocol][crlf]Host:{domínio} [crlf]Connection: Keep-Alive[crlf]Upgrade: websocket[crlf][crlf]"
    l = f"{cor4}×"*40
    print(f"{l}")
    ip = input(f"{cor3}IP OU SNI 🌐 >>> {cor2}")
    os.system("clear")
    print(f"""
{cor4}{l}
{cor6}{gg}
{cor4}{l}
{cor2}IP:{cor6}{ip}{cor2}|Porta:{cor1}80{fch}{cor2}|UDP padrão:{cor1}7300
{l}
{cor6}DNS GOOGLE 
{cor2}Primário ~~> {cor3} 8.8.8.8
{cor2}Secundário ~~> {cor3} 8.8.4.4
{l}
{cor6}DNS CLOUDFLARE
{cor2}Primário ~~> {cor3} 1.1.1.1
{cor2}Secundário ~~> {cor3} 1.0.0.1
{cor6}DNS CUSTOM
{cor2}Primário ~~> {cor3} 8.8.4.4
{cor2}Secundário ~~> {cor3} 1.0.0.1
    """)