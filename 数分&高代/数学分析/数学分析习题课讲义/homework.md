# 《数学分析习题课讲义》练习题

## Chapter1  引论

#### 1.3 几个常用的初等不等式

1、

（1）仿照书P3$(1.1)$即可得，1移左边，因式分解

（2）右式为左式多项式展开的第三项，显然成立

（3）因为同号，直接数学归纳法即可

2、

（1）平均值不等式中令$a_i=i$，即得结论

（2）欲证式两边平方，结合平均值不等式，只需证$\sum_{1}^{n}((n+1)-i)\times i< \frac{n(n+2)^2}{6}$，易得

（3）第二问的范围更紧确

（4）原式即$n\sqrt[n]{\prod_1^ni^r}\le\sum_1^ni^r$,显然

3、

显然有$\sum\frac{1}{a_i}\ge\frac{n}{\sqrt[n]{\prod a_i}}$，此即为结论

4、

左小于号：平方后几何不等式   右小于号：平方后显然

5、

（1）分类讨论后显然

（2）右小于号显然，又问部分反例$0,-1,1$

​          左小于号：$左\le\left|a_1\right|-\left|\sum_2^n a_k\right|\le\left|a_1+\sum_2^n a_k\right|=右$

（3）展开之后结论显然

（4）分类讨论后显然

6、

（1）归纳后式子为$b_n^2\sum_1^{n-1}a_i^2+a_n^2\sum_1^{n-1}b_i^2\ge2a_nb_n(\sum_1^{n-1}a_ib_i)$，用基本不等式则显然成立

（2）拉格朗日不等式说明左端大于0，结论显然

（3）$\overrightarrow{A}=(a_1,a_2,\cdots,a_n),\overrightarrow{B}=(b_1,b_2,\cdots,b_n)$，结论显然

（4）代入得$(\sum a_i^2-\sum b_i^2)^2+(2\sum a_ib_i)^2\le(\sum a_i^2+\sum b_i^2)^2$，化简即得

7、

向前：对$n=2^{k+1}$
$$
\frac{\prod_{i=1}^{2^{k+1}}x_i}{\prod_{i=1}^{2^{k+1}}(1-x_i)}=\frac{\prod_{i=1}^{2^k}x_i}{\prod_{i=1}^{2^k}(1-x_i)}\cdot \frac{\prod_{i=2^k+1}^{2^{k+1}}x_i}{\prod_{i=2^k+1}^{2^{k+1}}(1-x_i)}\le \frac{(\sum_{i=1}^{2^k}x_i)^{2^k}}{[\sum_{i=1}^{2^k}(1-x_i)]^{2^k}}\cdot \frac{(\sum_{i=2^k+1}^{2^{k+1}}x_i)^{2^k}}{[\sum_{i=2^k+1}^{2^{k+1}}(1-x_i)]^{2^k}}
$$
则问题为即证：
$$
\frac{(\sum_{i=1}^{2^k}x_i)^{2^k}}{[\sum_{i=1}^{2^k}(1-x_i)]^{2^k}}\cdot \frac{(\sum_{i=2^k+1}^{2^{k+1}}x_i)^{2^k}}{[\sum_{i=2^k+1}^{2^{k+1}}(1-x_i)]^{2^k}}\le \frac{(\sum_{i=1}^{2^{k+1}}x_i)^{2^{k+1}}}{[\sum_{i=1}^{2^{k+1}}(1-x_i)]^{2^{k+1}}}
$$
令$S_1 =\sum_{i=1}^{2^k}x_i,S_2=\sum_{i=2^k+1}^{2^{k+1}}x_i $，上式两边同时开$2^k$次方后即得结果

向后：若对$n=k+1$成立，则将$a_k$平分为两个数，则得到对$n=k$也成立

8、

柯西不等式显然

## Chapter2 数列极限

#### 2.1 数列极限的基本概念

1、

（1）显然

（2）显然

