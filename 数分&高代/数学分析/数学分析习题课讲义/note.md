# 数学分析习题课讲义

## Chapter1 引论

#### 1.1 关于习题课教案的组织

#### 1.2 书中常用记号

$\mathbb{Q}$:所有有理数所称的集合

$O_\delta(a)$表示以$a$为中心，以$\delta$为半径的邻域，即开区间$(a-\delta,a+\delta)$，如不必写出半径，可简记为$O(a)$（O可替换成U）

#### 1.3 几个常用的初等不等式

伯努利不等式：$(1+h)^n\ge1+nh\;\;\{h>-1,n\in\mathbb{N}_+\}$

平均值不等式：$\frac{a_1+a_2+\cdots+a_n}{n}\ge\sqrt[n]{a_1a_2\cdots a_n}$

柯西不等式：$(a_1^2+a_2^2+\cdots+a_n^2)(b_1^2+b_2^2+\cdots+b_n^2)\ge(a_1b_1+a_2b_2+\cdots+a_nb_n)^2$

#### 1.4 逻辑符号与对偶法则

## Chapter2 数列极限

#### 2.1 数列极限的基本概念

数列$\{a_n\}$收敛于$a$的定义是：$\forall \varepsilon>0,\exists N\in \mathbb{N}_+,\forall n>N$，成立$\left|a_n-a\right|<\varepsilon$

子列：给定数列$\{a_n\}$，从中任意选取无限项，按原来的顺序组成的数列称为$\{a_n\}$的一个子列

#### 2.2 收敛数列的基本性质

判定数列发散的方法：1、数列无界 2、收敛的对偶定义3、有发散子列4、两子列收敛于不同极限5、柯西收敛准则

#### 2.3 单调数列

单调有界数列一定收敛，单调无界数列一定是具有确定符号的无穷大量

#### 2.4 柯西命题和斯托尔兹定理

柯西命题：设$x_n$收敛于$l$，则它的前项的算术平均值也收敛于$l$，即有
$$
\lim_{n\to\infty}\frac{x_1+x_2+\cdots+x_n}{n}=l
$$
$\frac{0}{0}$型斯托尔兹定理：$\{a_n\}\{b_n\}$都是无穷小量，$\{a_n\}$严格单减数列，则
$$
\lim_{n\to\infty}\frac{b_{n+1}-b_n}{a_{n+1}-a_n}=l\Rightarrow\lim_{n\to\infty}\frac{b_n}{a_n}=l(l=\text{const}\; or \;\infty)
$$
$\frac{*}{\infty}$型斯托尔兹定理：$\{a_n\}$是严格单增无穷大量，则
$$
\lim_{n\to\infty}\frac{b_{n+1}-b_n}{a_{n+1}-a_n}=l\Rightarrow\lim_{n\to\infty}\frac{b_n}{a_n}=l\;\;(l=\text{const}\; or \;\infty)
$$

#### 2.5 自然底数和欧拉常数

自然对数：
$$
e=\lim_{n\to\infty}(1+\frac{1}{n})^n=\sum_{i=0}^\infty\frac{1}{i!}
$$
欧拉常数：
$$
\gamma = \lim_{n\to\infty}1+\frac{1}{2}+\cdots+\frac{1}{n}-\ln n
$$

#### 2.6 由迭代生成的数列

迭代生成的数列即是满足$a_{n+1}=f(a_n)$的数列，其中$f$和$n$无关

设数列$\{x_n\}$满足递推公式$x_{n+1}=f(x_n)$，若有$\lim_{x\to\infty}x_n=\xi,\lim_{x\to\infty}f(x_n)=f(\xi)$，则极限$\xi$一定是方程$f(x)=x$的根，这时称$\xi$为函数$f$的不动点

设数列$\{x_n\}$满足递推公式$x_{n+1}=f(x_n)$，其中的函数$f$在区间$I$上单调，同时数列$\{x_n\}$的每一项都在区间$I$中，则只有两种可能：(1)当单调增加时，$\{x_n\}$为单调数列 (2)当单调减少时，$\{x_n\}$的两个子列$\{x_{2k}\}$和$\{x_{2k-1}\}$分别为单调数列，且具有相反的单调性

