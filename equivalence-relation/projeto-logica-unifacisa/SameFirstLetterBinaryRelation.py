#coding: utf-8

from BinaryRelation import BinaryRelation


class SameFirstLetterBinaryRelation(BinaryRelation):
    """A Binary Relation which elements in an ordered pair share the same first letter."""

    def contains_ordered_pair(self, x, y):
        """
        This method returns a boolean value indicating if both elements of a given ordered pair have the same first letter.

        Arguments:
        x - The first element of the ordered pair.
        y - The second element of the ordered pair.

        Return True if the ordered pair belongs to the binary relation, otherwise, return False.
        """
        mesma_primeira_letra = True
        if(x[0] != y[0]):
            mesma_primeira_letra = False
        return mesma_primeira_letra

    def relation(self, S):
        """
        This method returns a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.

        Arguments:
        S - The input set.

        Return a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        """
        S_S = set([(x, y) for x in S for y in S])
        result_relation = set()
        for pair in S_S:
            if self.contains_ordered_pair(pair[0], pair[1]):
                result_relation.add(pair)
        return result_relation
