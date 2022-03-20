# 《高等代数》丘维声

## Chapter1 线性方程组

#### 1.1 解线性方程组的矩阵消元法

$n$个未知量的线性方程组称为$n$元线性方程组，一般形式为：
$$
\left\{\begin{array}{**lr**}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n=b_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n=b_2\\
\cdots\cdots\\
a_{n1}x_1+a_{n2}x_2+\cdots+a_{nn}x_n=b_n
\end{array}\right.
$$
对于上述方程组，如果$x_1,x_2,\cdots,x_n$分别用数$c_1,c_2,\cdots,c_n$代入后，每个方程变为恒等式，那么称$n$元有序数组$(c_1,c_2,\cdots,c_n)'$是上述线性方程组的一个解，$()'$表示将解写成一列的形式，方程组所有解的集合称为这个方程组的解集

线性方程组的初等变换：1）把一个方程的倍数加到另一个方程上 2）互换两个方程的位置 3）用一个非零数乘某一个方程

简化行阶梯形矩阵：1）其为阶梯形矩阵 2）其每个非零行的主元都为1  3）每个主元所在列的其余元素都是0

一般解：如果$n$元方程组的一部分未知量可以用其余未知量的至多一次的式子来表示，那么把这个表达式称为这个线性方程组的一般解，这些其余未知量称为自由未知量（例子参考p11）

#### 1.2 线性方程组的解的情况及其判别准则

解的情况：系数和常数项为有理数（或实数，复数）的$n$元线性方程组的解的情况有且只有三种可能：无解，有唯一解，有无穷多解，将方程的增广矩阵化为阶梯阵后，如果出现"0=d"（d为非零数）的情况，则无解，否则有解，当有解时，如果阶梯形矩阵的非零行数目$r$等于未知量数目$n$，则有唯一解，如果$r<n$，则有无穷多解

相容：如果一个线性方程组有解，那么称它是相容的，否则称它是不相容的

齐次线性方程组：常数项全为0的线性方程组称为齐次线性方程组，$(0,0,\cdots,0)'$是齐次线性方程组的一个解，称为零解，其余解（如果有）称为非零解

#### 1.3 数域

复数集的一个子集$\mathbb{K}$如果满足：

$(1)0,1\in\mathbb{K}$

$(2)a,b\in\mathbb{K}\Rightarrow a\pm b,ab\in\mathbb{K}$

$(3)a,b\in\mathbb{K},b\ne0\Rightarrow \frac ab\in\mathbb{K}$

那么，称$\mathbb{K}$为一个数域

## Chapter2 行列式

#### 2.1 n元排列

在$n$元排列$a_1a_2\cdots a_n$中，从左到右任取一对数$a_ia_j$（其中$i<j$），如果$a_i>a_j$，那么称这一对数构成逆序，一个$n$元排列中逆序的总数称为逆序数，记作$\tau(a_1a_2\cdots a_n)$，逆序数为奇数的排列称为奇排列，否则称为偶排列

#### 2.2 n阶行列式的定义

$n$级矩阵$\mathbf{A}=(a_{ij})$的行列式如下定义，记作$|\mathbf{A}|$或$\det \mathbf{A}$：
$$
\begin{vmatrix}
 a_{11} & a_{12} & \cdots & a_{1n}\\
 a_{21} & a_{22} & \cdots & a_{2n}\\
 \vdots & \vdots &  & \vdots\\
 a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}=\sum_{j_1j_2\cdots j_n}(-1)^{\tau(j_1j_2\cdots j_n)}a_{1j_1}a_{2j_2}\cdots a_{nj_n}
$$

#### 2.3 行列式的性质

行列互换（即矩阵按对角线翻转），行列式的值不变

行列式一行或一列的公因子可以提出去

行列式中若某一行是两组数的和，则此行列式等于两个行列式的和（具体见p40）

#### 2.4 行列式按一行（列）展开

余子式：$n$级矩阵$\mathbf{A}$中，划去第$i$行和第$j$列，剩下的元素按原来次序组成的$n-1$级矩阵的行列式称为矩阵$\mathbf{A}$的$(i,j)$元的余子式，记作$M_{ij}$，令$A_{ij}=(-1)^{i+j}M_{ij}$，称其称为矩阵$\mathbf{A}$的$(i,j)$元的代数余子式

