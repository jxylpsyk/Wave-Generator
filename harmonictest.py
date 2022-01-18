import numpy as np
import simpleaudio as sa
print("integral frequencies work best")
FUND = float(input("input fundamental frequency >>"))
sample_rate = 44100
T = 0.6
t = np.linspace(0, T, int(T*sample_rate), False)
print(" rules for typing loudness of harmonics")
print("type in a value between 0 < x <= 1")
print("If you want to type 0, type a number like 0.0001")

H2 = float(input("level of H2 >>"))
H3 = float(input("level of H3 >>"))
H4 = float(input("level of H4 >>"))
H5 = float(input("level of H5 >>"))
H6 = float(input("level of H6 >>"))
H7 = float(input("level of H7 >>"))
H8 = float(input("level of H8 >>"))
H9 = float(input("level of H9 >>"))
H10 = float(input("level of H10 >>"))

if H2 == 0 or H3 == 0 or H4 == 0 or H5 == 0 or H6 == 0 or H7 == 0 or H8 == 0 or H9 == 0 or H10 == 0:
    print("bruh, what did i tell you?")
elif 0 < H2 <= 1 and 0 < H3 <= 1 and 0 < H4 <= 1 and 0 < H5 <= 1 and 0 < H6 <= 1 and 0 < H7 <= 1 and 0 < H8 <= 1 and 0 < H9 <= 1 and 0 <= H10 <= 1 :
    N11 = np.sin(FUND * t * 2 * np.pi)
    N12 = np.sin(FUND*(2**(2/12)) * t * 2 * np.pi)
    N13 = np.sin(FUND*(2**(4/12)) * t * 2 * np.pi)
    N14 = np.sin(FUND*(2**(5/12)) * t * 2 * np.pi)
    N15 = np.sin(FUND*(2**(7/12)) * t * 2 * np.pi)

    N21 = np.sin(2 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N22 = np.sin(2 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N23 = np.sin(2 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N24 = np.sin(2 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N25 = np.sin(2 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N31 = np.sin(3 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N32 = np.sin(3 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N33 = np.sin(3 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N34 = np.sin(3 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N35 = np.sin(3 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N41 = np.sin(4 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N42 = np.sin(4 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N43 = np.sin(4 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N44 = np.sin(4 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N45 = np.sin(4 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N51 = np.sin(5 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N52 = np.sin(5 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N53 = np.sin(5 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N54 = np.sin(5 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N55 = np.sin(5 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N61 = np.sin(6 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N62 = np.sin(6 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N63 = np.sin(6 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N64 = np.sin(6 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N65 = np.sin(6 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N71 = np.sin(7 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N72 = np.sin(7 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N73 = np.sin(7 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N74 = np.sin(7 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N75 = np.sin(7 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N81 = np.sin(8 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N82 = np.sin(8 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N83 = np.sin(8 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N84 = np.sin(8 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N85 = np.sin(8 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N91 = np.sin(9 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N92 = np.sin(9 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N93 = np.sin(9 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N94 = np.sin(9 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N95 = np.sin(9 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    N101 = np.sin(10 * FUND * (2 ** (0 / 12)) * t * 2 * np.pi)
    N102 = np.sin(10 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
    N103 = np.sin(10 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
    N104 = np.sin(10 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
    N105 = np.sin(10 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)

    Empty_note1 = np.sin(1.108 * t * 2 * np.pi)
    Empty_note2 = (1/H2) * np.sin(1.104 * t * 2 * np.pi)
    Empty_note3 = (1/H3) * np.sin(1.091 * t * 2 * np.pi)
    Empty_note4 = (1/H4) * np.sin(1.078 * t * 2 * np.pi)
    Empty_note5 = (1/H5) * np.sin(1.065 * t * 2 * np.pi)
    Empty_note6 = (1/H6) * np.sin(1.052 * t * 2 * np.pi)
    Empty_note7 = (1/H7) * np.sin(1.039 * t * 2 * np.pi)
    Empty_note8 = (1/H8) * np.sin(1.026 * t * 2 * np.pi)
    Empty_note9 = (1/H9) * np.sin(1.013 * t * 2 * np.pi)
    Empty_note10 = (1/H10) * np.sin(1 * t * 2 * np.pi)

    C1 = np.hstack((Empty_note1, N11, N12, N13, N14, N15))
    C1 *= 32767/np.max(np.abs(C1))
    C1 = C1.astype(np.int16)

    C2 = np.hstack((Empty_note2, N21, N22, N23, N24, N25))
    C2 *= 32767 / np.max(np.abs(C2))
    C2 = C2.astype(np.int16)

    C3 = np.hstack((Empty_note3, N31, N32, N33, N34, N35))
    C3 *= 32767 / np.max(np.abs(C3))
    C3 = C3.astype(np.int16)

    C4 = np.hstack((Empty_note4, N41, N42, N43, N44, N45))
    C4 *= 32767 / np.max(np.abs(C4))
    C4 = C4.astype(np.int16)

    C5 = np.hstack((Empty_note5, N51, N52, N53, N54, N55))
    C5 *= 32767 / np.max(np.abs(C5))
    C5 = C5.astype(np.int16)

    C6 = np.hstack((Empty_note6, N61, N62, N63, N64, N65))
    C6 *= 32767 / np.max(np.abs(C6))
    C6 = C6.astype(np.int16)

    C7 = np.hstack((Empty_note7, N71, N72, N73, N74, N75))
    C7 *= 32767 / np.max(np.abs(C7))
    C7 = C7.astype(np.int16)

    C8 = np.hstack((Empty_note8, N81, N82, N83, N84, N85))
    C8 *= 32767 / np.max(np.abs(C8))
    C8 = C8.astype(np.int16)

    C9 = np.hstack((Empty_note9, N91, N92, N93, N94, N95))
    C9 *= 32767 / np.max(np.abs(C9))
    C9 = C9.astype(np.int16)

    C10 = np.hstack((Empty_note10, N101, N102, N103, N104, N105))
    C10 *= 32767 / np.max(np.abs(C10))
    C10 = C10.astype(np.int16)

    channel_list = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10]
    for channel in channel_list :
        play = sa.play_buffer(channel, 1, 2, sample_rate)
    play.wait_done()

    if FUND < 40:
        print("did that sound come from your ass?")
    elif FUND == 69:
        print("w0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO")
        q1 = ""
        i=1
        x = 69
        while q != "asdfg":
            print(i * x)
            i += 1
    elif FUND == 69:
        print("w0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO0oO")
        q2 = ""
        j=1
        x2 = 420
        while q != "asdfg":
            print(j * x2)
            j += 1
    elif 2000 < FUND < 14500:
        print("I hope you didn't summon all the bats")
    elif FUND > 14500:
        print("it aint worth trying higher, i guess you get the point")
else:
    print("pls read rules once more")


if H2 == H3 == H4 == H5 == H6 == H7 == H8 == H9 == H10 != 0.69:
    print("all same, lame choice")
    print(f"only {H2}'s...")
elif H2 == H3 == H4 == H5 == H6 == H7 == H8 == H9 == H10 == 0.69:
    print("omg!! he only typed the sex number")
    print("typing 0.420 won yield anything new, don't worry")
elif H2 == H3 == H4 == H5 == H6 == H7 == H8 == H9 == H10 == 0.42:
    print("I told you")