设$a$是$f(x)$的不动点，函数$f$在$a$处连续，在点$a$的邻域$(a-r,a+r)$上严格单调增加，并且在区间$(a-r,a)$上有$f(x)>x$，而在区间$(a,a+r)$上有$f(x)<x$，那么迭代产生数列只要第一项在$(a-r,a+r)$内，且不等于$a$，则以后就不会越出这个区间，而且是以$a$为极限的严格单调数列

## Chapter3 实数系的基本定理

#### 3.1 确界的概念和确界存在定理

如果$A$是一个有上界的实数集，则称$A$的最小上界为$A$的上确界，记为$\sup A$

如果$A$是一个有下界的实数集，则称$A$的最大下界为$A$的下确界，记为$\inf A$

对无上界的数集$A$，约定$\sup A=+\infty$，对无下界的数集$A$，约定$\inf A=-\infty$

####  3.2 闭区间套定理

称$\{I_n\}$是一个闭区间套，如果每个$I_n$是闭区间，而且成立单调减少的包含关系，即$I_1\supset I_2\supset \cdots\supset I_n\supset\cdots$

闭区间套定理：若$\{I_n\}$为闭区间套，则$\cap_{i=1}^\infty I_i\ne \varnothing$，若$I_n$的长度$\left|I_n\right|\to0$，则$\cap_{i=1}^\infty I_i$是单点集

#### 3.3 凝聚定理

凝聚定理（波尔查诺-魏尔斯特拉斯定理）：有界数列必有收敛子列

#### 3.4 柯西收敛准则

称数列$\{x_n\}$为基本数列（或柯西数列），如果对每个$\varepsilon>0$，存在$N$，使得对每一对正整数$n,m>N$，成立$\left|a_n-a_m\right|<\varepsilon$

柯西收敛准则：收敛数列和基本数列等价

压缩映射：设函数$f$在区间$[a,b]$上定义，$f([a,b])\subset [a,b]$，并群在一个常数$0<k<1$，使得对一切$x,y\in [a,b]$成立不等式$\left|f(x)-f(y)\right|\le k\left|x-y\right|$，则称$f$是$[a,b]$上的一个压缩映射，称$k$为压缩常数

压缩映射原理：若$f$为$[a,b]$上的压缩映射，则：

（1）$f$在$[a,b]$中存在唯一的不动点$\xi=f(\xi)$

（2）由任何初始值$a_0\in [a,b]$和递推公式$a_{n+1}=f(a_n)$生成的数列$\{a_n\}$一定收敛于$\xi$

（3）成立事后估计$\left|a_n-\xi\right|\le \frac{k}{1-k}\left|a_n-a_{n-1}\right|$和先验估计$\left|a_n-\xi\right|\le \frac{k^n}{1-k}\left|a_1-a_0\right|$

#### 3.5 覆盖定理

开覆盖：设有$[a,b]\sub \cup_\alpha O_\alpha$，其中每个$O_\alpha$是开区间，则称$\{O_\alpha\}$是区间$[a,b]$的一个开覆盖

覆盖定理（海涅-博雷尔定理）：如果$\{O_\alpha\}$是区间$[a,b]$的一个开覆盖，则存在$O_\alpha$的一个有限子集$\{O_1,O_2,\cdots,O_k\}$，它是区间$[a,b]$的一个开覆盖，也就是说$[a,b]\sub\cup_{i=1}^kO_i$

加强形式的覆盖定理：如果$\{O_\alpha\}$是区间$[a,b]$的一个开覆盖，则存在一个正数$\delta>0$，使得对于区间$[a,b]$中的任何两个点$x',x''$，只要$\left| x'-x''\right|<\delta$，就存在开覆盖中的一个开区间，它覆盖$x',x''$（称这个数$\delta$为开覆盖的勒贝格数）

#### 3.6 数列的上极限和下极限

极限点：数列的极限点就是数列的收敛子列的极限没约定若存在正/负无穷大量的极限，则将$\pm \infty$也作为极限点，称收敛子列的极限为有限极限点，将$\pm \infty$称作无线极限点

上/下极限：数列的上极限是数列的最大极限点，记为$\lim_{n\to\infty}\sup x_n$，数列的下极限是数列的最小极限点，记为$\lim_{n\to\infty}\inf x_n$

数列$\{x_n\}$收敛的充分必要条件是是数列的上极限和下极限均为有限且相等

