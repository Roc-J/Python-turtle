def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
result = square(toSquare)
print "The result of",toSquare,"squared is",result

