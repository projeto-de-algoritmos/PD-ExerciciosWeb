# [2272 . Substring com maior variação](https://leetcode.com/problems/substring-with-largest-variance/)
dificuldade : Difícil

A variância de uma string é definida como a maior diferença entre o número de ocorrências de quaisquer 2 caracteres presentes na string. Observe que os dois caracteres podem ou não ser iguais.
Dada uma string sque consiste apenas em letras minúsculas do inglês, retorne a maior variação possível entre todas as substrings de s .
Uma substring é uma sequência contígua de caracteres dentro de uma string.

#
*Exemplo 1:*
Entrada: s = "aababbb"
 Saída: 3
 Explicação:
Todas as variações possíveis junto com suas respectivas substrings estão listadas abaixo:
- Variação 0 para substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb" e "bbb".
- Variação 1 para substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb" e "bab".
- Variação 2 para substrings "aaba", "ababbb", "abbb" e "babb".
- Variação 3 para substring "babbb".
Como a maior variância possível é 3, nós a retornamos.

#
*Exemplo 2:*

Entrada: s = "abcde"
 Saída: 0
 Explicação:
Nenhuma letra ocorre mais de uma vez em s, então a variação de cada substring é 0.

## Restrições:

1 <= s.length <= 10⁴
sconsiste em letras minúsculas do inglês.
