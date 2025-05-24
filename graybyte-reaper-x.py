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
    pass

ascii_art = (
    f"\n\n\n\n{Fore.CYAN}░█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}─█▀▀█ {Fore.GREEN}░█──░█ 　 {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}░█▀▀▀ {Fore.CYAN}─█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}── {Fore.CYAN}▀▄░▄▀{Style.RESET_ALL}\n"
    f"{Fore.CYAN}░█─▄▄ {Fore.GREEN}░█▄▄▀ {Fore.YELLOW}░█▄▄█ {Fore.GREEN}░█▄▄▄█ 　 {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}░█▀▀▀ {Fore.CYAN}░█▄▄█ {Fore.GREEN}░█▄▄█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}▀▀ {Fore.CYAN}─░█──{Style.RESET_ALL}\n"
    f"{Fore.CYAN}░█▄▄█ {Fore.GREEN}░█─░█ {Fore.YELLOW}░█─░█ {Fore.GREEN}──░█── 　 {Fore.MAGENTA}░█─░█ {Fore.CYAN}░█▄▄▄ {Fore.CYAN}░█─░█ {Fore.GREEN}░█─── {Fore.YELLOW}░█▄▄▄ {Fore.MAGENTA}░█─░█ {Fore.CYAN}── {Fore.CYAN}▄▀░▀▄{Style.RESET_ALL}\n\n\n\n"
    f"{Fore.GREEN}[!!] INPUT/OUTPUT DIRECTORIES ARE AUTOMATICALLY SET [!!]\n\n{Style.RESET_ALL}"
    f"{Fore.CYAN}INPUT: {Fore.GREEN}<script_directory>/parts\n"
    f"{Fore.CYAN}OUTPUT: {Fore.GREEN}<script_directory>/executed\n\n{Style.RESET_ALL}"
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

working_directory = os.getcwd()
input_directory = os.path.join(working_directory, "parts")
output_directory = os.path.join(working_directory, "executed")

log_directory = "ChaosLogger"

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

def log_error(error_msg):
    error_file_path = os.path.join(log_directory, 'byte-error-log.txt')
    timestamp = datetime.now().strftime('%d-%B-%Y | %I:%M:%S %p')
    plain_error_msg = error_msg.replace(f"{Fore.CYAN}", "").replace(f"{Fore.RED}", "").replace(f"{Fore.YELLOW}", "").replace(f"{Fore.GREEN}", "").replace(f"{Style.RESET_ALL}", "").replace(f"{Style.BRIGHT}", "")
    entry = (
        f"\n{plain_error_msg}\n"
        f"ENCOUNTERED ON: {timestamp}\n"
        f"-----------------------------------------------------------------------------------------------------------------------------------------------\n\n"
    )
    if not os.path.exists(error_file_path):
        with open(error_file_path, 'w', encoding='utf-8') as error_file:
            error_file.write(log_ascii_art)
    with open(error_file_path, 'a', encoding='utf-8') as error_file:
        error_file.write(entry)

sys.stderr = open(os.devnull, 'w')

if not os.path.exists(input_directory):
    os.makedirs(input_directory)
    log_error("INPUT DIRECTORY NOT FOUND, CREATED: " + input_directory)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"\n{Fore.GREEN}[+] Output Directory Created: {output_directory.ljust(50)} [+]{Style.RESET_ALL}\n")

input_files = [file for file in os.listdir(input_directory) if file.endswith(".txt")]

if not input_files:
    log_error("NO .TXT FILES FOUND IN " + input_directory)
    sys.exit(1)

if not os.path.exists("x.py"):
    log_error("X.PY NOT FOUND")
    sys.exit(1)

for input_file in input_files:
    start_time = time.time()
    start_datetime = datetime.now()
    
    print(f"\n{Fore.CYAN}### Processing File: {input_file.ljust(50)} ###{Style.RESET_ALL}")
    time.sleep(0.5)
    
    input_file_path = os.path.join(input_directory, input_file)
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            url_count = sum(1 for line in f if line.strip())
        print(f"{Fore.GREEN}[+] Loaded Successfully: {input_file.ljust(50)} [+]{Style.RESET_ALL}\n")
        print(f"{Fore.GREEN}[+] Total URLs: {str(url_count).rjust(10)} {Style.RESET_ALL}\n")
    except FileNotFoundError:
        log_error("FILE NOT FOUND: " + input_file_path)
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
        process = subprocess.Popen(
            [sys.executable, "x.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_file_path)
        if stdout or stderr:
            log_error(f"X.PY OUTPUT FOR {input_file}:\nSTDOUT: {stdout}\nSTDERR: {stderr}")
    except Exception as e:
        log_error(f"FAILED TO EXECUTE X.PY FOR {input_file}: {str(e)}")
        continue
    
    time.sleep(0.5)
    
    output_file_path = os.path.join(output_directory, input_file)
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    shutil.move(input_file_path, output_directory)
    
    end_time = time.time()
    end_datetime = datetime.now()
    time_taken = end_time - start_time
    
    print(f"\nSTART: {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}")
    print(f"END: {end_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}")
    print(f"TIME TAKEN: {time_taken:.2f} SECONDS | URLS CHECKED: {url_count}\n")
    print(f"{Fore.CYAN}## EXECUTION OF {input_file} DONE ##{Style.RESET_ALL}\n")
    
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
