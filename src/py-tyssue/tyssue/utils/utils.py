import numpy as np
import warnings

def _to_3d(df):

    df_3d = np.asarray(df).repeat(3).reshape((df.size, 3))
    return df_3d

def set_data_columns(eptm, data_specs):

    for name, data_dict in data_specs.items():
        if 'setting' in name:
            continue
        for col, (default, dtype) in data_dict.items():
            df = getattr(eptm, '{}_df'.format(name))
            df[col] = default

def update_default(default_params, params=None):
    warnings.warn('Deprecated, use kwargs instead')
    _params = default_params
    if params is not None:

        _params.update(params)
    return _params
