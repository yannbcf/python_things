Build assembly executable using nasm:
```
nasm -f win64 main.asm -o main.obj

(link is MSVC link.exe tool)
link main.obj /subsystem:console /entry:_start /out:main.exe /libpath:"optional/path/to/libs" kernel32.lib
```

Build c executable using clang
```
clang main.c -o main.exe
```

Both executables do the same thing, we can see that even a very low level language hides a lot of the inner workings of a computer
