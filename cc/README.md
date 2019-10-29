# C++

## Supported environments
- C++ 14, C++ 17
- OS: Ubuntu 16.04, Ubuntu 18.04, macOS X Mojave 10.14

## Run
```
g++ -std=c++17 main.cc wc.cc -I . -o main
./main
```

## Test
```
g++ -std=c++17 test_wc.cc wc.cc -I . -l gmock -l gtest -l gtest_main -o test
./test
```
