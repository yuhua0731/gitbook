---
description: OmniSort分拣系统供包机
---

# ✨ SPF-Sort\_Packet\_Feeder

{% embed url="https://gitlab.hcrobots.com/embedded/SPF-Sort_Packet_Feeder" %}
供包机代码仓库
{% endembed %}

{% embed url="https://gitlab.hcrobots.com/embedded-tool/arm-linux-gnueabihf" %}
编译工具
{% endembed %}

```bash
# install dependencies
sudo apt install cmake autoconf automake
# clone arm-linux-gnueabihf from gitlab
git clone git@10.0.1.250:embedded/arm-linux-gnueabihf.git
# update PATH
vi /etc/profile
# append export PATH=$PATH:<your arm-linux-gnueabihf path>/bin at the end
source /etc/profile

# now you can run ./1CommandBuild.ARM.335x.sh
./1CommandBuild.ARM.335x.sh
```

## [Reference](https://stackoverflow.com/questions/2531827/what-are-makefile-am-and-makefile-in)

`Makefile.am` is a programmer-defined file and is used by `automake` to generate the `Makefile.in` file (the `.am` stands for **a**uto**m**ake). The `configure` script typically seen in source tarballs will use the `Makefile.in` to generate a `Makefile`.

The [`configure script`](https://en.wikipedia.org/wiki/Configure\_script) itself is generated from a programmer-defined file named either `configure.ac` or `configure.in` (deprecated). I prefer `.ac` (for **a**uto**c**onf) since it differentiates it from the generated `Makefile.in` files and that way I can have rules such as `make dist-clean` which runs `rm -f *.in`. Since it is a generated file, it is not typically stored in a revision system such as Git, SVN, Mercurial or CVS, rather the `.ac` file would be.

Read more on [GNU Autotools](https://en.wikipedia.org/wiki/GNU\_build\_system). Read about [`make`](https://en.wikipedia.org/wiki/Make\_\(software\)) and [`Makefile`](https://en.wikipedia.org/wiki/Makefile) first, then learn about [`automake`](https://en.wikipedia.org/wiki/Automake), [`autoconf`](https://en.wikipedia.org/wiki/Autoconf), [`libtool`](https://en.wikipedia.org/wiki/GNU\_Libtool), etc.
