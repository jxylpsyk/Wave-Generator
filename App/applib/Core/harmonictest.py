import numpy as np

from .constants import SAMPLE_RATE

# print("integral frequencies work best")
# FUND = float(input("input fundamental frequency >>"))
T = 1
#print(" rules for typing loudness of harmonics")
#print("type in a value between 0 <= x <= 1")
t = np.linspace(0, T, int(T * SAMPLE_RATE), False)

sldr_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def variabledef(fund_freq):
    H2 = sldr_list[0]
    H3 = sldr_list[1]
    H4 = sldr_list[2]
    H5 = sldr_list[3]
    H6 = sldr_list[4]
    H7 = sldr_list[5]
    H8 = sldr_list[6]
    H9 = sldr_list[7]
    H10 = sldr_list[8]
    H11 = sldr_list[9]
    H12 = sldr_list[10]
    H13 = sldr_list[11]
    H14 = sldr_list[12]
    H15 = sldr_list[13]
    H16 = sldr_list[14]
    H17 = sldr_list[15]
    H18 = sldr_list[16]
    H19 = sldr_list[17]
    H20 = sldr_list[18]
    H21 = sldr_list[19]

    N11 = np.sin(fund_freq * t * 2 * np.pi)
    N21 = np.sin(2 * fund_freq * t * 2 * np.pi)
    N31 = np.sin(3 * fund_freq * t * 2 * np.pi)
    N41 = np.sin(4 * fund_freq * t * 2 * np.pi)
    N51 = np.sin(5 * fund_freq * t * 2 * np.pi)
    N61 = np.sin(6 * fund_freq * t * 2 * np.pi)
    N71 = np.sin(7 * fund_freq * t * 2 * np.pi)
    N81 = np.sin(8 * fund_freq * t * 2 * np.pi)
    N91 = np.sin(9 * fund_freq * t * 2 * np.pi)
    N101 = np.sin(10 * fund_freq * t * 2 * np.pi)
    N111 = np.sin(11 * fund_freq * t * 2 * np.pi)
    N121 = np.sin(12 * fund_freq * t * 2 * np.pi)
    N131 = np.sin(13 * fund_freq * t * 2 * np.pi)
    N141 = np.sin(14 * fund_freq * t * 2 * np.pi)
    N151 = np.sin(15 * fund_freq * t * 2 * np.pi)
    N161 = np.sin(16 * fund_freq * t * 2 * np.pi)
    N171 = np.sin(17 * fund_freq * t * 2 * np.pi)
    N181 = np.sin(18 * fund_freq * t * 2 * np.pi)
    N191 = np.sin(19 * fund_freq * t * 2 * np.pi)
    N201 = np.sin(20 * fund_freq * t * 2 * np.pi)
    N211 = np.sin(21 * fund_freq * t * 2 * np.pi)

    # N11, N21, N31, N41, N51, N61, N71, N81, N91, N101, N111, N121, N131, N141, N151, N161, N171, N181, N191, N201, N211  = N_list

    return (
        N11
        + (H2 * N21)
        + (H3 * N31)
        + (H4 * N41)
        + (H5 * N51)
        + (H6 * N61)
        + (H7 * N71)
        + (H8 * N81)
        + (H9 * N91)
        + (H10 * N101)
        + (H11 * N111)
        + (H12 * N121)
        + (H13 * N131)
        + (H14 * N141)
        + (H15 * N151)
        + (H16 * N161)
        + (H17 * N171)
        + (H18 * N181)
        + (H19 * N191)
        + (H20 * N201)
        + (H21 * N211)
    )


def freqassignfunc(numb, value):
    sldr_list[(int(numb) - 2)] = float(value)

def return_sldr_list():
    return sldr_list

# INTERFACE CODE FOR TESTING

