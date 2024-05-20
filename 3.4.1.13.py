beatles = []
print("step1:", beatles)

beatles.append("david corenswet")
beatles.append("henry cavil")
beatles.append("harrison ford")

print("step2:", beatles)
for i in range(1):
    beatles.append("lynda carter, gal gadot")
print("step3:", beatles)

del beatles[3]
print("step4:", beatles)

beatles.insert(4, "sylvester stallone")
print("step5:", beatles)

print("the fab", len(beatles))