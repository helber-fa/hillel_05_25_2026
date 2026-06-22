def count_h(word):
    return word.count("h")

print(id(count_h))

new_fn = count_h

print(count_h("hello"))
print(new_fn("hhello"))
print(type(new_fn))
print(id(new_fn))

print(max([1,2,3,4]))
print(max(["hhh", "hello", ''], key=count_h))
print(max(["hhh", "hello", ''], key=lambda x:x.count("h")))
new_lambda = lambda x,y:pow(x,y)
print(new_lambda(2,5))