sequence_length = 10
degree = 4
a = (degree ** i for i in range(1, sequence_length + 1))
print(type(a), tuple(a))


#############################################################################

def geom_progress(sequence_length, degree):
    for i in range(1, sequence_length + 1):
        yield degree ** i


b = geom_progress(10, 3)
print(type(b), list(b))
