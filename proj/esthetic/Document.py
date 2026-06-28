from Loggers.g_logging import *
import re

from Building.IDocument import DocumentIdentifier

def nicify_doc_id(did: DocumentIdentifier):
    try:
        #res = re.split(pattern=r'[\\/]',string=str(did))[-1]
        return re.split(string=str(did),pattern=r'[\\/]')[-1]
    except Exception as e:
        g_logger.warning(f"document_id {did} didn't want to be nicified", e)
        return did


