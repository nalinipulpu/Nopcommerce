import logging


class CustomLogger:
    @staticmethod
    def custom_logger():
        logging.basicConfig(filename='C:\\Users\\nalin\\PycharmProjects\\nopcommerceApp\\Logs\\nopcommerceApp.log',
                            # datefmt='YYYY-MM-DD HH:MI:Sec',
                            format='%(asctime)s: %(levelname)s: %(message)s'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


# CustomLogger.custom_logger().info('jhgfdcvbjugf')
# logger = CustomLogger.custom_logger()
# logger.info('******** test home page title started *******')
# logger.info('********  Test_001Login test started *******')
