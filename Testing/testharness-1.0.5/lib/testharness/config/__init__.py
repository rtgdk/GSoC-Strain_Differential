"""
Python testharness Module.

This module provides the default configuration the testharness uses.

Copyright (C) 2001-2006 Oisin Mulvihill.
Email: oisin.mulvihill@gmail.com

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library (see the file LICENSE.TXT); if not,
write to the Free Software Foundation, Inc., 59 Temple Place,
Suite 330, Boston, MA 02111-1307 USA.

"""

filename="tester.ini"

default="""
#
# Template test harness config file.
#
[TestHarness]
#If this is yes the test harness will exit after the first failure.
assert_equals_failure_causes_exit = yes
tests =

"""
