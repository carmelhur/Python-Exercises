import os
import logging

logger = logging.getLogger(__name__)


class ProcessChecking:
    @staticmethod
    def validate_directory(dir_path: str) -> bool:
        if not os.path.exists(dir_path):
            logger.error("Directory not found: %s", dir_path)
            return False
        if not os.path.isdir(dir_path):
            logger.error("Path is not a directory: %s", dir_path)
            return False
        return True