（3）即证$(1+n)<(1+\frac{1}{\varepsilon})^n$，取$N = \frac{1}{3\varepsilon}$，右侧展开到第三项即可

（4）取$N=2a-\log_a^\varepsilon$

2、

显然

3、

正向显然，反向数列可能不收敛，比如$1,-1,1,-1,\cdots$

4、

显然

5、

对$\varepsilon>0$，令$f(x)=\varepsilon x-\log_ax$，易得$f(x)$不恒正，结论得证

#### 2.2 收敛数列的基本性质

1、

充分性：显然

必要性：用无穷小量来证明也很容易

2、

（1）$ans = max(a_1,a_2,\cdots,a_n)$，$\lim < n\sqrt[n]{n\cdot max(a_i)^n }= max(a_i)$，大于号显然，夹逼即得结果

（2）夹逼放缩，结果为2

（3）同样放缩，结果为1

（4）利用$\lim_{n\to\infty}\sqrt[n]{n}=1$即可

3、

（1）展开即得$ans = \sum_0^{2^{n+1}-1}x^i=\frac{1-x^{2^{n+1}}}{1-x}$

（2）$ans= \sum_2^n\frac{(i+1)(i-1)}{i^2}=\frac{1}{2}$

（3）$ans= \sum_2^n\frac{(i-1)(i+2)}{i(i+1)}=\frac{1}{3}$

（4）$ans= \sum_1^n\frac{1}{2i}+\frac{1}{2(i+2)}-\frac{1}{i+1}=\frac{1}{4}$

（5）$ans=\sum_1^n\frac{1}{\nu}(\frac{1}{i(i+1)\cdots(i+\nu-1)}-\frac{1}{(i+1)(i+2)\cdots(i+\nu)})=\frac{1}{\nu\cdot\nu!}$

4、

$s_n-as_n=\frac{(a-a^2)(1-a^{n+1})}{1-a}\Rightarrow s_n=\frac{a}{1-a}$

5、

因为正数列收敛，设极限为a，则$\min(min(a_1,\cdots,a_N),a/2)$为其下界，例如数列${1+\frac{1}{n}}$则没有最小值

6、

因为极限无穷大，所以从某一项开始一定大于某个确定常数，则在前面的这些项中存在最小值

7、

显然可得

8、

无界数列发散

9、

由调和级数发散可知结论

#### 2.3 单调数列

1、

显然，反之不成立，比如$a_n=(-1)^n\frac{1}{n}$

2、

不难看出$a_i\le b_1\; b_i \ge a_1$，单调有界则收敛，结合极限得两者收敛于同一值

3、

显然

4、

$x_n$单调递减且为正，收敛于0

5、

同上，收敛于0

6、<font color="red">UNSOLVED</font>



7、

$x_n$正且单减，极限存在，解$x=sinx$得$x=0$，所以极限为0

8、

由提示得数列单减，易得极限为0

9、

10、

（1）显然单调

（2）显然不单调

（3）$\sqrt[n]{n!}\le\sqrt[n+1]{(n+1)!}\Leftrightarrow(n!)^{n+1}\le(n+1)!^n\Leftrightarrow n!\le(n+1)^n$

11、

充分性：显然

必要性：设收敛子列极限为$A$，不妨设子列单减，则对任意$\varepsilon>0$，存在$K$使得对$n>K$有$a_n<A+\varepsilon$，设子列中的第$K$项为原数列中的第$N$项，则由数列单减知符合收敛条件，原数列收敛

12、

显然$x_n$单减，有极限，等比数列求和后不难发现极限为$\frac{1}{2}$

#### 2.4 柯西命题与斯托尔兹定理

1、<font color="red">UNSOLVED</font>



2、

若发散，则题式极限不可能为a，则收敛，设极限为b，则有前面的过程易得b=a

3、

$ans=\frac{a+b}{2}$

4、

用$\varepsilon$证明易得

5、

显然易得

6、

显然易得

7、

