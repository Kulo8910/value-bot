# Value Telegram Bot

Bot Telegram tự động gửi kèo từ file `value_bet.txt` mỗi 5 phút nếu value > 10%.

## Cài đặt

```bash
pip install -r requirements.txt
```

## Thiết lập

1. Chạy `get_chat_id.py` để lấy Chat ID Telegram
2. Mở `send_from_file_auto.py`, thay dòng:
```python
CHAT_ID = <YOUR_CHAT_ID>
```
3. Đảm bảo file `value_bet.txt` nằm cùng thư mục.
4. Chạy bot:

```bash
python send_from_file_auto.py
```

## Tính năng

- Lọc kèo có value > 10%
- Gửi mỗi 5 phút nếu có dòng mới
