import winsound

def Solfege():
    frequencies = [262, 294, 330, 349, 392, 440, 494]
    duration = 500

    for e in frequencies:
        winsound.Beep(e, duration)

if __name__ == '__main__':
    Solfege()