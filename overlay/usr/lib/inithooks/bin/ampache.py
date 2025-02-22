#!/usr/bin/python3
"""Set Ampache admin password

Option:
    --pass=     unless provided, will ask interactively
"""
APP = "Ampache"

import sys
import getopt
import bcrypt
from mysqlconf import MySQL
import subprocess

from libinithooks.dialog_wrapper import Dialog
from libinithooks import inithooks_cache


def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print(f"Syntax: {sys.argv[0]} [options]", file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            f"{APP} Password",
            d"Enter new password for the {APP} 'admin' account.")

    # XXX the rest needs to be updated...

    CONF = '/var/www/ampache/.env'
    # read .env lines
    with open(CONF, 'r') as fob:
        conf_lines = fob.readlines()

    # find APP_URL and set it to domain
    for i in range(len(conf_lines)):
        line = conf_lines[i].strip()
        if '=' not in line:
            continue
        key, value = line.split('=', 1)
        if key == 'APP_URL':
            line = f'APP_URL=https://{domain}'
        conf_lines[i] = line + '\n'

    # write .env lines
    with open(CONF, 'w') as fob:
        fob.writelines(conf_lines)

    subprocess.run(['/usr/local/bin/turnkey-artisan', 'config:clear'])

    salt = bcrypt.gensalt()
    hashpass = bcrypt.hashpw(password.encode('utf8'), salt).decode('utf8')
    
    m = MySQL()
    m.execute('UPDATE snipeit.users SET password=%s WHERE id=1;', (hashpass,))
    #m.execute('UPDATE snipeit.users SET email=%s WHERE id=1;', (email,))


if __name__ == "__main__":
    main()
