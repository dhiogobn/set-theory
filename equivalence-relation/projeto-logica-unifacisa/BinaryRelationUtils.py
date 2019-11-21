#coding: utf-8


class BinaryRelationUtils(object):
    """Class providing utilities to verify properties of a binary relation."""

    @staticmethod
    def verify_reflexivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is reflexive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is reflexive
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        rho = binary_relation.relation(input_set)
        reflexive = True
        for i in rho:
            x = i[0]
            if (x,x) not in rho:
                reflexive = False
        return reflexive

    @staticmethod
    def verify_symmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is symmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is symmetric
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        rho = binary_relation.relation(input_set)
        symmetry = True
        for i in rho:
            x = i[0]
            y = i[1]
            if ((x, y) and (y, x)) not in rho:
                symmetry = False
        return symmetry

    @staticmethod
    def verify_transitivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is transitive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is transitive
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        rho = binary_relation.relation(input_set)
        transitivity = True
        for i in rho:
            x = i[0]
            y = i[1]
            for j in rho:
                if(j[0] ==y):
                    if(x,j[1]) not in rho:
                        transitivity = False
        return transitivity

    @staticmethod
    def verify_antisymmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is antisymmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        antisymmetric or False if it is not.
        """
        # TODO: Replace line below with actual code.
        rho = binary_relation.relation(input_set)
        antisymmetry = True
        for i in rho:
            x = i[0]
            y = i[1]
            if (x, y) and (y, x) in rho and x!=y:
                antisymmetry = False
        return antisymmetry
    
    @staticmethod
    def verify_equivalency(binary_relation, input_set):
        """
        This method verifies if a given binary relation is an equivalence relation.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        an equivalence relation or False if it is not.
        """
        # TODO: Replace line below with actual code.
        utils = BinaryRelationUtils()
        equivalency = False
        if(utils.verify_reflexivity(binary_relation, input_set) and utils.verify_symmetry(binary_relation, input_set) and utils.verify_transitivity(binary_relation, input_set)):
            equivalency = True
        return equivalency

    @staticmethod
    def get_partitioning(binary_relation, input_set):
        """
        This method first verifies if binary relation is an equivalence relation and, if it is, generates a partitioning of the input set using the binary relation. If the binary relation is not an equivalence relation, it returns None.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return None if the binary relation is not an equivalence relation or a partitioning of the input set (e.g.: {{1, 3, 5, ...}, {2, 4, 6, ...}}) if it is an equivalence relation.
        """
        # TODO: Replace line below with actual code.
        utils = BinaryRelationUtils()
        lista_de_conjuntos = []
        if(utils.verify_equivalency(binary_relation, input_set)):
            rho = binary_relation.relation(input_set)
            for x in input_set:
                partitioning = set()
                for y in input_set:
                    if(x, y) in rho:
                        partitioning.add(y)
                if partitioning not in lista_de_conjuntos:
                    lista_de_conjuntos.append(partitioning)
            return lista_de_conjuntos
        else:
            return None
