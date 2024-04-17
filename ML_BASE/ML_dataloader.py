
from torch.utils.data import DataLoader, TensorDataset


def add_features(df, features):
    for feature in features:
        df_grouped = df.groupby("sequence")[feature]
        df_rolling = df_grouped.rolling(5, center=True)

        df[feature + "_lag1"] = df_grouped.shift(1)
        df[feature + "_diff1"] = df[feature] - df[feature + "_lag1"]
        df[feature + "_lag2"] = df_grouped.shift(2)
        df[feature + "_diff2"] = df[feature] - df[feature + "_lag2"]
        df[feature + "_roll_mean"] = df_rolling.mean().reset_index(0, drop=True)
        df[feature + "_roll_std"] = df_rolling.std().reset_index(0, drop=True)
    df.dropna(axis=0, inplace=True)
    return


class dataloader:
    pass