## Chapter4 函数极限

#### 4.1 函数极限的定义

函数$f$在点$a$处有极限的定义是：存在数$A$，使得函数$f(x)$在$x$趋于$a$时以$A$为极限，即$\forall \varepsilon>0,\exists \delta>0,\forall x\in O_\delta(a)-\{a\}$，成立$\left|f(x)-A\right|<\varepsilon$

#### 4.2 函数极限的基本性质

单调函数的单侧极限存在定理：设$f$在区间$(a,b)$上单调，则$f(b^-)=\lim_{x\to b^-}f(x)$一定有意义，当$f$单调增加时，如$f$在$(a,b)$上有上界，则称$f(b^-)$为有限数，否则$f(b^-)=+\infty$

海涅归结原理：设$a,A\in\mathbb{R}$，存在极限$\lim_{x\to a}f(x)=A$的充分必要条件是：对满足条件$x_n\ne a,\lim_{n\to\infty} x_n=a$的每个数列$\{x_n\}$，都有$\lim_{n\to\infty}f(x_n)=A$

函数极限的柯西收敛准则：函数$f$在点$a$有极限的充分必要条件是：对每一个给定的$\varepsilon>0$，存在$\delta>0$，使得对于在$O_\delta(a)-\{a\}$中的每一对点$x',x''$，满足不等式$\left|f(x')-f(x'')\right|<\varepsilon$

#### 4.3 两个重要极限

$$
\lim_{x\to0}\frac{\sin x}{x}=1,\lim_{x\to0}(1+x)^{\frac{1}{x}}=e
$$

#### 4.4 无穷小量、有界量、无穷大量和阶的比较

$f(x)=o(g(x))(x\to a)$的定义是：$\lim_{x\to a}\frac{f(x)}{g(x)}=0$

$f(x)=O(g(x))(x\to a)$的定义是：存在常数$M>0$使得$\left|\frac{f(x)}{g(x)}\right|\le M$在$a$的某个去心邻域上成立

$f(x)\sim g(x)(x\to a)$的定义是：$\lim_{x\to a}\frac{f(x)}{g(x)}=1$

斯特林公式：$n!\sim (\frac ne)^n\sqrt{2\pi n}$

素数定理：$\pi(x)\sim \frac x{\ln x}(x\to\infty)$其中$\pi(x)$表示不超过$x$的素数个数

## Chapter5 连续函数

#### 5.1 连续性概念

函数$f$在点$a$连续：（1）$\lim_{x\to a}f(x)=f(a)$

（2）对于收敛于$a$的每个数列$\{x_n\}$，有$\lim_{n\to \infty}f(x_n)=f(a)$

间断点：若存在两个单侧极限，则为第一类，否则为第二类

区间上连续函数的定义：函数$f$在区间$I$的每一点都连续，则称函数$f$在区间$I$上连续，若包含端点则按左连续或右连续来定义，采用$f\in C(I)$表示函数$f$为区间$I$上的连续函数

振幅：对于点$a$的邻域$O_\delta(a)$，定义$f$在这个邻域上的振幅为$\omega_f(a,\delta)=\sup\{f(x)\}-\inf\{f(x)\},x\in O_\delta(a)$，函数$f$在点$a$的振幅为$\omega_f(a)=\lim_{\delta\to 0}\omega_f(a,\delta)$，函数$f$在点$a$连续的充分必要条件为$\omega_f(a)=0$

#### 5.2 零点存在定理和介值定理

零点存在定理：设$f\in C[a,b]$，并满足条件$f(a)f(b)<0$，则存在点$\xi\in(a,b)$使得$f(\xi)=0$

介值定理：若$f\in C[a,b]$，$a\le x_1 < x_2 \le b$，且$f(x_1)\ne f(x_2)$，则$f$可取到在$f(x_1)$和$f(x_2)$之间的每个值

#### 5.3 有界性定理和最值定理

有界性定理：有界闭区间上的连续函数一定有界

最值定理：有界闭区间上的连续函数一定取到最大值和最小值

#### 5.4 一致连续性和康托尔定理

