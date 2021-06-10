% make chirp signal as wav file
filename = "chirp-0-30000-60s.wav";

fs = 96000;
t = 0:1/fs:60;
y = chirp(t,0,60,30000);


audiowrite(filename, y, fs);