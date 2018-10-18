import yaml

with open('internals/config.yml', encoding='utf-8') as rotor_data:
    data = yaml.safe_load(rotor_data)
rotor_cont = data.get('rotor_contents')
rotor_pos = data.get('rotor_positions')


def config_text():
    text = [
        f'ENTRY ROTOR:\n'
        f'Contents: {rotor_cont.get("alphabet")}\n\n'
        f'ROTOR A:\n'
        f'Contents: {rotor_cont.get("rotor_a")}\n'
        f'Position: {rotor_pos.get("rotor_a")}\n\n'
        f'ROTOR B:\n'
        f'Contents: {rotor_cont.get("rotor_b")}\n'
        f'Position: {rotor_pos.get("rotor_b")}\n\n'
        f'ROTOR C:\n'
        f'Contents: {rotor_cont.get("rotor_c")}\n'
        f'Position: {rotor_pos.get("rotor_c")}\n\n'
        f'REFLECTOR ROTOR:\n'
        f'Contents: {rotor_cont.get("rotor_d")}\n\n'
        f'PLUGBOARD:\n'
        f'Plugs: {", ".join(data.get("plugboard"))}\n'
    ]
    return ''.join(text)


def help_text():
    text = [
        'To Encrypt: Enter a message and press enter.\n'
        'To Decrypt: Enter an encrypted message with the same settings that were used to encrypt it.\n'
        'Only characters in the ISO basic Latin alphabet will be processed.\n'
        'For configuration please see the config.md file.\n'
    ]
    return ''.join(text)
