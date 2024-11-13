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
int isNotEqual(int, int);
int test_isNotEqual(int, int);
//#include "allEvenBits.c" // anyOddBit.c
int allOddBits();
int test_allOddBits();
int is_any_odd_bit_set();
int test_is_any_odd_bit_set();
//#include "is_all_even_bits_set.c"	// allEvenBit.c
//#include "bitwise_not.c"	// bang.c
//#include "abs_value_int.c" // absVal.c
//#include "counting_bits.c" //bitCount.c
int bang(int);
int test_bang(int);
//%#include "isTmax.c" // isTmax.c
int isTmin(int);
int test_isTmin(int);
//#include "isNegative.c"	// getByte.c
int isPositive(int);
int test_isPositive(int);
//#include "negative_one.c"	// minusOne
int examine_fitness_twos_comple(int, int);
int test_examine_fitness_twos_comple(int, int);
//#include "examine_sign_twos_comple.c"	// sign.c
//#include "isLess.c"
int isGreater(int, int);
int test_isGreater(int, int);
//#include "ternary_op.c"	// conditional.c
//#include "abs_value_float.c"	// floatAbsVal.c
//#include "two_times_float.c"	// float_twice.c
int is_equal_float(unsigned, unsigned);
int test_is_equal_float(unsigned, unsigned);
unsigned from_int_to_float(int);
unsigned test_from_int_to_float(int);
