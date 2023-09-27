import turtle as t
t.color('blue')
t.fillcolor('red')
t.begin_fill()
while True:
    t.forward(100)
    #t.dot()
    t.left(270)
    if abs(t.pos()) < 1:
        break
t.end_fill()