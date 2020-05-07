import argparse as ap
import hashlib
# Pyython parser om aangepaste argumenten te kunnen gebruiken.
parser = ap.ArgumentParser(description='Dit is een simpele password cracker')
#parser.add_argument("-h", "--help", help="Enter ")
parser.add_argument("-w", "--wordlist", required=True, help="Enter here the wordlist you want to use")
parser.add_argument("-p", "--passhash", required=True, help="Enter here your md5 hash password")
parser.add_argument("-v", "--verbose", action='store_true', help="Verbose mode gives you extra information")
args = parser.parse_args()


def main(wordlist, passhash):
    # De flag zorgt ervoor dat wanneer een match gevonden is we uit de loop gaan.
    flag = 0

    # Opent het text bestand, bij een error quit
    try:
        passwd_file = open(wordlist, "r")
    except OSError:
        print("no file found")
        quit()

    # Leest alle woorden in het txt bestand uit en slaat het op als hash in de var digest
    for word in passwd_file:

        # Dit maakt van alle worden in het bestand een hash
        enc_wrd = word.encode('utf-8')
        verwerk = hashlib.md5(enc_wrd.strip()).hexdigest()


        # Als een hash in het text bestand gelijk is aan de opgegeven hash dan print password found
        if verwerk == args.passhash:
            print("Password found")
            print("password is " + word)
            flag = 1
            break

    # Als flag 0 is, is het wachtwoord niet gevonden
    if flag == 0:
        print("Password is not in the list")

# Roept de functie main op, als verbose is aangeven voert die een aangepaste versie aan, anders de standaard crack.
if __name__ == "__main__":
    #main(args.wordlist, args.passhash)
    crack = main(args.wordlist, args.passhash)

    if args.verbose:
        print("Wordlist used: %s \nMd5 hash used: %s \nOutcome: %s" % (args.wordlist, args.passhash, crack))
    else:
        crack


