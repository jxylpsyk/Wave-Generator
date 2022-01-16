#making this code took a while...
import numpy as np
import simpleaudio as sa

# this part is for calculating frequencies of all notes
A4_freq = 440
A3_freq = 220
Ash3_freq = 0.5**(11/12) * A4_freq
Bb3_freq = 0.5**(11/12) * A4_freq
B3_freq = 0.5**(10/12) * A4_freq
C4_freq = 0.5**(9/12) * A4_freq
Csh4_freq = 0.5**(8/12) * A4_freq
Db4_freq = 0.5**(8/12) * A4_freq
D4_freq = 0.5**(7/12) * A4_freq
Dsh4_freq = 0.5**(6/12) * A4_freq
Eb4_freq = Dsh4_freq
E4_freq = 0.5**(5/12) * A4_freq
F4_freq = 0.5**(4/12) * A4_freq
Fsh4_freq = 0.5**(3/12) * A4_freq
G4b_freq = 0.5**(3/12) * A4_freq
G4_freq = 0.5**(2/12) * A4_freq
Gsh4_freq = 0.5**(1/12) * A4_freq
Ab4_freq = 0.5**(1/12) * A4_freq
Ash4_freq = 2**(1/12) * A4_freq
Bb4_freq = 2**(1/12) * A4_freq
B4_freq = 2**(2/12) * A4_freq
C5_freq = 2**(3/12) * A4_freq
Csh5_freq = 2**(4/12) * A4_freq
Db5_freq = 2**(4/12) * A4_freq
D5_freq = 2**(5/12) * A4_freq
Dsh5_freq = 2**(6/12) * A4_freq
Eb5_freq = Dsh5_freq
E5_freq = 2**(7/12) * A4_freq
F5_freq = 2**(8/12) * A4_freq
Fsh5_freq = 2**(9/12) * A4_freq
G5b_freq = 2**(9/12) * A4_freq
G5_freq = 2**(10/12) * A4_freq
Gsh5_freq = 2**(11/12) * A4_freq
Ab5_freq = 2**(11/12) * A4_freq
A5_freq = 2**(12/12) * A4_freq
Ash5_freq = 2**(13/12) * A4_freq
Bb5_freq = 2**(13/12) * A4_freq
B5_freq = 2**(14/12) * A4_freq
C6_freq = 2**(15/12) * A4_freq
Csh6_freq = 2**(16/12) * A4_freq
Db6_freq = 2**(16/12) * A4_freq
D6_freq = 2**(17/12) * A4_freq
Dsh6_freq = 2**(18/12) * A4_freq
Eb6_freq = Dsh6_freq
E6_freq = 2**(19/12) * A4_freq
F6_freq = 2**(20/12) * A4_freq
F6sh_freq = 2**(21/12) * A4_freq
G6b_freq = 2**(21/12) * A4_freq
G6_freq = 2**(22/12) * A4_freq
Gsh6_freq = 2**(23/12) * A4_freq
Ab6_freq = 2**(23/12) * A4_freq
A6_freq = 2**(23/12) * A4_freq
# setting variables for different possible durations of time
sample_rate = 44100
T1 = 0.15
T2 = 0.3
T3 = 0.45
T4 = 0.6
T5 = 0.9
T6 = 1.2


t1 = np.linspace(0, T1, int(T1 * int(sample_rate)), False)
t2 = np.linspace(0, T2, int(T2 * int(sample_rate)), False)
t3 = np.linspace(0, T3, int(T3 * int(sample_rate)), False)
t4 = np.linspace(0, T4, int(T4 * int(sample_rate)), False)
t5 = np.linspace(0, T5, int(T5 * int(sample_rate)), False)

# defining all notes and with their lengths.... i know pretty chaotic
A51 = np.sin(A5_freq * t1 * 2 * np.pi)
E51 = np.sin(E5_freq * t1 * 2 * np.pi)
Fsh51 = np.sin(Fsh5_freq * t1 * 2 * np.pi)
Csh63 = np.sin(Csh6_freq * t3 * 2 * np.pi)
B55 = np.sin(B5_freq * t5 * 2 * np.pi)
B53 = np.sin(B5_freq * t3 * 2 * np.pi)
A55 = np.sin(A5_freq * t5 * 2 * np.pi)

E44 = np.sin(E4_freq * t4 * 2 * np.pi)
Gsh45 = np.sin(Gsh4_freq * t5 * 2 * np.pi)
A43 = np.sin(A4_freq * t3 * 2 * np.pi)
Gsh43 = np.sin(Gsh4_freq * t3 * 2 * np.pi)
Fsh45 = np.sin(Fsh4_freq * t5 * 2 * np.pi)
E43 = np.sin(E4_freq * t3 * 2 * np.pi)
Fsh43 = np.sin(Fsh4_freq * t3 * 2 * np.pi)

#this one is for certain purposes
empty_note1 = np.sin(19 * 0.05 * 2 * np.pi)
empty_note2 = np.sin(19 * 0.05 * 2 * np.pi)

# Audio data is stacked and formed in this step, along with changes to volumes of each note

channel1 = np.hstack((empty_note1, E51, Fsh51, A51, Fsh51, Csh63, Csh63, B55, E51, Fsh51, A51, Fsh51, B53, B53, A55))
channel2 = np.hstack((20*empty_note2, E44, A43, Fsh43, Gsh45, E44, Gsh43, E43, Fsh45))
# more necessary stuff
channel1 *= 32767/np.max(np.abs(channel1))
channel1 = channel1.astype(np.int16)

channel2 *= 32767/np.max(np.abs(channel2))
channel2 = channel2.astype(np.int16)

channel_list = [channel1, channel2]

for channel in channel_list:
    play_obj = sa.play_buffer(channel, 1, 2, sample_rate)

play_obj.wait_done()