$n$级矩阵$\mathbf{A}$的行列式$|\mathbf{A}|$等于它的第$i$行元素与自己的代数余子式的乘积之和，即：
$$
|\mathbf{A}|=a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in}=\sum_{j=1}^na_{ij}A_{ij}
$$
范德蒙德(Vandermonde)行列式（证明用数学归纳法）：
$$
\begin{vmatrix}
 1 & 1 & 1 & \cdots & 1\\
 a_1 & a_2 & a_3 & \cdots & a_n\\
 a_1^2 & a_2^2 & a_3^2 & \cdots & a_n^2 \\
 \vdots & \vdots & \vdots &  & \vdots\\
 a_1^{n-2} & a_2{n-2} & a_3^{n-2} & \cdots & a_n^{n-2} \\ 
 a_1^{n-1} & a_2{n-1} & a_3^{n-1} & \cdots & a_n^{n-1}
\end{vmatrix}=\prod_{1\le j<i\le n}(a_i-a_j)
$$

#### 2.5 克拉默法则

数域$\mathbb{K}$上$n$个方程的$n$元线性方程组有唯一解的充分必要条件是其系数矩阵的行列式$|\mathbf{A}|\ne 0$

克拉默法则：把$n$个方程的$n$元线性方程组的系数矩阵$\mathbf{A}$的第$j$列换成常数项，得到的矩阵记作$\mathbf{B}_j$

$n$个方程的$n$元线性方程组的系数行列式$|\mathbf{A}|\ne 0$时，其唯一解为$(\frac{|\mathbf{B}_1|}{|\mathbf{A}|},\frac{|\mathbf{B}_2|}{|\mathbf{A}|},\cdots,\frac{|\mathbf{B}_n|}{|\mathbf{A}|})'$

#### 2.6 行列式按k行（列）展开

$k$阶子式：$n$级矩阵$\mathbf{A}$中任意取定$k$行，$k$列，位于这些行和列的交叉处的$k^2$个元素按原来的排法组成的$k$级矩阵的行列式称为$\mathbf{A}$的一个$k$阶子式，记作$\mathbf{A}\begin{pmatrix}i_1,i_2,\cdots,i_k\\j_1,j_2,\cdots,j_k\end{pmatrix}$

## Chapter3 n维向量空间$\mathbb{K}^n$

#### 3.1 n维向量空间$\mathbb{K}^n$及其子空间

取定一个数域$\mathbb{K}$，设$n$时任意给定的一个正整数，令$\mathbb{K}^n=\{(a_1,a_2,\cdots,a_n)|a_i\in\mathbb{K},i=1,2,\cdots,n\}$

在$\mathbb{K}^n$中规定加法运算如下$(a_1,a_2,\cdots,a_n)+(b_1,b_2,\cdots,b_n)=(a_1+b_1,a_2+b_2,\cdots,a_n+b_n)$

在$\mathbb{K}$的元素与$\mathbb{K}^n$的元素之间规定数量乘法运算如下$k(a_1,a_2,\cdots,a_n)=(a_1,a_2,\cdots,a_n)$

把$(0,0,\cdots,0)$记作$\mathbb{K}^n$的零元，称$-\alpha$是$\alpha$的负元

$n$维向量空间：数域$\mathbb{K}$上所有$n$元有序数组组成的集合$\mathbb{K}^n$，连同定义在它上面的加法运算和数乘运算，成为数域$\mathbb{K}$上的一个$n$维向量空间，$\mathbb{K}^n$的元素称为$n$维向量，设向量$\alpha=(a_1,a_2,\cdots,a_n)$，称$a_i$是$\alpha$的第$i$个分量

线性表出：在$\mathbb{K}^n$中，给定向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$，对于$\beta\in\mathbb{K}^n$，如果存在$\mathbb{K}$中一组数$c_1,c_2,\cdots,c_s$使得$\beta=c_1a_1+c_2a_2+\cdots+c_sa_s$，那么称$\beta$可以由$a_1,a_2,\cdots,a_s$线性表出

可以把线性方程组有没有解的问题归结为：常数项列向量$\beta$能不能由系数矩阵的列向量组线性表出

子空间：$\mathbb{K}^n$的一个非空子集$\mathbb{U}$如果满足：$1)\alpha,\gamma\in\mathbb{U}\Rightarrow\alpha+\gamma\in\mathbb{U}\;\;2)\alpha\in\mathbb{U},k\in\mathbb{K}\Rightarrow k\alpha\in\mathbb{U}$，那么称$\mathbb{U}$是$\mathbb{K}^n$的一个线性子空间，简称子空间

张成：$\mathbb{K}^n$中，向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$的所有线性组合组成的集合$\mathbb{W}$是$\mathbb{K}^n$的一个子空间，称它为$\alpha_1,\alpha_2,\cdots,\alpha_s$张成的子空间，记作$\langle\alpha_1,\alpha_2,\cdots,\alpha_s\rangle$

#### 3.2 线性相关与线性无关的向量组

