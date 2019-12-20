import numpy

message = "X X Z ZX I ZX X X Z Z Z I X Z ZX X I Z Z I I ZX Z X I ZX X X ZX Z Z X X Z Z I I ZX X Z X Z Z I X ZX I ZX I ZX" \
          " X X ZX ZX ZX ZX ZX ZX X I Z Z ZX Z ZX ZX X Z I ZX Z X I Z Z X X ZX I ZX I ZX X I Z ZX X X Z Z Z I X Z Z X X " \
          "ZX I Z X ZX ZX I I ZX X I Z Z ZX Z ZX Z X ZX X Z X ZX I Z Z I X Z ZX ZX Z Z Z I I Z ZX I X ZX ZX I I Z ZX Z " \
          "ZX ZX ZX X X ZX ZX I I ZX X X ZX Z ZX ZX Z ZX ZX I X Z Z I X ZX Z ZX Z ZX X I Z ZX ZX X X ZX I ZX I ZX X X ZX" \
          " ZX ZX Z ZX Z Z I X ZX I ZX I Z ZX ZX ZX Z Z I X ZX Z X X Z Z I X Z ZX X I Z Z I I ZX Z X I ZX X X ZX Z Z X" \
          " X Z Z I I ZX X Z X Z Z I X ZX Z ZX Z ZX X I Z ZX X Z I ZX X Z I Z Z I I ZX X X ZX ZX I ZX I ZX Z ZX Z ZX Z " \
          "X I Z Z X X ZX I ZX I ZX X I Z ZX X X Z Z Z I X Z ZX I X Z ZX Z ZX ZX X I Z Z Z X X ZX X I Z ZX Z ZX Z ZX X" \
          " I Z ZX X ZX I Z Z I X Z Z X X ZX X I ZX Z Z I X Z Z X X Z ZX Z ZX ZX Z X I ZX X X ZX Z ZX ZX Z ZX X Z I ZX " \
          "I ZX I Z Z X I Z Z I X Z Z X X Z Z Z Z ZX X I ZX Z Z I X ZX Z ZX Z ZX X ZX X ZX Z X I Z ZX ZX Z Z ZX ZX Z " \
          "ZX I ZX I ZX Z ZX Z ZX Z X I ZX X ZX I Z Z I X ZX Z Z ZX ZX I ZX I Z Z X X Z ZX ZX ZX Z Z I X ZX X I Z ZX" \
          " ZX ZX Z Z Z I X ZX I ZX I ZX X X ZX ZX ZX ZX ZX ZX X I Z Z ZX Z ZX ZX X Z I ZX Z X I Z Z X X ZX I ZX I ZX " \
          "X I Z ZX X X Z Z Z I I Z I Z X ZX I ZX X Z X X ZX ZX ZX I X Z X X Z Z X ZX I Z Z I X ZX ZX I I ZX I ZX I Z" \
          " Z X X ZX I Z X ZX ZX I I Z ZX Z Z Z Z I I ZX ZX I I ZX ZX I I Z X ZX I Z Z I I ZX ZX I I ZX ZX X X Z X ZX I" \
          " Z Z I I ZX ZX X X ZX ZX I I Z Z I X ZX X I Z Z ZX Z Z Z Z I I ZX ZX X X ZX ZX X X Z I ZX X Z Z I X ZX ZX ZX" \
          " ZX Z ZX Z ZX ZX X I Z ZX X Z X Z Z I X ZX Z X X Z Z I X Z ZX ZX Z ZX ZX I I ZX X X ZX ZX ZX X X ZX ZX I I Z" \
          " ZX Z Z Z Z I I Z I Z X ZX X I Z ZX ZX ZX ZX Z Z X X ZX ZX I I ZX X X Z Z Z I X ZX Z ZX Z ZX Z X I ZX X ZX X" \
          " ZX X ZX X ZX ZX I I ZX ZX X I Z Z I X X I X I ZX X ZX X ZX I ZX I ZX Z ZX Z ZX ZX I X Z I ZX X Z Z I X Z Z" \
          " X X ZX X I ZX Z Z I X ZX Z X X Z Z I X Z ZX Z ZX ZX ZX I I ZX Z ZX Z ZX ZX I I ZX I ZX I Z Z ZX ZX ZX ZX I" \
          " I Z ZX Z Z Z Z I I Z I Z X ZX X I Z ZX ZX ZX ZX Z Z X X ZX ZX I I ZX X X Z Z Z I X ZX Z ZX Z ZX Z X I ZX X" \
          " ZX X ZX X ZX X ZX ZX I I ZX ZX X I Z Z I X X I Z ZX ZX X I Z ZX Z Z Z Z I ZX X Z X ZX I Z Z I X ZX Z Z ZX " \
          "Z X ZX X Z Z I X Z ZX ZX Z ZX ZX I I ZX X X ZX ZX ZX X X ZX I ZX I ZX X X ZX ZX ZX Z ZX Z Z I X ZX X I Z ZX" \
          " X X ZX ZX X ZX X Z X ZX X Z Z I X ZX X I Z ZX X X ZX ZX ZX I X Z Z I X Z ZX X I Z Z I I ZX Z Z ZX ZX I ZX " \
          "I Z Z X I Z Z I X ZX ZX ZX ZX Z ZX Z ZX ZX X I Z ZX X Z X Z Z I X X I X I ZX X ZX X ZX I ZX I ZX Z ZX Z ZX " \
          "ZX I X Z Z I X Z Z X X ZX X I ZX Z Z I X X I Z ZX ZX X I Z ZX Z Z Z Z X ZX I Z Z I X Z Z I I ZX X X ZX ZX " \
          "ZX X X ZX ZX I I Z ZX Z Z Z Z I X Z Z X X ZX I Z X ZX ZX I X Z Z I X ZX Z X I Z ZX ZX Z Z ZX ZX Z Z Z I I " \
          "ZX X Z I Z ZX I X Z Z X X ZX I ZX I ZX X I Z ZX X X Z Z Z I X ZX X I Z ZX ZX ZX Z Z Z I X X I X I ZX X ZX X " \
          "ZX I ZX I ZX Z ZX Z ZX ZX I X Z Z I X ZX Z X I ZX X X ZX ZX ZX X I Z Z I X X I Z ZX ZX X I Z ZX Z Z Z Z Z I" \
          " X Z ZX I X Z ZX Z ZX ZX ZX I X Z X Z I Z ZX ZX Z ZX I Z X ZX Z X I Z ZX Z ZX ZX I ZX I ZX X X ZX ZX ZX Z ZX" \
          " Z Z I X ZX Z X I ZX X X Z Z Z I X ZX ZX I I ZX X X ZX Z Z X X ZX Z X I ZX X X ZX ZX ZX Z Z ZX X ZX X ZX ZX " \
          "I I ZX ZX X I Z Z I X Z ZX ZX Z Z Z X X ZX Z X I Z Z X X ZX ZX I X Z X X Z Z Z I X I ZX Z I Z X Z I X ZX Z I " \
          "X I X I I X ZX Z Z X X ZX ZX ZX ZX Z Z X Z X Z Z X X Z ZX Z ZX ZX Z X I I Z I Z X X X X X X I I ZX X X ZX I X" \
          " ZX ZX ZX ZX ZX Z I Z I Z X I ZX ZX ZX ZX I X ZX ZX X I ZX ZX X I ZX X X ZX ZX ZX Z Z I Z I Z X X Z Z X I X I" \
          " X ZX X ZX X X Z Z Z I Z"
