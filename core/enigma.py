from internals.rotors import Rotors
from internals.storage import config_text, help_text


class Enigma(object):
    @staticmethod
    def split():
        print('------------------------------')

    def wait(self):
        self.get_input('Press enter to return to the menu...')
        self.menu()

    def get_input(self, text):
        try:
            return input(text)
        except KeyboardInterrupt:
            print('\nProcess interrupted. Returning to menu.')
            self.menu()

    def message(self):
        self.split()
        print('Please enter a message to process...')
        ended = False
        text = None
        while not ended:
            text = self.get_input('>')
            if not text:
                print('Message cannot be blank.')
            else:
                ended = True
        return text

    def menu(self):
        self.split()
        print('Please select an option...\n(1) Encrypt\n(2) Settings\n(3) Help\n(4) Exit')
        mode = self.get_input('>')
        if mode == '1':
            text = self.message()
            encrypted = Rotors().encrypt(text)
            if encrypted:
                self.split()
                print(encrypted + '\n')
                self.wait()
            else:
                print('String contained no valid characters. A-Z Only.')
        elif mode == '2':
            print(config_text())
            self.wait()
        elif mode == '3':
            print(help_text())
            self.wait()
        elif mode == '4':
            exit()
        else:
            print('Invalid mode.')
            self.menu()
