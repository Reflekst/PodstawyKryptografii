import Tests as tests
import StreamEncoder as stE
import BBS as bbs

st = stE.streamEncoder(path = "Text.txt")
print("Wiadomość:")
print(st.clearText)
st.setBBS()
st.setEncoder()

print("Wiadomość zaszyfrowana:")
print(st.endcoder)

print("Wiadomość odszyfrowana:")
st.decrypt()

print("Testy:")
test = tests.StandardTests(binaryString=st.endcoder)

test.singleBitsTest()
test.seriesTest()
test.longestSeriesTest()
test.pokerTest()

files = ["string1.txt","string2.txt","string3.txt"]

for file in files:
   print("Plik - "+file)
   test = tests.StandardTests(path = file)
   test.singleBitsTest()
   test.seriesTest()
   test.longestSeriesTest()
   test.pokerTest()
   print()

f = open("tenMln.txt","a")
bbs1 = bbs.BlumBlumShub()
f.write(bbs1.bits(r = 1000000))
f.close()
