def moveTower(height,fromPole, toPole, withPole):

    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)

        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


moveTower(3,"A","B","C")


def hanoi(n, source, target, helper):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, helper, target)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, target, source)


source = [4, 3, 2, 1]
target = []
helper = []
print("Source {}, target {} ,helper {}".format(source,target,helper))
hanoi(len(source), source, target, helper)

print("Source {}, target {} ,helper {}".format(source,target,helper))