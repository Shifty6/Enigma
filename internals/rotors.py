import yaml

with open('internals/config.yml', encoding='utf-8') as rotor_data:
    data = yaml.safe_load(rotor_data)

rotor_cont = data.get('rotor_contents')
rotor_pos = data.get('rotor_positions')


class Rotors(object):
    def __init__(self):
        self.alpha = rotor_cont.get('alphabet')
        self.a_pos = rotor_pos.get('rotor_a')
        self.b_pos = rotor_pos.get('rotor_b')
        self.c_pos = rotor_pos.get('rotor_c')
        self.a_cont = rotor_cont.get('rotor_a')
        self.b_cont = rotor_cont.get('rotor_b')
        self.c_cont = rotor_cont.get('rotor_c')
        self.d_cont = rotor_cont.get('rotor_d')
        self.plugboard = data.get('plugboard')

    def get_cont(self):
        a = self.a_cont[self.a_pos:] + self.a_cont[:self.a_pos]
        b = self.b_cont[self.b_pos:] + self.b_cont[:self.b_pos]
        c = self.c_cont[self.c_pos:] + self.c_cont[:self.c_pos]
        return a, b, c

    def cycle(self):
        self.a_pos += 1
        if self.a_pos > 25:
            self.a_pos = 0
            self.b_pos += 1
            if self.b_pos > 25:
                self.b_pos = 0
                self.c_pos += 1
                if self.c_pos > 25:
                    self.c_pos = 0

    def get_plugboard(self, char):
        for plug in self.plugboard:
            if len(plug) == 2:
                if char.upper() == plug[0]:
                    char = plug[1]
                    break
        return char

    def encrypt(self, text):
        text_out = ''
        for char in text:
            if char.isalpha():
                char_in = self.get_plugboard(char)
                (a, b, c), d, alpha = self.get_cont(), self.d_cont, self.alpha
                a_in = a[alpha.index(char_in.upper())]
                b_in = b[alpha.index(a_in)]
                c_in = c[alpha.index(b_in)]
                d_in = d[alpha.index(c_in)]
                c_out = alpha[c.index(d_in)]
                b_out = alpha[b.index(c_out)]
                a_out = alpha[a.index(b_out)]
                char_out = self.get_plugboard(a_out)
                text_out += char_out
                self.cycle()
        return text_out
