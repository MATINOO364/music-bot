from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)


from config import TOKEN


from handlers.start import start
from handlers.search import search_text
from handlers.music import (
    button_handler,
    channel_music
)

from handlers.admin import statistics



async def error_handler(update, context):

    print(
        "ERROR:",
        context.error
    )



def main():

    app = Application.builder()\
        .token(TOKEN)\
        .build()



    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(

        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            search_text
        )
    )


    app.add_handler(

        CallbackQueryHandler(
            button_handler
        )
    )



    app.add_handler(

        MessageHandler(
            filters.AUDIO,
            channel_music
        )
    )


    app.add_handler(

        CommandHandler(
            "stats",
            statistics
        )
    )



    app.add_error_handler(
        error_handler
    )



    print(
        "Bot Started..."
    )


    app.run_polling()



if __name__ == "__main__":

    main()