线性无关：如果从$k_1\alpha_1+k_2\alpha_2+\cdots+k_s\alpha_s=0$可以推出所有的系数$k_1,k_2,\cdots,k_s$全为0，那么称$\alpha_1,\alpha_2,\cdots,\alpha_s$是线性无关的

#### 3.3 极大线性无关组，向量组的秩

极大线性无关组：向量组的一个部分组称为一个极大线性无关组，如果这个部分组本身是线性无关的，但是从这个向量组的其余向量中任取一个添进去，得到的新的部分组线性相关

向量组等价：如果向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$的每一个向量都可以由向量组$\beta_1,\beta_2,\cdots,\beta_r$线性表出，那么称向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$可以由向量组$\beta_1,\beta_2,\cdots,\beta_r$线性表出，如果向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$与向量组$\beta_1,\beta_2,\cdots,\beta_r$可以互相线性表出，那么称向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$与向量组$\beta_1,\beta_2,\cdots,\beta_r$等价，记作$\{\alpha_1,\alpha_2,\cdots,\alpha_s\}\cong\{\beta_1,\beta_2,\cdots,\beta_r\}$

向量组的秩：向量组的极大线性无关组所含向量的个数称为这个向量组的秩，向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$的秩记作$\text{rank}\{\alpha_1,\alpha_2,\cdots,\alpha_s\}$

#### 3.4 向量空间$\mathbb{K}^n$及其子空间的基与维数

基：设$\mathbb{U}$是$\mathbb{K}^n$的一个子空间，如果$\alpha_1,\alpha_2,\cdots,\alpha_r\in\mathbb{U}$，并且满足：1）$\alpha_1,\alpha_2,\cdots,\alpha_r$线性无关 2）$\mathbb{U}$中每一个向量都可以由$\alpha_1,\alpha_2,\cdots,\alpha_r$线性表出 那么称$\alpha_1,\alpha_2,\cdots,\alpha_r$是$\mathbb{U}$的一个基

维数：$\mathbb{K}^n$的非零子空间$\mathbb{U}$的一个基所含向量的个数称为$\mathbb{U}$的维数，记作$\dim\mathbb{U}$

#### 3.5 矩阵的秩

矩阵$\mathbf{A}$的行（列）秩等于$\mathbf{A}$的行（列）空间的维数

矩阵的秩：矩阵$\mathbf{A}$的行秩与列秩统称为$\mathbf{A}$的秩，记作$\text{rank}(\mathbf{A})$

#### 3.6 线性方程组有解的充分必要条件

数域$\mathbb{K}$上线性方程组$x_1\alpha_1+x_2\alpha_2+\cdots+x_n\alpha_n=\beta$有解的充分必要条件是：它的系数矩阵与增广矩阵的秩相等

#### 3.7 齐次线性方程组的解集的结构

基础解系：齐次线性方程组有非零解时，如果它的有限多个解$\eta_1,\eta_2,\cdots,\eta_t$满足：1）$\eta_1,\eta_2,\cdots,\eta_t$线性无关 2）齐次线性方程组的每一个解都可以由$\eta_1,\eta_2,\cdots,\eta_t$线性表出 那么称$\eta_1,\eta_2,\cdots,\eta_t$是齐次线性方程组的一个基础解系

数域$\mathbb{K}$上$n$元齐次线性方程组的解空间$\mathbb{W}$的维数为$\dim\mathbb{W}=n-\text{rank}(\mathbf{A})$

#### 3.8 非齐次线性方程组的解集的结构

##  Chapter4 矩阵的运算

#### 4.1 矩阵的加法、数量乘法与乘法运算

乘法：设$\mathbf{A}=(a_{ij})_{s\times n},\mathbf{B}=(b_{ij})_{n\times m}$，令$\mathbf{C}=(c_{ij})_{s\times m}$，其中：
$$
c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\cdots+a_{in}b_{nj}=\sum_{k=1}^na_{ik}b_{kj},i=1,2,\cdots,s;j=1,2,\cdots,m
$$
单位矩阵：主对角线上元素都是1，其余元素都是0的$n$级矩阵称为$n$级单位矩阵，记作$\mathbf{I}_n$，简记为$\mathbf{I}$

可交换：对于两个矩阵$\mathbf{A},\mathbf{B}$，如果$\mathbf{AB}=\mathbf{BA}$，则称$\mathbf{A}$与$\mathbf{B}$可交换

#### 4.2 特殊矩阵

对角矩阵：主对角线以外的元素全为0的方阵称为对角矩阵，记作$\text{diag}\{d_1,d_2,\cdots,d_n\}$

