import argparse
import sys
from raspy_hermes.config import Settings
from raspy_hermes.gateway.telegram_gateway import TelegramGateway
from raspy_hermes.utils.logger import setup_logger

logger = setup_logger("main")

def main():
    parser = argparse.ArgumentParser(description="Raspy_Hermes Bot Runner")
    parser.add_argument("--dry-run", action="store_true", help="Validar configuración y salir")
    parser.add_argument("--test-msg", type=str, help="Simular un mensaje de entrada de usuario")
    args = parser.parse_args()

    settings = Settings.load()
    logger.info(f"Cargado {settings.app_name} ({settings.environment}) con {len(settings.agents)} agentes.")

    if args.dry_run:
        logger.info("Modo dry-run finalizado con éxito.")
        sys.exit(0)

    gateway = TelegramGateway(settings)

    if args.test_msg:
        reply = gateway.process_text_simulated("UsuarioPrueba", args.test_msg)
        print("\n--- Respuesta del Bot ---")
        print(reply)
        print("-------------------------\n")
        sys.exit(0)

    gateway.start()

if __name__ == "__main__":
    main()
