# Primitive Root Checker
This program takes two integers $g$ and $p$ as input and outputs whether or not $g$ is a primitive root of $p$.

# Example
$g=2$ and $p=5$
<br>
<br>
$2^1\ mod\ 5 = 2$
<br>
$2^2\ mod\ 5 = 4$
<br>
$2^3\ mod\ 5 = 3$
<br>
$2^4\ mod\ 5 = 1$

If we're able to plug in any coprime $i$, with the boundaries $1 \leq i < p-1$ into the following expression:
$$g^i\ mod\ p$$
And the output always differs, then $g$ is a primitive root of $p$. So, with respect to this, if we examine the output above, we can clearly see that $2$ is a primitive root of $5$.

![image](https://user-images.githubusercontent.com/56341190/188978526-087fba9a-3502-42fa-aa6d-24ebf3571d55.png)


# How to use
1) <code>~$ git clone https://github.com/philipsinnott/primitive-root-checker</code>
2) <code>~$ cd primitive-root-checker</code>
3) <code>~$ py main.py</code>
