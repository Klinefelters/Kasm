int c = 0;
str s = 'Hello World';
lst l = [1, 2, 3, 4, 5];

while (c < 10) {
    printf(s);
    c = c ++;
}

for (int i = 0; i < 5; i++) {
    printf(l[i]);
}

if (c == 10) {
    printf('Goodbye World');
    c = c--;
} else if (c < 10) {
    printf('ERROR - c is less than 10');
} else {
    printf('ERROR - c is greater than 10');
}

loop{
    printf('This is an infinite loop');
}

def add(a, b) {
    return a + b;
}