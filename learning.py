# coding=utf-8
"""
- Purpose:   Describe the purpose of this module in one line.
- Author:    VIPSH.
- Created:   22-04-2023.
- Copyright: (c) Barco 2023.
- Licence:   All Rights Reserved.


If needed/desired/indicated/beneficial/... extra details can be added here.
If not remove this whole section

.. note::

    Rst/Sphinx keywords can be used but don't go crazy. The same remarks as in
    https://mx.barco.com:4700/knowledge_base/adding_docstring_to_function.html#more-extensive-example
    are valid.

.. warning::

    With rst indentation and blank space is important. Don't remove the blank
    before/after. Also the blank lines around the
    directives like ".. note::" and ".. warning::" are important.

"""


class AClass(object):
    """ Class AClass (this comment is manadatory) """

    def a_method(self, arg1, arg2):
        """
        Summary line, ends with a period.

        Detailed description and extra information (optional).

        Multiple paragraphs allowed.
        Also have a look at https://mx.barco.com:4700/knowledge_base/adding_docstring_to_function.html

        :param arg1: Describe what arg1 does and what should be passed to it.
        :param arg2: Describe what arg2 does and what should be passed to it.
        :return: Describe what the function returns. Delete this line completely if nothing is returned.
        """
        self.do_something()
        print("Inside a_method")
        print("something ...!!")