则$a_{2k+1}=a_1+k\varepsilon,a_{2k+2}=a_2+k\varepsilon$，易得

8、

同上构造，易得

9、

易得$\{a_n\}$ 单减，所以有极限，解得

10、

对$\varepsilon >0$，存在$N$，使得对$n>N$，有$\left|a_n-\alpha\right|<\varepsilon,\left|b_n-\beta\right|<\varepsilon$

将原式分为$\frac{1}{n}[(a_1b_n+\cdots+a_Nb_{n+1-N})+(a_{N+1}b_{n-N}+\cdots+a_{n-N}b_{N+1})+(a_{n+1-N}b_N+\cdots+a_nb_1)]$

则有上式小于$\frac1n[2N\times M+n(\alpha\beta+(\alpha+\beta)\varepsilon+\varepsilon^2)]$，其中$M$是上式第一项和第三项元素中的最大值

因为$\varepsilon $任意，所以极限即为$\alpha\beta$

#### 2.5 自然底数和欧拉常数

1、

（1）$ans = e^{-1}$

（2）$ans=\sqrt{e}$

（3）$ans=e^2$

（4）$ans=\infty$

（5）$ans=1$

（6）$ans=e$

2、

右不等号显然，左不等号两边取自然底数的指数得$e<(1+\frac{k}{n})^{\frac{n}{k}+1}$，此式子在书P39有类似的

3、

需求式去对数，结合$\ln(1+x)=x,x\to0$得$ans = \sqrt{e}$ 

4、

$ans=e$

5、

结合$\lim\frac{n}{\sqrt[n]{n!}}=e$ 得$ans=0$

6、

运用斯托尔兹公式得$ans=1$

7、

该式子显然对$n=1$成立

假设对$n=k-1$成立，则当$n=k$时

左侧乘以$\frac ke(1+\frac1k)^k$，中间乘以$k$，右侧乘以$\frac ke(1+\frac1k)^{k+1}$，由此可得结论成立

8、<font color="red">UNSOLVED</font>



9、

递推关系可得 $a_n=\sum_{i=1}^n\frac{n^!}{i!};\lim_{n\to\infty}a_n=n!(e-1);\ln x_n=\sum_{i=1}^n\frac{1}{a_n}=\frac{1}{(e-1)}\sum_{i=1}^n\frac{1}{i!}=1$

$ans=e$

#### 2.6 由迭代生成的数列

1、

（1）显然$x_{n}$单增，设极限为$X$，题式两边取极限得$X=\sqrt{a+X}$，由正数列解得$ans=\frac{1+\sqrt{1+4a}}{2}$

（2）同上过程得$ans=a$

2、

由P51不动点推论得结论显然

3、

不难发现有$x_2>1,x_3<0$，对$n\ge3$有$\frac{a_{n+1}}{a_n}=b(1-x_n)\ge4$，则结论显然

4、

$b\in[-1,1],ans=1$

5、

$x_n=\frac{1-b^{n+1}}{1-b}+(a-1)b^n=\frac{1}{1-b}+[\frac{b}{b-1}+(a-1)]b^n，\{a\in\mathbb{R},b\in(-1,1)\}\or\{b=\mathbb{R}-\{1\},a=\frac{1}{1-b}\}$

6、

$x_{n+1}=a^nx_1+b(1+a+\cdots+a^{n-1})$

$if(a==1)\;x_n=x_1+b(n-1);else \;\;x_n=a^{n-1}x_1+b(\frac{1-a^{n-1}}{1-a})=\frac{b}{1-a}+a^{n-1}(x_1-\frac{b}{1-a})$

（1）$\{a\in(-1,1)\}\or\{a=1,b=0\}$

（2）$\{a\in(-\infty,-1)\cup(1,+\infty)\}\or\{a=1,b\ne0\}$

（3）$\{a=1,b=0\}$

（4）$a=-1$，若$x_1=\frac{b}{2}$则收敛，否则发散

7、