"""
print("type 'yes' for yes or press enter for no")
sineask = input("do you want a sine wave?  >>>")

if sineask.lower() in ["yes", "y"]:
    sineval()
else:
    squareask = input("do you want a square wave?  >>>")
    if squareask.lower() in ["yes", "y"]:
        squareval()
    else:
        triangleask = input("do you want a triangle wave?  >>>")
        if triangleask.lower() in ["yes", "y"]:
            triangleval()
        else:
            sawtoothask = input("do you want a sawtooth wave?  >>>")
            if sawtoothask.lower() in ["yes", "y"]:
                sawtoothval()
            else:
                impulseask = input("do you want an impulse wave?  >>>")
                if impulseask.lower() in ["yes", "y"]:
                    impulseval()

print("harmonic values are as follows:")
for u in sldr_list:
    print(u)
print("do you want to change a harmonic value?")
print("type 'yes' if yes else press enter")
w = input(">>> ")

if w.lower() in ["yes", "y"]:
    print("type the number 'n' to select the n'th harmonic")
    print("then type the required value of the harmonic")

while w.lower() in ["yes", "y"]:
    numb1 = int(input("input the harmonic number(between 2 and 21)  >>> "))
    value1 = float(input("input value of the harmonic selected  >>> "))
    freqassignfunc(numb1, value1)
    print("do you want to make another change?")
    w = input(">>> ")
print("harmonic values are as follows")
for l in sldr_list:
    print(l)

if w.lower() != "yes" or w.lower() != "y":
    H2 = sldr_list[0]
    H3 = sldr_list[1]
    H4 = sldr_list[2]
    H5 = sldr_list[3]
    H6 = sldr_list[4]
    H7 = sldr_list[5]
    H8 = sldr_list[6]
    H9 = sldr_list[7]
    H10 = sldr_list[8]
    H11 = sldr_list[9]
    H12 = sldr_list[10]
    H13 = sldr_list[11]
    H14 = sldr_list[12]
    H15 = sldr_list[13]
    H16 = sldr_list[14]
    H17 = sldr_list[15]
    H18 = sldr_list[16]
    H19 = sldr_list[17]
    H20 = sldr_list[18]
    H21 = sldr_list[19]

    if -1 <= H2 <= 1 and -1 <= H3 <= 1 and -1 <= H4 <= 1 and -1 <= H5 <= 1 and -1 <= H6 <= 1 and -1 <= H7 <= 1 and -1 <= H8 <= 1 and -1 <= H9 <= 1 and -1 <= H10 <= 1 and -1 <= H11 <= 1 and -1 <= H12 <= 1 and -1 <= H13 <= 1 and -1 <= H14 <= 1 and -1 <= H15 <= 1 and -1 <= H16 <= 1 and -1 <= H17 <= 1 and -1 <= H18 <= 1 and -1 <= H19 <= 1 and -1 <= H20 <= 1 and -1 <= H21 <= 1:
        variabledef()

        Note_1 = N11 + (H2 * N21) + (H3 * N31) + (H4 * N41) + (H5 * N51) + (H6 * N61) + (H7 * N71) + (H8 * N81) + (
                H9 * N91) + (H10 * N101) + (H11 * N111) + (H12 * N121) + (H13 * N131) + (H14 * N141) + (H15 * N151) + (
                         H16 * N161) + (H17 * N171) + (H18 * N181) + (H19 * N191) + (H20 * N201) + (H21 * N211)

        Cpro = np.hstack(Note_1)
        Cpro *= 32767 / np.max(np.abs(Cpro))
        Cpro = Cpro.astype(np.int16)
        play1 = sa.play_buffer(Cpro, 1, 2, sample_rate)
        play1.wait_done()

# if -1 <= H2 <= 1 and -1 <= H3 <= 1 and -1 <= H4 <= 1 and -1 <= H5 <= 1 and -1 <= H6 <= 1 and -1 <= H7 <= 1 and -1 <= H8 <= 1 and -1 <= H9 <= 1 and -1 <= H10 <= 1 and -1 <= H11 <= 1 and -1 <= H12 <= 1 and -1 <= H13 <= 1 and -1 <= H14 <= 1 and -1 <= H15 <= 1 and -1 <= H16 <= 1 and -1 <= H17 <= 1 and -1 <= H18 <= 1 and -1 <= H19 <= 1 and -1 <= H20 <= 1:

#    N11 = np.sin(FUND * t * 2 * np.pi)
#    N21 = np.sin(2 * FUND * t * 2 * np.pi)
#    N31 = np.sin(3 * FUND * t * 2 * np.pi)
#    N41 = np.sin(4 * FUND * t * 2 * np.pi)
#    N51 = np.sin(5 * FUND * t * 2 * np.pi)
#    N61 = np.sin(6 * FUND * t * 2 * np.pi)
#    N71 = np.sin(7 * FUND * t * 2 * np.pi)
#    N81 = np.sin(8 * FUND * t * 2 * np.pi)
#    N91 = np.sin(9 * FUND * t * 2 * np.pi)
#    N101 = np.sin(10 * FUND * t * 2 * np.pi)
#    N111 = np.sin(11 * FUND * t * 2 * np.pi)
#    N121 = np.sin(12 * FUND * t * 2 * np.pi)
#    N131 = np.sin(13 * FUND * t * 2 * np.pi)
#    N141 = np.sin(14 * FUND * t * 2 * np.pi)
#    N151 = np.sin(15 * FUND * t * 2 * np.pi)
#    N161 = np.sin(16 * FUND * t * 2 * np.pi)
#    N171 = np.sin(17 * FUND * t * 2 * np.pi)
#    N181 = np.sin(18 * FUND * t * 2 * np.pi)
#    N191 = np.sin(19 * FUND * t * 2 * np.pi)
#    N201 = np.sin(20 * FUND * t * 2 * np.pi)

"""

# END OF INTERFACE CODE



# USEFULL REMINANTS OF PREVIOUSLY FUNCTIONAL CODE

