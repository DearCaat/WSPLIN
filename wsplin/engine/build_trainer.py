from .base import BaseTrainer
from .iNet_cls import *
from .wsplin import *
from .ioplin import *

from .dino import *
from .ssl import *
from .ioplin import *

def build_trainer(config):

    if config.TRAINER.NAME.lower() == 'inet_cls':
        engine = INetClsEngine(config)
    elif config.TRAINER.NAME.lower() == 'wsplin':
        engine = WSPLINEngine(config)
    elif config.TRAINER.NAME.lower() == 'dino':
        engine = DINOEngine(config)
    elif config.TRAINER.NAME.lower() == 'ssl':
        engine = SSLEngine(config)
    elif config.TRAINER.NAME.lower() == 'ioplin':
        engine = IOPLINEngine(config)
    else:
        raise NotImplementedError
    base = BaseTrainer(engine=engine,config=config)
    return base.train_one_epoch,base.predict,base.validate,base.best_metrics