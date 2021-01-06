# competitive-programming

This repo has a bunch of personal code snippets related to competitive programming.

C++ code is typically compiled with

```bash
g++ a.cpp -o a.out && ./a.out
```

This can be invoked using the shortcut script `./compile.sh`. An example of copying input from the web and running a test case might be something like.

```
pbpaste | ./compile.sh csesfi/bit-strings.cpp
```

`.cpp` files are initialised with

```cpp
#include <bits/stdc++.h>
#define MODN 1000000007;

using namespace std;

int main() {
    //code here
}
```