若$x_1<1$，则有$x_{n+1}-1<\frac{1}{x_n}(x_n-1)$，易得$\{x_n-1\}$不收敛，所以$\{x_n\}$不收敛，又显然有$x_n\ne1$

对$x_1>1$，易得数列单减有下界，然后易得极限为1

8、

由P51不动点推论得结论显然

9、

由P51不动点推论得结论显然

## Chapter3 实数系的基本定理

#### 3.1 确界的概念和确界存在定理

1、

假设不唯一，不妨设上确界不唯一，不妨设有两个上确界$a,b$且$a<b$，则易得$b$不可能为上确界，得证

2、

有可能$\sup A=a$，后者正确

3、

$\forall \varepsilon>0,\exists k\in\mathbb{R}\;\;a_k>b-\varepsilon$，所以$b$即是$A$的上确界

4、

（1）$\sup==+\infty,\inf=0$

（2）$\sup=1,\inf=0$

（3）$\sup=e,\inf=2$

（4）$\sup=e^-1,\inf=0$

（5）$\sup=\frac\pi2,\inf=-\frac\pi2$

（6）$\sup=1,\inf=-1$

（7）$\sup=+\infty,\inf=-\infty$

5、

（1）$\forall k\in\mathbb{R},x_k+b_k\le \max(x_n)+max(y_n)\le \sup\{x_n\}+\sup\{y_n\}$，得证

（2）同上类似得

6、$\forall x\in A,\forall y\in B,x\le y \Rightarrow \forall y \in B,\sup A\le y \Rightarrow \sup A \le \inf B$

7、

结论显然

8、

$A=\{1\},B=\{2\}$

9、

同上

#### 3.2 闭区间套定理

1、

2、

3、

4、

5、

#### 3.3 凝聚定理

1、

2、

3、

4、

#### 3.4 柯西收敛准则

1、

（1）是，此为定义的另一种写法

（2）不一定是，$x_n=\frac{1}{2n}$

（3）$\left|x_{n+2}-x_n\right|\le \frac{2}{n^2},\left|x_{n+2}-x_n\right|\le\left|x_{n+2}-x_{n+1}\right|+\left|x_{n+1}-x_n\right|\le \frac{1}{n^2}+\frac{1}{(n+1)^2}$

由此发现$p=1$是比$p=2$更强的一个结论，所以只需考虑$p=1$，不难得到为基本数列

（4）此命题比上面更强，所以是基本数列

2、

$\exist \varepsilon>0,\forall N\in \mathbb{R},\exists n,m>N,\left|a_m-a_n\right|<\varepsilon$

3、

（1）$\forall \varepsilon>0,\exists N,s.t.\varepsilon>\frac{1}{N!},\forall m,n>N,\left|a_m-a_n\right|\le\sum_{i=N+1}^\infty\frac{1}{i!}\le\frac{2}{(N+1)!}<\varepsilon$

（2）同1.3易得

（3）同上易得

4、

（1）显然$a_n$每项有正有负

（2）同3.1易得

5、

显然

6、

仿照例题易得

7、

不难得到压缩率为q，不动点即为解

#### 3.5 覆盖定理

1、

$O_i=(\frac{1}{2^i},1)$

2、

3、

4、

5、

#### 3.6 数列的上极限和下极限

1、

（1）$\lim\sup x_n=1,\lim \inf x_n=0$

（2）$\lim\sup x_n=1,\lim \inf x_n=-1$

（3）$\lim\sup x_n=+\infty,\lim \inf x_n=-\infty$

（4）$\lim\sup x_n=+\infty,\lim \inf x_n=0$

2、

显然

3、

4、

5、

6、

7、

8、

9、

10、

11、

## Chapter4 函数极限

#### 4.1 函数极限的定义

1、

$原=\lim_{x\to0}\frac{2}{\sqrt{1+x}+\sqrt{1-x}}$，对$\forall \varepsilon>0$，取$\delta<1-\frac1{(1+\varepsilon)^2}$，即有对$\forall x\in O_\delta(0),\frac{2}{\sqrt{1+x}+\sqrt{1-x}}<\frac{1}{\sqrt{1-\delta}}<1+\varepsilon$

