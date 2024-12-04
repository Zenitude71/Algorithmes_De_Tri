class SortingResult:
    """ Représente le résultat d'un tri. """

    def __init__(self, time: int, sortedArray: list[int]):
        """
        Initialise les valeurs de la class SortingResult.
        :param time: Temps de réalisation du tri.
        :param sortedArray: Tableau trié.
        """
        self._time: int = time
        self._sortedArray = sortedArray

    def get_time(self):
        """ Récupère l'attribut time. """
        return self._time

    def get_sorted_array(self):
        """ Récupère l'attribut sortedArray. """
        return self._sortedArray