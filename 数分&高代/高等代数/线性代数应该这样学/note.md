# 线性代数应该这样学

## Chapter1 向量空间

#### 1.1 复数

所有复数的集合  $\mathbb{C}=\left \{  a+bi:a,b\in \mathbb{R}\right \}$

加法逆-负数，乘法逆-倒数

$\mathbb{F}$(Field)总表示$\mathbb{R}$或$\mathbb{C}$，即把$\mathbb{F}$变为$\mathbb{R}$或者$\mathbb{C}$结论仍然成立

#### 1.2 向量空间的定义

$\mathbb{F}^{n} = \{(x_{1},\cdots,x_{n}):x_{i}\in\mathbb{F},i=1,\cdots,n\}$

**向量空间**：给定域$\mathbb{F}$，$\mathbb{F}$上的向量空间$\mathbb{V}$是一个集合，其上定义了两种运算

* 向量加法$+$：$\mathbb{V}+\mathbb{V}\to\mathbb{V}$，把$\mathbb{V}$中的两个元素$\mathbf{u},\mathbf{v}$映射到V中另一个元素，记作$\mathbf{u}+\mathbf{v}$
* 向量乘法  $ \cdot $  ：$\mathbb{F}\times\mathbb{V}\to\mathbb{V}$，把$\mathbb{F}$中的一个元素$a$和$\mathbb{V}$中的一个元素$\mathbf{u}$变为到V中另一个元素，记作$a\cdot\mathbf{u}$

**多项式**：一个函数$\mathbf{p}:\mathbb{F}\to\mathbb{F}$称为系数在$\mathbb{F}$中的多项式，如果存在$a_{0},\cdots,a_{m}\in\mathbb{F}$使得
$$
\mathbf{p}(z)=a_{0}+a_{1}z+a_{2}z^{2}+\cdots+a_{m}z^{m},z\in\mathbb{F}.
$$

定义$\mathbf{P}(\mathbb{F})$为系数在$\mathbb{F}$中的左右多项式构成的**集合**

* 若$\mathbf{p},\mathbf{q}\in\mathbf{P}(\mathbb{F})$，则$(\mathbf{p}+\mathbf{q})(z)=\mathbf{p}(z)+\mathbf{q}(z),z\in\mathbb{F}$
* 若$a\in\mathbb{F},\mathbf{p}\in\mathbf{P}(\mathbb{F})$，则$(a\mathbf{p})(z)=a\mathbf(p)(z),z\in\mathbb{F}$

#### 1.3 向量空间的性质

#### 1.4 子空间

**子空间**：$\mathbb{V}$的子集$\mathbb{U}$称为$\mathbb{V}$的子空间，如果$\mathbb{U}$也是向量空间

* 例如$\{(x_{1},x_{2},0):x_{1},x_{2}\in\mathbb{F}\}$是$\mathbb{F}^{3}$的一个子空间

#### 1.5 和与直和

设$\mathbb{U}_{1},\cdots,\mathbb{U}_{m}$都是$\mathbb{V}$的子空间，则$\mathbb{U}_{1},\cdots,\mathbb{U}_{m}$的**和**记为$\mathbb{U}_{1}+\cdots+\mathbb{U}_{m}$，定义为$\mathbb{U}_{1},\cdots,\mathbb{U}_{m}$中元素所有可能的和所构成的集合，更明确的说：
$$
\mathbb{U}_{1}+\cdots+\mathbb{U}_{m}=\{\mathbf{u}_{1}+\cdots+\mathbf{u}_{m}:\mathbf{u}_{1}\in\mathbb{U}_{1},\cdots,\mathbf{u}_{m}\in\mathbb{U}_{m}\}
$$
如果$\mathbb{V}$的每个元素都可以**唯一**地写成$\mathbf{u}_{1}+\cdots+\mathbf{u}_{m}$，其中$\mathbf{u}_{j}\in\mathbb{U}_{j}$，则称$\mathbb{V}$是子空间$\mathbb{U}_{1},\cdots,\mathbb{U}_{m}$的**直和**，记为
$$
\mathbb{V}=\mathbb{U}_{1}\oplus\cdots\oplus\mathbb{U}_{m}
$$

