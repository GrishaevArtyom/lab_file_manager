import os

def is_within_working_dir(working_dir, target_path):
    """Проверяет, находится ли target_path внутри working_dir."""
    working_dir = os.path.abspath(working_dir)
    target_path = os.path.abspath(target_path)
    return os.path.commonpath([working_dir]) == os.path.commonpath([working_dir, target_path])