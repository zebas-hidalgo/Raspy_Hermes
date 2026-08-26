import os
from raspy_hermes.config import Settings
from raspy_hermes.agents.router import MessageRouter
from raspy_hermes.agents.manager import AgentManager
from raspy_hermes.gateway.base import BaseGateway
from raspy_hermes.utils.logger import setup_logger

logger = setup_logger("telegram_gateway")

class TelegramGateway(BaseGateway):
    def __init__(self, settings: Settings):
        self.settings = settings
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.router = MessageRouter(settings)
        self.manager = AgentManager(settings)
        self.app = None

    def process_text_simulated(self, user_name: str, text: str) -> str:
        agent_id = self.router.resolve_agent(text)
        agent = self.manager.get_agent(agent_id)
        logger.info(f"Mensaje recibido de {user_name}: '{text}' -> Enrutado a {agent.display_name}")
        return (
            f"🤖 *[{agent.display_name}]*\n\n"
            f"He recibido tu consulta sobre: _{text}_\n\n"
            f"Procesando en entorno Kronos_School (Turnos máx: {agent.max_turns})..."
        )

    def start(self):
        if not self.token or self.token == "tu_token_aqui":
            logger.warning("TELEGRAM_BOT_TOKEN no configurado. Ejecutando en modo simulación/CLI.")
            return

        try:
            from telegram.ext import ApplicationBuilder, MessageHandler, filters
            self.app = ApplicationBuilder().token(self.token).build()
            
            async def handle_message(update, context):
                if update.message and update.message.text:
                    resp = self.process_text_simulated(update.effective_user.name, update.message.text)
                    await update.message.reply_text(resp, parse_mode="Markdown")

            self.app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
            logger.info("Iniciando Gateway de Telegram...")
            self.app.run_polling()
        except ImportError:
            logger.warning("python-telegram-bot no instalado. Modo pasivo activado.")

    def stop(self):
        if self.app:
            self.app.stop()
