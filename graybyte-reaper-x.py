import subprocess
import os
import time
import shutil
from colorama import init, Fore, Style
from datetime import datetime
import sys

try:
    init()
except:
    print(f"{Fore.RED}[!!] cOlOrAmA MoDuLe nOt fOuNd [!!]\n{Style.RESET_ALL}")

ascii_art = (
    f"\n\n{Fore.RED}░█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}─█▀▀█ {Fore.GREEN}░█──░█ 　 {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}░█▀▀▀ {Fore.RED}─█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}── {Fore.RED}▀▄░▄▀{Style.RESET_ALL}\n"
    f"{Fore.RED}░█─▄▄ {Fore.GREEN}░█▄▄▀ {Fore.YELLOW}░█▄▄█ {Fore.GREEN}░█▄▄▄█ 　 {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}░█▀▀▀ {Fore.RED}░█▄▄█ {Fore.GREEN}░█▄▄█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}▀▀ {Fore.RED}─░█──{Style.RESET_ALL}\n"
    f"{Fore.RED}░█▄▄█ {Fore.GREEN}░█─░█ {Fore.YELLOW}░█─░█ {Fore.GREEN}──░█── 　 {Fore.MAGENTA}░█─░█ {Fore.CYAN}░█▄▄▄ {Fore.RED}░█─░█ {Fore.GREEN}░█─── {Fore.YELLOW}░█▄▄▄ {Fore.MAGENTA}░█─░█ {Fore.CYAN}── {Fore.RED}▄▀░▀▄{Style.RESET_ALL}\n\n"
    f"{Fore.GREEN}[!!] INPUT/OUTPUT DIRECTORIES ARE AUTOMATICALLY SET [!!]\n\n"
    f"INPUT: {Fore.GREEN}{{}}/parts\n"
    f"OUTPUT: {Fore.GREEN}{{}}/executed\n\n"
    f"--------------------------------------------------------------------------------{Style.RESET_ALL}"
).format(os.getcwd(), os.getcwd())
print(ascii_art)

log_ascii_art = (
    "█▀█ █▀▀ ▄▀█ █▀█ █▀▀ █▀█ ▄▄ ▀▄▀   █░░ █▀█ █▀▀ █▀\n"
    "█▀▄ ██▄ █▀█ █▀▀ ██▄ █▀▄ ░░ █░█   █▄▄ █▄█ █▄█ ▄█\n\n"
    "gRaYbYtE cHaOsLoGgEr-dEtAiLeD lOgS\n"
    "mY LiFe iS A LiE AnD IM LiViNg iN ThIs oNlY TrUtH -gRaYbYtE\n"
    "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
    "fOr mOrE InFoRmAtIoN AnD HeLp\n\n"
    "TeLeGrAm : https://t.me/rex_cc\n"
    "fAcEbOoK : https://www.facebook.com/graybyt3\n"
    "iNsTaGrAm : https://www.instagram.com/gray_byte\n"
    "X : https://x.com/gray_byte\n"
    "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
)

##**************************************************************************
# SeT ThE DiReCtOrY Or pAtHs hErE In tHiS FoRmAt                          *
#                                                                         *
# LiNuX "/home/username/Desktop/parent-dir/graybyte-reaper-x/attack/"     *
# WiNdOwS: "C:\\Users\\Administrator\\Desktop\\graybyte-reaper-x\\attack" *
#                                                                         *
#**************************************************************************

working_directory = os.getcwd()
input_directory = os.path.join(working_directory, "parts")
output_directory = os.path.join(working_directory, "executed")

log_directory = "ChaosLogger"

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

def log_error(error_msg):
    error_file_path = os.path.join(log_directory, 'byte-error-log.txt')
    timestamp = datetime.now().strftime('%d-%B-%Y | %I:%M:%S %p')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    plain_error_msg = error_msg.replace(f"{Fore.RED}", "").replace(f"{Style.RESET_ALL}", "")
    entry = (
        f"\n{plain_error_msg}\n"
        f"eNcOuNtReD On : {timestamp}\n"
        f"-----------------------------------------------------------------------------------------------------------------------------------------------\n\n"
    )
    if not os.path.exists(error_file_path):
        with open(error_file_path, 'w', encoding='utf-8') as error_file:
            error_file.write(log_ascii_art)
    with open(error_file_path, 'a', encoding='utf-8') as error_file:
        error_file.write(entry)

