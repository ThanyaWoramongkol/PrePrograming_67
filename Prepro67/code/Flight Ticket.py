"""Flight Ticket"""

def main(txt):
    """-"""
    name = txt[txt.find("Name")+4:txt.find("From")].strip()
    start = txt[txt.find("From")+4:txt.find("To")].strip().lower()
    stop = txt[txt.find("To")+2:].strip().lower()
    print(name, start, stop, sep="\n")
main(input())
