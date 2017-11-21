from netmiko import ConnectHandler

def main():


    # Enter commands to send here! SHOW COMMANDS ONLY!
    command_list = [
        'show vpc brief',
        'show vlan summary'
    ]

    # Enter devices you wish to connect to
    device_list = [
        # Copy / paste the section below for each device

        {'device_type':'cisco_nxos',  # cisco_ios, cisco_nxos, cisco_iosxr, cisco_iosxe
        'ip':'10.53.224.1',
        'username':'admin',
        'password':'mypassword',
        'port':22},

        {'device_type':'cisco_nxos',  # cisco_ios, cisco_nxos, cisco_iosxr, cisco_iosxe
        'ip':'10.53.224.2',
        'username':'admin',
        'password':'mypassword',
        'port':22},
    ]

    # Do not edit past here.
    for device in device_list:
        run_commands(command_list,device)

def run_commands(commands,device_info):
    connection = ConnectHandler(**device_info)
    print('\n\n**Device: {}'.format(device_info['ip']))
    for command in commands:
        output = connection.send_command(command)
        print('\n\n***Output for command: {}***'.format(command))
        print(output)

if __name__ == '__main__':
    main()
