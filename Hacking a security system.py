"""There is a security system where there is a main_lock and a main_key and a code for each lock_x. A hacker
got the main_lock and the main_key but does not know what the code is. Write a code to find the number of attempts
it will take him to unlock the lock_x. The code%lock=key for every lock. If a lock has been accessed 10 times with
the wrong key the lock is changed to lock+main_key. The function hack contains a main_key, main_lock and lock_x
(whose key_x is to be found by the hacker to access the data). The function hack(main_key, main_lock, lock_x) returns
the number of attempts it takes the hacker to find key_x and if not possible returns 'system with high level of
security.'
Examples:
hack(1,2,8)=4
hack(1,2,13)=17
hack(5,101,111)=996
hack(10,101,111)=system with high level of security"""


def hack(main_key, main_lock, lock_x):
    code = main_lock + main_key
    attempts = 0
    i = 1
    while i <= 1000:
        while attempts < 10*i:
            if code % lock_x == main_key:
                attempts += 1
                return attempts
            else:
                attempts += 1
                code += main_lock
        else:
            lock_x += main_key
            i += 1
            code = main_lock + main_key
    else:
        return 'security system with high level of security'


print(hack(10, 101, 111))