* 若 $\mathbb{U}=\{(x,y,0)\in\mathbb{F}^{3}:x,y\in\mathbb{F},\mathbb{W}=\{(0,0,z)\in\mathbb{F}^{3}:z\in\mathbb{F}\}$，则$\mathbb{F}^{3}=\mathbb{U}\oplus\mathbb{W}$

## Chapter2 有限维向量空间

#### 2.1 张成与线性无关

张成 $span(\mathbf{v}_{1},\cdots,\mathbf{v}_{m})=\{a_{1}\mathbf{v}_{1}+\cdots+a_{m}\mathbf{v}_{m}:a_{1},\cdots,a_{m}\in\mathbb{F}\}$

* $(7,2,9)\in span((2,1,3),(1,0,1))$
* 空组$span()={\mathbf{0}}$
* 如果$span(\mathbf{v}_{1},\cdots,\mathbf{v}_{m})$等于$\mathbb{V}$，则称$(\mathbf{v}_{1},\cdots,\mathbf{v}_{m})$张成$\mathbb{V}$

如果一个向量空间可以由它的一组向量张成，则称其为有限维的

多项式的次数由其最高阶变量的指数确定，如果多项式恒等于0，则规定其次数为$-\infty$

对于非负整数$m$，令$\mathbf{P}_{m}(\mathbf{F})$表示系数在$\mathbf{F}$中并且次数不超过$m$的所有多项式所组成的集合

对于$(\mathbf{v}_{1},\cdots,\mathbf{v}_{m})$中一组向量，如果使得$a_{1}\mathbf{v}_{1}+\cdots+a_{m}\mathbf{v}_{m}$等于$\mathbf{0}$的$a_{1},\cdots,a_{m}\in\mathbb{F}$只有$a_{1}=\cdots=a_{m}=0$，则称$(\mathbf{v}_{1},\cdots,\mathbf{v}_{m})$是**线性无关**的，空组$()$是线性无关的

#### 2.2 基

若$\mathbb{V}$中一个向量组既是线性无关的又张成$\mathbb{V}$，则称之为$\mathbb{V}$的**基**

#### 2.3 维数

有限维向量空间的任意基的长度称为这个向量空间的**维数**，$\mathbb{V}$的维数记为$\dim\mathbb{V}$

* $\dim\mathbb{F}^{n}=n,\dim\mathbf{P}_{m}(\mathbb{F})=m+1$

## Chapter3 线性映射

#### 3.1 定义与例子

从$\mathbb{V}$到$\mathbb{W}$的**线性映射**是具有下列性质的函数$\mathbf{T}：\mathbb{V}\to\mathbb{W}$：(对于线性映射$\mathbf{T}\mathbf{v}=\mathbf{T}(\mathbf{v})$)

* 加性 对所有$\mathbf{u},\mathbf{v}\in\mathbb{V}$都有$\mathbf{T}\mathbf{u}+\mathbf{v}=\mathbf{T}\mathbf{u}+\mathbf{T}\mathbf{v}$
* 齐性 对所有$a\in \mathbb{F},\mathbf{v}\in \mathbb{V}$都有$\mathbf{T}(a\mathbf{v})=a(\mathbf{T}\mathbf{v})$

从$\mathbb{V}$到$\mathbb{W}$的所有线性映射所构成的集合记为$\mathbf{L}(\mathbb{V},\mathbb{W})$

如果$\mathbf{T}\in\mathbf{L}(\mathbb{U},\mathbb{V}),\mathbf{S}\in\mathbf{L}(\mathbb{V},\mathbb{W})$，那么定义$\mathbf{S}\mathbf{T}\in\mathbf{L}(\mathbb{U},\mathbb{W})$如下，我们称$\mathbf{S}\mathbf{T}$是$\mathbf{S}$和$\mathbf{T}$的乘积：
$$
(\mathbf{S}\mathbf{T})(\mathbf{v})=\mathbf{S}(\mathbf{T}\mathbf{v}),\mathbf{v}\in \mathbb{U}.
$$

#### 3.2 零空间和值域

对于$\mathbf{T}\in\mathbf{L}(\mathbb{V},\mathbb{W})$，$\mathbb{V}$中被$\mathbf{T}$映射成$\mathbf{0}$的那些向量所组成的子集称为$\mathbf{T}$的零空间，记为$\text{null}\mathbf{T}$：
$$
\text{null}\mathbf{T}=\{\mathbf{v}\in\mathbb{V}:\mathbf{Tv}=\mathbf{0}\}
$$
线性映射$\mathbf{T}：\mathbb{V}\to\mathbb{W}$称为是单的，如果当$\mathbf{u},\mathbf{v}\in\mathbb{V},\mathbf{Tu}=\mathbf{Tv}$时，必有$\mathbf{u}=\mathbf{v}$

对于$\mathbf{T}\in\mathbf{L}(\mathbb{V},\mathbb{W})$，由$\mathbb{W}$中形如$\mathbf{Tv}(\mathbf{v}\in\mathbb{V})$的向量所组成的子集称为$\mathbf{T}$的值域，记为$\text{range}\mathbf{T}$：
$$
\text{range}\mathbf{T}=\{\mathbf{Tv}:\mathbf{v}\in\mathbb{V}\}
$$
线性映射$\mathbf{T}：\mathbb{V}\to\mathbb{W}$称为是满的，如果它的值域等于$\mathbb{W}$

定理：$\dim\mathbb{V}=\dim\text{null}\mathbf{T}+\dim\text{range}\mathbf{T}$

#### 3.3 线性映射的矩阵

设$\mathbf{T}\in\mathbf{L}(\mathbb{V},\mathbb{W})$，$(\mathbf{v}_{1},\cdots,\mathbf{v}_{n})$是$\mathbb{V}$的基，$(\mathbf{w}_{1},\cdots,\mathbf{w}_{m})$是$\mathbb{W}$的基，那么对于每个$k=1,\cdots,n$，$\mathbf{Tv_{k}}$都可以唯一地写成这些$\mathbf{w}$的线性组合：$\mathbf{Tv_{k}}=a_{1,k}\mathbf{w}_{1}+\cdots+a_{m,k}\mathbf{w}_{m}$，其中$a_{j,k}\in\mathbb{F},j=1,\cdots,m$。因为线性映射由其在基上的值确定，所以线性映射$\mathbf{T}$由这些标量$a_{j,k}$完全确定，由这些$a$所构成的$m\times n$矩阵称为$\mathbf{T}$关于基$(\mathbf{v}_{1},\cdots,\mathbf{v}_{n})$和基$(\mathbf{w}_{1},\cdots,\mathbf{w}_{m})$的矩阵，记为：
$$
\mathbf{M}(\mathbf{T},(\mathbf{v}_{1},\cdots,\mathbf{v}_{n}),(\mathbf{w}_{1},\cdots,\mathbf{w}_{m}))=\begin{bmatrix}
  a_{1,1}& \cdots & a_{1,n}\\
  \vdots&  & \vdots\\
  a_{m,1}& \cdots &a_{m,n}
\end{bmatrix}
$$

* 如果基在上下文中是自明的，那么将上式简记为$\mathbf{M}(\mathbf{T})$

#### 3.4  可逆性

线性映射$\mathbf{T}\in\mathbf{L}(\mathbb{V},\mathbb{W})$称为可逆的，如果存在线性映射$\mathbf{S}\in\mathbf{L}(\mathbb{W},\mathbb{V})$使得$\mathbf{TS}$等于$\mathbb{W}$上的恒等映射，并且$\mathbf{ST}$等于$\mathbb{V}$上的恒等映射，$$\mathbf{S}$$称为$\mathbf{T}$的逆

称两个向量空间是同构的，如果存在从一个向量空间到另一个向量空间的可逆线性映射

一个向量空间到其自身的线性映射称为算子，我们说线性映射$\mathbf{T}：\mathbb{V}\to\mathbb{V}$是$\mathbb{V}$上的算子，我们采用$\mathbf{L}(\mathbb{V})$来表示$\mathbb{V}$上算子的集合，也就是说$\mathbf{L}(\mathbb{V})=\mathbf{L}(\mathbb{V},\mathbb{V})$

## Chapter4 多项式

#### 4.1 次数

#### 4.2 复系数

每个不是常数的复系数多项式都有根

#### 4.3 实系数

$z=\text{Re}\;z+(\text{Im}\;z)i$

## Chapter5 特征值和特征向量

#### 5.1 不变子空间

对于$\mathbf{T}\in\mathbf{L}(\mathbb{V})$和$\mathbb{V}$的子空间$\mathbb{U}$，如果对于每个$\mathbf{u}\in\mathbb{U}$都有$\mathbf{Tu}\in\mathbb{U}$，则称$\mathbb{U}$在$\mathbf{T}$下是不变的

对于$\mathbf{T}\in\mathbf{L}(\mathbb{V})$和标量$\lambda\in\mathbb{F}$，如果有非零向量$\mathbf{u}\in\mathbb{V}$使得$\mathbf{Tu}=\lambda\mathbf{u}$，则称$\lambda$为$\mathbf{T}$的特征值

设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，并且$\lambda\in\mathbb{F}$为$\mathbf{T}$的特征值，如果向量$\mathbf{u}\in\mathbb{V}$满足$\mathbf{Tu}=\lambda\mathbf{u}$，则称$\mathbf{u}$是$\mathbf{T}$相应于$\lambda$的特征向量

#### 5.2 多项式对算子的应用

#### 5.3 上三角矩阵

3.3中的线性变换的矩阵，如果其映射是从一个向量空间到其自身，也就是说这个映射是一个算子，也就是说只有一组基，这样的映射显然是一个方阵，记作$\mathbf{M}(\mathbf{T},(\mathbf{v}_{1},\cdots,\mathbf{v}_{n}))$，称$\mathbf{T}$关于$(\mathbf{v}_{1},\cdots,\mathbf{v}_{n})$的矩阵

一个矩阵称为上三角的，如果位于对角线下方的元素全为0，典型形式如下：
$$
\begin{bmatrix}
  \lambda_{1}&  & *\\
  & \ddots & \\
  0&  &\lambda_{n}
\end{bmatrix}
$$
设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$关于$\mathbb{V}$的某个基有上三角矩阵，则这个上三角矩阵对角线上的元素恰好是$\mathbf{T}$的所有特征值

#### 5.4 对角矩阵

对角矩阵是对角线以外的元素全是0的方阵

算子$\mathbf{T}\in\mathbf{L}(\mathbb{V})$关于$\mathbb{V}$的某个基有对角矩阵当且仅当$\mathbb{V}$有一个由$\mathbf{T}$的特征向量所组成的基

#### 5.5 实向量空间的不变子空间

## Chapter6 内积空间

#### 6.1 内积

$\mathbf{w}=(w_{1},\cdots,w_{n})\in\mathbb{C}^{n}$ 与$\mathbf{z}=(z_{1},\cdots,z_{n})\in\mathbb{C}^{n}$的内积为$w_{1}\overline{z_{1}}+\cdots+w_{n}\overline{z_{n}}$

有 $\mathbf{w}\cdot\mathbf{z}=\overline{\mathbf{z}\cdot\mathbf{w}}$

$\mathbb{V}$上的内积就是一个函数，它把$\mathbb{V}$中元素的每个有序对$(\mathbf{u},\mathbf{v})$都映射成一个数$\left \langle\mathbf{u},\mathbf{v} \right \rangle \in \mathbb{F} $

#### 6.2 范数

对于$\mathbf{v} \in \mathbb{V}$，$\mathbf{v}$的范数记为$\left \|  \mathbf{v}\right \| $，定义为$\left \|  \mathbf{v}\right \|=\sqrt{\left \langle\mathbf{v},\mathbf{v} \right \rangle}$

对于两个向量$\mathbf{u},\mathbf{v}\in\mathbb{V}$，如果$\left \langle\mathbf{u},\mathbf{v} \right \rangle=0$，则称$\mathbf{u}$和$\mathbf{v}$是正交的

柯西-施瓦茨不等式：若$\mathbf{u},\mathbf{v}\in\mathbb{V}$，则$\left|\left \langle\mathbf{u},\mathbf{v} \right \rangle \right|\le\left\|\mathbf{u}\right\|\left\|\mathbf{v}\right\|$

#### 6.3 标准正交基

如果一个向量组中的向量两两正交，并且每个向量的范数都为1，则称这个向量组是标准正交的

#### 6.4 正交投影与极小化问题

如果$\mathbb{U}$是$\mathbb{V}$的子集，那么$\mathbb{U}$的正交补记为$\mathbb{U}^{\perp}$，是由$\mathbb{V}$中与$\mathbb{U}$的每个向量都正交的那些向量组成的集合：
$$
\mathbb{U}^{\perp}=\{\mathbf{v}\in\mathbb{V}:\left \langle\mathbf{v},\mathbf{u} \right \rangle=0,\mathbf{u}\in\mathbb{U}\}
$$
设$\mathbb{U}$是$\mathbb{V}$的子空间，并且$\mathbf{v}\in\mathbb{V}$，则$\left\|\mathbf{v}-P_{\mathbb{U}}\mathbf{v}\right\|\le\left\|\mathbf{v}-\mathbf{u}\right\|,\mathbf{u}\in\mathbb{U}$

#### 6.5 线性泛函与伴随

$\mathbb{V}$上的线性泛函是从$\mathbb{V}$到$\mathbb{F}$的线性映射，如$\varphi:\mathbb{F}^{3}\to\mathbb{F}\;\; \varphi(z_{1},z_{2},z_{3})=2z_{1}-5z_{2}+z_{3}$

设$\mathbf{T}\in\mathbf{L}(\mathbb{V},\mathbb{W})$，$\mathbf{T}$的伴随记为$\mathbf{T}^{*}$，是如下定义的从$\mathbb{W}$到$\mathbb{V}$的函数，给定$\mathbf{w}\in\mathbb{W}$，$\mathbf{T}^{*}\mathbf{w}$是$\mathbb{V}$中唯一一个满足下面条件的向量
$$
\left \langle\mathbf{Tv},\mathbf{w} \right \rangle=\left \langle\mathbf{v},\mathbf{T}^{*}\mathbf{w} \right \rangle,\mathbf{v}\in\mathbb{V}
$$
一个$m\times n$矩阵的共轭转置是通过互换行和列，然后对每个元素取复共轭所得到的$n\times m$矩阵

$\mathbf{M}(\mathbf{T}^{*},(\mathbf{w}_{1},\cdots,\mathbf{w}_{m}),(\mathbf{v}_{1},\cdots,\mathbf{v}_{n}))$是$\mathbf{M}(\mathbf{T},(\mathbf{v}_{1},\cdots,\mathbf{v}_{n}),(\mathbf{w}_{1},\cdots,\mathbf{w}_{m}))$的共轭转置，注意这里的基都要是规范正交基

## Chapter7 内积空间上的算子

#### 7.1 自伴算子与正规算子

算子$\mathbf{T}\in\mathbf{L}(\mathbb{V})$称为自伴的，如果$\mathbf{T}=\mathbf{T}^{*}$

算子$\mathbf{T}\in\mathbf{L}(\mathbb{V})$称为正规的，如果$\mathbf{T}\mathbf{T}^{*}=\mathbf{T}^{*}\mathbf{T}$

#### 7.2 谱定理

复谱定理：设$\mathbb{V}$是复内积空间，$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，则有$\mathbb{V}$一个由$\mathbf{T}$的特征向量组成的规范正交基当且仅当$\mathbf{T}$是正规的

实谱定理：设$\mathbb{V}$是实内积空间，$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，则$\mathbb{V}$有一个由$\mathbf{T}$的特征向量组成的规范正交基当且仅当$\mathbf{T}$是自伴的

#### 7.3 实内积空间上的正规算子

分块对角矩阵是如下形式的方阵：
$$
\begin{bmatrix}
  \mathbf{A}_{1}&  & 0\\
  & \ddots & \\
  0&  &\mathbf{A}_{m}
\end{bmatrix}
$$

#### 7.4 正算子

对于算子$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，如果$\mathbf{T}$是自伴的，并且对所有$\mathbf{v}\in\mathbb{V}$都有$\left \langle\mathbf{Tv},\mathbf{v} \right \rangle\ge0$，则称$\mathbf{T}$为正的

算子$\mathbf{S}$称为算子$\mathbf{T}$的平方根，如果满足$\mathbf{S}^{2}=\mathbf{T}$， 记$\mathbf{S}=\sqrt{\mathbf{T}}$

#### 7.5 等距同构

算子$\mathbf{S}\in\mathbf{L}(\mathbb{V})$称为等距同构，如果对于所有的$\mathbf{v}\in\mathbb{V}$都有$\left\|\mathbf{Sv}\right\|=\left\|\mathbf{v}\right\|$

#### 7.6 极分解与奇异值分解

极分解：如果$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，则有一个等距同构$\mathbf{S}\in\mathbf{L}(\mathbb{V})$使得$\mathbf{T}=\mathbf{S}\sqrt{\mathbf{T^{*}T}}$

设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$ ,$\mathbf{T}$的奇异值就是$\sqrt{\mathbf{T^{*}T}}$的特征值，而且每个特征值$\lambda$都要重复$\dim\text{null}(\mathbf{T^{*}T}-\lambda\mathbf{I})$次

## Chapter8 复空间向量上的算子

#### 8.1 广义特征向量

设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，并且$\lambda$是$\mathbf{T}$的特征值，对于向量$\mathbf{v}\in\mathbb{V}$，如果存在正整数$j$使得$(\mathbf{T}-\lambda\mathbf{I})^{j}\mathbf{v}=0$，则称$\mathbf{v}$是$\mathbf{T}$的相应于$\lambda$的广义特征向量

一个算子称为幂零的，如果它的某个幂等于$0$

#### 8.2 特征多项式

设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，并且$\lambda\in\mathbb{F}$，则对$\mathbb{V}$的每个使得$\mathbf{T}$具有上三角矩阵的基，$\lambda$在$\mathbf{T}$的矩阵对角线上都恰好出现$\dim\text{null}(\mathbf{T}-\lambda\mathbf{I})^{\dim\mathbf{V}}$次

设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，$\mathbf{T}$的特征值$\lambda$的重数定义为相应于$\lambda$的广义特征向量所构成的子空间的维数。

设$\mathbb{V}$是复向量空间，并且$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，令$\lambda_{1},\cdots,\lambda_{m}$表示$\mathbf{T}$的所有互不相同的特征值，令$d_{1},\cdots,d_{m}$表示$\mathbf{T}$的特征值的重数，则多项式$(z-\lambda_{1})^{d_{1}}\cdots(z-\lambda_{m})^{d_{m}}$称为$\mathbf{T}$的特征多项式

凯莱-哈密顿定理：设$\mathbb{V}$是复向量空间，并且$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，并设$q$是$\mathbf{T}$的特征多项式，那么$q(\mathbf{T})=0$

#### 8.3 算子的分解

#### 8.4 平方根

设$\mathbb{V}$是复向量空间，如果$\mathbf{T}\in\mathbf{L}(\mathbb{V})$是可逆的，那么$\mathbf{T}$有平方根

#### 8.5 极小多项式

多项式$a_0+a_1z+a_2z^2+\cdots+a_{m-1}z^{m-1}+z^m$称为$\mathbf{T}$的极小多项式，其中$m$是使得$(\mathbf{I},\mathbf{T},\mathbf{T}^2,\cdots,\mathbf{T}^m)$线性无关的最小整数

#### 8.6 约当形

设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$,$\mathbb{V}$的基称为$\mathbf{T}$的约当基，如果$\mathbf{T}$关于这个基有分块对角矩阵
$$
\begin{bmatrix}
  \mathbf{A}_{1}&  & 0\\
  & \ddots & \\
  0&  &\mathbf{A}_{m}
\end{bmatrix}
$$
其中每个$\mathbf{A}_j$都是形如
$$
\begin{bmatrix}
  \lambda_{1}& 1& & 0\\
 &\ddots & \ddots & \\
 &&\ddots&1\\
  0&  &&\lambda_{m}
\end{bmatrix}
$$
的上三角矩阵

## Chapter9 实向量空间上的算子

#### 9.1 方阵的特征值

设$\mathbf{A}$是一个$n\times n$矩阵，它的元素都含于$\mathbb{F}$，一个数$\lambda\in\mathbb{F}$称为$\mathbf{A}$的特征值，如果有非零的$n\times 1$矩阵$\mathbf{x}$使得$\mathbf{Ax}=\lambda\mathbf{x}$

#### 9.2 分块上三角矩阵

分块上三角矩阵是如下形式的方阵
$$
\begin{bmatrix}
  \mathbf{A}_{1}&  & *\\
  & \ddots & \\
  0&  &\mathbf{A}_{m}
\end{bmatrix}
$$
其中$\mathbf{A}_1,\cdots,\mathbf{A}_m$都是方阵

对于实向量空间上的每个算子，都有基使得该算子关于此基具有分块上三角矩阵，并且对角线上块的大小不超过$2 \times 2$

#### 9.3 特征多项式

把$1 \times 1$矩阵$\begin{bmatrix}\lambda\end{bmatrix}$的特征多项式定义为$x-\lambda$

把$2 \times 2$矩阵$\begin{bmatrix}a&c\\b&d\end{bmatrix}$的特征多项式定义为$(x-a)(x-d)-bc$

设$\mathbb{V}$是实向量空间，并设$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，如果$\alpha^2<4\beta$，并且$\mathbf{T}^2+\alpha\mathbf{T}+\mathbf{I}$不是单的，则称有序实数对$(\alpha,\beta)$ 为$\mathbf{T}$的特征对，把$\mathbf{T}$的特针对$(\alpha,\beta)$ 的重数定义为$\frac{\dim\text{null}(\mathbf{T}^2+\alpha\mathbf{T}+\mathbf{I})^{\dim\mathbb{V}}}{2}$

$\mathbf{T}\in\mathbf{L}(\mathbb{V})$的特征多项式为其分块上三角矩阵$\mathbf{A}_1,\cdots,\mathbf{A}_m$的特征多项式之积

## Chapter10 迹与行列式

#### 10.1 基变换

如果$(\mathbf{u}_1,\cdots,\mathbf{u}_n)$和$(\mathbf{v}_1,\cdots,\mathbf{v}_n)$都是的基，那么$\mathbf{M}(\mathbf{I},(\mathbf{u}_1,\cdots,\mathbf{u}_n),(\mathbf{v}_1,\cdots,\mathbf{v}_n))$是可逆的，并且$\mathbf{M}(\mathbf{I},(\mathbf{u}_1,\cdots,\mathbf{u}_n),(\mathbf{v}_1,\cdots,\mathbf{v}_n))^{-1}=\mathbf{M}(\mathbf{I},(\mathbf{v}_1,\cdots,\mathbf{v}_n),(\mathbf{u}_1,\cdots,\mathbf{u}_n))$

#### 10.2 迹

对于$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，$\mathbf{T}$的特征多项式中$z^{n-1}$的系数的相反数称为$\mathbf{T}$的迹，记作$\text{trace}\mathbf{T}$

定义方阵$\mathbf{A}$的迹为其对角线元素之和，记为$\text{trace}\mathbf{A}$

算子关于一个基的矩阵的对角线元素之和并不依赖于这个基的选取

#### 10.3 算子的行列式

对于$\mathbf{T}\in\mathbf{L}(\mathbb{V})$，定义$\mathbf{T}$的行列式为$\mathbf{T}$的特征多项式的常数项乘以$(-1)^{\dim\mathbb{V}}$，记为$\det\mathbf{T}$

一个算子是可逆的当且仅当它的行列式不等于零

#### 10.4 矩阵的行列式

#### 10.5 体积

