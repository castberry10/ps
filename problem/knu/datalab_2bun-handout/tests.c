/* Testing Code */

#include <limits.h>
#include <math.h>

/* Routines used by floation point test code */

/* Convert from bit level representation to floating point number */
float u2f(unsigned u) {
  union {
    unsigned u;
    float f;
  } a;
  a.u = u;
  return a.f;
}

/* Convert from floating point number to bit-level representation */
unsigned f2u(float f) {
  union {
    unsigned u;
    float f;
  } a;
  a.f = f;
  return a.u;
}

/* Copyright (C) 1991-2020 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <https://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 10.0.0.  Version 10.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2017, fifth edition, plus
   the following additions from Amendment 1 to the fifth edition:
   - 56 emoji characters
   - 285 hentaigana
   - 3 additional Zanabazar Square characters */
//#include "isEqual.c"	
int test_isNotEqual(int x, int y)
{
  return x != y;
}
//#include "allEvenBits.c" // anyOddBit.c
int test_allOddBits(int x) {
  int i;
  for (i = 1; i < 32; i+=2)
      if ((x & (1<<i)) == 0)
   return 0;
  return 1;
}
int test_is_any_odd_bit_set(int x) {
    int i;
    for (i = 1; i < 32; i+=2)
        if (x & (1<<i))
      return 1;
    return 0;
}
//#include "is_all_even_bits_set.c"	// allEvenBit.c
//#include "bitwise_not.c"	// bang.c
//#include "abs_value_int.c" // absVal.c
//#include "counting_bits.c" //bitCount.c
int test_bang(int x)
{
  return !x;
}
//%#include "isTmax.c" // isTmax.c
int test_isTmin(int x) {
    return x == 0x80000000;
}
//#include "isNegative.c"	// getByte.c
int test_isPositive(int x) {
  return x > 0;
}
//#include "negative_one.c"	// minusOne
int test_examine_fitness_twos_comple(int x, int n)
{
  int TMin_n = -(1 << (n-1));
  // This convoluted way of generating TMax avoids overflow
  int TMax_n = (int) ((1u << (n-1)) - 1u);
  return x >= TMin_n && x <= TMax_n;
}
//#include "examine_sign_twos_comple.c"	// sign.c
//#include "isLess.c"
int test_isGreater(int x, int y)
{
  return x > y;
}
//#include "ternary_op.c"	// conditional.c
//#include "abs_value_float.c"	// floatAbsVal.c
//#include "two_times_float.c"	// float_twice.c
int test_is_equal_float(unsigned uf, unsigned ug) {
    float f = u2f(uf);
    float g = u2f(ug);
    return f == g;
}
unsigned test_from_int_to_float(int x) {
  float f = (float) x;
  return f2u(f);
}