一致连续：函数$f$在区间$I$上一致连续，如果对每一个$\varepsilon>0$，存在$\delta>0$，使得当$x',x''\in I$且$\left|x'-x''\right|<\delta$时，成立$\left|f(x')-f(x'')\right|<\varepsilon$（简单来说，导数不为无穷大）

有界开区间$(a,b)$上的连续函数$f$在$(a,b)$上一致连续的充分必要条件是存在两个有限的单侧极限$f(a^+),f(b^-)$

康托尔定理：有界闭区间上的连续函数必在这个区间上一致连续

#### 5.5 单调函数

单调函数的间断点是跳跃点，且至多为可列个。

## Chapter6 导数与微分

#### 6.1 导数及其计算

$f'(x_0)=\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$

反函数求导公式：设$x=\varphi(y)$在点$y_0$的某邻域上为严格单调连续函数，且有$\varphi'(y_0)\ne0$，若$y=f(x)$是$x=\varphi(y)$的反函数，则$f(x)$在点$x_0=\varphi(y_0)$处可导，且$f'(x_0)=\frac{1}{\varphi'(y_0)}$

#### 6.2 高阶导数及其他求导法则

莱布尼茨公式：
$$
(uv)^{(n)}=\binom n0u^{(0)}v^{(n)}+\binom n1u'v^{(n-1)}+\binom n2u''v^{(n-2)}+\cdots+\binom nnu^{(n)}v^{(0)}=\sum_{k=0}^n\binom nku^{(k)}v^{(n-k)}
$$
若$y=y(x)$和$x=x(y)$互为反函数，则有$y'(x)=\frac{1}{x'(y)}$

设$x=\varphi(t),y=\psi(t)$在区间$(a,b)$上可导，且$\forall t \in (a,b),\varphi(t)\ne0$，则

（1）$x=\varphi(t)$是区间$(a,b)$上的严格单调连续函数，因而存在反函数$t=t(x)$

（2）在$x=\varphi(t)$和$y=\psi(t)$之间存在函数关系$y=\psi(t(x))$，简记为$y=y(x)$

（3）函数$y=y(x)$可导，且有$y'(x)=\left.\frac{\psi'(t)}{\varphi'(t)}\right|_{t=t(x)}$

#### 6.3 一阶微分及其形式不变性

微分是增量中的线性主部，具体来说，考虑$y=f(x)$在点$x_0$由自变量的增量$\Delta x$引起的因变量的增量$\Delta y$，若有常数$a$，使得$\Delta y=a\Delta x+o(\Delta x)(\Delta x\to0)$，则称$\Delta y$有线性主部$a\Delta x$，这时称$y=f(x)$在点$x_0$可微，并将这个线性主部称为$y=f(x)$在点$x_0$的微分

在某点可微的充分必要条件是在某点可导

上述微分的记号是$dy=f'(x_0)dx$

## Chapter7 微分学的基本定理

#### 7.1 微分学中值定理

极值：设函数$f(x)$在点$x_0$的一个邻域$O(x_0)$上有定义，如果对于每个$x\in O(x_0)$成立不等式$f(x)\le(\ge)f(x_0)$，则称$f(x)$在点$x_0$处达到极大值(极小值)，极值点必须是函数的定义域中的内点

内点：设$S$为$\mathbb{R}$中的一个非空点集，称点$x\in S$为$S$的内点，如果存在点$x$的一个邻域$O(x)\sub S$

费马定理：若$x_0$是函数$f$的极值点，且存在导数$f'(x_0)$，则一定有$f'(x_0)=0$

驻点：若$f'(x_0)=0$，则称$x_0$为驻点或平稳点

罗尔定理：设$f$在$[a,b]$上连续，在$(a,b)$上可微，且有$f(a)=f(b)$，则存在$\xi\in(a,b)$，使得$f'(\xi)=0$

拉格朗日中值定理：设$f$在$[a,b]$上连续，在$(a,b)$上可微，则存在$\xi\in(a,b)$，使得$f'(\xi)=\frac{f(b)-f(a)}{b-a}$

柯西中值定理：设函数$f,g$在$[a,b]$上连续，在$(a,b)$上可微，且满足条件$g(b)-g(a)\ne0,\forall x\in(a,b),f'^2(x)+g'^2(x)\ne0$，则存在$\xi\in(a,b)$，使得$\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(\xi)}{g'(\xi)}$

达布定理：设$f(x)$在区间$I$上可微，则$f'(x)$具有介值性质，即$f'(I)$仍为区间

单侧导数极限定理：设在区间$[a,b)$上有定义的函数$f$在$(a,b)$上可微，又在点$a$右连续，若导函数$f'(x)$在点$a$存在右侧极限$f'(a^+)=A$，则$f$在点$a$也一定存在右侧导数$f'_+(a)$，且成立$f'(a^+)=f'_+(a)=A$

#### 7.2 泰勒定理

泰勒展开式：$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}+r_n(x)$

