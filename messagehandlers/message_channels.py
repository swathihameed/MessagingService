# channel_factory.py

from .sms_handlers import SMSChannel
from .email_handlers import EmailChannel


class ChannelType:
    """ class to get the appropriate channel handler."""

    @staticmethod
    def get_channel(channel_type: str):
        """
        Returns an instance of the channel handler based on the channel type.

        Args:
            channel_type (str): The type of the channel ("SMS" or "Email").

        Returns:
            An instance of SMSChannel or EmailChannel.

        Raises:
            ValueError: If the channel type is unsupported.
        """
        channel_map = {
            "SMS": SMSChannel,
            "Email": EmailChannel,
        }

        if channel_type not in channel_map:
            raise ValueError(f"Unsupported channel type: {channel_type}")

        return channel_map[channel_type]()
