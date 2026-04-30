import numpy as np

from sklearn.metrics import f1_score
from transformers import Trainer
from torch.nn import CrossEntropyLoss


class WeightedTrainer(Trainer):
    def __init__(self, class_weights, **kwargs):
        super().__init__(**kwargs)
        self.class_weights = class_weights

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop('labels')
        outputs = model(**inputs)
        loss = CrossEntropyLoss(weight=self.class_weights.to(model.device))(outputs.logits, labels)
        return (loss, outputs) if return_outputs else loss
    
    
def compute_metrics(eval_pred):
    preds = np.argmax(eval_pred.predictions, axis=-1)
    labels = eval_pred.label_ids
    return { 
        'f1_macro': f1_score(labels, preds, average='macro')
    }
    
