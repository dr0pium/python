class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

   
    def __init__(self):
        self.__status = False  
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This method toggles the power status of the television.
        If the power is on, it turns it off. If the power is off, it turns it on.
        """
        self.__status = not self.__status
    def mute(self):
        if self.__status:  
            if not self.__muted:
                self.__saved_volume = self.__volume
                self.__muted = True 
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__saved_volume
 


    def channel_up(self) -> None:
        """
        Increases the channel by 1, up to a maximum value. 
        If the current channel is the maximum, it wraps around to the minimum channel.
        """
        if self.__status: 
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by 1, down to a minimum value. 
        If the current channel is the minimum, it wraps around to the maximum channel.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self) -> None:
        """
        Increases the volume by 1, up to a maximum value. 
        If the television is muted, it will be unmuted before the volume is increased.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = min(self.__saved_volume + 1, Television.MAX_VOLUME)
            else:
                self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self) -> None:
        """
        Decreases the volume by 1, down to a minimum value. 
        If the television is muted, it will be unmuted before the volume is decreased.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = max(self.__saved_volume - 1, Television.MIN_VOLUME)
            else:
                self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self) -> str:
        """
        Returns a string representation of the television's status, 
        including power status, current channel, and current volume.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"