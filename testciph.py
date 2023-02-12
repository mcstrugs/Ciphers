#!/usr/bin/env python3

from Code import *

print(toNum("abc def"))

a = Code("abc xyz")
a.add(1)
print(a.code)
a.print()
a.add_code(Code("aaa"))
a.print()
a.add_code(Code("zzzzzzz"))
a.print()
print(type(a))
a.append(Code("xyz"))
a.print()