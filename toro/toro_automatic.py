import toro

class ToroBotAutomatic(toro.ToroBot):
    """
    Classe que irá ser responsável por cuidar de puxar os dados e avisar automaticamente quando chover.
    """
    pass

    def __init__(self):
        super.__init__()
        #

    # Discord stuff
    async def on_ready(self) -> None:
        """
        No momento em que o bot é iniciado, printa no terminal com qual usuário está logado.
        Para debug apenas.
        """
        print(f'Logado como {self.user}')
        print(f'Nome do bot: {self.bot_name}')
        print(f'Versão: {self.version}')
        print(f'Desenvolvido por: {self.author}')

    async def on_message(self, message):
        """
        Método herdado da classe discord.Client
        Será chamado quando um model Message é criado e enviado.
        """
        if message.content.startswith('$tempo'): # TODO: Existe o discord.ext.commands, decorators que ajudam no parse. Utilizar depois.
            await message.channel.send(self.get_weather())

    # OpeanWeather stuff
    def it_will_rain_automatic(self, contents: str) -> None:
        """
        Método que decide se irá chover ou não. Caso true, chama notify_all(). Caso false, faz nada.
        """
        if contents["weather"][0]["main"] != "Clear":
            self.notify_all()
        else:
            pass

    def notify_all(self):
        """
        Método para enviar um @everyone avisando para não esquecer o
        guarda chuva.
        """
        pass