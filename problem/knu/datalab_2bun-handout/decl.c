#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define TMin INT_MIN
#define TMax INT_MAX

#include "btest.h"
#include "bits.h"

test_rec test_set[] = {
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
 {"isNotEqual", (funct_t) isNotEqual, (funct_t) test_isNotEqual, 2,
    "! ~ & ^ | + << >>", 6, 2,
  {{TMin, TMax},{TMin,TMax},{TMin,TMax}}},
//#include "allEvenBits.c" // anyOddBit.c
 {"allOddBits", (funct_t) allOddBits, (funct_t) test_allOddBits, 1,
    "! ~ & ^ | + << >>", 12, 2,
  {{TMin, TMax},{TMin,TMax},{TMin,TMax}}},
 {"is_any_odd_bit_set", (funct_t) is_any_odd_bit_set, (funct_t) test_is_any_odd_bit_set, 1,
    "! ~ & ^ | + << >>", 12, 2,
  {{TMin, TMax},{TMin,TMax},{TMin,TMax}}},
//#include "is_all_even_bits_set.c"	// allEvenBit.c
//#include "bitwise_not.c"	// bang.c
//#include "abs_value_int.c" // absVal.c
//#include "counting_bits.c" //bitCount.c
 {"bang", (funct_t) bang, (funct_t) test_bang, 1,
    "~ & ^ | + << >>", 12, 4,
  {{TMin, TMax},{TMin,TMax},{TMin,TMax}}},
//%#include "isTmax.c" // isTmax.c
 {"isTmin", (funct_t) isTmin, (funct_t) test_isTmin, 1, "! ~ & ^ | +", 10, 1,
  {{TMin, TMax},{TMin,TMax},{TMin,TMax}}},
//#include "isNegative.c"	// getByte.c
 {"isPositive", (funct_t) isPositive, (funct_t) test_isPositive, 1,
    "! ~ & ^ | + << >>", 8, 2,
  {{TMin, TMax},{TMin,TMax},{TMin,TMax}}},
//#include "negative_one.c"	// minusOne
 {"examine_fitness_twos_comple", (funct_t) examine_fitness_twos_comple, (funct_t) test_examine_fitness_twos_comple, 2,
    "! ~ & ^ | + << >>", 15, 2,
  {{TMin, TMax},{1,32},{TMin,TMax}}},
//#include "examine_sign_twos_comple.c"	// sign.c
//#include "isLess.c"
 {"isGreater", (funct_t) isGreater, (funct_t) test_isGreater, 2,
    "! ~ & ^ | + << >>", 24, 3,
  {{TMin, TMax},{TMin,TMax},{TMin,TMax}}},
//#include "ternary_op.c"	// conditional.c
//#include "abs_value_float.c"	// floatAbsVal.c
//#include "two_times_float.c"	// float_twice.c
 {"is_equal_float", (funct_t) is_equal_float, (funct_t) test_is_equal_float, 2,
    "$", 25, 2,
     {{1, 1},{1,1},{1,1}}},
 {"from_int_to_float", (funct_t) from_int_to_float, (funct_t) test_from_int_to_float, 1,
    "$", 30, 4,
     {{1, 1},{1,1},{1,1}}},
  {"", NULL, NULL, 0, "", 0, 0,
   {{0, 0},{0,0},{0,0}}}
};
