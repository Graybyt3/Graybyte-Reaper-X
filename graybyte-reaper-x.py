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
    print(f"{Fore.CYAN}[!!] COLORAMA MODULE NOT FOUND [!!]\n{Style.RESET_ALL}")

ascii_art = (
    f"\n\n\n\n{Fore.CYAN}░█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}─█▀▀█ {Fore.GREEN}░█──░█ 　 {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}░█▀▀▀ {Fore.CYAN}─█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}── {Fore.CYAN}▀▄░▄▀{Style.RESET_ALL}\n"
    f"{Fore.CYAN}░█─▄▄ {Fore.GREEN}░█▄▄▀ {Fore.YELLOW}░█▄▄█ {Fore.GREEN}░█▄▄▄█ 　 {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}░█▀▀▀ {Fore.CYAN}░█▄▄█ {Fore.GREEN}░█▄▄█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}▀▀ {Fore.CYAN}─░█──{Style.RESET_ALL}\n"
    f"{Fore.CYAN}░█▄▄█ {Fore.GREEN}░█─░█ {Fore.YELLOW}░█─░█ {Fore.GREEN}──░█── 　 {Fore.MAGENTA}░█─░█ {Fore.CYAN}░█▄▄▄ {Fore.CYAN}░█─░█ {Fore.GREEN}░█─── {Fore.YELLOW}░█▄▄▄ {Fore.MAGENTA}░█─░█ {Fore.CYAN}── {Fore.CYAN}▄▀░▀▄{Style.RESET_ALL}\n\n\n\n"
    f"{Fore.GREEN}[!!] INPUT/OUTPUT DIRECTORIES PATH SHOULD BE IN THIS FORMAT[!!]\n\n{Style.RESET_ALL}"
    f"{Fore.CYAN}WINDOWS: {Fore.GREEN}\"C:\\\\USERS\\\\ADMINISTRATOR\\\\DESKTOP\\\\XX\\\\PARTS\" (USE DOUBLE BACKSLASHES)\n"
    f"{Fore.CYAN}LINUX: {Fore.GREEN} \"/HOME/YOURUSERNAME/DESKTOP/XX/PARTS\" (SINGLE FORWARD SLASHES)\n{Style.RESET_ALL}"
    f"{Fore.CYAN}MACOS: FUCK MACOS USERS, GOTO HELL YOU RICH FUCKING BASTARD PAPPUS\n\n{Style.RESET_ALL}"
)
print(ascii_art)

log_ascii_art = (
    "█▀█ █▀▀ ▄▀█ █▀█ █▀▀ █▀█ ▄▄ ▀▄▀   █░░ █▀█ █▀▀ █▀\n"
    "█▀▄ ██▄ █▀█ █▀▀ ██▄ █▀▄ ░░ █░█   █▄▄ █▄█ █▄█ ▄█\n\n"
    "GRAYBYTE CHAOSLOGGER-DETAILED LOGS\n"
    "MY LIFE IS A LIE AND IM LIVING IN THIS ONLY TRUTH -GRAYBYTE\n"
    "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
    "FOR MORE INFORMATION AND HELP\n\n"
    "TELEGRAM: https://t.me/rex_cc\n"
    "FACEBOOK: https://www.facebook.com/graybyt3\n"
    "INSTRAGRAM: https://www.instagram.com/gray_byte\n"
    "X: https://x.com/gray_byte\n"
    "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
)

##**************************************************************************
# SET THE DIRECTORY OR PATHS HERE IN THIS FORMAT                          *
#                                                                         *
# LINUX "/HOME/USERNAME/DESKTOP/PARENT-DIR/GRAYBYTE-REAPER-X/ATTACK/"     *
# WINDOWS: "C:\\USERS\\ADMINISTRATOR\\DESKTOP\\GRAYBYTE-REAPER-X\\ATTACK" *
#                                                                         *
#**************************************************************************

input_directory = "C:\\Users\\Administrator\\Desktop\\test\\files"
output_directory = "C:\\Users\\Administrator\\Desktop\\test\\executed"

log_directory = "ChaosLogger"

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