2、

同上类似得

3、

同上类似得

4、

显然分子上是无穷小量，所以$a=4，ans = 10$

5、

不难得到$x^2+ax+b=(x-2)(x+4)\Rightarrow a =2,b=-8$

6、

$a\in(-1,1)$

7、

$\forall \varepsilon > 0,\exists \delta = a\varepsilon,\forall x\in O_\delta(a)-\{a\},s.t.\left|\ln x-\ln a\right|<\varepsilon$

8、

同上过程可得

9、

由定义可得结论显然

10、

比如下面的函数就不一定存在性相同
$$
f(x)=\begin{cases}
  x + 1& x < 0\\
  x & x \ge 0
\end{cases}
$$
11、

用4.2知识显然

12、

迪利克雷函数将1改为x，再平移

13、

显然

14、

#### 4.2 函数极限的基本性质

1、

（1）

（2）

（3）

（4）

2、

$ans=1$

3、

$ans=1$

4、

$ans=0$

5、

$ans=bl$

6、

显然

7、

类似数列

8、

显然

9、

显然

10、

显然

11、

#### 4.3 两个重要极限

1、

（1）利用$\arctan x + \arctan \frac{1}{x} = \frac\pi2$得$ans=e^{-\frac2\pi}$

（2）$原=\lim_{x\to0^+}(\cos x)^\frac{\cos x}{\sin x}=\lim_{x\to0^+}(1-\frac{x^2}{2})^\frac1x=1$

（3）$ans=e^2$

（4）等价于$\lim_{x\to 0}x^x=1$

（5）$ans=-1$

（6）$ans=\frac2\pi$

2、

（1）$ans=0$

（2）$ans=1$

3、

$原=\lim_{x\to 0}(\frac{a^x+b^x}{2})^\frac1x=\lim_{x\to 0}(1+\frac{a^x-1+b^x-1}{2})^\frac1x=\lim_{x\to 0}(1+x(\frac{\ln ab} 2))^\frac1x=\sqrt{ab}$

4、

$ans=\sqrt[n]{a_1a_2\cdots a_n}$

5、

由二倍角公式易得$ans=\sin x$

#### 4.4 无穷小量、有界量、无穷大量和阶的比较

1、

（1）$ans=3$

（2）$ans=1$

（3）$ans=1$

（4）$ans=2$

（5）$ans=1$

（6）$ans=$

2、

显然

3、

显然

4、

（1）$ans=1$

（2）$ans=-1$

（3）$ans=\frac32$

（4）$ans=-\frac{1}{12}$

（5）$ans=\frac23$

（6）$ans=e^{\frac16}$

## Chapter5 连续函数

#### 5.1 连续性概念

1、

（1）$\exists \varepsilon>0,\forall \delta>0,\exists x\in O_\delta(a),\left|f(x)-f(a)\right|>\varepsilon$；$\exists \{x_n\},s.t.\lim_{n\to\infty}x_n=a,\lim_{x\to\infty}\ne f(a)$

（2）柯西收敛准则易得

2、

（1）每个整数都是间断点，第一类

（2）连续点

（3）每个整数都是间断点，第一类

（4）$x=-1$第二类，其余第一类

3、

由闭区间得结论显然

4、

仿照P125例题即得成立

5、

根据题所给公式，由连续函数的加性可得结论成立

6、

显然

7、

显然

8、

其处处不连续，可见连续性第二种证明，左右也都没有极限

9、

将迪利克雷函数的$1$变为$x$，其在$x=0$处连续，其余不连续

10、

仿照练习5.5.2，方法类似

11、

和上方法类似

12、

用连续的第二种证明方法可得

#### 5.2 零点存在定理和介值定理

1、

易得$\min\{f(x_i)\}\le f(\xi)\le \max\{f(x_i)\}$，由介质定理易得结论成立

