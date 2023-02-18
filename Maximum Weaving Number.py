"""Maximum Weaving Number
Given two numbers A=a1a2...an and B= b1b2...Bm, we can weave these two numbers to produce the following numbers.

a1b1a2b2...anbnb(n+1)...bm,, if m>n

a1b1a2b2...ambma(m+1)...an if m<n

a1b1a2b2...anbn if m=n.

Similarly, we can also get b1a1b2a2.... as above.

We can also start weaving from the end. By weaving from the end, we can form the words: anbnb(n-1)a(n-1)... ,
bnanb(n-1)a(n-1)...

Thus, by weaving A and B, four new numbers are formed: weaving from the beginning, starting with A, weaving from
the beginning, starting with B, weaving from the end, starting with A, weaving from the end, starting with B.
While weaving two numbers A and B, if all the digits of A are weaved and some more digits are there in B,
the remaining digits of B are just appended at the end. For example, if A = 27 and B = 54 then there are four
numbers that can be woven

2574

5247

7425

4752

and maximum out of these is 7425

Given two numbers A and B, write a code to compute the numbers woven by A &B and find the maximum woven number."""


a = input('Enter the first number : ')
b = input('Enter the second number to weave the first one with : ')
numbers = []
if len(a) > len(b):
    c = b
elif len(a) < len(b):
    c = a
else:
    c = a
num = ''
for i in range(len(c)):
    num += a[i] + b[i]
if c == b:
    num += a[len(c):]
elif len(a) < len(b):
    num += b[len(c):]
numbers.append(int(num))
num = ''
a_rev = a[::-1]
b_rev = b[::-1]
for i in range(len(c)):
    num += a_rev[i] + b_rev[i]
if c == b:
    num += a_rev[len(c):]
elif len(a) < len(b):
    num += b_rev[len(c):]
numbers.append(int(num))
num = ''
for i in range(len(c)):
    num += b[i] + a[i]
if c == b:
    num += a[len(c):]
elif len(a) < len(b):
    num += b[len(c):]
numbers.append(int(num))
num = ''
for i in range(len(c)):
    num += b_rev[i] + a_rev[i]
if c == b:
    num += a_rev[len(c):]
elif len(a) < len(b):
    num += b_rev[len(c):]
numbers.append(int(num))
print(max(numbers))