皮亚诺余项：若函数$f$在点$x_0$存在$n$阶导数$f^{(n)}(x_0)$，则有$r_n(x)=o((x-x_n)^n)(x\to x_0)$

拉格朗日余项：若函数$f$在点$x_0$的某邻域$O(x_0)$上$n+1$阶可微，则$\forall x\in O(x_0),x\ne x_0,\exists\xi \in(x_0,x)$，使得$r_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$

柯西余项：若函数$f$在点$x_0$的某邻域$O(x_0)$上$n+1$阶可微，则$\forall x\in O(x_0),x\ne x_0,\exists\eta \in(x_0,x)$，使得$r_n(x)=\frac{f^{(n+1)}(\eta)}{(n+1)!}(x-\eta)^n(x-x_0)$

积分型余项：若函数$f$在点$x_0$的某邻域$O(x_0)$上$n+1$阶可微，则有$r_n(x)=\frac{1}{n!}\int_{x_0}^xf^{(n+1)}(t)(x-t)^ndt$

## Chapter8 微分学的应用

#### 8.1 函数极限的计算

洛必达法则：两函数$f(x),g(x)$在以$x=a$为断掉的开区间可微，如果$\lim_{x\to a} f(x)=\lim_{x\to a} g(x)=0/\infty$，则有$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$

#### 8.2 函数的单调性

设函数$f\in C(I)$，在$I$的内点处处可微，则

1、$f$为区间上$I$的单调函数的充分必要条件是导函数不变号