2、

将其变换为关于角度的函数，不难发现其为一个连续周期函数，而其在一个周期里不可能单调，易得结论成立（利用最值即可）

3、

易得$x=\frac{2k\pi}{n}$时$f(x)>0$，$x=\frac{(2k+1)\pi}{n}$时$f(x)<0$，可见结论成立

4、

显然

5、

（1）$f(-\infty)=-\infty,f(+\infty)=+\infty$，由此得结论显然

（2）$f(-\infty)=+\infty,f(+\infty)=+\infty,f(0)<0$，由此得结论显然

6、

同上面5（1）

7、

其为常值函数

8、

（1）显然（一对一映射-单射）

（2）显然

9、

显然

10、



#### 5.3 有界性定理和最值定理

1、

则将其根据其间断点分成一个个连续函数，其依次有界，所以整体有界

2、

将其分为一个闭区间和一个极限区间，则结论显然

3、

4、

不一定

5、

设$\lim_{x\to\infty}f(x)=A$，$\forall \varepsilon>0, \exists N,\forall x > N ,f(x)\in(A-\varepsilon,A+\varepsilon)$，如果$\forall x\in[a,N],f(x)\in (A-\varepsilon,A+\varepsilon)$，则可得出其为常值函数，否则一定有最大值或者最小值

6、

$\forall y, \exists\;\delta_1,\delta_2,s.t. \forall x_1\in(a,a+\delta_1),x_2\in(b-\delta_2,b)\;\;f(x_1)>y,f(x_2)>y$

令$y$大到大于中间区间的最大值，即得证明

7、

与上类似

8、

零点存在定理易得

9、



#### 5.4 一致连续性和康托尔定理

1、

取$\delta=\frac\varepsilon L$即满足要求

2、

不难得到$f((a,b))\sub[f(b^-)-(b-a)\frac\varepsilon\delta,f(a^+)+(b-a)\frac\varepsilon\delta]$

3、

（1）线性组合一致连续，乘积不一定，反例$f(x)=g(x)=x$

（2）不一定，反例同（1）

4、

连续周期函数有界，其在其周期的闭区间上一致连续，得其在定义域上一直连续

5、

（1）将其分为两个区间，一个左闭右开区间由极限得成立，另一个由闭区间得成立

（2）二次方不成立

（3）$g(x)$需要一致连续

6、

易证

7、

易证

8、

（1）取$f(0^+),f(0^-)$即得结论

（2）不一定，同上取$b$为间断点即得

9、

（1）不一致

（2）不一致

（3）不一致

#### 5.5 单调函数

1、

设$\delta=\inf\{\left|O(x)\right|\},x\in(a,b)$，则对$\forall x',x''\in(a,b)$，构造以$x',x''$为第一项和最后一项的数列，在其中插入一些项使得数列的最大间隔为$\frac\delta2$，这样不难看出对数列的任意相邻两项都有前一项小于后一项，那么就有$f(x')<f(x'')$

2、

假设不成立，则必然存在无理数$ir$和有理数$r$，使得$ir>r,f(ir)<f(r)$（等价性由分类讨论和对称易得）,假设这样的数存在，则由$r$和$ir$之间存在无穷多个有理数可得，为使满足假设和题意，对所有的$r'\in\mathbb{Q}$，都有$f(r')>f(r)$，则令这样的有理数按从小到大构成数列$\{r_n\}$，则有此数列极限为$ir$，而$\lim_{n\to\infty}f(r_n)\ge f(r)>f(ir)$，矛盾

3、

$\lim_{x\to a^+}g(x)=\lim_{x\to a^+}f(x^+)=f(x^+)=g(x)$

4、

易得对所有整数有$f(x)=f(1)x$，然后易得有理数也有此结论，利用单调性和上面第二题过程易得对无理数也有此结论

## Chapter6 导数与微分

#### 6.1 导数及其计算

1、

显然

2、

$f'(0)=0$

3、

