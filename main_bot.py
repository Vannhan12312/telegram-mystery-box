from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Tạo một nút inline
    # \U0001F48E là mã emoji kim cương (💎)
    play_button = InlineKeyboardButton(text="\U0001F48E Play", callback_data="play_callback")
    
    # Ghép nút vào một danh sách để tạo InlineKeyboard
    keyboard = [[play_button]]  # Một hàng, chứa một nút
    
    # Tạo InlineKeyboardMarkup
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Gửi tin nhắn kèm theo inline keyboard
    await update.message.reply_text(
        text="Chọn tác vụ:",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Hàm xử lý khi người dùng bấm nút
    query = update.callback_query
    await query.answer()
    
    # Kiểm tra callback_data
    if query.data == "play_callback":
        await query.edit_message_text(text="Bạn đã bấm nút Play!")
    else:
        await query.edit_message_text(text="Không rõ bạn vừa bấm gì...")

def main():
    # Thay bằng token thật của bot
    BOT_TOKEN = "7875186963:AAHiuJrA2CHJswXFRY5Itfzk38pObJQgt_M"
    
    # Xây dựng ứng dụng
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Khi người dùng gõ /start, gọi hàm start
    app.add_handler(CommandHandler("start", start))
    
    # Xử lý callback data khi người dùng ấn vào nút
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # Chạy bot
    app.run_polling()

if __name__ == "__main__":
    main()