2、$f$为区间上$I$的严格单调函数的充分必要条件是除了导函数不变号以外，还在集合$\{x\in I|f'(x)=0\}$中不包含任何长度大于零的区间

#### 8.3 函数的极值与最值

若函数$f$在点$x_0$处$n$阶可微，$f'(x_0)=f''(x_0)=\cdots=f^{(n-1)}(x_0)=0$，但$f^{(n)}(x_0)\ne 0$，则若$n$为奇数，则$x_0$一定不是极值点，若$n$为偶数，则$x_0$一定是$f$的极值点，若$f^{(n)}(x_0)>0$，则$x_0$是极小值点，若$f^{(n)}(x_0)<0$，则$x_0$是极大值点

#### 8.4 函数的凸性

凸函数：设函数$f$在区间$I$上定义，若对每一对点$x_1,x_2\in I,x_1\ne x_2$和每个$\lambda \in (0,1)$，成立不等式$f(\lambda x_1+(1-\lambda)x_2)\le \lambda f(x_1)+(1-\lambda)f(x_2)$，则称$f$为区间$I$上的下凸函数，若严格成立不等号，则称$f$为严格下凸函数，上凸函数与之相反

函数$f$在区间$I$上为下凸函数的充分必要条件是函数$f'$在区间$I$上为单调增加函数

下凸函数的詹森不等式：如$f$为区间$I$上的二阶可微下凸函数，则对任何$x_1,x_2,\cdots,x_n\in I$与满足条件$\lambda_1+\lambda_2+\cdots+\lambda_n=1$的$n$个正数$\lambda_1,\lambda_2,\cdots,\lambda_n$成立不等式$\lambda_1f(x_1)+\lambda_2f(x_2)+\cdots+\lambda_nf(x_n)\ge f(\lambda_1x_1+\lambda_2x_2+\cdots+\lambda_nx_n)$

#### 8.5 不等式

广义的算术平均值-几何平均值不等式：设有非负数$x_1,x_2,\cdots,x_n$和正数$\lambda_1,\lambda_2,\cdots,\lambda_n$，且$\lambda_1+\lambda_2+\cdots+\lambda_n=1$，则成立不等式：
$$
\prod_{k=1}^nx_k^{\lambda_k}\le\sum_{k=1}^n\lambda_kx_k
$$
赫尔德不等式：设$x_1,x_2,\cdots,x_n$和$y_1,y_2,\cdots,y_n$均为非负数，又有$p>1,q>1,\frac1p+\frac1q=1$，则成立不等式：
$$
\sum_{k=1}^nx_ky_k\le\left(\sum_{k=1}^nx_k^p\right)^\frac1p\left(\sum_{k=1}^ny_k^q\right)^\frac1q
$$
闵可夫斯基不等式：设$x_1,x_2,\cdots,x_n$和$y_1,y_2,\cdots,y_n$均为非负数，又有$p\ge 1$，则成立不等式：
$$
\left[\sum_{k=1}^n(x_k+y_k)^p\right]^\frac1p=\left(\sum_{k=1}^nx_k^p\right)^\frac1p+\left(\sum_{k=1}^ny_k^p\right)^\frac1p
$$

#### 8.6 函数作图

#### 8.7 方程求根与近似计算

## Chapter9 不定积分

#### 9.1 不定积分的计算方法

第一换元法-凑微分法（直接代换法）：设$\int f(u)du=F(u)+C,u=u(x)$可微，则
$$
\int f(u(x))u'(x)dx=F(u(x))+C
$$
第二换元法-代入换元法（逆代换法）：设不定积分$\int f(x)dx$存在，$x=x(t)$可微且存在反函数$t=t(x)$，又若$\int f(x(t))x'(t)dt=F(t)+C$，则得到
$$
\int f(x)dx=F(t(x))+C
$$
分部积分法：设$u(x)$与$v(x)$可微，且在$u(x)v'(x)$和$v(x)u'(x)$中至少有一个存在原函数，则
$$
\int u(x)v'(x)dx=u(x)v(x)-\int v(x)u'(x)dx
$$

#### 9.2 几类可积函数

## Chapter10 定积分

#### 10.1 定积分概念与可积条件

定积分定义：

称点集$P=\{x_0,x_1,\cdots,x_{n-1},x_n\}$为$[a,b]$的一个分划，如果满足条件$a=x_0<x_1<\cdots<x_{n-1}<x_n=b$，记$\Delta x_i=x_i-x_{i-1},i=1,2,\cdots,n$，并称$\left||P|\right|=max\{\Delta x_i\}$为分划$P$的细度

设$P=\{x_0,x_1,\cdots,x_{n-1},x_n\}$为$[a,b]$的一个分划，对每个子区间$[x_{i-1},x_i]$，任取$\xi_i\in[x_{i-1},x_i]$，则称$\xi=\{\xi_i|i=1,2,\cdots,n\}$为从属于$P$的一个介点集，并称和式$\sum_{i=1}^nf(\xi_i)\Delta x_i$或$\sum_Pf(\xi_i)\Delta x_i$为$f$在区间$[a,b]$上的一个黎曼和

设$I$为实数，且$\forall \varepsilon>0,\exists \delta>0$，对$\left||P|\right|<\delta$的每个分划$P$，以及对从属于$P$的每个介点集$\xi$，成立$\left|\sum_{i=1}^nf(\xi_i)\Delta x_i-I\right|<\varepsilon$，则称函数$f$在区间$[a,b]$上黎曼可积或简称可积，记为$f\in R[a,b]$，并称$I$为$f$在区间$[a,b]$上的黎曼积分或定积分，记为$\int_a^b f(x)dx=I$

振幅：设$P=\{x_0,x_1,\cdots,x_{n-1},x_n\}$为$[a,b]$的一个分划，对$i=1,2,\cdots,n$，记$M_i=\sup\{f(x)|x\in[x_{i-1},x_i]\},m_i=\inf\{f(x)|x\in[x_{i-1},x_i]\}$，则称$\omega_i=M_i-m_i$为$f$在$[x_{i-1},x_i]$上的振幅，$\sum_{i=1}^n\omega_i\Delta x_i$为$f$的振幅面积

可积的充分必要条件：

（1）$\forall \varepsilon>0,\exists \delta>0$，对$\left||P|\right|<\delta$的每个分划$P$，成立$\sum_P\omega_i \Delta x_i<\varepsilon$

（2）$\forall \varepsilon>0,\exists P,s.t.\sum_P\omega_i \Delta x_i<\varepsilon$

（3）$\forall \varepsilon,\eta>0,\exists P,s.t.\sum \Delta x_i<\varepsilon ,i\in\{i|w_i\ge\eta\}$

零测度集：如果一个点集可以用总长度任意小的至多可列个开区间覆盖，就称这个点集为零测度集，如果某种性质在一个零测度集之外成立，就说这个性质几乎处处成立

#### 10.2 定积分的性质

积分第一中值定理：设$f,g\in R[a,b],m\le f(x)\le M,\forall x\in[a,b]$，$g$在$[a,b]$上不变号，则存在$\eta \in[m,M]$，使
$$
\int_a^bf(x)g(x)dx=\eta\int_a^bg(x)dx
$$
如果$f$连续，则存在$\xi\in[a,b]$，使得$f(\xi)=\eta$

积分中值第二定理：设$f\in R[a,b]$，$g$在$[a,b]$上单调，则存在$\xi\in[a,b]$，使
$$
\int_a^bf(x)g(x)dx=g(a)\int_a^\xi f(x)dx+g(b)\int_\xi^bf(x)dx
$$
黎曼定理：设$f\in R[a,b]$，$g$以$T$为周期且在$[0,T]$上可积，则
$$
\lim_{p\to+\infty}\int_a^bf(x)g(px)dx=\frac1T\int_0^Tg(x)dx\int_a^bf(x)dx
$$

#### 10.3 变限积分与微积分基本定理

牛顿-莱布尼茨公式：设$f\in R[a,b]$，$F$是$f$在$[a,b]$上的原函数，则对每一个$x\in[a,b]$，成立
$$
\int_a^xf(t)dt=F(x)-F(a)
$$

#### 10.4 定积分的计算

## Chapter11 积分学的应用

#### 11.1 积分学在几何计算中的应用

设没有自交点的平面封闭曲线的参数方程为$x=x(t),y=y(t),t\in[\alpha,\beta]$，当$t$从$\alpha$增加到$\beta$时，点$(x(t),y(t))$以逆时针方向绕闭曲线一周，则该闭曲线所围成的面积为$S=\frac12\int_\alpha^\beta(xdy-ydx)$

在极坐标中由射线$\theta=\theta_1,\theta=\theta_2$与连续曲线$\rho=\rho(\theta)$围成的扇形面积为$S=\frac12\int_{\theta_1}^{\theta_2}\rho^2(\theta)d\theta$

密度均匀的分段光滑曲线$y=f(x)(x\in[a,b])$的质心的横坐标与纵坐标为：
$$
x_c=\frac{\int_a^bx\sqrt{1+(f'^2(x))}dx}{\int_a^b\sqrt{1+(f'^2(x))}dx},y_c=\frac{\int_a^bf(x)\sqrt{1+(f'^2(x))}dx}{\int_a^b\sqrt{1+(f'^2(x))}dx}
$$
古尔丁第一定理：设平面曲线的质心坐标为$(x_c,y_c)$，且曲线位于右半平面内，则曲线绕$y$轴旋转一周所产生的旋转曲面的面积$S_y$等于质心绕$y$轴一周所经过的路程$2\pi x_c$乘以曲线的弧长$l$，即$S_y=2\pi x_c l$

古尔丁第二定理：设平面图形的质心坐标为$(x_c,y_c)$，且图形位于右半平面内，则曲线绕$y$轴旋转一周所产生的旋转立体的体积$V_y$等于质心绕$y$轴一周所经过的路程$2\pi x_c$乘以曲线的面积$S$，即$Y_y=2\pi x_c S$

#### 11.2 不等式

哈达玛不等式：设$f$是$(a,b)$上的下凸函数，则对每一对$x_1,x_2\in(a,b),x_1<x_2$，有：
$$
f(\frac{x_1+x_2}{2})\le\frac{1}{x_2-x_1}\int_{x_1}^{x_2}f(t)dt\le\frac{f(x_1)+f(x_2)}{2}
$$
詹森不等式：设$f,p\in R[a,b],m\le f(x) \le M,p(x)$非负且$\int_a^bp(x)>0$，则当$\varphi$是$[m,M]$上的下凸函数时，成立不等式：
$$
\varphi\left(\frac{\int_a^bp(x)f(x)dx}{\int_a^bp(x)d(x)}\right)=\frac{\int_a^bp(x)\varphi(f(x))dx}{\int_a^bp(x)dx}
$$
施瓦茨积分不等式：设$f,g\in R[a,b]$，则
$$
\left(\int_a^bf(x)g(x)dx\right)^2\le\int_a^bf^2(x)dx\int_a^bg^2(x)dx
$$
杨氏不等式：设$f$在$[0,+\infty)$上连续可导且严格单调增加，$f(0)=0,a,b>0$，$g(y)$是$f(x)$的反函数，则有：
$$
ab\le\int_0^af(x)dx+\int_0^bg(y)dy
$$
赫尔德不等式：设$f,g\in R[a,b],p,q$为满足$\frac1p+\frac1q=1$的一对正实数，则成立：
$$
\left(\int_a^b|f(x)g(x)|dx\right)\le\left(\int_a^b|f(x)|^pdx\right)^\frac1p\left(\int_a^b|g(x)|^qdx\right)^\frac1q
$$
闵可夫斯基不等式：设$f,g\in R[a,b],1\le p<+\infty$，则成立
$$
\left(\int_a^b|f(x)+g(x)|^pdx\right)^\frac1p\le\left(\int_a^b|f(x)|^pdx\right)^\frac1p\left(\int_a^b|g(x)|^pdx\right)^\frac1p
$$

#### 11.3 积分估计与近似计算

#### 11.4 积分学在分析中的其他应用

沃利斯公式：
$$
\lim_{n\to\infty}\frac{1}{2n+1}\left[\frac{2\cdot4\cdots(2n)}{1\cdot3\cdots(2n-1)}\right]^2=\frac\pi2,\frac{(2n)!!}{(2n-1)!!}\sim\sqrt{\pi n}
$$

## Chapter12 广义积分

#### 12.1 广义积分的定义

内闭可积：设$I$为区间，函数$f$在$I$上有定义，如果对任意有界闭区间$[a,b]\sube I,f\in R[a,b]$，则称$f$在$I$上内闭可积

奇点：称$b$为函数$f(x)$在定义域区间$[a,b)$上的奇点，如果$b=+\infty$或者$f(x)$在点$b$左侧无界，假如$f(x)$在区间$[a,b)$上内闭可积，$b$为$f(x)$在$[a,b)$上的奇点，则定义广义积分如下：
$$
\int_a^bf=\int_a^bf(x)dx=\lim_{b'\to b^-}\int_a^{b'}f(x)dx
$$
设$a<c<b$，如果$c$为$f$在$[a,c)$与$(c,b]$上的奇点或$a,b$分别为$f$在$(a,c]$与$[c,b)$上的奇点，则定义广义积分：
$$
\int_b^af=\int_a^cf+\int_c^bf
$$

#### 12.2 广义积分的敛散性判别法

迪利克雷判别法：设$f$在$[a,b)$上内闭可积，$b$为奇点，广义积分$\int_a^bf$收敛的充分必要条件是存在分解$f=uv$使得

（1）函数$u$在$[a,b)$上单调，且$\lim_{x\to b^-}u(x)=0$

（2）对任何$b^->a$，积分$\int_a^{b'}v(x)dx$存在并有界

阿贝尔判别法：设$f$在$[a,b)$上内闭可积，$b$为奇点，广义积分$\int_a^bf$收敛的充分必要条件是存在分解$f=uv$使得

（1）函数$u$在$[a,b)$上单调有界

（2）积分$\int_a^bv(x)dx$收敛

#### 12.3 广义积分的计算

#### 12.4 广义积分的特殊性质

## Chapter13 数项级数

#### 13.1 无穷级数的基本概念

无穷级数概念：
$$
\sum_{n=1}^{\infty}a_n=a_1+a_2+\cdots+a_n+\cdots
$$
$a_n$为通项，部分和数列$S_n=a_1+a_2+\cdots+a_n$，当部分和数列$\{S_n\}$收敛时，称无穷级数收敛，否则为发散，当无穷级数收敛时，称极限$S=\lim_{n\to\infty}S_n$为无穷级数的和，无穷级数可简记为级数。

#### 13.2 正项级数

比较判别法：大收敛则小收敛，小发散则大发散，核心是找到比较的级数和放缩

#### 13.3 一般项级数

称收敛级数$\sum a_n$为绝对收敛级数，如果$\sum|a_n|$也收敛，否则称为条件收敛级数