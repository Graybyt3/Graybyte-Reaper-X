import subprocess
import os
import time
from colorama import init, Fore, Style
from datetime import datetime
import sys

try:
    init()
except:
    print(f"{Fore.RED}[!!] COLORAMA MODULE NOT FOUND [!!]\n{Style.RESET_ALL}")

ascii_art = (
    f"\n\n\n{Fore.RED}░█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}─█▀▀█ {Fore.GREEN}░█──░█ 　 {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}░█▀▀▀ {Fore.RED}─█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}── {Fore.RED}▀▄░▄▀{Style.RESET_ALL}\n"
    f"{Fore.RED}░█─▄▄ {Fore.GREEN}░█▄▄▀ {Fore.YELLOW}░█▄▄█ {Fore.GREEN}░█▄▄▄█ 　 {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}░█▀▀▀ {Fore.RED}░█▄▄█ {Fore.GREEN}░█▄▄█ {Fore.YELLOW}░█▀▀▀ {Fore.MAGENTA}░█▄▄▀ {Fore.CYAN}▀▀ {Fore.RED}─░█──{Style.RESET_ALL}\n"
    f"{Fore.RED}░█▄▄█ {Fore.GREEN}░█─░█ {Fore.YELLOW}░█─░█ {Fore.GREEN}──░█── 　 {Fore.MAGENTA}░█─░█ {Fore.CYAN}░█▄▄▄ {Fore.RED}░█─░█ {Fore.GREEN}░█─── {Fore.YELLOW}░█▄▄▄ {Fore.MAGENTA}░█─░█ {Fore.CYAN}── {Fore.RED}▄▀░▀▄{Style.RESET_ALL}\n\n"
    f"{Fore.YELLOW}[!!] INPUT/OUTPUT DIRECTORIES ARE AUTOMATICALLY SET BASED ON HARDCODED DIR [!!]\n\n"
    f"📥 INPUT DIRECTORY:  {Fore.GREEN}{{}}/parts\n{Style.RESET_ALL}"
    f"{Fore.YELLOW}⚠️ WARNING ⚠️{Style.RESET_ALL}{Fore.RED}  FILES WILL BE DELETED AFTER EXECUTION DONE{Style.RESET_ALL} {Fore.YELLOW}⚠️ WARNING ⚠️{Style.RESET_ALL}\n\n"
    f"{Fore.YELLOW}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.RESET_ALL}"
).format(os.getcwd(), os.getcwd())
print(ascii_art)

log_ascii_art = (
    "░█▀▀█ ░█▀▀█ ─█▀▀█ ░█──░█ 　 ░█▀▀█ ░█▀▀▀ ─█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ ── ▀▄░▄▀\n"
    "░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█▄▄▄█ 　 ░█▄▄▀ ░█▀▀▀ ░█▄▄█ ░█▄▄█ ░█▀▀▀ ░█▄▄▀ ▀▀ ─░█──\n"
    "░█▄▄█ ░█─░█ ░█─░█ ──░█── 　 ░█─░█ ░█▄▄▄ ░█─░█ ░█─── ░█▄▄▄ ░█─░█ ── ▄▀░▀▄\n\n"
    "GRAYBYTE CHAOS-LOGGER-DETAILED LOGS\n"
    "MY LIFE IS A LIE AND IM LIVING IN THIS ONLY TRUTH -GRAYBYTE\n"
    "══════════════════════════════════════════════════════════════════════════════════════════\n"
    "FOR MORE INFORMATION AND HELP\n\n"
    "TELEGRAM : https://t.me/rex_cc\n"
    "FACEBOOK : https://www.facebook.com/graybyt3\n"
    "INSTAGRAM : https://www.instagram.com/gray_byte\n"
    "X : https://x.com/gray_byte\n"
    "══════════════════════════════════════════════════════════════════════════════════════════\n"
)

working_directory = os.getcwd()
input_directory = os.path.join(working_directory, "parts")
log_directory = "CHAOS-LOGGER"

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
        f"ENCOUNTRED ON : {timestamp}\n"
        f"{Fore.YELLOW}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.RESET_ALL}"
    )
    if not os.path.exists(error_file_path):
        with open(error_file_path, 'w', encoding='utf-8') as error_file:
            error_file.write(log_ascii_art)
    with open(error_file_path, 'a', encoding='utf-8') as error_file:
        error_file.write(entry)

if not os.path.exists(input_directory):
    error_msg = f"{Fore.RED}🆘 [CRITICAL-ERROR] INPUT DIRECTORY NOT FOUND: {input_directory} 🆘{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input(f"{Fore.RED}PRESS ENTER TO CONTINUE OR CTRL+C TO EXIT...{Style.RESET_ALL}")
    sys.exit(1)

input_files = [file for file in os.listdir(input_directory) if file.endswith(".txt")]

if not input_files:
    error_msg = f"{Fore.RED}🆘 [CRITICAL-ERROR] NO FILES FOUND IN {input_directory} [CRITICAL-ERROR]🆘{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input(f"{Fore.RED}PRESS ENTER TO CONTINUE OR CTRL+C TO EXIT......{Style.RESET_ALL}")
    sys.exit(1)

