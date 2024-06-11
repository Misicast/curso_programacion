import abc


class Screen(abc.ABC):

    @abc.abstractmethod
    def render(self):
        pass