if not os.path.exists(input_directory):
    error_msg = f"{Fore.RED}[!!] iNpUt dIrEcToRy nOt fOuNd: {input_directory} [!!]\n{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input("pReSs eNtEr tO CoNtInUe oR CtRl+c tO ExIt...")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

input_files = [file for file in os.listdir(input_directory) if file.endswith(".txt")]

if not input_files:
    error_msg = f"{Fore.RED}[!!] No fIlEs fOuNd iN {input_directory} [!!]\n{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input(f"{Fore.RED}pReSs eNtEr tO CoNtInUe oR CtRl+c tO ExIt......{Style.RESET_ALL}")

if not os.path.exists("x.py"):
    error_msg = f"{Fore.RED}[!!] x.py pReSs eNtEr tO CoNtInUe oR CtRl+c tO ExIt...... [!!]{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input(f"{Fore.RED}pReSs eNtEr ExIt......{Style.RESET_ALL}")
    sys.exit(1)

for input_file in input_files:
    start_time = time.time()
    start_datetime = datetime.now()
    
    input_file_path = os.path.join(input_directory, input_file)
    
    try:
        with open(input_file_path, 'r') as f:
            url_count = sum(1 for line in f if line.strip())
        print(f"{Fore.YELLOW}### Processing File: {input_file_path}{' ' * (75 - len(input_file_path))}###{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Loaded Successfully: {input_file}{' ' * (50 - len(input_file))}[+]{Style.RESET_ALL}\n")
        print(f"{Fore.GREEN}[+] Total URLs:        {url_count}{Style.RESET_ALL}\n\n")
    except FileNotFoundError:
        error_msg = f"{Fore.RED}[!!] FiLe nOt fOuNd: {input_file_path} [!!]{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        continue
    
    checking_file_path = os.path.join(log_directory, 'byte-stream.txt')
    if not os.path.exists(checking_file_path):
        with open(checking_file_path, 'w', encoding='utf-8') as ww:
            ww.write(log_ascii_art)
    with open(checking_file_path, 'a', encoding='utf-8') as ww:
        ww.write(f"\nFiLeNaMe: {input_file}\n")
        ww.write(f"FiLe tAkEn fOr eXeCuTiOn : {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        ww.write("-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    
    try:
        #*********************************************
        # CHaNgE ThE x.py tO YoUr fIlE NaMe hErE     #
        #*********************************************

        process = subprocess.Popen([sys.executable, "x.py"], stdin=subprocess.PIPE, text=True)
        process.communicate(input=input_file_path)

    except Exception as e:
        error_msg = f"{Fore.RED}[!!] fAiLeD To eXeCuTe x.py FoR {input_file}\n[!!] cHeCk eNvIrOnMeNt vAlIdAtIoN\n[-] PrOcEsSiNg sToPpEd............\n{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        break
    
    output_file_path = os.path.join(output_directory, input_file)
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    shutil.move(input_file_path, output_directory)
    
    end_time = time.time()
    end_datetime = datetime.now()
    time_taken = end_time - start_time
    
    print(f"START: {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}")
    print(f"END: {end_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}")
    print(f"TIME TAKEN: {time_taken:.2f} SECONDS | URLS CHECKED: {url_count}")
    print(f"\n{Fore.GREEN}## MOVED {input_file} TO {output_directory} ##{Style.RESET_ALL}\n")
    print("--------------------------------------------------------------------------------")
    
    checked_file_path = os.path.join(log_directory, 'byte-archive.txt')
    if not os.path.exists(checked_file_path):
        with open(checked_file_path, 'w', encoding='utf-8') as check_file:
            check_file.write(log_ascii_art)
    with open(checked_file_path, 'a', encoding='utf-8') as check_file:
        check_file.write(f"\nFiLeNaMe: {input_file}\n")
        check_file.write(f"sTaRt: {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        check_file.write(f"eNd: {end_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        check_file.write(f"tImE TaKeN: {time_taken:.2f} sEcOnDs | uRlS ChEcKeD: {url_count}\n")
        check_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    
    time.sleep(1)
