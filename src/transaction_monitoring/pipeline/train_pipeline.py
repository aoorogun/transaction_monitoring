import pandas as pd
import polars as pl
import numpy as np
from river import drift
from river import stream
from river import tree
from river import metrics
from river import imblearn
from river import evaluate
from river import neural_net as nn
from river import facto
from river import preprocessing as pp
from river import optim
from sklearn.neural_network import MLPClassifier

def train_models():
    """Initialize and return different models for training."""
    hatc = tree.HoeffdingAdaptiveTreeClassifier(
    grace_period=100,
    delta=1e-5,
    leaf_prediction='nb',
    nb_threshold=10,
    seed=0
    )


    hatc_eddm = tree.HoeffdingAdaptiveTreeClassifier(
        grace_period=100,
        delta=1e-6,
        leaf_prediction='nb',
        nb_threshold=10,
        seed=0,
        drift_detector=drift.binary.EDDM()
    )

    hatc_ddm = tree.HoeffdingAdaptiveTreeClassifier(
        grace_period=100,
        delta=1e-5,
        leaf_prediction='nb',
        nb_threshold=10,
        seed=0,
        drift_detector=drift.binary.DDM()
    )

    hatc_eddm2 = tree.HoeffdingAdaptiveTreeClassifier(
        grace_period=100,
        delta=1e-5,
        leaf_prediction='nb',
        nb_threshold=10,
        seed=0,
        drift_detector=drift.binary.EDDM()
    )

    drc_hatc = drift.DriftRetrainingClassifier(
        model=tree.HoeffdingAdaptiveTreeClassifier(
        grace_period=100,
        delta=1e-5,
        leaf_prediction='nb',
        nb_threshold=10,
        seed=0),
        drift_detector=drift.binary.EDDM()
    )

    hsc_hatc = imblearn.HardSamplingClassifier(
            classifier= tree.HoeffdingAdaptiveTreeClassifier(
                grace_period=100,
                delta=1e-5,
                leaf_prediction='nb',
                nb_threshold=10,
                seed=0
            ),
            p=0.1,
            size=40,
            seed=42,
        )

    mlp = (
        pp.StandardScaler() |
        nn.MLPRegressor(
            hidden_dims=(5,),
            activations=(
                nn.activations.ReLU,
                nn.activations.ReLU,
                nn.activations.Identity
            ),
            optimizer=optim.SGD(1e-3),
            seed=42
        )
    )

    mlp_online = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1, random_state=42)


    ffm = facto.FFMClassifier(
        n_factors=10,
        intercept=.5,
        seed=42,
    )

    return [hatc, drc_hatc, hsc_hatc, mlp_online]