messageDigest = message.split(" ")

X = numpy.array([[0, 1], [1, 0]])
I = numpy.array([[1, 0], [0, 1]])
Z = numpy.array([[1, 0], [0, -1]])
ZX = numpy.dot(Z, X)
H =  numpy.array([[1, 1], [1, -1]])
CNOT = numpy.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

XI = numpy.kron(X, I)
II = numpy.kron(I, I)
ZI = numpy.kron(Z, I)
ZXI = numpy.kron(ZX, I)
HI = numpy.kron(H, I)

init1 = numpy.array([1, 0, 0, 0])
init2 = numpy.array([0, 0, 0, 1])

initial = (1 / 2 ** (1 / 2) * (init1 + init2))
digest = ""
for m in messageDigest:
    if m == "I":
        init1 = numpy.transpose(numpy.dot(init1,II))
        init2 = numpy.transpose(numpy.dot(init2,II))
    elif m == "X":
        init1 = numpy.transpose(numpy.dot(init1,XI))
        init2 = numpy.transpose(numpy.dot(init2,XI))
    elif m == "Z":
        init1 = numpy.transpose(numpy.dot(init1,ZI))
        init2 = numpy.transpose(numpy.dot(init2,ZI))
    elif m == "ZX":
        init1 = numpy.transpose(numpy.dot(init1,ZXI))
        init2 = numpy.transpose(numpy.dot(init2,ZXI))
    else:
        print("Unknown Op: {0}".format(m))

    dig1 = numpy.transpose(numpy.dot( init1,CNOT))
    dig2 = numpy.transpose(numpy.dot(init2, CNOT))
    dig1 = numpy.transpose(numpy.dot(dig1,HI))
    dig2 = numpy.transpose(numpy.dot(dig2,HI))
    dig = dig1 + dig2
    if dig[0] != 0:
        digest += "00"
    elif dig[1] != 0:
        digest += "01"
    elif dig[2] != 0:
        digest += "10"
    elif dig[3] != 0:
        digest += "11"
print(digest)