def log_error(error_msg):
    error_file_path = os.path.join(log_directory, 'byte-error-log.txt')
    timestamp = datetime.now().strftime('%d-%B-%Y | %I:%M:%S %p')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    plain_error_msg = error_msg.replace(f"{Fore.CYAN}", "").replace(f"{Style.RESET_ALL}", "")
    entry = (
        f"\n{plain_error_msg}\n"
        f"ENCOUNTECYAN ON: {timestamp}\n"
        f"-----------------------------------------------------------------------------------------------------------------------------------------------\n\n"
    )
    if not os.path.exists(error_file_path):
        with open(error_file_path, 'w', encoding='utf-8') as error_file:
            error_file.write(log_ascii_art)
    with open(error_file_path, 'a', encoding='utf-8') as error_file:
        error_file.write(entry)

if not os.path.exists(input_directory):
    error_msg = f"{Fore.CYAN}[!!] INPUT DIRECTORY NOT FOUND: {input_directory} [!!]\n{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input("PRESS ENTER TO CONTINUE OR CTRL+C TO EXIT...")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"{Fore.GREEN}[+] CREATING OUTPUT DIRECTORY ............\nCREATED: {output_directory}\n{Style.RESET_ALL}")

input_files = [file for file in os.listdir(input_directory) if file.endswith(".txt")]

if not input_files:
    error_msg = f"{Fore.CYAN}[!!] NO FILES FOUND IN {input_directory} [!!]\n{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input(f"{Fore.CYAN}PRESS ENTER TO CONTINUE OR CTRL+C TO EXIT......{Style.RESET_ALL}")

if not os.path.exists("x.py"):
    error_msg = f"{Fore.CYAN}[!!] X.PY PRESS ENTER TO CONTINUE OR CTRL+C TO EXIT...... [!!]{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input(f"{Fore.CYAN}PRESS ENTER EXIT......{Style.RESET_ALL}")
    sys.exit(1)

for input_file in input_files:
    start_time = time.time()
    start_datetime = datetime.now()
    
    time.sleep(0.5)
    print(f"{Fore.GREEN}[+] LOADING FILE ............ {input_file}{Style.RESET_ALL}")
    input_file_path = os.path.join(input_directory, input_file)
    time.sleep(0.5)
    
    try:
        with open(input_file_path, 'r') as f:
            url_count = sum(1 for line in f if line.strip())
        print(f"{Fore.GREEN}[+] LOADED SUCCESSFULLY, RUNNING WITH: {input_file}:\n[+] TOTAL URL LOADED: {url_count}{Style.RESET_ALL}")
    except FileNotFoundError:
        error_msg = f"{Fore.CYAN}[!!] FILE NOT FOUND: {input_file_path} [!!]{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        continue
    
    checking_file_path = os.path.join(log_directory, 'byte-stream.txt')
    if not os.path.exists(checking_file_path):
        with open(checking_file_path, 'w', encoding='utf-8') as ww:
            ww.write(log_ascii_art)
    with open(checking_file_path, 'a', encoding='utf-8') as ww:
        ww.write(f"\nFILENAME: {input_file}\n")
        ww.write(f"FILE TAKEN FOR EXECUTION: {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        ww.write("-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    
    try:
        #*********************************************
        # CHANGE THE X.PY TO YOUR FILE NAME HERE     #
        #*********************************************

        process = subprocess.Popen([sys.executable, "x.py"], stdin=subprocess.PIPE, text=True)
        process.communicate(input=input_file_path)

    except Exception as e:
        error_msg = f"{Fore.CYAN}[!!] FAILED TO EXECUTE X.PY FOR {input_file}\n[!!] CHECK ENVIRONMENT VALIDATION\n[-] PROCESSING STOPPED............\n{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        break
    
    time.sleep(0.5)
    
    output_file_path = os.path.join(output_directory, input_file)
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    shutil.move(input_file_path, output_directory)
    print(f"{Fore.GREEN}\nMOVING EXECUTED URL LIST - {input_file}\nMOVED TO: {output_directory}\n{Style.RESET_ALL}")
    
    end_time = time.time()
    end_datetime = datetime.now()
    time_taken = end_time - start_time
    
    checked_file_path = os.path.join(log_directory, 'byte-archive.txt')
    if not os.path.exists(checked_file_path):
        with open(checked_file_path, 'w', encoding='utf-8') as check_file:
            check_file.write(log_ascii_art)
    with open(checked_file_path, 'a', encoding='utf-8') as check_file:
        check_file.write(f"FILENAME: {input_file}\n")
        check_file.write(f"START: {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        check_file.write(f"END: {end_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        check_file.write(f"TIME TAKEN: {time_taken:.2f} SECONDS | URLS CHECKED: {url_count}\n")
        check_file.write("-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    
    time.sleep(0.5)