# N12 = np.sin(FUND*(2**(2/12)) * t * 2 * np.pi)
# N13 = np.sin(FUND*(2**(4/12)) * t * 2 * np.pi)
# N14 = np.sin(FUND*(2**(5/12)) * t * 2 * np.pi)
# N15 = np.sin(FUND*(2**(7/12)) * t * 2 * np.pi)


# N22 = np.sin(2 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N23 = np.sin(2 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N24 = np.sin(2 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N25 = np.sin(2 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N32 = np.sin(3 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N33 = np.sin(3 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N34 = np.sin(3 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N35 = np.sin(3 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N42 = np.sin(4 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N43 = np.sin(4 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N44 = np.sin(4 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N45 = np.sin(4 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N52 = np.sin(5 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N53 = np.sin(5 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N54 = np.sin(5 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N55 = np.sin(5 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N62 = np.sin(6 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N63 = np.sin(6 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N64 = np.sin(6 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N65 = np.sin(6 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N72 = np.sin(7 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N73 = np.sin(7 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N74 = np.sin(7 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N75 = np.sin(7 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N82 = np.sin(8 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N83 = np.sin(8 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N84 = np.sin(8 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N85 = np.sin(8 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N92 = np.sin(9 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N93 = np.sin(9 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N94 = np.sin(9 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N95 = np.sin(9 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N102 = np.sin(10 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N103 = np.sin(10 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N104 = np.sin(10 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N105 = np.sin(10 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N112 = np.sin(11 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N113 = np.sin(11 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N114 = np.sin(11 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N115 = np.sin(11 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N122 = np.sin(12 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N123 = np.sin(12 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N124 = np.sin(12 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N125 = np.sin(12 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N132 = np.sin(13 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N133 = np.sin(13 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N134 = np.sin(13 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N135 = np.sin(13 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N142 = np.sin(14 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N143 = np.sin(14 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N144 = np.sin(14 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N145 = np.sin(14 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N152 = np.sin(15 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N153 = np.sin(15 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N154 = np.sin(15 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N155 = np.sin(15 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N162 = np.sin(16 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N163 = np.sin(16 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N164 = np.sin(16 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N165 = np.sin(16 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N172 = np.sin(17 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N173 = np.sin(17 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N174 = np.sin(17 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N175 = np.sin(17 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N182 = np.sin(18 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N183 = np.sin(18 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N184 = np.sin(18 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N185 = np.sin(18 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N192 = np.sin(19 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N193 = np.sin(19 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N194 = np.sin(19 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N195 = np.sin(19 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# N202 = np.sin(20 * FUND * (2 ** (2 / 12)) * t * 2 * np.pi)
# N203 = np.sin(20 * FUND * (2 ** (4 / 12)) * t * 2 * np.pi)
# N204 = np.sin(20 * FUND * (2 ** (5 / 12)) * t * 2 * np.pi)
# N205 = np.sin(20 * FUND * (2 ** (7 / 12)) * t * 2 * np.pi)


# Note_2 = N12 + (H2 * N22) + (H3 * N32) + (H4 * N42) + (H5 * N52) + (H6 * N62) + (H7 * N72) + (H8 * N82) + ( H9 * N92) + (H10 * N102) + (H11 * N112) + (H12 * N122) + (H13 * N132) + (H14 * N142) + (H15 * N152) + ( H16 * N162) + (H17 * N172) + (H18 * N182) + (H19 * N192) + (H20 * N202)
# Note_3 = N13 + (H2 * N23) + (H3 * N33) + (H4 * N43) + (H5 * N53) + (H6 * N63) + (H7 * N73) + (H8 * N83) + ( H9 * N93) + (H10 * N103) + (H11 * N113) + (H12 * N123) + (H13 * N133) + (H14 * N143) + (H15 * N153) + ( H16 * N163) + (H17 * N173) + (H18 * N183) + (H19 * N193) + (H20 * N203)
# Note_4 = N14 + (H2 * N24) + (H3 * N34) + (H4 * N44) + (H5 * N54) + (H6 * N64) + (H7 * N74) + (H8 * N84) + ( H9 * N94) + (H10 * N104) + (H11 * N114) + (H12 * N124) + (H13 * N134) + (H14 * N144) + (H15 * N154) + ( H16 * N164) + (H17 * N174) + (H18 * N184) + (H19 * N194) + (H20 * N204)
# Note_5 = N15 + (H2 * N25) + (H3 * N35) + (H4 * N45) + (H5 * N55) + (H6 * N65) + (H7 * N75) + (H8 * N85) + ( H9 * N95) + (H10 * N105) + (H11 * N115) + (H12 * N125) + (H13 * N135) + (H14 * N145) + (H15 * N155) + ( H16 * N165) + (H17 * N175) + (H18 * N185) + (H19 * N195) + (H20 * N205)

