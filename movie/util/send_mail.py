from smtplib import SMTP_SSL as SMTP
import logging
import logging.handlers
import sys
from email.mime.text import MIMEText


def send_confirmation():
    with open('shield.html', 'r') as f:
        content = f.readlines()
        print(content)
    text = ''
    for item in content:
        text = text + item
    sender = '516495459@qq.com'
    receiver = 'east.snow@163.com'
    # receiver ="455323661@qq.com" #li qi jun
    # receiver = 'meijutuisong@163.com'
    # receiver = "493586337@qq.com"  # chen guo
    msg = MIMEText(text, _charset='utf-8')
    msg['Subject'] = "The walking dead link"
    msg['To'] = receiver

    try:
        conn = SMTP('smtp.qq.com')
        conn.set_debuglevel(True)
        conn.login('516495459@qq.com', 'Eastsnow1986\\')
        try:
            conn.sendmail(sender, receiver, msg.as_string())
        finally:
            conn.close()

    except Exception as exc:
        logger.error("ERROR!!!")
        logger.critical(exc)
        sys.exit("Mail failed: {}".format(exc))


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    random_ass_condition = True

    if random_ass_condition:
        send_confirmation()
