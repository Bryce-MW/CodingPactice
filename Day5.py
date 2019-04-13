"""
Prompt:
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it
holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has
an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference
pointer functions that converts between nodes and memory addresses.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import Dict, Any, Union
import collections.abc

pointer_store: Dict[int, Any] = {}
ref_counts: Dict[int, int] = collections.defaultdict(lambda: 0)


def get_pointer(pointed: Any) -> int:
    """
    In CPython, this actually returns the memory address, otherwise not.
    :param pointed: object to return pointer to
    :return: pointer to object
    """
    pointer_store[id(pointed)] = pointed
    return id(pointed)


def dereference_pointer(pointer: int) -> Any:
    """
    Technically, this is not really dereferenceing a pointer and there are better ways to do this.
    :param pointer: the pointer to return the object of
    :return: the object pointed to by the pointer
    """
    return pointer_store[pointer]


class Element:
    """
    An element of a doubly linked list using XOR. A doubly linked list using XOR only has one pointed called Both.
    There are also booleans for if the element is the start or the end of one of these lists.
    """

    def __init__(self, element: Any):
        """
        Creates a new `Element` with no pointer that is both the first and last element in some list. The value of the
        `Element` is set.
        :param element: the value to set the `Element` to
        """
        self.element: Any = element
        self.both: int = 0
        self.start: bool = True
        self.end: bool = True


class DoublyLinkedList(collections.abc.MutableSequence):
    """
    A doubly linked list which is of type `collections.abc.MutableSequence` meaning that it may be used like most other
    mutable sequences but much slower.
    """

    def __init__(self):
        """
        Creates a new Doubly Linked List with no `Element`s.
        """
        self.start: Union[int, None] = None

    def add(self, element: Any) -> None:
        """
        Add a new `Element` to the doubly linked list
        :param element: `Element` value to add
        :return: None
        """
        if self.start is None:
            self.start, ref_counts[self.start] = get_pointer(Element(element))
            ref_counts[self.start] += 1
        else:
            past_pointer: int = 0
            current_element: Element = dereference_pointer(self.start)
            while not current_element.end:
                new_element: Element = dereference_pointer(current_element.both ^ past_pointer)
                past_pointer = get_pointer(current_element)
                current_element = new_element
            new_element: Element = Element(element)
            current_element.both ^= get_pointer(new_element)
            current_element.end = False
            new_element.start = False
            new_element.both = get_pointer(current_element)
            ref_counts[get_pointer(new_element)] += 1

    def get(self, index: int, element: bool = False) -> Any:
        """
        Gets the `Element` at the specified index.
        :param element: boolean of if the raw `Element` is wanted
        :param index: the index from which to get the `Element`
        :return: the value of the `Element`
        """
        if self.start is None:
            raise IndexError
        past_pointer: int = 0
        current_element: Element = dereference_pointer(self.start)
        if index != 0:
            for i in range(index):
                try:
                    new_element: Element = dereference_pointer(current_element.both ^ past_pointer)
                    past_pointer = get_pointer(current_element)
                except KeyError:
                    raise IndexError
                current_element = new_element
        return (not element and current_element) or current_element.element

    def insert(self, index: int, element: Any) -> None:
        """
        Inserts the `Element` at the index.
        :param index: index to insert the `Element` at
        :param element: the value to set the `Element` to
        :return: None
        """
        before: Element = self.get(index - 1, element=True)
        after: Element = self.get(index, element=True)
        before.both ^= get_pointer(after)
        after.both ^= get_pointer(before)
        element: Element = Element(element)
        element.end = False
        element.start = False
        element.both = get_pointer(after) ^ get_pointer(before)
        before.both ^= get_pointer(element)
        after.both ^= get_pointer(element)
        ref_counts[get_pointer(element)] += 1

    def __getitem__(self, index: Union[int, slice]) -> Any:
        """
        Returns the item at the index.
        :param index: index from which to get the item
        :return: the item at the index
        """
        if isinstance(index, int):
            return self.get(index)
        else:
            new_list: DoublyLinkedList = DoublyLinkedList()
            for i in index.indices(self.__len__()):
                new_list.add(self.__getitem__(i))
            return new_list

    def __setitem__(self, index, element) -> None:
        """
        Sets the value of the `Element` at the index to element
        :param index: the index of the `Element` to set
        :param element: the value to set to the `Element`
        :return: None
        """
        if isinstance(index, int):
            if self.start is None:
                raise IndexError
            past_pointer: int = 0
            current_element: Element = dereference_pointer(self.start)
            for j in range(index):
                new_element = dereference_pointer(current_element.both ^ past_pointer)
                try:
                    past_pointer = get_pointer(current_element)
                except KeyError:
                    raise IndexError
                current_element = new_element
            current_element.element = element
        else:
            for j, item in zip(index.indices(self.__len__()), element):
                self.__setitem__(index, item)

    def __delitem__(self, index: Union[int, slice]) -> None:
        """
        Removes the element at the index.
        :param index: index of element to remove
        :return: None
        """
        if isinstance(index, int):
            item: Element = self.get(index, element=True)
            if item.start and item.end:
                self.start = None
                ref_counts[id(item)] -= 1
                if ref_counts[id(item)] <= 0:
                    del pointer_store[id(item)]
            elif item.start:
                after: Element = self.get(index + 1, element=True)
                after.start = True
                after.both ^= get_pointer(item)
                if ref_counts[id(item)] <= 0:
                    del pointer_store[id(item)]
            elif item.end:
                before: Element = self.get(index - 1, element=True)
                before.end = True
                before.both ^= get_pointer(item)
                if ref_counts[id(item)] <= 0:
                    del pointer_store[id(item)]
            else:
                before: Element = self.get(index - 1, element=True)
                after: Element = self.get(index + 1, element=True)
                before.both ^= get_pointer(item)
                after.both ^= get_pointer(item)
                before.both ^= get_pointer(after)
                after.both ^= get_pointer(before)
                if ref_counts[id(item)] <= 0:
                    del pointer_store[id(item)]
        else:
            for j in index.indices(self.__len__()):
                self.__delitem__(j)

    def __len__(self) -> int:
        """
        Gets the length of the list.
        :return: length of the list
        """
        if self.start is None:
            return 0
        count: int = 1
        past_pointer: int = 0
        current_element: Element = dereference_pointer(self.start)
        while not current_element.end:
            new_element: Element = dereference_pointer(current_element.both ^ past_pointer)
            past_pointer: int = get_pointer(current_element)
            current_element = new_element
            count += 1
        return count


if __name__ == "__main__":
    a = DoublyLinkedList()
    a.add("Hello")
    a.add(", ")
    a.add("World")
    a.add("!")
    print("".join(a))
