class Actor:
    """A thing that participates in the game
    
    The responsibility of actor is to move. Thus, it has move()
    method, which should be overridden by derived classes.
    """

    def _move(self):
        """Executes movement. This method should be overriden by 
        derived classes."""

        raise NotImplementedError("execute not implemented in base class")
