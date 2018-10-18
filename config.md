## Enigma Machine Configuration

Navigate to `internals/config.yml` and open it for editing.

```yml
rotor_contents:
  alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
  rotor_a: JGDQOXUSCAMIFRVTPNEWKBLZYH
  rotor_b: NTZPSFBOKMWRCJDIVLAEYUXHGQ
  rotor_c: JVIUBHTCDYAKEQZPOSGXNRMWFL
  rotor_d: QYHOGNECVPUZTFDJAXWMKISRBL

rotor_positions:
  rotor_a: 0
  rotor_b: 0
  rotor_c: 0

plugboard:
 - "AB"
```

### `rotor_contents` Contents

* `alphabet`: Sets the base alphabet from which all indexes will be based on.
* `rotor_a`: Sets the mapping for the first rotor. Mapping is done via the index position of the inputted character's position in the base alphabet.
* `rotor_b`: Sets the mapping for the second rotor. Mapping is done via the index position of the character returned by the first rotor.
* `rotor_c`: Sets the mapping for the third rotor. Mapping is done via the index position of the character returned by the second rotor.
* `rotor_d`: Sets the mapping for the reflector. Mapping is done via the index position of the character returned by the third rotor.

### `rotor_positions` Contents

* `rotor_a`: Sets the starting index position for the first rotor.
* `rotor_b`: Sets the starting index position for the second rotor.
* `rotor_c`: Sets the starting index position for the third rotor.

### `plugboard` Contents

* `- "AB"` Swaps the letters A and B, both when entering the rotors and when leaving them.