$a=\frac{1}{2e}$

4、

相切即导数相同，结论显然

5、

易得交点为$x=\frac\pi2+k\pi$，则结论显然

6、

$p(x)=\sum(x-x_i)^{n_i},p'(x)=\sum n_i(x-x_i)^{n_i-1}$，由此易证

7、

处处可导

8、

（1）一定连续

（2）n不为1

（3）n不为1，2

9、

$f'(0)=1\Rightarrow f(\Delta x)=1+ \Delta x+o(\Delta x);f'(x_0)=\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}=\frac{f(x_0)(f(\Delta x)-1)}{\Delta x}=f(x_0)$

10、

$f(x)$在0处连续，其余不连续，不可导

$g(x)$在0处可导，其余不连续，不可导

11、

$f'(0)=1$

12、

$f'(0)=0$

#### 6.2 高阶导数及其他求导法则

1、

$y'(1+x^2)=1\Rightarrow y''(1+x^2)+2xy'=0\Rightarrow (1+x^2)y^{(n+2)}+2x(1+n)y^{(n+1)}+n(n+1)y^{(n)}=0$

$y^{(2k+1)}(0)=(2k)!,y^{(2k)}(0)=0$

2、

3、

4、

5、

6、

7、

8、

9、

10、

11、

12、

13、

14、

设$f(x)+1=q(x)(x-1)^4$，则$f'(x)=(4q(x)-(x-1)q(x))(x-1)^3$，即$(x-1)^3|f'(x)$，同理有$(x+1)^3|f'(x)$，结合7次多项式得$f(x)=-x(x-1)^3(x+1)^3$

#### 6.3 一阶微分及其形式不变性

## Chapter7 微分学的基本定理

#### 7.1 微分学中值定理

1、

（1）令$f(x)=ax^2+bx+c-e^x$，若$f(x)=0$有四个不相同的根，则$f'(x)=2ax+b-e^x=0$有三不同解，由单调性易得矛盾

（2）令$f(x)=4ax^3+3bx^2+2cx-a-b-c,F(x)=ax^4+bx^3+cx^2-(a+b+c)x$，则$F(0)=F(1)=0$，罗尔定理得结论成立

（3）显然

（4）若有，则$f'(x)=5x^4+4ax^3+3bx^2+2cx+d$有四根，则$f''(x)=20x^3+12ax^2+6bx+2c$有三根，则$f'''(x)=60x^2+24ax+6b$有两根，而$\Delta=24*24a^2-24*60b\le0$，所以不可能

（5）

（6）

2、

$f(x)$在$a$和$b$的邻域内异号，由零点存在定理知$\exists\xi\in(a,b)s.t.f(a)=f(b)=f(\xi)$，再结合罗尔定理得证

3、

令$g(x)=\ln x$，代入柯西中值定理即可

4、

同上令$g(x)=x^2$即得，如果$a=-b$或$f'(0)=0$，取$\xi=0$即满足要求

5、

6、

显然

7、

反证法即可

8、

$f(x+\Delta x)-f(x)=2ax\Delta x+a(\Delta x)^2+b\Delta x$

$f'(x+\theta\Delta x)\Delta x=2ax\Delta x+2\theta a(\Delta x)^2+b\Delta x$

9、

发现$2\sqrt{x+\theta x}=\sqrt{x+1}+\sqrt{x}$

10、

11、

显然

12、

求导证明即可

13、

$f(x)=ax+b$

14、

若有界，积分则得矛盾

15、

16、

显然

17、

18、

19、

（1）显然

（2）

20、

显然

#### 7.2 泰勒定理

## Chapter8 微分学的应用

#### 8.1 函数极限的计算

1、

（1）不满足形状

（2）洛后极限不存在

（3）死循环

（4）死循环

2、

（1）

洛后，$原=\frac{2x(a^{x^2}\ln a-b^{x^2}\ln b)}{2(a^x\ln a-b^x\ln b)(a^x-b^x)}=0$