if not os.path.exists("yourscript-name.extention"):
    error_msg = f"{Fore.RED}🆘 [CRITICAL-ERROR] yourscript-name.extention NOT FOUND IN CURRENT DIRECTORY [CRITICAL-ERROR]🆘{Style.RESET_ALL}"
    print(error_msg)
    log_error(error_msg)
    input(f"{Fore.RED}PRESS ENTER TO EXIT......{Style.RESET_ALL}")
    sys.exit(1)

for input_file in input_files:
    start_time = time.time()
    start_datetime = datetime.now()
    
    input_file_path = os.path.join(input_directory, input_file)
    
    try:
        url_count = 0
        with open(input_file_path, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if line.strip():
                    url_count += 1
        print(f"{Fore.WHITE}🎯 FILE LOCATION: {input_file_path} 🐇🐇{Style.RESET_ALL}")
        print(f"{Fore.GREEN}📥 LOADED SUCCESSFULLY: {input_file}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🌐 URLS FOUND: {url_count}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}═══════════════════════════════════════════════════ EXECUTION LOG ═════════════════════════════════════════════{Style.RESET_ALL}")
        
    except FileNotFoundError:
        error_msg = f"{Fore.RED}🆘 [CRITICAL-ERROR] FILE NOT FOUND: {input_file_path} [CRITICAL-ERROR] 🆘{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        continue
    except Exception as e:
        error_msg = f"{Fore.RED}🆘 [CRITICAL-ERROR] ERROR READING FILE {input_file}: {str(e)} [CRITICAL-ERROR] 🆘{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        continue
    
    checking_file_path = os.path.join(log_directory, 'byte-stream.txt')
    if not os.path.exists(checking_file_path):
        with open(checking_file_path, 'w', encoding='utf-8') as ww:
            ww.write(log_ascii_art)
    with open(checking_file_path, 'a', encoding='utf-8') as ww:
        ww.write(f"\nFILENAME: {input_file}\n")
        ww.write(f"FILE TAKEN FOR EXECUTION : {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        ww.write("═════════════════════════════════════ EXECUTION LOG ═══════════════════════════════════════════════════\n")
    
    try:
        with open(os.devnull, 'w') as devnull:
            process = subprocess.Popen(
                [sys.executable, "yourscript-name.extention"],
                #Example: mybot.py
                stdin=subprocess.PIPE,
                stdout=devnull,
                stderr=devnull,
                text=True
            )
            process.communicate(input=input_file_path)
    except Exception as e:
        error_msg = f"{Fore.RED}🆘 [CRITICAL-ERROR] FAILED TO EXECUTE yourscript-name.extention FOR {input_file}\n[-] {str(e)}\n[!!] CHECK ENVIRONMENT / SCRIPT [CRITICAL-ERROR] 🆘{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        sys.exit(1)
    
    end_time = time.time()
    end_datetime = datetime.now()
    time_taken = end_time - start_time
    
    print(f"⏱️ START TIME: {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}")
    print(f"⏱️ END TIME:   {end_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}")
    print(f"⏱️ TIME TAKEN: {time_taken:.2f} SECONDS | URLs CHECKED: {url_count}")
    
    if time_taken < 1.0:
        error_msg = f"{Fore.RED}🆘🆘🆘 [DANGER] EXECUTION TOO FAST ({time_taken:.2f}s) for {input_file}! LIKELY SCRIPT FAILURE OR CRASH. HALTING ALL OPERATIONS! [DANGER] 🆘🆘🆘{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
        sys.exit(1)
    
    try:
        os.remove(input_file_path)
        print(f"{Fore.YELLOW}🗑️ DELETED {input_file} AFTER PROCESSING{Style.RESET_ALL}")
    except Exception as e:
        error_msg = f"{Fore.RED}🆘 [CRITICAL-ERROR] FAILED TO DELETE: {input_file}: {str(e)} [CRITICAL-ERROR]{Style.RESET_ALL}"
        print(error_msg)
        log_error(error_msg)
    
    print(f"{Fore.GREEN}✅ PROCESSING COMPLETED: {input_file}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.RESET_ALL}\n")
    
    checked_file_path = os.path.join(log_directory, 'byte-archive.txt')
    if not os.path.exists(checked_file_path):
        with open(checked_file_path, 'w', encoding='utf-8') as check_file:
            check_file.write(log_ascii_art)
    with open(checked_file_path, 'a', encoding='utf-8') as check_file:
        check_file.write(f"\nFILENAME: {input_file}\n")
        check_file.write(f"START: {start_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        check_file.write(f"END: {end_datetime.strftime('%d-%B-%Y | %I:%M:%S %p')}\n")
        check_file.write(f"TIME TAKEN: {time_taken:.2f} SECONDS | URLs CHECKED: {url_count}\n")
        check_file.write("═══════════════════════════════════════════════════════════════════════════════════════════════\n")
    
    time.sleep(1)

print(f"\n{Fore.MAGENTA}✅ ALL FILES PROCESSED AND DELETED. OPERATION COMPLETE..{Style.RESET_ALL}")