基本矩阵：只有一个元素是1，其余元素全为0的矩阵记作基本矩阵，记作$\mathbf{E}_{ij}$

上（下）三角矩阵：主对角线下（上）元素全为0的方阵称为上（下）三角矩阵

初等矩阵：由单位矩阵经过一次初等行（列）变换得到的矩阵称为初等矩阵

对称矩阵：一个矩阵$\mathbf{A}$如果满足$\mathbf{A}^\text{T}=\mathbf{A}$，那么称$\mathbf{A}$是对称矩阵

斜对称矩阵：一个矩阵$\mathbf{A}$如果满足$\mathbf{A}^\text{T}=-\mathbf{A}$，那么称$\mathbf{A}$是斜对称矩阵

#### 4.3 矩阵乘积的秩和行列式

设$\mathbf{A}=(a_{ij})_{s\times n},\mathbf{B}=(b_{ij})_{n\times m}$，则$\text{rank}(\mathbf{AB})\le \min\{\text{rank}(\mathbf{A}),\text{rank}(\mathbf{B})\}$

设$\mathbf{A}=(a_{ij})_{n\times n},\mathbf{B}=(b_{ij})_{n\times n}$，则$|\mathbf{AB}|=|\mathbf{A}||\mathbf{B}|$

#### 4.4 可逆矩阵

可逆矩阵：对于数域$\mathbb{K}$上的矩阵$\mathbf{A}$，如果存在数域$\mathbb{K}$上的矩阵$\mathbf{B}$，使得$\mathbf{AB}=\mathbf{BA}=\mathbf{I}$，那么称$\mathbf{A}$是可逆矩阵，$\mathbf{A}^{-1}=\mathbf{B},\mathbf{B}^{-1}=\mathbf{A}$，$n$级矩阵可逆的充分必要条件是$|\mathbf{A}|\ne 0$

#### 4.5 矩阵的分块

#### 4.6 正交矩阵·欧几里得空间$\mathbb{R}^n$

正交矩阵：实数域上的$n$级矩阵$\mathbf{A}$如果满足$\mathbf{A}^\text{T}\mathbf{A}=\mathbf{I}$，那么称$\mathbf{A}$为正交矩阵

内积：在$\mathbb{R}^n$中，任给$\alpha=(a_1,a_2,\cdots,a_n),\beta=(b_1,b_2,\cdots,b_n)$，规定$(\alpha,\beta)=a_1b_1+a_2b_2+\cdots+a_nb_n=\alpha\beta^\text{T}$，这个二元实值函数$(\alpha,\beta)$称为$\mathbb{R}^n$的一个内积（通常称为标准内积）

欧几里得空间：当$n$维向量空间有了标准内积之后，就称$\mathbb{R}^n$为一个欧几里得空间

向量的长度：在欧几里得空间$\mathbb{R}^n$中，向量$\alpha$的长度$|\alpha|$规定为$|\alpha|=\sqrt{(\alpha,\alpha)}$

正交向量组：由非零向量组成的向量组如果其中每两个不同的向量都正交，那么它们为正交向量组

正交基：欧几里得空间$\mathbb{R}^n$中，$n$个向量组成的正交向量组一定是$\mathbb{R}^n$的一个基，称它为正交基

施密特正交化：设$\alpha_1,\alpha_2,\cdots,\alpha_s$是欧几里得空间$\mathbb{R}^n$中一个线性无关的向量组，令$\beta_1=\alpha_1,\beta_2=\alpha_2-\frac{(\alpha_2,\beta_1)}{(\beta_1,\beta_1)}\beta_1,\cdots\cdots,\beta_s=\alpha_s-\sum_{j-1}^{s-1}\frac{(\alpha_s,\beta_j)}{(\beta_j,\beta_j)}\beta_j$

则$\beta_1,\beta_2,\cdots,\beta_s$是正交向量组，并且$\beta_1,\beta_2,\cdots,\beta_s$和$\alpha_1,\alpha_2,\cdots,\alpha_s$等价

#### 4.7 $\mathbb{K}^n$到$\mathbb{K}^s$的线性映射

映射：设$S$和$S'$是两个集合，如果存在一个对应法则$f$，使得集合中每一个元素$a$，都有集合$S'$中唯一确定的元素$b$与它对应，那么称$f$是集合$S$到$S'$的一个映射，记作$f:S\longrightarrow S',a\mapsto b$，其中$b$称为$a$在$f$下的象，$a$称为$b$在$f$下的一个原象，$a$在$f$下的象用符号$f(a)$或$fa$表示，于是映射$f$也可记成$f(a)=b,a\in S$

