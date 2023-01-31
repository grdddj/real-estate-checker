from websites.idnes import Idnes
from websites.bezrealitky import Bezrealitky
from websites.sreality import Sreality
from websites.mmreality import Mmreality
from websites.remax import Remax

import logger
from send_pushbullet import send_pushbullet_message
from send_mail import send_email


def report_to_email() -> None:
    websites = [Bezrealitky, Idnes, Mmreality, Remax, Sreality]
    reports: list[str] = []

    for website in websites:
        try:
            for report in website().to_report():
                reports.append(report)
                logger.log_info(report)
        except Exception as e:
            logger.log_exception(e)
            send_pushbullet_message(
                title="Error", body=f"Error in {website.__name__}: {e}"
            )

    if not reports:
        logger.log_info("No new reports")
        return

    try:
        email_text = "\n\n".join(reports)
        send_email(email_text)
    except Exception as e:
        logger.log_exception(e)
        send_pushbullet_message(title="Error", body=f"Error in send_email: {e}")


if __name__ == "__main__":
    report_to_email()
