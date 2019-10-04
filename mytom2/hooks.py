import logging

logger = logging.getLogger(__name__)

def target_post_save(target,created):
    print("target post save")