值域：$S$的所有元素在$f$下的象组成的集合叫做$f$的值域或$f$的象，记作$f(S)$或$\text{Im}f$

恒等映射：映射$f:S\longrightarrow S$如果把$S$中的每一个元素对应到它自身，即$\forall x\in S,f(x)=x$，那么称$f$是恒等映射，记作$1_S$

映射合成：相继施行映射$g:S\longrightarrow S'$和$f:S'\longrightarrow S''$，得到$S$到$S''$的一个映射，称为$f$与$g$的乘积（或合成），记作$fg$，即$(fg)(a)=f(g(a)),\forall a\in S$

逆映射：设$f:S\longrightarrow S'$，如果存在一个映射$g:S'\longrightarrow S$，使得$fg=1_{S'},gf=1_S$，那么称映射$f$是可逆的，此时称$g$为$f$的一个逆映射

线性映射：数域$\mathbb{K}$上的向量空间 $\mathbb{K}^n$到$\mathbb{K}^s$的一个映射$\sigma$如果保持加法和数量乘法，即$\forall \alpha,\beta \in \mathbb{K}^n,k\in\mathbb{K},\sigma(\alpha+\beta)=\sigma(\alpha)+\sigma(\beta),\sigma(k\alpha)=k\sigma(\alpha)$，那么称$\sigma$是 $\mathbb{K}^n$到$\mathbb{K}^s$的一个线性映射

核：设$\sigma$是 $\mathbb{K}^n$到$\mathbb{K}^s$的一个线性映射，$\mathbb{K}^n$的一个子集$\{\alpha\in\mathbb{K}|\sigma(\alpha)=0\}$称为映射$\sigma$的核，记作$\text{Ker}\sigma$

## Chapter5 矩阵的相似与相抵

#### 5.1 等价关系与集合的划分

笛卡尔积：设$S,M$是两个集合，则集合$\{(a,b)|a\in S,b \in M\}$称为$S$与$M$的笛卡尔积，记作$S\times M$

二元关系：设$S$是一个非空集合，我们把$S\times S$的一个子集$W$叫做$S$上的一个二元关系，如果$(a,b)\in W$，那么称$a$和$b$有$W$关系，当$a$和$b$有$W$关系时，记作$aWb$或$a\sim b$

等价关系：集合$S$上的一个二元关系$“\sim”$如果具有下述性质：$\forall a,b,c\in S,a\sim a ,a\sim b \Rightarrow b \sim a ,a\sim b\;b\sim c\Rightarrow a\sim c$（反身，对称，传递）那么称$“\sim”$是$S$上的一个等价关系

等价类：设$“\sim”$是集合$S$上的一个等价关系，$a\sim S$ ，令$\bar{a} =\{x\in S|x\sim a\}$，称$\bar{a}$是由$a$确定的等价类

划分：如果集合$S$是一些非空子集$S_i(i\in I)$的并集，并且其中不相等的子集一定不相交，那么称集合$\{S_i|i\in I\}$是$S$的一个划分，记作$\pi(S)$

商集：设$“\sim”$是集合$S$上的一个等价关系，由所有等价类组成的集合称为$S$对于关系$“\sim”$的商集，记作$“S/\sim”$

#### 5.2 矩阵的相抵

数域$\mathbb{K}$上所有$s\times n$矩阵组成的集合记作$\mathbf{M}_{s\times n}(\mathbb{K})$

相抵：对于数域$\mathbb{K}$上的$s\times n$矩阵$\mathbf{A}$和$\mathbf{B}$，如果从$\mathbf{A}$经过一系列初等行变换和初等列变换能变成矩阵$\mathbf{B}$，那么称$\mathbf{A}$与$\mathbf{B}$是相抵的，记作$\mathbf{A}\sim \mathbf{B}$

相抵是集合$\mathbf{M}_{s\times n}(\mathbb{K})$上的一个二元关系，其也是等价关系，在相抵关系下，矩阵$\mathbf{A}$的等价类称为$\mathbf{A}$的相抵类

设数域$\mathbb{K}$上的$s\times n$矩阵$\mathbf{A}$的秩为$r$,那么$\mathbf{A}$相抵于$\begin{pmatrix}\mathbf{I}_r& 0\\0&0\end{pmatrix}$，其被称为相抵标准型

设数域$\mathbb{K}$上的$s\times n$矩阵$\mathbf{A}$的秩为$r$,则存在$\mathbb{K}$上的$s$级，$n$级可逆矩阵$\mathbf{P},\mathbf{Q}$，使得$\mathbf{A}=\mathbf{P}\begin{pmatrix}\mathbf{I}_r& 0\\0&0\end{pmatrix}\mathbf{Q}$