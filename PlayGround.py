from Crypto.Util.number import bytes_to_long, long_to_bytes
import os

alice_n = 17076498954505451321861119187729608757416905748867673888110876027453110303809918524948169536577185009725422636230582777751694760854745372838514526794977168980920985183480524141333711115233599125338182976448921374937390114899156362042708864365541798300522589522145664475311378703829810669442629548206236717298608728361314202046190112352158981081513551383513539439992638105251243490030080400407761002218040842348387684329337920895373544435826296548819466755568180630427687532756967027894903752312575345105900871880133312939399972998499864894933353341278217027846929478575996736832500945330491531018098316270751574762249  # Alice's modulus
bob_n = 24013931831232453281518966703896935736579923596763663442887932342463401388694231179675633142563508390638324096418142016403796592874546102637282709981349828515627864402237928489533475173833847031793167583797656645048519100930036698097419117422705349421063067725601837677342686605785991794918193759898208415092096382520677696121700320901801150549995678591709374648264923032295635998712646210679016968529991268307423471583495735852776032376049015007865071024655011075722012619811633975077171223538628559915256165007964674072134567522119172998111045971050032009368095770051750902712736998687296409687016286673471252330313    # Bob's modulus
e = 65537
captured = []
PATH = os.path.dirname(os.path.abspath(__file__))
with open(PATH + "\\" + "output.txt", 'r') as f:
    for line in f.readlines():
        if "alice: " in line:
            captured.append(int(line[7:].strip()))
        if "bob: " in line:
            captured.append(int(line[5:].strip()))
print(captured.pop(0))

def encrypt(pt, n, e):
    return pow(pt, e, n)

def decrypt_step(ciphertexts, alice_n, bob_n, e):
    upper = 2**501
    lower = 0
    flag = None
    step = 0

    for i in range(1, len(ciphertexts)-3, 2):
        current_mid = (upper + lower) // 2
        question_msg = f"Is your number greater than {current_mid}?".encode()
        question_pt = bytes_to_long(question_msg)
        question_ct = encrypt(question_pt, alice_n, e)
        if question_ct != ciphertexts[i]:
            print("no u, binary search error")
            return None

        yes_msg = f"Yes!, my number is greater than {current_mid}".encode()
        no_msg = f"No!, my number is lower or equal to {current_mid}".encode()
        yes_pt = bytes_to_long(yes_msg)
        no_pt = bytes_to_long(no_msg)
        yes_ct = encrypt(yes_pt, bob_n, e)
        no_ct = encrypt(no_pt, bob_n, e)

        if ciphertexts[i+1] == yes_ct:
            lower = current_mid
        elif ciphertexts[i+1] == no_ct:
            upper = current_mid
        else:
            print("no u, ciphertext what???")
            return None

        step += 1

    final_msg = f"so your number is {upper}?".encode()
    final_pt = bytes_to_long(final_msg)
    final_ct = encrypt(final_pt, alice_n, e)
    if final_ct == captured[-3]:
        flag = upper
    else:
        print("I have no idea-")
        return None

    return flag

flag = decrypt_step(captured, alice_n, bob_n, e)
if flag is not None:
    flag_bytes = long_to_bytes(flag)
    print("Flag:", flag_bytes.decode())