# Notes 1

Split expression folding into 2 phases:

- Rewrite expr tree.
- Expr Simply.

___
First phase is to _modify/mutate_ directly the ast tree (not recommended). Fold some constant.

- Example: 1 + 2 + a + 4 + 5 * 4   =>  3 + a + 9

Float folding may cause some errors.
Because python's float is actually double precision floating point number, unlike like java float, which is single.
___
Second phase is to simplify the expression by constant propagation.

- Example:
  - final a = 3
  - 1 + 2 + a + 4 + 5 * 4 => 30
