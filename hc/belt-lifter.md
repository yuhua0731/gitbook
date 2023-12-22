# 🛗 belt-lifter

{% embed url="http://10.0.2.251/embedded/belt-lifter" %}
代码仓库
{% endembed %}

## Install dependencies

* cmake

## Generate Makefile and compile

```sh
> cmake .
-- The C compiler identification is AppleClang 13.1.6.13160021
-- The CXX compiler identification is AppleClang 13.1.6.13160021
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/huayu/hcrobot/gitlab/belt-lifter
> make
[  5%] Building C object CMakeFiles/belt-lifter.dir/src/belt-lifter.c.o
/Users/huayu/hcrobot/gitlab/belt-lifter/src/belt-lifter.c:331:1: warning: non-void function does not return a value [-Wreturn-type]
}
^
1 warning generated.
[ 11%] Building C object CMakeFiles/belt-lifter.dir/src/canopen_motor_base.c.o
[ 16%] Building C object CMakeFiles/belt-lifter.dir/src/canopen_tpdo_data_parser.c.o
[ 22%] Building C object CMakeFiles/belt-lifter.dir/src/global_shared_data.c.o
[ 27%] Linking C shared library libbelt-lifter.dylib
[ 27%] Built target belt-lifter
[ 33%] Building C object CMakeFiles/belt-lifter-static.dir/src/belt-lifter.c.o
/Users/huayu/hcrobot/gitlab/belt-lifter/src/belt-lifter.c:331:1: warning: non-void function does not return a value [-Wreturn-type]
}
^
1 warning generated.
[ 38%] Building C object CMakeFiles/belt-lifter-static.dir/src/canopen_motor_base.c.o
[ 44%] Building C object CMakeFiles/belt-lifter-static.dir/src/canopen_tpdo_data_parser.c.o
[ 50%] Building C object CMakeFiles/belt-lifter-static.dir/src/global_shared_data.c.o
[ 55%] Linking C static library libbelt-lifter-static.a
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: libbelt-lifter-static.a(canopen_motor_base.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: libbelt-lifter-static.a(canopen_tpdo_data_parser.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: libbelt-lifter-static.a(canopen_motor_base.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: libbelt-lifter-static.a(canopen_tpdo_data_parser.c.o) has no symbols
[ 55%] Built target belt-lifter-static
[ 61%] Building C object CMakeFiles/test_c_api.elf.dir/test/test_c_api.c.o
[ 66%] Linking C executable test_c_api.elf
[ 66%] Built target test_c_api.elf
[ 72%] Building C object CMakeFiles/test_relative_step.elf.dir/test/test_relative_step.c.o
[ 77%] Linking C executable test_relative_step.elf
[ 77%] Built target test_relative_step.elf
[ 83%] Building C object CMakeFiles/test_lift_3_steps.elf.dir/test/test_lift_3_steps.c.o
[ 88%] Linking C executable test_lift_3_steps.elf
[ 88%] Built target test_lift_3_steps.elf
[ 94%] Building C object CMakeFiles/test_c_api_sdo_retry.elf.dir/test/test_c_api_sdo_retry.c.o
[100%] Linking C executable test_c_api_sdo_retry.elf
[100%] Built target test_c_api_sdo_retry.elf
~/hcrobot/gitlab/belt-lifter relative-pos..safty-sensor *1 ?3 >   
```
