import asyncio

class ToroBot():
    """Classe do Bot."""
    name = 'Toro'
    role = <placeholder>

    def __init__(self) -> None:
        pass

    def connect(self, api_key: str) -> None:
        """Método para conectar ao serviço do Discord."""
        pass

    def read_commands(self, command: str) -> None:
        """Método que irá ler os comandos enviado pelos
        usuários da sala."""
        pass

    def read_weather(self):
        """Método que irá conectar ao serviço do OpenWeather.
        Aqui ficará a decisão de avisar se vai chover ou não."""
        pass

    def notify_all(self):
        """Método para envilar um @all avisando para não esqucer o
        guarda chuva."""
        pass

    def return_weather(self) -> str:
        """Método que irá retornar dados do tempo de uma determinada
        região seguindo o padrão ISO.
        Este método irá receber dados do read_commands() e read_weather()"""
        pass
